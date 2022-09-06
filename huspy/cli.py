import os
import subprocess


__version__ = '0.1.1'

huspy_sh = '''
#!/bin/sh
if [ -z "$huspy_skip_init" ]; then
  debug () {
    if [ "$HUSPY_DEBUG" = "1" ]; then
      echo "huspy (debug) - $1"
    fi
  }

  readonly hook_name="$(basename "$0")"
  debug "starting $hook_name..."

  if [ "$HUSPY" = "0" ]; then
    debug "HUSPY env variable is set to 0, skipping hook"
    exit 0
  fi

  if [ -f ~/.huspyrc ]; then
    debug "sourcing ~/.huspyrc"
    . ~/.huspyrc
  fi

  export readonly huspy_skip_init=1
  sh -e "$0" "$@"
  exitCode="$?"

  if [ $exitCode != 0 ]; then
    echo "huspy - $hook_name hook exited with code $exitCode (error)"
  fi

  exit $exitCode
fi
'''


def log(*args):
    print('huspy -', *args)


def git(*args):
    subprocess.run(['git', *args])
    return True


def install():
    dir = os.getenv('HUSPY_DIR')
    if not dir:
        dir = '.huspy'

    if os.getenv('HUSPY') == '0':
        log('HUSPY env variable is set to 0, skipping install')
        return

    # // Ensure that we're inside a git repository
    # // If git command is not found, status is null and we should return.
    if not git('rev-parse'):
        return

    # // Custom dir help
    url = 'https://github.com/SethWen/huspy'

    # // Ensure that we're not trying to install outside of cwd
    if not os.path.join(os.getcwd(), dir).startswith(os.getcwd()):
        raise Exception(f'.. not allowed see {url}')

    # // Ensure that cwd is git top level
    if not os.path.exists('.git'):
        raise Exception(f'.git can\'t be found see {url}')

    try:
        # Create .huspy/_
        os.makedirs(os.path.join(dir, '_'), exist_ok=True)

        # Copy huspy.sh to .huspy/_/huspy.sh
        dest_huspy = os.path.join(dir, '_/huspy.sh')
        with open(dest_huspy, 'w') as f:
            f.write(huspy_sh)

        # Configure repo
        git('config', 'core.hooksPath', dir)
        log('Git hooks installed')
    except:
        log('Git hooks failed to install')
        raise


def set(file, cmd):
    dir = os.path.dirname(file)
    if not os.path.exists(dir):
        raise Exception(f'can\'t create hook, {dir} directory doesn\'t exist (try running huspy install)')

    with open(file, 'w') as f:
        f.write(f'''#!/usr/bin/env sh
. "$(dirname -- "$0")/_/huspy.sh"

# your command
{cmd}        
''')
    os.chmod(file, 0o0755)
    log(f'created {file} with command:\n    {cmd}\n')


def add(file, cmd):
    if os.path.exists(file):
        with open(file, 'a') as f:
            f.write(f'{cmd}\n')
        log(f'append {file} with command:\n    {cmd}\n')
    else:
        set(file, cmd)


def uninstall():
    git('config', '--unset', 'core.hooksPath')
    log('unconfig git hooks path')