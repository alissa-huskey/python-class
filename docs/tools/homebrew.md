Homebrew
========

Homebrew is a package manager for macOS.  It simplifies the installing,
upgrading and uninstalling of software, especially tools used by developers.

```{include} ../toc.md
```

```{seealso}
* [Homebrew](http://brew.sh/)
* [Introduction to Homebrew](https://opensource.com/article/20/6/homebrew-mac)
* [macOS migrations with Brewfile](https://openfolder.sh/macos-migrations-with-brewfile)
```

Install
-------

Follow these steps to install Homebrew.

1. Install xcode if you haven't already.

   ```bash
   xcode-select --install
   sudo xcodebuild -runFirstLaunch
   ```
2. Install homebrew

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```

Usage
-----

### Search

You can search for packages using the `brew search` command. For example, here
we search for `tree`, a simple command line utility to visualize directory
contents.

```{code-block} console
$ brew search tree

==> Formulae
as-tree             datree              tree                treecc              tre
cherrytree          pstree              tree-sitter         treefrog

==> Casks
figtree                          sourcetree                       treesheets
```

### Install packages

To install a package, use the `brew install` command.

```{code-block} console
$ brew install tree

Running `brew update --preinstall`...
==> Auto-updated Homebrew!
Updated 3 taps (homebrew/core, homebrew/cask and homebrew/bundle).
==> Updated Formulae
Updated 6 formulae.
==> Updated Casks
Updated 32 casks.

==> Downloading https://ghcr.io/v2/homebrew/core/tree/manifests/2.0.1
Already downloaded: /Users/alissa/Library/Caches/Homebrew/downloads/d24fb0a138ed9e3dd82f7d5ec5ec5462416e3bb6c18e94d7da2037d0a972be73--tree-2.0.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/tree/blobs/sha256:da97488f8fe9d7a3a311c93baa359af
Already downloaded: /Users/alissa/Library/Caches/Homebrew/downloads/52e03620976260ba550b29f9ba73c86a9078c942ea4ee36f68a4433f0f0207c5--tree--2.0.1.arm64_monterey.bottle.tar.gz
==> Pouring tree--2.0.1.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/tree/2.0.1: 8 files, 166.7KB
==> Running `brew cleanup tree`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

### Install GUI apps

You can also install GUI applications via homebrew. These are called casks, and
will be listed under the {guilabel}`==> Casks` section in search.

To install these you also use the `brew install` command with the `--cask`
flag. For example, here we use homebrew to install the
[Discord](http://discord.com/) app.

```{code-block} console
$ brew install --cask discord

==> Downloading https://dl.discordapp.net/apps/osx/0.0.264/Discord.dmg
Already downloaded: /Users/alissa/Library/Caches/Homebrew/downloads/23e9163504b96c03d9bf1f5e535e296e0c35a1425277c5f6c7dec5cdc2b36de1--Discord.dmg
==> Installing Cask discord
==> Moving App 'Discord.app' to '/Applications/Discord.app'
🍺  discord was successfully installed!
```

### Install from a Brewfile

The `brew bundle` command installs all packages listed in a `Brewfile`.

Here is a example `Brewfile`.

```{code-block} ruby
:caption: ~/.Brewfile

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
cask "vlc"                                # cross-platform media viewer
cask "electric-sheep"                     # crowdsourced abstract screensaver
cask "github"                             # github desktop

# Popular apps
# ------------

cask "discord"
cask "dropbox"
cask "brave-browser"
cask "google-chrome"
cask "firefox"
cask "steam"
```

Save it to your home directory with the name `.Brewfile`, then
run `brew bundle install --global` to install all of the packages listed in the
file.

```console
$ brew bundle install --global

Running `brew update --preinstall`...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> Updated Formulae
Updated 5 formulae.
==> Updated Casks
Updated 1 cask.

Installing visual-studio-code
Installing pyenv
Installing git

...

```

Store it in Github or Dropbox to greatly simplify setting up a new computer.

### Listing packages

You can list all installed packages (including dependencies) using the `brew
list` (or `brew ls`) command.

```{code-block} console
$ brew list

==> Formulae
ack			gnupg			libusb			pango
amass			gnutls			libuv			pcre
antlr			gobject-introspection	libvmaf			pcre2
aom			gpgme			libx11			perl

...

==> Casks
adobe-creative-cloud	firefox			private-internet-access	visual-studio-code
alfred			google-chrome		qbittorrent		vlc
```

To get a list of just the top-level packages (without dependencies) use the
`brew leaves` command.

```{code-block} console
$ brew leaves

ack
antlr
autoenv
bash-completion
bat
bats-core

...
```

Pipe it to `column` to columnize the list of packages.

```{code-block} console
$ brew leaves | column

ack			findutils		litecli			rlwrap
antlr			fzf			lzip			thefuck
autoenv			gh			make			tldr
bash-completion		git			mas-cli/tap/mas		todo-txt

...
```

### Package info

You can get more information about a package like the homepage and if/where it
is installed, use the `brew info` command.

```{code-block} console
$ brew info tree

tree: stable 2.0.1 (bottled)
Display directories as trees (with optional color/HTML output)
http://mama.indstate.edu/users/ice/tree/
/opt/homebrew/Cellar/tree/2.0.1 (8 files, 166.7KB) *
  Poured from bottle on 2022-01-29 at 00:27:11
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/tree.rb
License: GPL-2.0-or-later
==> Analytics
install: 88,536 (30 days), 172,682 (90 days), 405,746 (365 days)
install-on-request: 84,459 (30 days), 165,284 (90 days), 383,222 (365 days)
build-error: 4 (30 days)
```

### Package status

You can use the `brew list` command to see if something is installed, and
if so, the location of all of the associated files.

```{code-block} console
$ brew list tree

/opt/homebrew/Cellar/tree/2.0.1/bin/tree
/opt/homebrew/Cellar/tree/2.0.1/share/man/man1/tree.1
```


```{code-block} console
$ brew list htop

Error: No such keg: /opt/homebrew/Cellar/htop
```

Add the `--versions` flag to get see the installed versions.

```{code-block} console
$ brew list --versions tree

tree 2.0.1
```


```{code-block} console
$ brew list --versions htop
```


You can also use the `brew --prefix` command to get the directory where the
files for a particular package can be found. With no arguments, it tells you
the homebrew install directory.

```{code-block} console
$ brew --prefix

/opt/homebrew
```

Or if followed by a package name, it tells you the install directory for that
particular package.

```{code-block} console
$ brew --prefix tree

/opt/homebrew/opt/tree
```

### Uninstall packages

To remove a package, use the `brew uninstall` command.

```{code-block} console
$ brew uninstall tree

Uninstalling /opt/homebrew/Cellar/tree/2.0.1... (8 files, 166.7KB)
```

### Getting help

You can see the detailed help documentation for homebrew by typing `man brew`.

```{code-block} console
$ man brew

BREW(1)                                   brew                                   BREW(1)



NAME
       brew - The Missing Package Manager for macOS (or Linux)

SYNOPSIS
       brew --version
       brew command [--verbose|-v] [options] [formula] ...

DESCRIPTION
       Homebrew is the easiest and most flexible way to install the UNIX tools Apple
       didn't include with macOS. It can also install software not packaged for your
       Linux distribution to your home directory without requiring sudo.

...
```

You can get see a brief usage summary with the `brew help` command.

```{code-block} console
$ brew help

Example usage:
  brew search TEXT|/REGEX/
  brew info [FORMULA|CASK...]
  brew install FORMULA|CASK...

...
```

You can also use `brew help` to get help for a specific command.

```{code-block} console
$ brew help install

Usage: brew install [options] formula|cask [...]

Install a formula or cask. Additional options specific to a formula may be
appended to the command.

...
```

You can see a see a list of all homebrew commands with `brew commands`.

```{code-block} console
$ brew commands

==> Built-in commands
--cache         casks           fetch           list            reinstall       update-report
--caskroom      cleanup         formulae        log             search          update-reset
--cellar        commands        gist-logs       migrate         shellenv        update
--env           completions     help            missing         tap-info        upgrade

...
```

Quickref
--------

Here is a quick reference summary of the most commonly used homebrew commands.

| command                                      | description                                    |
|----------------------------------------------|------------------------------------------------|
| `brew search {keyword}`                      | search for available packages                  |
| `brew info {package}`                        | show info about an installed package           |
| `brew install {package}`                     | install `{package}`                            |
| `brew uninstall {package}`                   | uninstall `{package}`                          |
| `brew install --cask {package}`              | install GUI `{package}`                        |
| `brew uninstall --cask {package}`            | uninstall GUI `{package}`                      |
| `brew list --versions | column`              | list all installed packages, columnized        |
| `brew list --versions {package}`             | list installed package versions                |
| `brew bundle dump`                           | make a Brewfile of installed packages          |
| `brew bundle --global install`               | install all packages from ~/.Brewfile          |
| `brew home {package}`                        | open the homepage for package                  |
| `brew leaves`                                | list installed top-level formula               |
| `brew leaves | column`                       | list installed top-level formula, columnized   |
| `brew help`                                  | show brief Homebrew help                       |
| `brew help {command}`                        | show help info for `{command}`                 |
| `man brew`                                   | show Homebrew manpage                          |
| `brew --prefix [{package}]`                  | path to install directory                      |

