# huspy

Git hooks for python.

Huspy is inspired by [Husky](https://github.com/typicode/husky). 

The code is transfered from Husky's typscript to python.

### Usage

```
pip install huspy

# In a git repository, this command will generate `./.huspy` directory, which is the git hooks directory.
huspy install

# This command will add a pre-commit hook.
huspy set ./huspy/pre-commit python test.py

# This command will uninstall the git hooks.
huspy uninstall
```

