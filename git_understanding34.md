Why is pushing directly to main problematic?
If multiple people are pushing directly to main, there’s a higher chance of merge. It’s hard to track what’s been changed, who made the changes, or why they were made.
When pushing directly to main, there’s no guarantee that the new code will work well, the code need to be tested and review.

How do branches help with reviewing code?
Each people works on their own branch for a feature or task. This means the changes are isolated from the main branch until they're reviewed and ready to be merged.
If a reviewer sees something that needs improvement or fixes, they can request changes on the branch itself. The developer can then make the changes on the branch without affecting main.

What happens if two people edit the same file on different branches?
If the two people made changes to different parts of the file, Git can usually merge the changes automatically.
If both people edited the same lines or close lines of the file, Git won’t know how to automatically combine them.
It will mark the file as having a merge conflict, then needs to be fixed mannually.
