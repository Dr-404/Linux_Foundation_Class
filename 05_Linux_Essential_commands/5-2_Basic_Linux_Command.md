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












