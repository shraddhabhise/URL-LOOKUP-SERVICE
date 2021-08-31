# URL-LOOKUP-SERVICE
A webservice designed to lookup for URL's and respond with appropriate response.

Creating a flask web application to detect if the user has entered a malware URL. 
The entered URL is checked in the following three ways:
1. If the URL entered is malformed. This means the user should enter an URL in the format of ("<http/https>://<hostname>.com"). If not then the message is displayed that the URL entered is malformed and please correct it.
2. If the entered URL is not malformed, and passes all the checks for validity (using regular expressions), then it is checked for the following conditions:
 a) If the URL is present in "malwarehosts" table of the database, then the URL entered has malware and this message is displayed to the user.
 b) if no, then the URL is safe and can be used by the user.

Files:
 
app.py
 
 Contains following function:
 
  a) home: 
  Normal landing page
  Access : /home
 
  b) list: 
  list the malware urls existing in the table malwarehosts. This is useful for admins to know the existing urls in the table.
  Access : /list
 
  c) addmalware and add: 
  for adding new malware url. This is useful for admins to add new url in the the database
  Access: /addmalware
 
  d) new_url and isValid: 
  new_url: Can be used by users to iput the url that they want to check. 
  isValid: the function that checks the user entered url for the following:
     - Is the url malforfed. This is comared using a regular expression to check the url for valid syntax. If not it informs the user to enter it again with proper   syntax.
     - Is the url a malware url. This is checked by comparing the url with the urls in the malwarehosts table. 
     - If none of the above condition satisfies then the URl is valid and safe to use.
  Access:
  /checkurl     (then enter the url to check)
 
sql.py

  - Responsible to create a database and table to store malware urls.
 
/templates directory
 
 - this folder contains the views to display the corresponding messages and UI interfaces.
 
 To Run:
 1. git clone <repository>
 2. install requirements.txt
 3. run the app by using: python3 app.py
 4. Hit the url where the flask is hosting the app after running
 5. /checkurl : will give you a give to enter your url. Please enter the url in the format https/http://<hostname> e.g (https://google.com). According to if the  the url has malware or if it is safe, the message will be displayed accordingly to the user.
 
 Admin can run:
 6. /list
 to list the existing malware urls in the "malwarehosts" table
 7. /addmalware
 to add a url that is detected as a malware to the table malwarehosts
      
 Database used: sqllite3
 Flask Framework: 2.0.1
 
 Future scope:
 1. convert it to containerized application
 2. scale it for more users and urls
 3. set proper admin priviledges to add and list the malware urls. So that users cannot access it.
