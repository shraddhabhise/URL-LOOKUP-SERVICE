# URL-LOOKUP-SERVICE
A webservice designed to lookup for URL's and respond with appropriate response.

Creating a flask web application to detect if the user has entered a malware URL. 
The entered URL is checked in the following three ways:
1. If the URL is entered is malformed. This means the user should enter an URL in the format of ("<http/https>://<hostname>.com"). If not then the message is displayed that the URL entered is malformed and please correct it.
2. If the entered URL is not malformed, and passes all the checks for validity (using regular expressions), then it is checked for the following conditions:
 a) If the URL is present in "malwarehosts" table of the database, then the URL entered has malware and this message is displayed to the user.
 b) if no, then the URL is safe and can be used by the user.

Functionalities:


