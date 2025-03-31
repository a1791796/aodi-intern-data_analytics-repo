What code smells did you find in your code?

Deeply nested conditionals, then I refactor it with guard clauses.
Commented-out code, I delete the unused code and comment this code.
Inconsistent naming, I always use a single letter as variable because of lazy, but makes code difficult to understand when lots of code.

How did refactoring improve the readability and maintainability of the code?

meaningful names make the code easier to understand.
Deeply nested conditionals were replaced with guard clauses, making it easier to follow.
Breaking long functions into smaller, short functions makes the logic clearer.
Eliminating commented-out code and magic numbers ensures that developers don’t need to think about the unclear logic.

How can avoiding code smells make future debugging easier?

Readable variable and function names mean developers don’t have to guess what a variable represents.
Avoiding deeply nested conditionals makes it easier to follow decision paths.
Shorter functions make it easier to isolate and fix issues.
