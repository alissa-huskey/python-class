---
substitutions:
  ctrltick: <kbd class="kbd docutils literal notranslate">⌃`</kbd>
  mktbtn: |
    <a href="https://marketplace.visualstudio.com/items?itemName=ID" class="btn btn-small btn-outline-info bg-white text-info btn-block" role="button">Marketplace</a>
  theme: |
    <div role="navigation" class="mt-5 position-static navbar navbar-light bg-light align-bottom shadow-none">
      <h4 role="span" class="navbar-brand m-0">NAME</h4>
      <a href="https://vscodethemes.com/e/ID" class="btn btn-small btn-outline-info text-info bg-white" role="button">VSCodeThemes</a>
      <a href="https://marketplace.visualstudio.com/items?itemName=ID" class="btn btn-small btn-outline-info bg-white text-info" role="button">Marketplace</a>
    </div>

    ![NAME][NAME]
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
VS Code
=======

```{include} ../toc.md
```

Resources
---------

:::{seealso}

```{centered} Visual Studio Code Docs
```

* [Intro > Getting Started Video](https://code.visualstudio.com/docs/introvideos/basics) \
  Five minute hello world tour which happens to use Python.

* [User Guide > User Interface](https://code.visualstudio.com/docs/getstarted/userinterface) \
  High level guide to the layout and what each part does.

* [Getting Started > Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) \
  Introduction to some of the most essential features such as the command
  palette, quick open, zen mode; editor shortcuts like how to select a line or
  quickly move or copy it up or down; and navigating around and between files
  via code symbols and history.

* [User Guide > Basic Editing](https://code.visualstudio.com/docs/editor/codebasics) \
  Oddly focuses less on editing than the Tips and Tricks page. Searching and
  replacing within and across files, advanced selection, formatting and
  indentation.

* [User Guide > Code Navigation](https://code.visualstudio.com/docs/editor/editingevolved) \
  Covers the powerful features for quickly finding and getting to the right
  parts of your codebase via quick open, toggling history and open editors,
  breadcrumbs, and code navigation. Briefly mentions navigating errors and
  quick fixes.


* [Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-python-hello-world-source-code-file) \
  The tutorial for writing Python using VS Code. A great deal of it is either
  installation and setup or focused on features we aren't using like Jupyter
  Notebooks or Django. However, following the Hello World steps could be
  helpful.

* [Editing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/editing) \
  Covers the editor features provided by the Python extension.

* [Visual Studio Code Docs](https://code.visualstudio.com/docs) \
  VS Code documentation home page.

```{centered} Third party tutorials
```

* [Visual Studio Code Python for Beginners: Hello World & Beyond](https://www.youtube.com/watch?v=dGeUH_bqNpA) \
  An intro to VS Code for Python beginners. It's made by a professional
  programmer who doesn't know Python so you get to see him figure things out as
  he goes along. (Recorded by a Windows user.)

* [Learn Python 3: Visual Studio Code for Beginners](https://www.youtube.com/watch?v=RdD47NPku30) \
  An in-depth walk-through via a Python hello world script. Covers core
  features like the activity bar, file explorer, terminal, split editors,
  command palette, settings, and workspaces.
  Python specific topics selecting an interpreter, linter, and formatter using
  virtual environments. (Recorded by a Windows user.)

* [Visual Studio Code Crash Course](https://www.youtube.com/watch?v=WPqXP_kLzpo) \
  An in-depth walk-through of core features like layout, search and replace,
  file navigation, keyboard shortcuts, customizations, the terminal and SCM.
  It's detailed with well labeled time markers so it's easy to skip around.
  (Recorded by a Mac user.)

:::

Essential Keyboard Shortcuts
----------------------------

```````{tabs}

`````{tab} MacOS

:::::{grid}
:gutter: 2

:::{grid-item-card}
:shadow: none

Editor
^^^

| Shortcut       | Action                    |
|----------------|---------------------------|
| {kbd}`⌘L`      | Select line               |
| {kbd}`⇧⌘K`     | Delete line               |
| {kbd}`⌘/`      | Toggle (un/)comment line  |

:::

:::{grid-item-card}
:shadow: none

Navigation
^^^

| Shortcut       | Action                    |
|----------------|---------------------------|
| {kbd}`⇧⌘P`     | Command Palette           |
| {kbd}`⌘P`      | Quick Open File           |
| {kbd}`⌘B`      | Toggle Sidebar            |
| {kbd}`⌘J`      | Toggle Panel              |
| {{ ctrltick }} | Toggle Terminal           |

:::

:::{grid-item-card}
:shadow: none

Editor
^^^

| Shortcut       | Reverse        | Action                    |
|----------------|----------------|---------------------------|
| {kbd}`⌘Enter`  | {kbd}`⇧⌘Enter` | Add line (above, below)   |
| {kbd}`⌥↑`      | {kbd}`⌥↓`      | Move line (up, down)      |
| {kbd}`⇧⌥↑`     | {kbd}`⇧⌥↓`     | Copy line (up, down)      |
| {kbd}`⌘]`      | {kbd}`⌘[`      | (Indent, Outdent)         |
| {kbd}`⌘Z`      | {kbd}`⇧⌘Z`     | (Undo, Redo)              |


:::

:::{grid-item-card}
:shadow: none
:class-card: border-0
:class-body: p-0

```{dropdown} Key

|       |                    |
|-------|--------------------|
| `⌘`   | {kbd}`Command`     |
| `⌃`   | {kbd}`Control`     |
| `⌥`   | {kbd}`Option`      |
| `⇧`   | {kbd}`Shift`       |
| `↑`   | {kbd}`Up arrow`    |
| `↓`   | {kbd}`Down arrow`  |

```

:::

:::::
% /grid

`````
% /MacOS tab

`````{tab} Windows/Linux

:::::{grid}
:gutter: 2

:::{grid-item-card}
:shadow: none

Editor
^^^

| Shortcut       | Action                    |
|----------------|---------------------------|
| {kbd}`⌃L`      | Select line               |
| {kbd}`⇧⌃K`     | Delete line               |
| {kbd}`⌃/`      | Toggle (un/)comment line  |

:::

:::{grid-item-card}
:shadow: none

Navigation
^^^

| Shortcut       | Action                      |
|----------------|-----------------------------|
| {kbd}`⇧⌃P`     | Command Palette             |
| {kbd}`⌃P`      | Quick Open File             |
| {kbd}`⌃B`      | Toggle Sidebar              |
| {kbd}`⌃J`      | Toggle Panel                |
| {{ ctrltick }} | Toggle Terminal             |

:::

:::{grid-item-card}
:shadow: none

Editor
^^^

| Shortcut       | Reverse        | Action                    |
|----------------|----------------|---------------------------|
| {kbd}`⌃Enter`  | {kbd}`⇧⌃Enter` | Add line (above, below)   |
| {kbd}`Alt↑`    | {kbd}`Alt↓`    | Move line (up, down)      |
| {kbd}`⇧Alt↑`   | {kbd}`⇧Alt↓`   | Copy line (up, down)      |
| {kbd}`⌃]`      | {kbd}`⌃[`      | (Indent, Outdent)         |
| {kbd}`⌃Z`      | {kbd}`⇧⌃Z`     | (Undo, Redo)              |

:::


:::{grid-item-card}
:shadow: none
:class-card: border-0
:class-body: p-0

```{dropdown} Key

|       |                    |
|-------|--------------------|
| `⌃`   | {kbd}`Control`     |
| `⇧`   | {kbd}`Shift`       |
| `↑`   | {kbd}`Up arrow`    |
| `↓`   | {kbd}`Down arrow`  |

```
% /dropdown

:::

`````
% /Windows/Linux tab

```````
% /tab-set

:::{seealso}

* [Getting Started > Default Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings#_default-keyboard-shortcuts)
* (PDF) Keyboard shortcuts for [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf), [Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
* Commands
  - {guilabel}`Help: Keyboard Shortcuts Reference`
  - {guilabel}`Preferences: Open Default Keyboard Shortcuts (JSON)`
  - {guilabel}`Preferences: Open Keyboard Shortcuts (JSON)`
  - {guilabel}`Preferences: Open Keyboard Shortcuts`

:::


Extensions
----------

Install the [python-class extension pack](https://marketplace.visualstudio.com/items?itemName=alissahuskey.vscode-python-class).

Suggested Settings
------------------

Below are some of the settings that I prefer and recommend. Each section
includes a description of what the change will do followed by the setting(s)
to change.

### Instructions

You can change your settings by either modifying your {file}`settings.json`
file or using the Settings UI, whichever you find easiest.

:::::{tab-set}

`````{tab-item} Settings (JSON)

On the left side of each section is a JSON dictionary containing the relevant
settings for the {file}`settings.json` file.

Add the contents of the dictionary for the setting you want to change from this
document into the dictionary in your {file}`settings.json` file.

1. Use the {guilabel}`Preferences: Open Settings (JSON)` command from the
   command palette to open your {file}`settings.json` file.

2. Make sure there's a `,` at the end of the last line inside the dictionary in
   the {file}`settings.json` file.

3. Copy the the part of the JSON from this document that is inside the `{` `}`.

4. Paste it inside the dictionary in the {file}`settings.json` file, just above
   the last `}` in the file.

`````

`````{tab-item} Settings (UI)

On the right side of each section is a list of relevant settings from the
Settings UI.

Each shows the category that the setting is listed under from left of the
Settings UI followed by the setting name and value.

```{image} assets/vscode-settings-ui.png
:class: mb-4
```

1. Use the {guilabel}`Preferences: Open Settings (UI)` command from the
   command palette.

2. Copy the setting title from this document and paste it in the
   {guilabel}`Search settings` input box.
   > You can confirm that it is the correct setting by checking the categories on
   > the left of the Settings UI against the path listed to the setting in this
   > document.

3. Change the value of the setting to match value show on the right of the
   setting in this document.

`````

:::::

```{seealso}

* [User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)

```


### Hide Open Editors

In the {file}`Explorer` don't show the "open editors" section.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                |     |
|----------------------------------------------------------------|-----|
| {menuselection}`Features --> Explorer › Open Editors: Visible` | `0` |

````

```{code-block} javascript
:caption: settings.json
{
    "explorer.openEditors.visible": 0
}
```

{{ clear }}

---

### Minimap

Make the minimap prettier and hide it by default. (You can open it using the
{guilabel}`View: Toggle Minimap` command.)

````{sidebar} Settings (UI)
:class: no-headings

|                                                             |                           |
|-------------------------------------------------------------|---------------------------|
| {menuselection}`Text Editor --> Minimap -->`                | ` `                       |
| `   ` {menuselection}`Editor › Minimap: Enabled`            | <input type="checkbox"> |
| `   ` {menuselection}`Editor › Minimap: Render Characters`  | <input type="checkbox"> |
| `   ` {menuselection}`Editor › Minimap: Max Column`         | `200`                     |
| `   ` {menuselection}`Editor › Minimap: Show Slider`        | `always`                  |

````

```{code-block} javascript
:caption: settings.json
{
    "editor.minimap.enabled": false,
    "editor.minimap.renderCharacters": false,
    "editor.minimap.maxColumn": 200,
    "editor.minimap.showSlider": "always"
}
```

{{ clear }}

---

### Reduce preview mode

When opening files via Quick Open ({kbd}`⌘P` / {kbd}`⌃P`) don't start in [preview mode](https://code.visualstudio.com/docs/getstarted/userinterface#_preview-mode).

````{sidebar} Settings (UI)
:class: no-headers

|                                                                                                         |     |
|---------------------------------------------------------------------------------------------------------|-----|
| {menuselection}`Workbench --> Editor Management --> Workbench › Editor: Enable Preview From Quick Open` | <input type="checkbox"> |

````

```{code-block} javascript
:caption: settings.json
{
    "workbench.editor.enablePreviewFromQuickOpen": false
}
```

{{ clear }}

---

### Autosave

Enable auto-save.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                        |              |
|------------------------------------------------------------------------|--------------|
| {menuselection}`Text Editor --> Files --> Files: Auto Save`            | `afterDelay` |

````

```{code-block} javascript
:caption: settings.json
{
    "files.autoSave": "afterDelay"
}
```

{{ clear }}

---

### Disable notices

Disable tips and startup pages.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                          |                         |
|--------------------------------------------------------------------------|-------------------------|
| {menuselection}`Workbench --> Workbench: Startup Editor`                 | `none`                  |
| {menuselection}`Workbench --> Appearance --> Workbench › Tips: Enabled`  | <input type="checkbox"> |
| {menuselection}`Extensions --> Python --> Python: Show Start Page`       | <input type="checkbox"> |

````

```{code-block} javascript
:caption: settings.json
{
    "workbench.startupEditor": "none",
    "workbench.tips.enabled": false,
    "python.showStartPage": false
}
```

{{ clear }}

---


### Live Share

Don't add Live Share guests names to your git commit messages.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                                                  |         |
|--------------------------------------------------------------------------------------------------|---------|
| {menuselection}`Extensions --> Visual Studio Live Share --> Liveshare: Populate Git Co Authors`  | `never` |

````

```{code-block} javascript
:caption: settings.json
{
    "liveshare.populateGitCoAuthors": "never"
}
```

{{ clear }}

---

### Highlight cursor line

In the editor highlight the line your cursor is currently on.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                      |                                 |
|----------------------------------------------------------------------|---------------------------------|
| {menuselection}`Text Editor -->`                                     | ` `                             |
| `   ` {menuselection}`Editor: Render Line Highlight`                 | `all`                           |
| `   ` {menuselection}`Editor: Render Line Highlight Only When Focus` | <input type="checkbox" checked> |

````

```{code-block} javascript
:caption: settings.json
{
    "editor.renderLineHighlight": "all",
    "editor.renderLineHighlightOnlyWhenFocus": true
}
```

{{ clear }}

---

### Disable suggestions

Suggestions are a great feature but they may interfere with retaining
information as you're learning. They can make the interface a bit noisy. These
settings disable them, though they can still be triggered using a shortcut key.

````{sidebar} Settings (UI)
:class: no-headers

|                                                                      |                         |
|----------------------------------------------------------------------|-------------------------|
| {menuselection}`Text Editor --> Editor › Parameter Hints: Enabled`   | <input type="checkbox"> |
| {menuselection}`Text Editor --> Suggestions`                         | ` `                     |
| `   ` {menuselection}`Editor: Suggest On Trigger Characters`         | <input type="checkbox"> |
| `   ` {menuselection}`Editor: Quick Suggestions`                     | [^json]                 |
| `   ` {menuselection}`Editor: Accept Suggestion On Commit Character` | <input type="checkbox"> |

````

```{code-block} javascript
:caption: settings.json
{
    "editor.acceptSuggestionOnCommitCharacter": false,
    "editor.suggestOnTriggerCharacters": false,
    "editor.parameterHints.enabled": false,
    "editor.quickSuggestions": {
        "other": false,
        "comments": false,
        "strings": false
    },
}
```

{{ clear }}

[^json]: edit in {file}`settings.json`

---


### Git

Automatically fetch updates from the default remote of the current Git
repository.


````{sidebar} Settings (UI)
:class: no-headers

|                                                        |        |
|--------------------------------------------------------|--------|
| {menuselection}`Extensions --> Git --> Git: Autofetch` | `true` |

````

```{code-block} javascript
:caption: settings.json
{
    "git.autofetch": true,
}
```

{{ clear }}

---

Themes
------

### Dark

* [One Dark Pro Monokai Darker](#one-dark-pro-monokai-darker)
* [Dolch Dark](#dolch-dark)
* [Verdandi Alter Customized](#verdandi-alter-customized)
* [Azure Dark](#azure-dark)
* [Black Ocean](#black-ocean)

{{ theme | replace("NAME", "One Dark Pro Monokai Darker") | replace("ID", "eserozvataf.one-dark-pro-monokai-darker") }}

{{ theme | replace("NAME", "Dolch Dark") | replace("ID", "be5invis.theme-dolch") }}

{{ theme | replace("NAME", "Verdandi Alter Customized") | replace("ID", "Shirayuki.verdandi-alter-customized") }}

{{ theme | replace("NAME", "Azure Dark") | replace("ID", "eddyw.azure-dark-theme") }}

{{ theme | replace("NAME", "Black Ocean") | replace("ID", "zamerick.black-ocean") }}

### Medium

* [Nord Extra Dark](#nord-extra-dark)
* [Subliminal](#subliminal)
* [Pretentious Name](#pretentious-name)
* [Mario Color](#mario-color)

{{ theme | replace("NAME", "Nord Extra Dark") | replace("ID", "yamenarahman.nord-extra-dark") }}

{{ theme | replace("NAME", "Subliminal") | replace("ID", "gaearon.subliminal") }}

{{ theme | replace("NAME", "Pretentious Name") | replace("ID", "zhiayang.pretentious-name") }}

{{ theme | replace("NAME", "Mario Color") | replace("ID", "alphatr.mario-theme") }}

### Light

* [One Dark Raincoat Light](#one-dark-raincoat-light)
* [Dolch Light](#dolch-light)

{{ theme | replace("NAME", "One Dark Raincoat Light") | replace("ID", "ginfuru.ginfuru-onedark-raincoat-theme") }}

{{ theme | replace("NAME", "Dolch Light") | replace("ID", "be5invis.theme-dolch") }}

[One Dark Pro Monokai Darker]: ../assets/monokai-darker.png
[Dolch Dark]: https://raw.githubusercontent.com/be5invis/vscode-theme-dolch/master/images/dolch.png
[Verdandi Alter Customized]: ../assets/verdandi.png
[Azure Dark]: https://raw.githubusercontent.com/eddyw/vscode-azuredark-theme/master/themes/screenshot.png
[Black Ocean]: https://raw.githubusercontent.com/Zamerick/black-ocean/master/img/BlackOcean.png
[Nord Extra Dark]: ../assets/nord.png
[Subliminal]: https://raw.githubusercontent.com/gaearon/subliminal/master/screenshot.png
[Pretentious Name]: ../assets/pretentious.png
[Mario Color]: ../assets/mario.png
[One Dark Raincoat Light]: ../assets/raincoat-light.png
[Dolch Light]: ../assets/dolch-light.png

