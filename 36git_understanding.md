What does each command do?

git checkout main -- <file>:
This will replace your local file with the version from main, all other files in your branch stay the same

git cherry-pick <commit>:
lets you take an individual commit from one branch and apply it to another branch.
for example, You're working on branch1, but a critical bug fix was committed to main.
You want to apply only that bug fix to your branch without merging all changes from main.

git log:
shows the history of commits in your repository, including details like commit hashes, authors, dates, and messages.

git blame <file>: 
shows who last modified each line in a file and when. This is useful for tracking changes and understanding the history of a file.

When would you use it in a real project (hint: these are all really important in long running projects with multiple developers)?

git checkout main -- <file>:
You're working on a branch and made changes to a file (md,py or so on),
but you realize you want to revert it back to the version from main without touching other files(you need to have the original version in main.)

git cherry-pick <commit>:
Suppose a teammate fixed a critical bug on main with commit hash, but you're working on a separate branch and don’t want all of main’s changes.

git log:
A bug appears in code, and you need to find when the bug is added.

git blame <file>:
Identifying who modified a certain chuck of code.

What surprised you while testing these commands?

I think git log and blame <file> are the most surprising commands because the combination of these two can clearly find out any edition history of the repo.
Which is really powerful in tracking progress.
