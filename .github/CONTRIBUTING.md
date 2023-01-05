# Contributing

## Pull requests

Before submitting a pull request make sure that the code is formatted with the "black" formatter <https://github.com/psf/black>. Also please ensure that the code adheres to the conventions highlighted in the docs folders. Also please reed on the naming conventions for git commits.

## Naming commits

I have now addopted a new way of naming commits, commits should follow the following format **[< type-of-commit >] < what you did > \n\n < what to do next >** e.g **[bugfix] fixed bug that crashes bot \n\n add typehinting to patch**. The "what you did" should be in the past tense, and the "wat to do next" should be in preasent of future.

### Type of commit

The types of commit can be one of the following:

| abreviation | description                       |
| ----------- | --------------------------------- |
| bugfix      | you fixed a bug                   |
| bugpatch    | made a temperary fix to a problem |
| newcog      | you added a new cog to the bot    |
| newcmnd     | you added a new command to a cog  |
| newdocs     | added more documentation          |
| newfile     | you added a new file              |
| rfcog       | you refactored a cog              |
| rfcmd       | refactored a cog                  |
| upcmd       | updated a command                 |
| upcog       | updated a cog                     |
| updocs      | updated docs                      |
| uppatch     | updated a patch                   |
| misc        | made a small change e.g spelling  |
