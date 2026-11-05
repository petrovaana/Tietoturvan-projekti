# Here are the projects vulnerabilities explained

The project contains 5 vulnerabilities from the 2025 OWASP list.

## A01 Broken Access Control

Access control keeps track of users acting within their rights. The system monitors what users are allowed to do and what data they are allowed to view and/or edit. The system might contain admins and regular users, and both have different rights.

Broken access control is a vulnerability where for example a user can view or modify data that should not be accessible for the specific user. Most commonly an attakcer can get around it's rights through modifying the URL or the HTML-page. In addition, commonly a developer might forget to secure all of HTTP-methods (DELETE/POST), and secure only the GET -method. Then an attacker is able to delete data without even logging in. 

In this case a user can view another user's task list by altering user_id in the URL. For example from: /tasks/users/1/ to: /tasks/users/2/. An attacker can view the name of who the list belongs to as well as the tasks on the list, as shown in the picture. As mentioned, this is one of the most common mistakes a developer can make.

In the file views.py the function user_task_list does not verify that the logged in user_id is the same as the user_id of the list. Additionally, the file contains a fix for A01, which checks that the IDs match. In case of modification of URL, the application raises Http404 issue, and block the exposure of another persons tasks. 

## A02 Security Misconfiguration
DEBUG=True 

## A09 Security Logging and Altering Failures


## A07 Authentication Failures


## A10 Mishandling of Exceptional Conditions or A05 Injection
