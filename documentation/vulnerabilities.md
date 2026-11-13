# Installation instructions



# Here are the projects vulnerabilities explained

The project contains 5 vulnerabilities from the 2025 OWASP list. All of the figures can be found in the screenshots directory.

## A01 Broken Access Control

Broken access control is a vulnerability where, for example, a user can view or modify data that should not be accessible to them. Most commonly attakcers can get around its rights by modifying the URL or the HTML page. Developers may also forget to secure all of HTTP methods (such as DELETE and POST) and secure only GET method, which could let the attacker modify or delete data without proper authorization.

In this application, a logged-in-user can view another user's to-do list by altering the user_id in the URL, for example from /tasks/users/4/ to /tasks/users/3/. An attacker can view the name of who the list belongs to as well as the tasks on the list, as shown in the picture flaw-A01-before.

How to fix it? 

In the file views.py the function user_task_list does not verify that the logged in user_id is the same as the owner's user_id of the list. Additionally, the file contains a fix for A01, which checks that the IDs match. The function receives user_id as a parameter from the URL and compares it with request.user.pk, which is the ID of the currently logged-in user. If the IDs do not match, the application raises Http404 issue, and blocks the exposure of another persons tasks.

## A02 Security Misconfiguration

Security misconfiguration is a vulnerability where a developer has configured the application poorly. It can show in many different ways such as unnecessary features being either installed or enabled or too specific error messages that give attackers too much information about the software. The code itself can be perfect yet with poor configuration, the application becomes vulnerable and gives an attacker a possibility to misuse the given information. For example, the more unnecessary features are enabled, the larger the attack surface.

In this application misconfiguration can be found in settings.py. Line 28 contains "DEBUG=True", which is usually used during development. The correct configuration would be "DEBUG=False", which hides the specifics of an error message. The pictures show a before and after a fix (flaw-A02). The error message exploids applications Framework, a full URL map, a handling function and shows that a user with a user ID = 2 does not exist. An attacker gains a lot of information about the application, and can use it for malicious intentions. Meanwhile, the fixed configuration states that the requested resource was not found. This is an example of when an attacker changes the URL user_id to a non existing user_id.

## A07 Authentication Failures

This is a vulnerability where an attacker can pretend to be another user. The application allows unlimited attempts to log in. If an attacker tries to log in several times, the application just informs them that the username or password is incorrect. This is shown in a figure flaw-A07-before. An attacker can try thousands of different passwords within seconds with a script, or use leaked information (usernames and their passwords). Eventually, an attacker may log into another users account. 

How to fix it?

The file settings.py contains a fix for the vulnerability. It uses axes-library, and the axes is added to INSTALLED_APPS and MIDDLEWARE. In addition, the AUTHENTICATION_BACKENDS contains 'axes.backends.AxesStandaloneBackend' to check that the user is not locked out before the password is verified. The file settings.py also contains 'AXES_FAILURE_LIMIT = 3' and 'AXES_COOLOFF_TIME = timedelta(minutes=5)' which work as rules in the application. A user can try to log in 3 times. If the password is still incorrect on a third try, the application block the user from trying to log in for 5 minutes. The figure flaw-A07-after contains an image of what it looks like for a user after 3 attempts to log in.

## A09 Security Logging and Alerting Failures

The vulnerability occurs when tha application does not log important security events, such as failed log ins. Without logging an attack is completely undetectable. In this application the vulnerability occurs when a user deletes a task. From figure flaw-A09-before can be seen that palvelin makes a usual log ""POST /tasks/2/delete/ HTTP/1.1" 302 0". It does not show who deleted the task and if the request was accepted. The vulnerability itself is not visible for the user. It can only be seen from palvelimen loki. Even though it is not visible for the user, this still is a vulnerability because deleting a task is a data altering event that should be traceable. 

How to fix it?

The [figure]("screenshots/flaw-A09-after.png") shows that after fixing the vulnerability, the loki contains a new row with task_id and actor_id showing that user 3 deleted a task 4. The vulnerability can be found in the files views.py and settings.py. In the file views.py function delete_task does not log anything, and the fix contains a piece of code which 

## A10 Mishandling of Exceptional Conditions

Mishandling of exceptional conditions is a vulnerability where the application does not know how to handle unexpected situations, such as invalid input. This can lead to the application crashing, revealing internal information or behaving unpredictably in general.

In the file views.py, the function create_task does not call form.is_valid() before saving the task. The method from.is_valid() checks that all of the submitted data is valid before the form is saved. In the figure flaw-A10-before, the task name field contains 3 spaces. Django strips spaces from the beginning and the end, leaving the field empty and the form invalid. However, the application attempts to save the data anyway and crashes with a ValueError. Since DEBUG is enabled, the error reveals details, such as server file paths. This is shown in the figure flaw-A10-before.

How to fix it?

The file views.py contains a commented-out fix for the vulnerability. The fix checks the form with form.is_valid() before saving it. In case of the input being invalid, the application informs the user with an error message and does not try to save the invalid input. Most importantly, the application does not crash anymore, but returns a HTTP 400 response instead.
