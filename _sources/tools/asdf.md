asdf
=====

asdf is a command line tool that lets you easily install and switch between
multiple versions of Python and other tools. It can replace a bunch of other
tool-specific version managers like pyenv, rbenv, goenv and nvm.


```{contents} Table of Contents
:backlinks: top
:local:
:depth: 2
```

Install
-------

:::::{tab-set}

:::{tab-item} Mac

To install:

```{code-block} console
:caption: command line

brew install asdf
```

Then add the following to your startup file:

```{code-block} console
:caption: startup file

$(brew --prefix asdf)/libexec/asdf.sh
```

:::

:::{tab-item} Other

To install:

```{code-block} console
:caption: command line

git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.9.0
```

Then add the following to your startup file:

```{code-block} console
:caption: startup file

. $HOME/.asdf/asdf.sh
```

Then close your terminal and start a new one.

:::

:::::

Usage
-----

First you'll need to add the plugin for whatever tool you want to install
with the `plugin add` command.

```{code-block} console
:caption: command line

$ asdf plugin add python
```

Then then you can install the version or versons of the tool you need.

```{code-block} console
:caption: command line

$ asdf install python 3.8.11
$ asdf install python 3.9.1
```

Next, choose which version to use by default:

```{code-block} console
:caption: command line

$ asdf global python 3.9.1
```

This adds the information to the file `~/.tool-versions` in your home directory.

```{code-block} console
:caption: ~/.tool-versions

$ python 3.9.1
```

Now you can test it out.

```{code-block} console
:caption: command line

$ python --version
3.9.1
```

To configure a project to use a particular version of a tool, use the `asdf local` command.

```{code-block} console
:caption: command line

$ cd my-project
$ asdf local python 3.8.11
```

This saves the information in a file called `.tool-versions` in the current directory.

```{code-block} console
:caption: ./.tool-versions

python 3.8.11
```

Now you can test it out:

```{code-block} console
:caption: command line

$ python --version
Python 3.8.11

$ cd ..
$ python --version
Python 3.9.1
```

Let's install another tool, `ruby`. This time we'll use `latest` for the
version number, which tells asdf to install/use the most recent version.

```{code-block} console
:caption: command line

$ asdf plugin add ruby
$ asdf install ruby latest
$ asdf global latest
```

You can use the `asdf list` command to see a list of everything currently installed.

```{code-block} console
:caption: command line

$ asdf list
python
  3.8.11
  3.9.1
ruby
  3.1.1
```

And the `asdf current` command to see the active tool versions and where they
are set.

```{code-block} console
:caption: command line

$ asdf current
python          3.8.11          ./.tool-versions
ruby            3.1.1           ~/.tool-versions
```

Python
------

There are a couple of extra features provided by the asdf python plugin.

### Default packages

If there are python modules that you want to be installed for every version of
python, you can add them to the file `~/.default-python-packages`.

For example, if you wanted to always install ipython you would put in the file:

```{code-block} bash
:caption: ~/.default-python-packages

ipython
```

### Patches

Sometimes there are issues installing a particular version of Python in a
particular environment, and to resolve these issues a {term}`patch` is created
to fix the problem.

A patch is a file that can be used to make changes to the Python build files
or source code before attempting to install it on your system.

To apply a patch, set the `ASDF_PYTHON_PATCH_URL` environment variable to the
URL of the patch file before doing the install.

```{code-block} console
:caption: command line

$ export ASDF_PYTHON_PATCH_URL="https://gist.githubusercontent.com/xight/74f84b8bde9ac6f539c3db20c2897d46/raw/cf2fd7ff5572afafb54d062f866e40d5e65cab43/config-sub.patch"
$ asdf install python 3.8.11
```


Reference
---------

### Command summary

This is a summary of asdf commands and what they do.

| Category          | Command                                | Description                                                 |
|-------------------|----------------------------------------|-------------------------------------------------------------|
| Meta              | `asdf help`                            | show help                                                   |
|                   | `asdf info`                            | print system debug info                                     |
|                   | `asdf update`                          | update asdf to the latest stable release                    |
| List available    | `asdf plugin list all | less`          | list all available plugins                                  |
|                   | `asdf list all PLUGIN | less`          | list available versions for a `PLUGIN`                      |
| See installed     | `asdf plugin list`                     | list installed plugins                                      |
|                   | `asdf list [PLUGIN]`                   | list installed versions                                     |
|                   | `asdf latest PLUGIN`                   | show latest version                                         |
|                   | `asdf current [PLUGIN]`                | display current version being used `PLUGIN` or all          |
|                   | `asdf where PLUGIN [VERSION]`          | show install path                                           |
|                   | `asdf shim-versions COMMAND`           | lists the plugins and versions that provide shims `COMMAND` |
|                   | `asdf which COMMAND`                   | show path to executable                                     |
| Manage installs   | `asdf install`                         | install everything in `./.tool-versions`                    |
|                   | `asdf plugin add PLUGIN`               | install plugin                                              |
|                   | `asdf plugin update [PLUGIN | --all]`  | update plugin(s)                                            |
|                   | `asdf plugin remove PLUGIN`            | remove plugin and uninstall all versions                    |
|                   | `asdf install PLUGIN VERSION`          | install version of plugin                                   |
|                   | `asdf uninstall PLUGIN VERSION`        | uninstall version of plugin                                 |
|                   | `asdf reshim PLUGIN [VERSION]`         | recreate shims                                              |
| Choose version    | `asdf global PLUGIN VERSION`           | set the package global version in `~/.tool-versions`        |
|                   | `asdf local PLUGIN VERSION`            | set the package local version in `./.tool-versions`         |
| Shell utils       | `asdf shell PLUGIN VERSION`            | set version to `ASDF_${LANG}_VERSION` in current shell      |
|                   | `asdf exec COMMAND [args...]`          | executes the command shim for current version               |
|                   | `asdf env COMMAND [UTIL=env]`          | runs util in the environment used for shim execution        |

### See also

```{seealso}

* [asdf docs](https://asdf-vm.com/manage/core.html)
* [github repo](https://github.com/asdf-vm/asdf)
* [python plugin](https://github.com/danhper/asdf-python)
* [asdf plugin repo](https://github.com/asdf-vm/asdf-plugins)

```
