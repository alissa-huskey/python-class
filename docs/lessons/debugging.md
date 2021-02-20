Using a Debugger
================

In the [](reading-code.md) lesson we learned how to walk through code step by
step and figure out how a line is evaluated and what the value of a variable
is are at a given point.

Thinking through code like this is a fundamental skill to develop. However,
there's also a tool that we can use to do this process called. Usually it's
used for figuring out problems in code, which is why it's called a debugger.

A debugger allows you to run a program normally until you reach a particular
point you want to know more about. Then the program is paused so you can see
what is in the scope at that point and experiment with code in the context of
that line. From there you can go forward or backwards in the code or continue
on until the next breakpoint.

Part 1: Setup
-------------

### Step 1: Create Hello World

In VS Code, create a file named {file}`hello_world.py` and paste the
following code and save it.

```{code-block} python
:linenos:
:caption: hello_world.py
msg = "Hello World"
print(msg)
```

### Step 2: Configure

The first time you run the debugger for a particular project you'll need to
configure it for that project. These settings are saved in the
{file}`.vscode/launch.json` file which can be generated for you.

I. Click the {guilabel}`Run` icon on the activity bar to show the
{guilabel}`Run` view in the sidebar.

![](https://code.visualstudio.com/assets/docs/editor/debugging/run.png)

II. Click the {guilabel}`create a launch.json file` link.

![](https://code.visualstudio.com/assets/docs/python/debugging/debug-start.png)

III. Select {guilabel}`Python File` from the menu that appears under the Command
Palette.

![](https://code.visualstudio.com/assets/docs/python/debugging/debug-configurations.png)

The {file}`launch.json` file will be created and opened for you.

![](https://code.visualstudio.com/assets/docs/python/debugging/configuration-json.png)

IV. Add a comma to the end of the line that starts with `"console"`, then add a
new line `"redirectedOutput": true`.

```{code-block} javascript
:caption: launch.json
:linenos:
:emphasize-lines: 12-13
{
	// Use IntelliSense to learn about possible attributes.
	// Hover to view descriptions of existing attributes.
	// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Current File",
			"type": "python",
			"request": "launch",
			"program": "${file}",
			"console": "integratedTerminal",
			"redirectOutput": true
		}
	]
}
```

```{warning}

The `launch.json` file is JSON, which looks a lot like Python but does have
some differences. The things you need to know for now are:

* Single quotes are not allowed for strings. Be sure to use double quotes (`"`)
  around `redirectedOutput`.
* `true` should be all lowercase, not capitalized

```

V. Save the file then close it.

Part 2: Run the debugger
------------------------

### Step 1: Add a breakpoint

The debugger will run the program normally until it hits a
{term}`breakpoint`, the place where we tell it to pause the program. Without
any breakpoints the program will run normally. So we'll start by adding a
breakpoint.

Hover over the gutter on line `2` just to the left of the line number until
you see a dim red dot. To add a breakpoint click the dot. It will change to
solid red and stay there after you move your cursor.

![](https://code.visualstudio.com/assets/docs/python/tutorial/breakpoint-set.png)

### Step 2: Start the debugger

```{admonition} Shortcut Key
:class: tip

| macOS      | Windows      | Command                        |
|------------|--------------|--------------------------------|
| {kbd}`F5`  |  {kbd}`F5`   | Debug: Start Debugging         |

```

I. Click the {guilabel}`Run` icon on the activity bar to open the
   {guilabel}`Run` view in the sidebar.

![](https://code.visualstudio.com/assets/docs/editor/debugging/run.png)



II. Next to the {guilabel}`RUN` sidebar title you will see the launch
    configuration you just created.Click the play button to the left of
    {guilabel}`Python: Current File`.

![](assets/debug-start.png)

### Step 3: Open the debug console

```{admonition} Shortcut Key
:class: tip

| macOS      | Windows      | Command                        |
|------------|--------------|--------------------------------|
| {kbd}`⇧⌘P` |  {kbd}`⇧⌃P`  | Debug Console                  |

```

Once you've started the debugger, click the {guilabel}`DEBUG CONSOLE` in the
bottom panel.

Part 3: Overview
----------------

![](assets/debug-parts-marked.png)

```{centered} Debug Toolbar
```

* **Continue**
* **Step**
* **Step In**
* **Step Out**
* **Restart**
* **Stop**

```{centered} Editor
```

* current line
* add to watch
* current value of variable

```{centered} Run Activity Bar Icon
```

* breakpoint count

```{centered} Run sidebar
```

* **Variables** -- lists the the variables that are defined at this point in
  the code execution, just like the Variables box from the [](reading-code.md)
  lesson

* **Watch** -- 

* **Call Stack** -- shows where you are in the code stack.

* **Breakpoints** -- lists your breakpoints and tools for managing them.

```{centered} Debug console
```

* **Input**
* **Output**

```{centered} Debug status
```

* **Input**
* **Output**

### Step 3: Variables

The debugger will stop at the first breakpoint in the program, and you will
see a yellow arrow next to that line in your file.

The {guilabel}`Variables` section in the sidebar shows you the variables that
are defined at this point in the code execution, just like the Variables box
from the [](reading-code.md) lesson.

![](https://code.visualstudio.com/assets/docs/python/tutorial/debug-step-02.png)

The variables has two sections.

The {guilabel}`Globals` section lists variables defined in the {term}`global scope`.
 Your global variables will be listed here and so will any modules you've
 imported.

The {guilabel}`Locals` section lists variables defined in the {term}`local scope`.
This is where you will find variables that are inside of the function
currently being run.

Since our script has no functions, the global scope is the same as the local
scope. You will see the the `msg` variable listed both places the value of
`"Hello World"`.

Part 3: Navigation
------------------

### Step 5: Stepping through the code

#### Step 5.1: Add some lines

This file is a bit too short to step through so let's make it a tad more
interesting. Add the following lines.

```{code-block} python
:linenos:
:caption: hello_world.py
:emphasize-lines: 4-8
msg = "Hello World"
print(msg)

msg = "It's a lovely day for coding, isn't it?"
print(msg)

msg = "Farewell."
print(msg)
```

Save the file, then add breakpoints to lines `5` and `8`.

#### Step 5.2: The debug toolbar

When the debugger is running you will see the debug toolbar.

![](https://code.visualstudio.com/assets/docs/python/tutorial/debug-toolbar.png)

For now you only need to worry about these three buttons.

| Button               | Shortcut   | Action                               |
|----------------------|------------|--------------------------------------|
| ![debug-continue][]  | {kbd}`F5`  | Continue to the next breakpoint      |
| ![debug-step-in][]   | {kbd}`F11` | Step down in the program             |
| ![debug-stop][]      | {kbd}`⇧F5` | Stop the debugger                    |


[debug-continue]: assets/debug-continue.png
[debug-step-in]: assets/debug-step-in.png
[debug-stop]: assets/debug-stop.png

Now that we have a few more lines of code to walk through, hit the 

### Step 5: Run code in the local context

Let's say we want to play around with the `msg` variable. For that we can use
the {guilabel}`Debug Console`.

From the bottom pane click the {guilabel}`Debug Console` header.

At the bottom of the pane you will see a prompt that works just like a Python
shell, but in the context of the current line. The results will appear in the
pane above the prompt.

In this case we have the `msg` variable defined. Let's play around with that
variable by typing the following three lines one at a time.

```python
msg
msg.capitalize()
msg.split()
```

![](https://code.visualstudio.com/assets/docs/python/tutorial/debug-step-03.png)


See Also
--------

```{seealso}

* [VS Code User Guide > Debugging](https://code.visualstudio.com/docs/editor/debugging)
* [VS Code > Python > Debugging](https://code.visualstudio.com/docs/python/debugging)

```


Glossary
--------

```{glossary} programming-concepts

breakpoint

  A place for the debugger to pause the program.

```

---

* [ ] debugging terms
	  * [ ] breakpoint
* [ ] debugger in vs code
	* [ ] run view from activity bar


	* [ ] debugger actions
		* [ ] continue/pause
		* [ ] step over
		* [ ] step over
		* [ ] step into
		* [ ] step out

	* [ ] variables
			* changing variables
	* [ ] call stack
	* [ ] debug console
