# Here are the projects vulnerabilities explained

The project contains 5 vulnerabilities from the 2025 OWASP list.

## A01 Broken Access Control
User id switching in the URL exposes other users task lists. 
views.py: user_task_list
user_id is not checked whether it is the same id as the logged in person. Another user can log in with their own id, and switch the user id in the URL, and view the other persons task list. The views.py file contains a fix for the issue, where the user_task_list function checks that the IDs match. In case they do not, the application raises a Http404 issue, and stops the process of showing another users task list. The task_list.html contains the view code for the

## A02 Security Misconfiguration
DEBUG=True 

## A09 Security Logging and Altering Failures


## A07 Authentication Failures


## A10 Mishandling of Exceptional Conditions or A05 Injection
