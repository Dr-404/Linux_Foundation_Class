# User and Group Management

## Difference type of user

#### root user (root group)

-Most powerful and can do anything

#### Other user

- Collected in group (eg. IT, Engineeer)
- Grant relevant premission to group

#### `groups` command

`groups`

- Describe what group user belong to

#### adding user with `useradd`

- eg. `useradd test`

#### changing user pass with `passwd`

- eg `sudo passwd test` 

#### adding user to sudo group with `usermod`

- `sudo usermod -aG group user`
- `sudo usermod -aG sudo test`
```
-a = append
-G = Group
```
## Making Group and Adding User

#### `gourpadd`

- adding group to system
-eg sudo goupadd -g 1006 hack

```
-g      =   group id
1006    =   GID

```
#### Group id

- root user has the UID of 0. 
- Most Linux distributions reserve the first 100 UIDs for system use. New users are assigned UIDs starting from 500 or 1000. 
- For example, new users in Ubuntu start from 1000:

#### `/etc/group`

- eg `cat /etc/group`


#### Adding user to group with `usermod`

- `sudo usermod -aG hack test`
- Logout and login

#### Removing user with `gpasswd`

- `sudo gpasswd -d user group`
- eg. `sudo gpasswd -d test sudo`








