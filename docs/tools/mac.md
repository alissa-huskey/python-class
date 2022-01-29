Mac Dev Env for Python
======================

Mac tool recommendations and setup guide for Python development.


```{contents} Table of Contents
:backlinks: entry
:depth: 1
:local:
```

TODO
----

* [ ] zshrc / bashrc
* [ ] .env


Quickstart
----------

```bash
# install core developer tools (required by Homebrew, also installs git)
xcode-select --install

# install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# install all brewfile packages
curl -sSL "https://raw.githubusercontent.com/alissa-huskey/python-class/master/docs/tools/brewfile.rb" | brew bundle install --file=-

# install vscode
# brew cask install visual-studio-code
code --install-extension ms-python.python              # Python extension
code --install-extension ms-vsliveshare.vsliveshare    # LiveShare

# install pyenv
# brew install pyenv

touch ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.zshrc

# install Python
pyenv install 3.8.11
pyenv global 3.8.11

# install Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```


XCode
-----

XCode is the Apple IDE (integrated development environment), a tool for writing
code. It also contains the foundational tools and libraries that other programs
rely on, and that programmers use when writing code.

### Install

:::{warning}

This step will take awhile, so it's a good idea to do this before bed or something.

:::

Run the following command at the command line. Some GUI windows will pop up,
prompting you to log into your apple account and accept the terms of service.
After you follow the prompts, the download and installation will begin.

```{code-block} console
:caption: command line
xcode-select --install
```

If installing from the command line does not work for some reason, you can
install XCode via the Apple App Stoe.

Homebrew
--------

* [Homebrew](https://brew.sh/)
* [Introduction to Homebrew](https://opensource.com/article/20/6/homebrew-mac)
* [macOS migrations with Brewfile](https://openfolder.sh/macos-migrations-with-brewfile)

Homebrew is a package manager for macOS.  It simplifies the installing,
upgrading and uninstalling of software, especially tools used by developers.

We'll use this to install other software.

### Install

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

pyenv
-----

* [pyenv](https://github.com/pyenv/pyenv#homebrew-on-macos)
* [Get started with pyenv & poetry](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/)
* [Installing Pythons with PyEnv](https://joachim8675309.medium.com/installing-pythons-with-pyenv-54cca2196cd3)
* [Installing pyenv on macOS](https://binx.io/blog/2019/04/12/installing-pyenv-on-macos/)

pyenv is a command line tool that lets you easily install and switch between
multiple versions of Python.


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

### Usage

| command                                 | description                                   |
|-----------------------------------------|-----------------------------------------------|
| `pyenv install --list`                    | list all available Python versions            |
| `pyenv install --list | grep '^\s*3.*'`  | list available Python versions >= 3.0         |
| `pyenv install {version}`                 | install a version of Python                   |
| `pyenv uninstall {version}`               | uninstall a version of Python                 |
| `pyenv versions`                          | list installed Python versions                |
| `pyenv version`                           | list the active Python version                |
| `pyenv global`                            | show the default Python version               |
| `pyenv global {version}`                  | set the default Python version                |
| `pyenv local`                             | show the Python version for this directory    |
| `pyenv local {version}`                   | set the Python version for this directory     |
| `pyenv help [{command}]`                  | show the help (optionally for {command})      |


Python
------

### Install

> This is for installing Python 3.8, but feel free to replace `3.8.0` with any
> version in `pyenv install --list`.

```bash
pyenv install 3.8.0
pyenv global 3.8.0
```

Poetry
------

* [Poetry](https://python-poetry.org/)

### Install

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

See the full [Poetry Guide](poetry.md).

VS Code
-------

* [Visual Studio Code](https://code.visualstudio.com/)
* [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

### Install

```bash
brew cask install visual-studio-code
code --install-extension ms-python.python              # Python extension
code --install-extension ms-vsliveshare.vsliveshare    # LiveShare
```

See the [VS Code Intro](vscode.md).


