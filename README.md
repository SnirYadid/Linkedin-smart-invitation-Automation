# Linkedin smart invite automation
The program sends requests automatically in a smart way. <br/>
The type of people who approve requests in the highest percentages are recruiters. <br/>
LinkedIn offers those who reach more than 500 connections more options, so you should reach the threshold as soon as possible. <br/>
The program sends requests intelligently in two possible options: <br/><br/>
First -   Recommended - Sending connection messages to a 2nd connection that work in human resources
- It is better to add the friend's name who works in the field who are looking to work in it but can work with any member.
- You can change the field of industry according to the fields of practice defined on LinkedIn, in line 88 - must be one of defined industries. <br/>

Second -  Search by LinkedIn recommendations based on keywords such as: recruiter, human resources and more.
## Install requirements
Router to the folder where you saved the project and…
```bash
   cd linkedin-smart-invite-automation
```
```bash
   pip install -r requirements.txt
```

   
**Get started:**

 - Change your `email`  in line 9
 - Change your `password` in line 10
 - Add the Key word in `matches` array that you want to filter in line 163 the search is in according to the "about" section in profile of linkedin member

 **You are ready to go.**

    python bot.py
## Note
You can not touch the computer while running the program, to prevent its collapse.
