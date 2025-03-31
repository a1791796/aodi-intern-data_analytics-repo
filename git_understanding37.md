What does git bisect do?

When there is a bug in your commit, git biset can find the first bug commit.

When would you use it in a real-world debugging situation?

would use git bisect when a bug appears, and don't know which commit caused it. 
Plus the project has many commits, making it too slow to check manually.The bug isn’t obvious from looking at code changes. 

How does it compare to manually reviewing commits?

it is fast (binary search) and finds the exact commit.
