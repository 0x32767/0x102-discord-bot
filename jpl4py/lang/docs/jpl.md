# The JPL programing language

## Introduction

JPL is a programing language that has c like syntax. The language is designed to be the easiest language with a c api and python call api. JPL is also emendable in python so that you can directly edit the environment.

## features

JPL is a very minimal language inspired by c.

### keywords

| Keyword | name     | Example                             |
| ------- | -------- | ----------------------------------- |
| for     | for loop | for ($i=0; i<=10; i++>) { print i } |
| if      | if       | if ($i==0) { print "zero" }         |
| else    | else     | else { print "not zero" }           |
| jfn     | JPL func | jfn name($args) { code }            |
| cfn     | C func   | cfn name($args) {" C-code "}        |

### primitive types

| Type | name    | Example   |
| ---- | ------- | --------- |
| num  | number  | $i = 0    |
| str  | string  | $s = ""   |
| bool | boolean | $b = true |
| null | null    | $n = null |
| list | list    | $l = []   |

> #### **variables**

All variables are prefixed with $, when being assigned or referenced. This makes the code more explicit in terms of variables. Variables can not be assigned to functions, only the primitive types are allowed.

> #### **for**

For loops are virtually identical to c for loops. But fields can not boe blank.

```jpl
for ($i=0; i<=10; i++) {
    // do stuff
}
```

> #### **if**

If statements also follow the convention of c. However, conditions must evaluate to a boolean and can not be booleans.

```jpl

if ($i==0) {
    print("zero")
} else {
    print("not zero")
}

```

> #### **else**

Else is a keyword that is added to the end of an if statement.

```jpl
if ($i==0) {
    print("zero")
} else {
    print("not zero")
}
```

> #### **jfn**

JPL functions can only be called from jpl and python, not from c. The syntax also follows the convention of c but with no type annotations. JFN functions also can not have explicit return types.

```jpl
jfn name($arg1, $arg2) {
    // do stuff
}
```

> #### **cfn**

C functions can be called from jpl and python, c functions can not call jpl functions, python functions or other c functions. The syntax follows the convention of c but with c code as the function content as a string.

```jpl
cfn name<int>() {"
    int a = 10;
    int b = 20;

    return a + b;
"}
```

> ### **syntax**

The syntax of this language is very limiting and can be tedious, but this will be improved in the feature.

## If statements

If statements have very little freedom in terms of the language. When an if statement is declared it needs to be immediately followed by an else statement. Nesting if statements are allowed so this would just lead to a lot of nesting. If statements can also be empty.

```jpl
if ($i==0) {
    print("zero")
} else {
    if ($i==1) {
        print("one")
    } else {
        print("not one")
    }
}
```
