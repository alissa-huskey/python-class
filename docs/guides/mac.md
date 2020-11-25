Mac Dev Env for Python
======================

Mac tool recommendations and setup guide for Python development.


Table of Contents
-----------------

* [Quickstart](#quickstart)
* [Homebrew](#homebrew)
* [VS Code](#vs-code)
* [pyenv](#pyenv)
* [Python](#python)
* [Poetry](#poetry)


Quickstart
----------

```bash
# install core developer tools (required by Homebrew, also installs git)
xcode-select --install

# install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# install vscode
brew cask install visual-studio-code
code --install-extension ms-python.python              # Python extension
code --install-extension ms-vsliveshare.vsliveshare    # LiveShare

# install pyenv
brew install pyenv
touch ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.zshrc

# install Python
pyenv install 3.8.0
pyenv global 3.8.0

# install Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Homebrew
-----

* [Homebrew](https://brew.sh/)
* [Introduction to Homebrew](https://opensource.com/article/20/6/homebrew-mac)
* [macOS migrations with Brewfile](https://openfolder.sh/macos-migrations-with-brewfile)

### Install

```bash
xcode-select --install
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Usage

| command                                      | description                                    |
|----------------------------------------------|------------------------------------------------|
| `brew search {keyword}`                        | search for available packages                  |
| `brew info {package}`                          | show info about an installed package           |
| `brew install {package}`                       | install {package}                              |
| `brew uninstall {package}`                     | uninstall {package}                            |
| `brew cask install {package}`                  | install GUI {package}                          |
| `brew cask install {package}`                  | uninstall GUI {package}                        |
| `brew list --versions \| column`               | list all installed packages, columnized        |
| `brew list --versions {package}`               | list installed package versions                |
| `brew bundle dump`                             | make a Brewfile of installed packages          |
| `brew bundle --global install`                 | install all packages from ~/.Brewfile          |
| `brew home {package}`                          | open the homepage for package                  |
| `brew leaves`                                  | list installed top-level formula               |
| `brew leaves \| column`                        | list installed top-level formula, columnized   |
| `brew help`                                    | show brief Homebrew help                       |
| `brew help {command}`                          | show help info for {command}                   |
| `man brew`                                     | show Homebrew manpage                          |

### The Brewfile

The `brew bundle` command installs all packages from a `Brewfile`.

Here is a sample Brewfile. You can copy it to `~/.Brewfile` then modify it to
suit your needs. When you're ready, run `brew bundle install --global`.

Store it in Github or Dropbox to greatly simplify setting up a new system in
the future.

*~/.Brewfile*
```ruby
# Development
# -----------

cask "visual-studio-code"                 # editor
brew "pyenv"                              # manage Python versions
brew "git"                                # most recent git version

# Recommended CLI utils
# ---------------------

brew "tree"                               # pretty directory viewer
brew "tldr"                               # cheat sheet for the CLI
brew "youtube-dl"                         # download youtube videos
brew "mas"                                # CLI for Mac App Store
brew "ack"                                # like grep but better
brew "jq"                                 # JSON processor
brew "gh"                                 # github CLI

# (better) gnu version
brew "coreutils"
brew "findutils"
brew "gnu-sed"
brew "gawk"

# Recommended GUI apps
# --------------------

cask "iterm2"                             # a nice terminal
cask "alfred"                             # launcher (Spotlight alternative)
cask "vlc"                                # cross-platform media viewer
cask "electric-sheep"                     # crowdsourced abstract screensaver
cask "github"                             # github desktop

# Popular apps
# ------------

cask "discord"
mas "desktop.WhatsApp", id: 1147396723
cask "dropbox"
cask "brave-browser"
cask "google-chrome"
cask "firefox"
cask "steam"
```

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

See the [VS Code Intro](vscode-intro.md).


pyenv
-----

* [pyenv](https://github.com/pyenv/pyenv#homebrew-on-macos)
* [Get started with pyenv & poetry](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/)
* [Installing Pythons with PyEnv](https://joachim8675309.medium.com/installing-pythons-with-pyenv-54cca2196cd3)
* [Installing pyenv on macOS](https://binx.io/blog/2019/04/12/installing-pyenv-on-macos/)


### Install

```bash
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
| `pyenv install --list \| grep '^\s*3.*'`  | list available Python versions >= 3.0         |
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

