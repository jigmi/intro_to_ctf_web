# Title
echo
## Authors

- @jiggy

## Category

- Web

## Description

Simple website that takes in user input, and echoes it back out.

## Difficulty

- easy

## Points

100

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Enumerate the landing page and fuzz input parameters, revealing it to be
vulnerable to SSTI, should also be known through the html comments hinting at
using jinja2 which is a server-side template vulnerable to SSTI.

### Walkthrough 

1. There is an input box that requires you to input a number. This is only validated on the frontend through the html attribute type="number". We can change this to text or intercept the request.

2. Fuzzing the parameters, and also inspecting the html comments on the index page reveals it to be using the jinja2 templating engine. For fuzzing, {{7*7}} evaluates to 49, revealing it to be using jinja2.

3. There is no validation/sanitization to prevent a SSTI attack. The SSTI jinja2 payload **{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read() }}** works

4. Enumerating the directory and sub directories, reveals that flag.txt is in the flags directory. We can use the payload **{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat ../flag/flags/flag.txt').read() }}** to get the flag.



Flag is `SECSOC{1h473j1nj42}`