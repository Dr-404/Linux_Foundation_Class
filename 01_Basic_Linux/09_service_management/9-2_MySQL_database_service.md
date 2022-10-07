# MySQL service 

## Starting MySQL

`service mysql start`

## Enter mysql from terminal

`sudo mysql -u root -p`

## Setting mysql password to root user

#### See what users are already in our MySQL
`select user, host, password from mysql.user;`

#### show database and use mysql database

`show databases;`
`use mysql`

#### Changing mysql root password with `update`

`set password for 'root'@'localhost' = PASSWORD('htun2425');`
`FLUSH PRIVILEGES;`

## Accessing a Remote Database

`mysql -u [username] -p $IP`

- eg `mysql -u root -p 192.168.100.101`

## Connecting to a Database

#### find which database are on the system
`show databases;`

#### connect database

`use [database_name]`

#### Find Tables
`show tables;`

#### See the structure of table

`describe tables`






