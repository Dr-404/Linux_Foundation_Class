# Managing service

## Basic Syntax for managing services

#### starting service

`service [servicename] start`

#### Stoping service

`service [servicename] stop`

#### Restarting service

`service [servicename] restart`

# Managing service with `systemctl`(systemd) command

- central management tool for controlling the system

# Basic sytax 

`sudo systemtl [options] [service_name]`
- eg `sudo systemctl status apache2`
```
Options

start		= starting services
stop		= stop currently running services
restart		= restart a running service
reload		= reloading configuration withou restarting service
enable		= start a service at boot 
disable		= diable service from starting atuomatically
status		= check the status of a service
is-active 	= check to see a service is currently active
is-eanble 	= check to see a service is currently enable
list-units	= show list of all units(services)
```

# Unit Management (serice+others)

## List Unit

`systemctl list-units --all`

- List all services whether active or not

## list only service unit

`systemctl list-units --type=service`

- only active service units

## Displaying a unit file

`systemctl cat [app.service]`

- eg. `systemctl cat apache2.service`

## Displaying Dependencies Tree

`systemctl list-dependencies apache2.service`

## Checking Unit Properties

`systemctl show apache2.service`

- to see low-level properties of a unit
- key=value format

# Using Shortcuts for Important Events

#### Put system into rescur (single-user) mode

`sudo systemctl resuce`

#### Halt the system
`sudo systemctl halt`

#### Power-off the system
`sudo systemctl poweroff`

#### restart or reboot the system
`sudo systemctl reboot`










