# Basic Linux Command


## 1. Finding Yourself

#### `pwd` 
Print working directory

#### `whoami` 
- As a hacker,
you usually need to have all those privileges to run the programs and
commands you need (many hacker tools won’t work unless you have root
privileges), so you’ll want to log in as root

## 2. Naviating the Linux Filesystem

### Changing Directories with `cd`

`cd .` = `.` (dot) mean current directory

`cd ..` = `..` (dot dot) mean move up one level 

## 3. Listing the Content of a Directory with `ls`

```ls -l``` <br>
`-l` = long listing 

```ls -a``` <br>
`a` = all including hidden file 

## 4. Getting Help and manual

```nmap --help``` <br>

``` man nmap```

## 5. Filtering with grep

``` nmap --help | grep host``

<h1 align="Center">Modifying Files and Directories</h1>

## 1. Creating Files with `cat`

1. `cat > helloworld`
2. Type the text and exit with control+c
3. append the text with `>>` eg `cat >> hellowordl`

## 2. Creating File with `touch`

#### `touch newfile`

- Create new file 
- sometime use to changes details of files such as created or modified time

## 3. Creating file with `echo`

`echo "HelloWorld" > hello.txt`



## 4. Creating a Directory

`mkdir newdirectory`

## 5. Copying a File

`cp oldfile (filepath/newfile)`

`cp oldfile /home/dr404/Desktop/newfile`

## 6. Renaming a File

`mv oldfiel Renamedfile`

## 7. Removing a File

`rm file2remove`

## 8. Removing a Directory

`rmdir dir2remove` or `rm -r dir2remove`



<h1 align="center">Viewing Files</h1>

#### 1. View the file with `cat`

#### 2. View the file with `head` (display first 10 lines of files)

- `head /etc/fonts/fonts.conf` (-20 options mean 20 line)

#### 3. View the file with `tail`

- same as head but show last line

#### 4. Viewing file with `more`

- display file content
- page down with enter
- `more /etc/fonts/font.conf`

#### 5. Viewing files with `less`

- same as more but it better

- use (/) to find words and `q` to quit

#### 6. Numbering the lines with `nl`

- `nl /etc/fonts/fonts.conf`


<h1 align="center">Text Editor</h1>

## 1. GUI text editor

- gedit
- subl (sublime-text)

## 2. CLI text editor

- nano
- vim


<h1 align="center">Finding Stuff</h1>



## Installing required package

`sudo apt install mlocate`

## Finding with `locate`

- locate use a database that is usually update once a day


## Finding with `find`
-more powerful than locate

`find direcotry options expression`

- Example

`find / -type f -name nmap`

```
    d      directory

    f      regular file

```

-  if you want to remove error combine with `2>/dev/null`

## Finding binary

1. `whereis` = locating binary file
eg. `whereis nmap`

2. which = more specific
- return PATH variable
eg. `which nmap`


## Wildcard

1. `?`      = single character 
- (eg. ?at = cat, hat, bat) not (what)

2. `[]`     = characters in square bracket
- Eg [c,b]at = cat, bat

3. `*`      = any characters any length
- Eg. *at = cat, what , bat
 

<h1 align="center"><code>git</code> and <code>pip</code></h1>

## `git` install

`sudo apt install git`

## `pip` install

`sudo apt install python3-pip`
 

## Usage of `git` and `pip`

`git clone` = clone repository
- eg. **Turbolister github**

`pip3 install` = install python Package















