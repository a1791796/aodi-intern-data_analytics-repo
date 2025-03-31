What is the difference between staging and committing?

Staging: Moves changes to the staging area, preparing them for the next commit, changes are not yet saved in the repo.
Committing: Takes all staged changes and saves them in the local repo with a commit message.

Why does Git separate these two steps?

When it's separated into two steps, you can make any changes and then do staging because it saves your change in the index. Commit it after you finalise the file which is very effective. For example: group related changes together in a single commit. If you're working on multiple tasks or features, you can commit each one separately with meaningful messages.


When would you want to stage changes without committing?

You might be working on multiple featuresat the same time. By staging your changes separately, you can group related changes into a logical commit.
prepare for future commits, stage as you go, but commit when ready.
