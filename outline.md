
--------------------
In the courses/cohort/.. page, the value in the Per Month box is not visible on light theme, everything is dark. 

Ok my app also needs a contact page where users can reach out and submit their issues, to us via email. ALso a privacy policy and other necessary pages like in C:\Users\adm\.vscode\Products\Freelancing; since we are recieving payments we need such. So implement them also the user the accept cookies, and accepting agreements during signups better than/similar to the example apps provided. The password forms also need the see and unsee password eye. Also fix the error:
IntegrityError at /accounts/register/learner/
(1062, "Duplicate entry '' for key 'me_users_tbl.username'")
Request Method:	POST
Request URL:	https://mlaudit.info/accounts/register/learner/

Django Version:	5.2.16
Exception Type:	IntegrityError
Exception Value:	
(1062, "Duplicate entry '' for key 'me_users_tbl.username'")
Exception Location:	/opt/render/project/src/.venv/lib/python3.14/site-packages/MySQLdb/connections.py, line 286, in query
Raised during:	accounts.views.register_learner
Python Executable:	/opt/render/project/src/.venv/bin/python3.14
Python Version:	3.14.3
Python Path:	
['/opt/render/project/src',
 '/opt/render/project/src/.venv/bin',
 '/opt/render/project/python/Python-3.14.3/lib/python314.zip',
 '/opt/render/project/python/Python-3.14.3/lib/python3.14',
 '/opt/render/project/python/Python-3.14.3/lib/python3.14/lib-dynload',
 '/opt/render/project/src/.venv/lib/python3.14/site-packages']
Server time:	Wed, 22 Jul 2026 02:10:31 +0



I also need the profile pages to look and function like the example; C:\Users\adm\.vscode\Products\BloodLink. But for the tutor profiles, I need something more, students may need to know more about their tutor eg their specilty etc, so do something about that. 

Ensure the email notifications work, eg: when users pay for courses(the course information), initial signups, and more. But only necessary stuff.

From the courses remove the tag "Monthly Subscription", the students can see the duration from the date.

I also need the course uploads to work so tutors can add courses efficiently. Links can be uploaded to a github folder(just like images get uploaded to a github folder). Videos will use Bunny stream API(I already added the credentials to .env)--no urls, it will use embedding code so users do not share the video urls, links will be to my database. All resources for a course should be stored properly and accordingly. For the videos play they UI should be properly structured to handle that. 

