Framework--Django
Database-- MySQL ; just make sure whoever/whatever scaffolds this uses mysqlclient (not PyMySQL, which has quirks with some Django features) and sets utf8mb4 as the charset from the start — retrofitting emoji/special-character support later is painful.
Payments-- Only paystack(not daraja, pastack can still do the work) and Manual cash 
For Meetings-- No Zoom APIs cannot afford to pay for the accounts, just manual links
For Videos storage -- I will use Bunny Stream since it is cheaper
I will not do transcripts for the videos, it's not necessary.

I intend to build a Kenyan platform where learners(teens and younger ones) can learn programming(in the modern sense, since AI already exists and it can already code efficiently), some basic ML, some Software Engineering, statistics, and Math(for ML), and some modern AI(Not so complex  stuff they'll understand easily at their level).  Also, I will later bring tutors on board to teach other subjects(like Math, Chemistry, Biology, Physics, and others- based on the current CBC curriculum--Junior Secondary School first, then will expand later),; and also other tutors for Software Engineering, Electronics & Robotics, Cybersecurity, etc. 

Now to the platform itself, I have not yet decided on the actual architecture, so I need your help and  different recommendations based on what will work best.  There will be pre-recorded video lessons(with transcripts, PDF notes, links, assignments, and resources), scheduled Google meet classes(and make-up classes for students who miss--prerecorded videos), and payments will be monthly(I will use paystack mpesa to fulfill payments on the web app, although I know some parents personally who will pay cash, so when they do, I just add the student information and create an account for them on my platform).The classes will be during the weekends and during the holiday season when schools close.  So every tutor on the platform will have ther dashboard where they post the videos, links, resources, assignments for a class, and  schedule classes for the students signed up for their course. there  will also be a proper grading system for learners(advice on this).

For paystack payments, UI and other things you can see what I did for the following apps(these are flask apps, but I'm sure some stuff can be transfered/restructured to django):
C:\Users\adm\.vscode\Products\Freelancing
C:\Users\adm\.vscode\Products\BloodLink

And for the course notes, upload to github repo etc you can see what I did in these apps:
C:\Users\adm\.vscode\Products\MachineLearning101




/accounts/register/tutor/