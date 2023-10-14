# Title
whereami
## Authors

- @jiggy

## Category

- Web

## Description

Directory traversal and local file inclusion

## Difficulty

- easy

## Points

100

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Click on the button, it sends a GET request to the /view_image endpoint containing
the query paramater file_name. The user is able to modify the parameter and view 
other files.

### Walkthrough 

1. There is a simple button on the landing page that once clicked, sends a GET request to the /view_image route, the request also contains the query paramater file_name, the value being the location of an image file static/images.png. 

2. The user is able to modify the query value to display other files.

3. The payload ../flag.txt goes back one directory, and retrieves the contents of flag.txt




Flag is `SECSOC{DIR3Ct0rYTR4v3r54L0rn0T}`