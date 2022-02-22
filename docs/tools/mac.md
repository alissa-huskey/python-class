Mac Dev Env for Python
======================

Mac tool recommendations and setup guide for Python development.


```{contents} Table of Contents
:backlinks: entry
:depth: 1
:local:
```


Quickstart
----------

```bash
# install core developer tools (required by Homebrew, also installs git)
xcode-select --install

# install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# install all brewfile packages
curl -sSL "https://raw.githubusercontent.com/alissa-huskey/python-class/master/docs/tools/brewfile.rb" | brew bundle install --file=-

# install vscode extensions
code --install-extension alissahuskey.vscode-python-class

touch ~/.zshrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.zshrc

# install Python
pyenv install 3.8.11
pyenv global 3.8.11

# install Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Steps
-----

### Step 1: XCode

XCode is the Apple IDE (integrated development environment), a tool for writing
code. It also contains the foundational tools and libraries that other programs
rely on, and that programmers use when writing code.

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

### Step 2: Homebrew

Homebrew is a package manager for macOS.  It simplifies the installing,
upgrading and uninstalling of software, especially tools used by developers.

We'll use this to install other software.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

See the [homebrew guide](homebrew.md).

### Step 3: pyenv

pyenv is a command line tool that lets you easily install and switch between
multiple versions of Python.

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

See the [pyenv guide](pyenv.md).

### Step 4: Python

> This is for installing Python 3.8, but feel free to replace `3.8.11` with any
> version in `pyenv install --list`.

```bash
brew install zlib openssl readline xz bzip2

pyenv install 3.8.11
pyenv global 3.8.11
```

#### TODO

- `[ ]` flags
- `[ ]` patches
- `[ ]` arm
- `[ ]` troubleshooting

### Step 5: Poetry

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

See the full [Poetry Guide](poetry.md).

### Step 5: VS Code

```bash
brew install --cask visual-studio-code
```

Install VS Code extensions.

```bash
code --install-extension alissahuskey.vscode-python-class
```

See the [VS Code Intro](vscode.md).

% ### Step 6: Startup files

% #### TODO

% * `[ ]` .zshrc / .bashrc
% * `[ ]` .env
