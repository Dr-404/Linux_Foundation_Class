# Basic Scripting


## Using Multiple Commands

Shell Script had the ability to enter multiple command

use semicolon `;` to run two command together

`whoami ; uname -a`



## Creating Script files

#### Specify the shell you want to use in the `first line` of the file

`#!/bin/bash`

**in normal script line `#` use to comment**

#### Making file with text editor

- You can use any text editor for scripting
- In this example, I use nano as text editor
`nano test.sh`

#### Example code


```
#!/bin/bash
# This scirpt display the data and who's logged on
date
who
```

## How to execue script

#### Checking permission

`ls -l test.sh`

#### Giving Permission to execute the file

`chmod u+x test.sh`

#### Run file

`./test.sh`






