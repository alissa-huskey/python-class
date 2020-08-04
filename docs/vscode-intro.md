VS Code Intro
=============


Reference
---------

* [Official Documentation](https://code.visualstudio.com/docs)
* [Documentation on readthedocs.io](https://vscode.readthedocs.io/en/latest/)
* [Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)


User Interface
--------------

**Layout**

![layout](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

* *(A) Activity Bar*: Links to open and close panels. 
* *(B) Side Bar*: The panel where activity bar links are opened.
* *(C) Editor Groups*: Where you edit your files
* *(D) Panel*: Panels for interacting with your code live here, notibly the Terminal.
* *(E) Status Bar*: Information and links related to your current open files and state.

**Sidebar** [ Cmd/Ctrl + B]
* File Explorer [ Ctrl/Cmd+Shift+E ]
  - Workspace: File Browser
  - Outline: TOC for open file (headers, functions, etc)
  - Timeline: File History
* Source Control: Git tools
* Extensions [ Cmd/Ctrl+Shift+X ]: Manage extensions
* Live Share: Manage LiveShare Sessions

> _Note_ I keep hidden: Run, Search

**Panel** [ Cmd/Ctrl +J ]
* Terminal [ Cmd/Ctrl + ` ]: Access the operating systemm command line.
* Problems: Display errors
* Output: View the output of the code you ran
* Debug: Run your code

**Editor**
* Tabs
  - Preview Mode: (shown in italics) A file was opened reusing an existing tab (single-click from File Browser.)
  - Unsaved Changes (shown with a white dot)


Tools
-----

* Command Palette [ Ctrl/Cmd+Shift+P ]: - Run VS Code commands
* Quick Open [ Ctrl/Cmd+P ]: - Open files
* Zen Mode [ Ctrl/Cmd, Z ]: Hide all panels except editor. [ Esc, Esc ] To exit

Editor
------

### Breadcrumbs
![breadcrumbs](https://code.visualstudio.com/assets/docs/getstarted/userinterface/breadcrumbs.png)

### Minimap
![minimap](https://code.visualstudio.com/assets/docs/getstarted/userinterface/minimap.png)

### Keyboard Shortcut

* `Cmd/Ctrl+/`: Toggle comment out line
* `shift+cmd+k`: Delete Line
* `Cmd/Ctrl+` ( `[` | `]` ): Decrease | Increase indentation
* `Alt/Option+` ( `Up` | `Down` ): Move line above | below
* `Shift+Alt/Option+` ( `Up` | `Down` ): Copy line above | below
* `Cmd/Ctrl+Enter`: Insert line after
* `Shift+Cmd/Ctrl+Enter`: Insert line Before
* `Cmd/Ctrl+J`: Join lines

Recommended Extensions
----------------------

* [LiveShare](https://marketplace.visualstudio.com/items?itemName=ms-vsliveshare.vsliveshare)
* [LiveShare Audio](https://marketplace.visualstudio.com/items?itemName=ms-vsliveshare.vsliveshare-audio)
* [Editor Config](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
  Ensures consistent code formatting.

  Create a file in your project dir or home dir named `.editorconfig` and append at least the following:

```ini
root = true

[*.py]
indent_style = space
indent_size = 4
```

Recommended Settings
--------------------

`Ctrl+Shift+P` > `Preferences: Open Settings (JSON)`

```json
{
    "files.trimTrailingWhitespace": false, // interfers with EditorConfig extension
    // Suggestions ---------------------------------------------------------------------
    //   disable auto suggestions, but they can still be triggered with alt+esc or ctrl+space
    //
    "editor.suggestOnTriggerCharacters": false,
    "editor.parameterHints.enabled": false,
    "editor.quickSuggestions": {
        "other": false,
        "comments": false,
        "strings": false
    },
    // Explorer ------------------------------------------------------------------------
    //   Don't show the "open editors" section in the Explorer
    //
    "explorer.openEditors.visible": 0,
    // minimap -------------------------------------------------------------------------
    //   Make the minimap prettier and hide it by default
    //   (open with `View: Toggle Minimap`)
    //
    "editor.minimap.enabled": false,
    "editor.minimap.renderCharacters": false,
    "editor.minimap.maxColumn": 200,
    "editor.minimap.showSlider": "always",
    // Python -------------------------------------------------------------------------
    //
    "python.showStartPage": false,
    "python.workspaceSymbols.exclusionPatterns": [
        "**/site-packages/**",
        "__pycache__/"
    ],
    // misc ----------------------------------------------------------------------------
    //
    // cmd+P: don't open files in preview mode
    "workbench.editor.enablePreviewFromQuickOpen": false,
}
```

Recommended Themes
------------------

[ Cmd/Ctrl+K, Cmd/Ctrl+T ] To Change Themes

Dark
* [One Dark Pro Monokai Darker](https://marketplace.visualstudio.com/items?itemName=eserozvataf.one-dark-pro-monokai-darker)
* [Dolch Dark](https://marketplace.visualstudio.com/items?itemName=be5invis.theme-dolch)
* [Verdandi](https://marketplace.visualstudio.com/items?itemName=Shirayuki.verdandi-alter-customized)
* [Azure Dark](https://marketplace.visualstudio.com/items?itemName=eddyw.azure-dark-theme)
* [Black Ocean](https://marketplace.visualstudio.com/items?itemName=zamerick.black-ocean)
* [Nord Extra Dark](https://marketplace.visualstudio.com/items?itemName=yamenarahman.nord-extra-dark)

Medium
* [Subliminal](https://marketplace.visualstudio.com/items?itemName=gaearon.subliminal)
* [Pretentious Name](https://marketplace.visualstudio.com/items?itemName=zhiayang.pretentious-name)
* [Mario Color](https://marketplace.visualstudio.com/items?itemName=alphatr.mario-theme)

Light
* [One Dark Raincoat Light](https://marketplace.visualstudio.com/items?itemName=ginfuru.ginfuru-onedark-raincoat-theme)
* [Dolch Light](https://marketplace.visualstudio.com/items?itemName=be5invis.theme-dolch)
