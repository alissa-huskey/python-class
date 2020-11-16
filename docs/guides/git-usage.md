Git Usage
=========

Quickref: Review, Commit & Push Steps
-------------------------------------

Reviewing your changes then committing and pushing them is kind of like a fancy
`ctrl+s`--that is, a best practice to get in the habit of doing so regularly
that it becomes automatic. This process should happen at the end of any
significant change and definitely before you walk away from your code. You can go
to bed angry, just don't go to bed without committing and pushing your code.

Here are the steps to follow in Repl.it.

**In the Console**

1. `git status` : Review which files have changed to make sure there is nothing unexpected.
2. `git add .` : Stage all changes.
3. `git status` : Sanity check to ensure that all changes are now staged.
4. `git diff --staged` : Review your changes to check for mistakes.
    Make any neccessary change then repeat from step 1.

**In Repl.it**

5. Commit & Push : In Repl.it:
   - Click the ![fork](assets/code-branch.png) **Version Control** link in the left-nav.
   - Add a brief description of your changes in the **What did you change?** text area.
   - Click **commit & push**.
