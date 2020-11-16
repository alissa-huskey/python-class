Git on Repl.it
==============

* [Introduction](#introduction)
* [Part 1: First Create a Github Account](#part-1-first-create-a-github-account)
* [Part 2: Connect it to your Repl.it](#part-2-connect-it-to-your-replit)
* [Part 3: Update the Repl.it Github Authorization](#part-3-update-the-replit-github-authorization)
* [Part 4: Review your changes](#part-4-review-your-changes)
* [Part 5: Commit &amp; Push Your Code](#part-5-commit--push-your-code)
* [Congratulations!](#congratulations)


Introduction
-----------------

***Version control*** refers to a system for keeping track of and managing
changes to a set of files. The most popular ***version control system*** today
is `git`, which is what we will be using.

Version control can be used for any text-based files (school work, essays,
books, manuals) but in software we're tracking changes to code and we refer to
the group of source code files for any particular project as a ***codebase***.
The set of version control data for a codebase or other group of of files is
called a ***repository*** or ***repo***.

Version control can take a bit of getting used to, but it is one of those
life-changing tools that you'll wonder how you ever lived without. Some of the
benefits include:

* Keep a remote backup of all of your work.
* Easily see what changes you have made since you were last working on a file.
* Review an older version of your work, or revert back to it.

[Github](http://github.com/) is a service that provides hosting for git repos.
Repl.it has an integration with Github that tucks away a lot of the complexity
behind a web interface.


Part 1: First Create a Github Account
-------------------------------------

1. Create an account on [Github.com](http://github.com) or sign into your
   existing account.


Part 2: Connect it to your Repl.it
----------------------------------

1. Open your your Repl.it repl.

2. On the left side-nav click the second icon down: ![fork](assets/code-branch.png)
   **Version Control**.

3. At the top of the new left-most pane, click the button that says **Connect
   to...**

4. It will ask you to Connect to Github. Click the button that says **Connect
   Repl.it to your GitHubAccount**

5. A new page will appear titled **Install & Authorize Repl.it Online IDE**.
   Click Save.

6. The new window will close and you'll be back at your repl. Click the
   **Connect to...** button again.

7. A dialog will appear titled **Create a new GitHub repository**. Choose a repo
   name (perhaps "python-class"?) and click **Create GitHub repository**.


Part 3: Update the Repl.it Github Authorization
-----------------------------------------------

When you authorized Repl.it for Github, you gave it blanket access to all
current and future repos. Now that the repo is created, you can change the
settings so that Repl.it only has access to that repo.

(You can skip this step if you don't care.)

1. Go to github.com

2. In the top right corner, click your avatar to bring up the user menu.

3. Click the **Settings** link.

4. On the left side, click the **Applications** link.

5. Under **Installed Github Apps** you should see **Repl.it Online IDE.**. Click
   the **Configure** button.

6. Under **Repository Access**, select the radio button next to **Only select
   repositories**.

7. Click the **Select repositories** drop-down. Click your newly created
   repository.

8. Click the **Save** button.


Part 4: Review your changes
---------------------------

The web interface does not include any features to review your changes, so
we'll have to use the command line.

(This gives you a chance to get a feel for the benefits of using version
control. But you can skip it for now if you'd prefer.)


#### Use `git status`

The `git status` tool shows you a list of files that have been changed since
your last commit.

##### In the Console

In the right-most Console pane, type:

```bash
> git status
```

You will see a list of the files that have been changed since your last commit.
It will look something like this.

```bash
> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .replit

no changes added to commit (use "git add" and/or "git commit -a")
```

#### Use `git diff`

The `git diff` tool shows the details of what you have changed.

The `diff` tool only shows changes to ***tracked*** files--ones that have been
previously added to your repository. To make sure that all of your changes show
up in the diff, we'll first need to add them.

##### In the Console

In the Console pane type:

```bash
> git add .
> git status
```

You will now see that all files with changes are listed under "Changes to be
committed:"

```bash
> git add .
> git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   .replit
    modified:   main.py
```

When a file is `staged` for commit, that means that it has been chosen to be
included in the commit.

Now you can use the diff tool with the `--staged` flag to review all of the
changes you've made since your last commit.

In the Console pane type:

```bash
> git diff --staged
```

This command will show you a ***diff*** of your changes--that is, a the chunk
of changes from each file that was changed.

```bash
> git diff --staged
diff --git a/.replit b/.replit
new file mode 100644
index 0000000..1acc15c
--- /dev/null
+++ b/.replit
@@ -0,0 +1 @@
+run = "python3 main.py"
\ No newline at end of file
diff --git a/main.py b/main.py
index e69de29..051463d 100644
--- a/main.py
+++ b/main.py
@@ -0,0 +1 @@
+print("hello python class!")
\ No newline at end of file
```

If you notice anything you want to change before you commit and push you can go
and edit the file then repeat the `git add` and `git diff` steps to review it
again.


Part 5: Commit & Push Your Code
-------------------------------

In git a ***commit*** is a record of a set of changes. The repository for your
code exists both on repl.it and on github. In order to update the repo on
github with your commits on repl.it the changes will be ***pushed*** to Github.

1. On the left side-nav, Click the![fork](assets/code-branch.png) **Version
   Control** icon again. In the left-most **Version Control** pane, it should
   now display a link to your newly created repository next to the github icon.

2. In the text-area that says **What did you change?** write a brief description
   of your changes. (If this first commit is a lot of files, you may want to
   put something like `First push from repl.it`. In the future, it's a good
   idea to commit frequently, ideally at logical stopping points.)

3. Click the **commit & push** button. If all goes well, your new commit will
   appear under **Previous Commits** and the **commit & push** button will
   dissappear.


Congratulations!
----------------

You've successfully created a git repository, reviewed your changes, commited
them, and pushed them to github!
