pyenv
=====

pyenv is a command line tool that lets you easily install and switch between
multiple versions of Python.


```{contents}
:backlinks: top
:local:
:depth: 2
```

```{seealso}
* [pyenv](https://github.com/pyenv/pyenv#homebrew-on-macos)
* [Get started with pyenv & poetry](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/)
* [Installing Pythons with PyEnv](https://joachim8675309.medium.com/installing-pythons-with-pyenv-54cca2196cd3)
* [Installing pyenv on macOS](https://binx.io/blog/2019/04/12/installing-pyenv-on-macos/)
```

### Install

```{code-block} console
:caption: command line

# install pyenv
brew install pyenv

# display your shell
echo $SHELL

# if $SHELL is /bin/zsh
touch ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.zshrc

# if $SHELL is /bin/bash
touch ~/.bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.bash_profile
```
Then close your terminal and start a new one.

### Quickref

| command                                 | description                                   |
|-----------------------------------------|-----------------------------------------------|
| `pyenv install --list`                  | list all available Python versions            |
| `pyenv install --list | grep '^\s*3.*'` | list available Python versions >= 3.0         |
| `pyenv install {version}`               | install a version of Python                   |
| `pyenv uninstall {version}`             | uninstall a version of Python                 |
| `pyenv versions`                        | list installed Python versions                |
| `pyenv version`                         | list the active Python version                |
| `pyenv global`                          | show the default Python version               |
| `pyenv global {version}`                | set the default Python version                |
| `pyenv local`                           | show the Python version for this directory    |
| `pyenv local {version}`                 | set the Python version for this directory     |
| `pyenv help [{command}]`                | show the help (optionally for {command})      |

