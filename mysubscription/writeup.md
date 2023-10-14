# Title
mysubscription
## Authors

- @jiggy

## Category

- Web

## Description

Jiggy's subscription is ready for the public to see if they are subscribed to his fantastic content, or is it really ready for production use. 

## Difficulty

- Medium

## Points

100

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Enumerate the landing page and other components of the site, then at the 
temporary_form exploit the union sql injection to enumerate the database
to find the flag.

### Walkthrough

1. Visit the website, submit the form and see that a form error is occuring no 
   matter the value, inspecting the html comments indicates that the form is out
   of action, and refers to a temporary form.
   
2. Enumerating robots.txt indicates that the endpoint /temporary_form exists,
   also just using the html comment note of temporary form and just bruteforcing
   the directory can work but is not intended

3. landing at /temporary_form presents a http authentication form, using the 
   default credentails username: admin and password: admin grants you access,
   the html comment from earlier indicates it was written by the user admin, 
   also admin admin is a default credential that should be tested.

4. the /temporary_form presents the same checking email function but works, 
   however, the input box for the email validates if it is an email, this can
   bypassed through intercepting the post request through burp or by simply inspecting
   the page and modifying the dom attribute type="email" of the input box to 
   type="text". This will allow any value to be inserted into the post parameters
   as there is no additional validation on the backend (yikes!).
   
5. The input box is vulnerable to Union SQLI as indicated by injecting **'** into the parameter which responds with an internal server error, the sql statement on the backend 
   is querying 5 columns from the users db and the email table. Using union enumeration by inserting 
   **'UNION null,null,null,null,null-- -** reveals there is 5 columns needed to validate the union statement for further exploitation. Note that the db is mysql and therefore requires comments to be 2 dashes and an additional dash with a space separating them (or just a space after the -- but for illustrative purposes i'll add a -) in order to be a comment. The comment is required in order for a valid statement as the query will break.
   
6. To find the location of the flag, union db enumeration needs to be undertaken. We can dump all the databases of the database by querying the various tables in the information_schema database, however specifically for the databases we can query the schemata table using **' UNION select null,schema_name,null,null,null from INFORMATION_SCHEMA.SCHEMATA-- -**

7. After dumping the databases, we can enumerate the tables of each database, if we enumerate the tables of mysql using **' UNION select null,TABLE_NAME,TABLE_SCHEMA,null,null from INFORMATION_SCHEMA.TABLES where table_schema='mysql'-- -** we find a table called flag

8. In order to dump the table flag inside the mysql database, we need to find the column names. **' UNION select null,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA,null from INFORMATION_SCHEMA.COLUMNS where table_name='flag'-- -** is querying the columns table in information_schema and our conditional statement will list out the column name for flag which is **flags**

9. We now know the db is mysql, the table is flag and the column name is flags. We can now execute a query statement to read the data of the flags table, using **'UNION select null,null,null,null,flags from mysql.flag-- -** we have attained the flag POGGERS
### Flag

`SECSOC{1l0v3uN10n1nJ3C710n}`

</details>
