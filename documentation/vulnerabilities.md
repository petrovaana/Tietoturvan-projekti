# Here are the projects vulnerabilities explained

The project contains 5 vulnerabilities from the 2025 OWASP list.

## A01 Broken Access Control

Access control keeps track of users acting within their rights. The system monitors what users are allowed to do and what data they are allowed to view and/or edit. The system might contain admins and regular users, and both have different rights.

Broken access control is a vulnerability where for example a user can view or modify data that should not be accessible for the specific user. Most commonly an attakcer can get around it's rights through modifying the URL or the HTML-page. In addition, commonly a developer might forget to secure all of HTTP-methods (DELETE/POST), and secure only the GET -method. Then an attacker is able to delete data without even logging in. 

In this case a user can view another user's task list by altering user_id in the URL. For example from: /tasks/users/1/ to: /tasks/users/2/. An attacker can view the name of who the list belongs to as well as the tasks on the list, as shown in the picture. As mentioned, this is one of the most common mistakes a developer can make.

In the file views.py the function user_task_list does not verify that the logged in user_id is the same as the user_id of the list. Additionally, the file contains a fix for A01, which checks that the IDs match. In case of modification of URL, the application raises Http404 issue, and block the exposure of another persons tasks. 

## A02 Security Misconfiguration

Security misconfiguration is a vulnerability where a developer has configured the application poorly. It can show in many different ways such as unnecessary features being either installed or enabled or too specific error messages that give attackers too much information about the software. The code itself can be perfect yet with poor configuration, the application becomes vulnerable and gives an attacker a possibility to misuse the given information. For example the more unnecessary features are enabled, the larger the attack surface.

In this application misconfiguration can be found in settings.py. Line 28 contains "DEBUG=True", which is usually used during development. The correct configuration would be "DEBUG=False" which hides the specifics of an error message. The pictures show a before and after a fix. The error message exploids applications Framework, a full URL map, a handling function and shows that a user with a user ID = 2 does not exist. An attacker gains a lot of information about the application and can use it for malicious intentions. Meanwhile the fixed configuration states that the requested resource was not found. This is an example of when an attacker changes the URL user_id to a non existing user_id.

## A09 Security Logging and Alerting Failures


## A07 Authentication Failures
- Rajattomat epäonnistuneet kirjautumisyritykset

## A10 Mishandling of Exceptional Conditions
