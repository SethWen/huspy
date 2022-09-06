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
