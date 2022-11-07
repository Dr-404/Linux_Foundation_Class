# Cracking `.zip` password with john the ripper

# Installation

- `snap install john-the-ripper`

- `git clone https://github.com/openwall/john.git`


## 1. Use `zip2john` tool to make hash

`zip2john test.zip > zip.hashes` 
or
`john-the-ripper.zip2john test.zip > zip.hashes`

## 2. Crack password with `john`

`john zip.hashes`



![zip_crack](../photo/zip_crack.png)


## Cracking with custom wordlist

`john --wordlist=wordlist.txt zip.hashes`



