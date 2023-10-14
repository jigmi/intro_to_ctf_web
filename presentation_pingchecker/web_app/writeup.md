# Title
pingchecker
## Authors

- @jiggy

## Category

- Web

## Description

Simple ping checker hidden in /robots.txt, vulnerable to remote code execution, there will be 3 different versions of
the ping checker which will increase in difficulty through easy to hard. The
increase of difficulties is attributed to an increase in front-end/back-end
validation and sanitization that the attacker must bypass.

## Difficulty

- Easy-Medium

## Points

100

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Enumerate the landing page and other components of the site, then at the
temporary_form exploit the union sql injection to enumerate the database
to find the flag.

### Walkthrough for easy

1. Visit the website, nothing except for a try harder image, trying all other
routes result in the same image, however directory enumeration reveals a robots.txt file that contains 3 various routes to differing levels of a ping checker.

2. Visiting the ping checker, shows a form to ping a server. There are multiple ways for an application to ping a server, this can occur entirely through javascript on the front end through sending a http request and then checking the status code. However another way is through the back-end interacting with the OS by sending a ping command on the system, e.g for linux it is ping {ip_address}. The application is made vulnerable to OS command injection through the use of injection operators that allow for multiple commands to be executed. **E.g ; and & allow for multiple commands to be run.**

3. However before even testing out the application for command injection, the form requires specifically for the input to be in an ip address cidr format.

4. Viewing the html source code reveals an event listener (onclick) for the form button. It returns the result of the function ValidateIpaddress which has our ip input passed in as an argument. Closer inspection reveals a js script called validation.js located in the /static folder which contains the ValidateIpaddress function. The function appears to be checking if its in a valid ip format and is either returning True if it complies with the ip format, and false if it doesnt. This in turn determines whether the form and its data is sent, if it receives false, this will prevent the normal browser behaviour of sending the form data.

5. As we discovered the validation of our input is occuring on the front-end, this can easily be bypassed depending on the browser's security mechanism. For example, we can easily inspect element the page and directly modify the DOM by removing the onclick event handler entirely, making the submission button not execute the ValidateIpaddress function, however different browsers might respond to this differently as this might incur errors on the frontend. A more certain way of bypassing the front-end validation is to simply use a tool like burpsuite to intercept the request after it is sent by the front-end, and then changing the payload.

6. For the payload, if we insert into the ip post parameter **; ls**. This will
effectively execute the ping, but also the ls command, listing out the directories. Further exploration of the directory, reveals that in the previous directory there is a flag directory by using **; ls ..** and then using **ls ../flag** This is simply just a directory traversal by going back once and then listing out the flag directory. This reveals a flag.txt.

7. we cat out the contents of it by just doing  **; cat ../flag/flag.txt** and tada, have the flag :D. Also instead of using directory traversal, we can simply chain multiple cd commands together to get into the directory, e.g **; cd ../flag ; cat flag.txt**. Also you can get use a python oneliner shell to spawn a shell but this is not needed.

### Walkthrough for medium


1. Bypass the JS front-end validation that we faced in easy, the same steps.

2. the payload **ip=127.0.0.1** is working, but when we try to insert ; afterwards so
**ip=127.0.0.1;ls** it does not work, it instead responds to us with "blacklisted character", this indicates an additional layer of defence that needs to be bypassed. We should try the payload one step at a time to see what exactly is getting blocked, trying **ip=127.0.0.1;** indicates that ; is getting detected.

3. We can try to use URL encoding, that is a method used to represent and transmit characters in a URL that is safe and complies with the requires of the URL format. Specifically  that URLS can only contain a limited set of characters ,special characters spaces and NON-ASCII characters might have special meanings that we do not intend for, there url encoding is  needed to ensure they are correctly interepreted and transmitted by the backend.

4. We try url encoding the semi colon ;, so **ip=127.0.0.1%0als**, it responds with **; not allowed!**, this indicates that we have passed a layer of validation and now the character is getting url decoded, but that ; is still not allowed. We can try another injection character specifically \n by url encoding it, **ip=127.0.0.1%0als** it also says **not allowed**. Can try && and url encode it, also not allowed. But trying || (OR) does not get incur a error message, **ip=127.0.0.1%7c%7cls**, the ping command runs successfully also.

5. But in order for the 2nd command to show any output using the || operator, the first command must fail, so we purposely make the ping command fail, **ip=127.0.0.cc1%7c%7cls**. We get the directory contents!

6. Lets try ls -la, but this is getting detected as a blacklisted character!?!?! Lets try echo hi, this is also getting blacklisted? But echo and ls work bythemselves. Turns out a space is also a blacklisted character! We can bypass this by simply urlencoding a space to %20. so it becomes **ip=127.0.c0.1%7c%7cls%20-la**. It works.

7. The flag is in the same location as the easy challenge, so its just **ip=127.0.c0.1%7c%7ccat%20../flag/flag.txt** BUT when we use the command cat, it responds with command not allowed, indicating we cannot use the cat command. We can instead use more (or tail/head/grep others), **127.0.0.c1%7c%7cmore%20../flag/flag.txt**

Flag is `SECSOC{r3M073C0D33X3CU710N608rr}`
