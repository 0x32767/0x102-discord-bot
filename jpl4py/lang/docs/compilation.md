# How are jpl files executed?

JPL tries to save execution time by being semi interpreted. Instead of following the regular interpreted language structure of:

- lexing
- parse tree
- checking
- execution

My language is sudo compiled to a json file where the checked parse tree is stored. This json file is then executed by the jpl engine. This is a way to keep tha language as simple as possible and optimize it for speed. JSON files being easily readable and editable makes it easy to edit the parse tree and change the behavior or features of the program. This would also make importing easier by looking up the function in another parse tree. This is how I intend to implement built-in functions.
