Screencasts
===========

You can record a screencast of your terminal activity with [asciinema](https://asciinema.org/) or the
windows port [PowerSession](https://github.com/ibigbug/PowerSession).

Install
-------


```````{tabs}

``````{tab} MacOS/Linux

Install the [asciinema](https://asciinema.org/) module using your preferred installer.

`````{tabs}

````{tab} pip

```{code-block} bash
:caption: command line
pip install asciinema
```

````

````{tab} poetry

```{code-block} bash
:caption: command line
poetry add asciinema
```

`````

``````


`````{tab} Windows

First install [scoop](https://scoop.sh/) if you haven't already:

```{code-block} powershell
:caption: PowerShell
iwr -useb get.scoop.sh | iex
```

Then use `scoop` to install [PowerSession](https://github.com/ibigbug/PowerSession):

```{code-block} powershell
:caption: PowerShell
scoop install PowerSession
```

`````

```````

Usage
-----


### Record

```````{tabs}

``````{tab} MacOS/Linux

To start recording run `asciinema rec` followed by a filename to record to. To
finish hit {kbd}`Ctrl-D` or type `exit`.

```{code-block} bash
:caption: command line
asciinema rec sess.cast
```

``````


`````{tab} Windows

To start recording run `PowerShell rec` followed by a filename to record to.
(You may need to use the command `PowerShell.exe` instead.) To finish hit
{kbd}`Ctrl-D` or type `exit`.

```{code-block} powershell
:caption: PowerShell
PowerSession rec sess.cast
```

`````

```````


### Play

```````{tabs}

``````{tab} MacOS/Linux

You can play back a previously recorded screencast with the command `asciinema play`
followed by the filename to play.

```{code-block} bash
:caption: command line
asciinema play sess.cast
```

``````


`````{tab} Windows

You can play back a previously recorded screencast with the command `PowerShell
play` followed by the filename to play.  (You may need to use the command
`PowerShell.exe` instead.)

```{code-block} powershell
:caption: PowerShell
PowerSession play sess.cast
```

`````

```````

