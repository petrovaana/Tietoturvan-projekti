# Cyber security project

This is a University security course application, To Do -app. It is deliberately vulnerable, and contains 
5 security vulnerabilities from different categories in the OWASP Top 10, 2025 list. The code contains 
fixes for ach vulnerability. They are commented out, for example as A09, vulnerability name, and a 
suggested fix. In addition, the project contains a detailed [documentation](documentation/vulnerabilities.md) with 
explanations for the vulnerabilities, their fixes and screanshots of the effects on the applications working. 

Users can create an account, log in and create tasks. After the task being completed, user can delete the 
task from the view. 

## How to get the application running:

You need Python and Git installed. Clone the repository and enter the project folder:

```bash
git clone https://github.com/petrovaana/Tietoturvan-projekti.git
cd Tietoturvan-projekti
```

Create and activate a virtual environment, then install Django:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install the correct Django version:
```bash
python -m pip install Django==6.1.2
```

Set a local development secret key:
```bash
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')
```

Set up the database and start the development server:
```bash
python manage.py migrate
python manage.py runserver
```

Open the http://127.0.0.1:8000/ in your browser. Create an account at /accounts/register/, then log in. 
