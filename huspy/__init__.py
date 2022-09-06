import os
import shutil
import subprocess


__version__ = '0.1.0'


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
        log('HUSKY env variable is set to 0, skipping install')
        return

    # // Ensure that we're inside a git repository
    # // If git command is not found, status is null and we should return.
    if not git('rev-parse'):
        return

    # // Custom dir help
    url = 'https://typicode.github.io/husky/#/?id=custom-directory'

    # // Ensure that we're not trying to install outside of cwd
    if not os.path.join(os.getcwd(), dir).startswith(os.getcwd()):
        raise Exception(f'.. not allowed see {url}')

    # // Ensure that cwd is git top level
    if not os.path.exists('.git'):
        raise Exception(f'.git can\'t be found see {url}')

    try:
        # Create .husky/_
        os.makedirs(os.path.join(dir, '_'), exist_ok=True)

        # Copy husky.sh to .husky/_/husky.sh
        dest_huspy = os.path.join(dir, '_/huspy.sh')
        if os.path.exists(dest_huspy):
            os.unlink(dest_huspy)
            log(f'{dest_huspy} exists, replace it')

        shutil.copyfile(os.path.join(os.path.dirname(__file__), '../huspy.sh'), os.path.join(dir, '_/huspy.sh'))

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
. "$(dirname -- "$0")/_/husky.sh"

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