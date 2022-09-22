# Essential Networking Foundation for Pentesting


## Network

- In computing, a network is a collection of two or more computers that can communicate.

- In order for networking to facilitate communication between devices, the machines on the network must be able to find each other.

- The systems responsible for making this possible are TCP and IP.

[Reference](https://www.redhat.com/sysadmin/sysadmin-essentials-networking-basics)


## Protocol

- Internet Protocol (IP) is the method or protocol by which data is sent from one computer to another on the internet. Each computer -- known as a host -- on the internet has at least one IP address that uniquely identifies it from all other computers on the internet.

- IP is the defining set of protocols that enable the modern internet. It was initially defined in May 1974 in a paper titled, "A Protocol for Packet Network Intercommunication," published by the Institute of Electrical and Electronics Engineers and authored by Vinton Cerf and Robert Kahn.

- At the core of what is commonly referred to as IP are additional transport protocols that enable the actual communication between different hosts. One of the core protocols that runs on top of IP is the Transmission Control Protocol (TCP), which is often why IP is also referred to as TCP/IP. However, TCP isn't the only protocol that is part of IP.

## How does IP routing work?

- When data is received or sent -- such as an email or a webpage -- the message is divided into chunks called packets. Each packet contains both the sender's internet address and the receiver's address. Any packet is sent first to a gateway computer that understands a small part of the internet. The gateway computer reads the destination address and forwards the packet to an adjacent gateway that in turn reads the destination address and so forth until one gateway recognizes the packet as belonging to a computer within its immediate neighborhood -- or domain. That gateway then forwards the packet directly to the computer whose address is specified.

Because a message is divided into a number of packets, each packet can, if necessary, be sent by a different route across the internet. Packets can arrive in a different order than the order they were sent. The Internet Protocol just delivers them. It's up to another protocol -- the Transmission Control Protocol -- to put them back in the right order.

[Reference](https://www.techtarget.com/searchunifiedcommunications/definition/Internet-Protocol)




## Internet protocol (IP)

- IP provides mechanisms that enable different systems to connect to each other to transfer data. Identifying each machine in an IP network is enabled with an IP address.

#### Public IP
- A public IP address is one that is accessible via the public internet

#### Local or Privat IP 

A local IP address can be generated via DHCP running on a local network router, providing an address that can only be accessed by users on the same local area network.

## IPv4 & IPv6

- The most widely used version of IP for most of the internet's existence has been Internet Protocol Version 4 (IPv4).

- IPv4 provides a 32-bit IP addressing system

- supports a total of 4,294,967,296 addresses.

![IPv4](../photo/ip4.png)



## Type of Network
1. LAN(Local Area Network)
2. PAN(Personal Area Network)
3. MAN(Metropolitan Area Network)
4. WAN(Wide Area Network)

## Private (Internal) IP 
- 10.0.0.0 to 10.255.255.255
- 172.16.0.0 to 172.31.255.255
- 192.168.0.0 to 192.168.255.255

eg. `ping meberlin.com`


## Analyzing Networks 

#### `ifconfig`
- IP address
- Mac Address


#### `iwconfig`
- Using the terminal, let’s take a look at some wireless devices with iwconfig



#### Changing Nework information

`ifconfig wlp2s0 192.168.100.22`

#### Spoofr MAC address

`ifconfig eth0 down`
`ifconfig eth0 hw ether 00:11:22:33:44:55:`
`ifconfig eth) up`

## TCP and UDP 

- `TCP` - secure, connection, slow
- `UDP` - connectionless, live session, Broadcast


# Network Mangement

## 1. `ip` command

- show routing table, network devices
- LINUX IPV4 address 

#### `ip route`
- show IP in table form

#### `ip addr`
- more complete informiation


## 2. `ifconfig` command

- Need to install net-tools

```
sudo apt install net-tools
```

#### `ifconfig | grep inet`

- only show IPv4 address

#### `ifconfig | grep ether`

- only show MAC address

## 3. `netstat` command

#### `netstat -r`

- show routing table

#### `netstat -t`

- only show tcp port

#### `netstat -l` 

- show listen port


## 4. `systemctl` command

#### `sudo systemctl status ssh`

- checking ssh service status

#### `sudo systemctl start ssh`

- Starting ssh service

#### `sudo systemctl stop ssh`

- Stopping ssh service

#### `sudo systemctl enable ssh`

- run ssh service after booting os

#### `sudo systemctl disable ssh`

- disabling ssh service 


# Manipulation the DNS

## `DNS`
- Translate Domain to IP address


## Examining DNS with `dig` command

#### `dig youtube.com ns`
- Finding name server

#### `dig youtube.com mx`

- Finding mail server

#### Changing DNS server

- `sudo nano /etc/resolv.conf` 

#### Blocking Website

- `sudo nano /etc/hosts`
- Replace local ip address with domain name

#### Mapping IP address

- `sudo nano /etc/hosts`
- Map `ip` with `dns_name`
- `sudo systemctl restart network-man


# SSH (Secure Shell)