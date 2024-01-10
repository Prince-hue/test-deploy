how to create a virtual environment
------------------------------------------------
pip install virtualenv
# Create a virtual environment named 'venv'
virtualenv venv
#activate virtualenv
venv\Scripts\activate
#install django
pip install django
#create django project
django-admin startproject yourprojectname .
#start server
python manage.py runserver
#exiting from virtualenv to global 
deactivate


how to deploy
----------------------------------------------
#add a vercel.json file 
#edit with the relative link of wsgi.py
"src": "push/wsgi.py", #take note of the backward slash
"dest": "push/wsgi.py"
#create a requirements.txt file in console
pip freeze > requirements.txt

#visit the railway site
https://railway.app/
#click on 'Start a New Project'
#search and click on 'provision mysql'
#click on the created database
#visit the variable section and update the database in your settings.py 
""""
"deploy_db": {
        "NAME": "railway",
        "HOST": "viaduct.proxy.rlwy.net",
        "PASSWORD": "dEb2baFh6Ab2Dde2cEEGCEb3AG4-3-cD",
        "PORT": 35864,
        "USER": "root",
        "ENGINE": "django.db.backends.mysql",
    },

""""
#also include this code at the bottom of settings.py
#make sure you have static folder in your app
""""
STATICFILES_DIRS = os.path.join(BASE_DIR, 'deploy/static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'deploy/static')

""""
#set ALLOWED_HOST = ['*'] to all
#set DEBUG = False

#in wsgi.py, set 
app = application
#create a .env file inside the main dir and paste the URL of the database provided by railway into it
MYSQL_PRIVATE_URL = "mysql://root:dEb2baFh6Ab2Dde2cEEGCEb3AG4-3-cD@mysql.railway.internal:3306/railway"


How to do a git push within vscode
------------------------------------------------------
#within the terminal, type the following commands
git init
git add .
git commit -m "Initial commit"
#If you haven't already, create a new repository on GitHub 
#(or any other Git hosting service). 
#Do not initialize it with a README or any other files.
git remote add origin https://github.com/Prince-hue/test-deploy.git
git push -u origin main 

#to change branches
git checkout -b name_of_branch
#check to see if any changes have been made
git status
#to record new changes
git commit -am "new_comment"
#git status will tell you no changes
git push origin name_of_branch


How to solve refusing to merge error
--------------------------------------------------------
#The "refusing to merge unrelated histories" error
#occurs when Git detects that the histories of the branches 
#you're trying to merge (or pull) have diverged and are 
#not directly related. This can happen when you have 
#initialized a Git repository locally, and then you create a 
#new repository on GitHub (or another remote repository) with its 
#own set of commits.
git pull origin main --allow-unrelated-histories
#Add and commit any changes resulting from the merge
git add .
git commit -m "Merge remote main into local main"
#Push the changes to the remote repository
git push origin main


How to deploy into vercel
--------------------------------------------------
#visit vecel main site and log in
https://vercel.com
#create a repository in github
#within settings.py
ALLOWED_HOST = [".vercel.app"]
#create file called vercel.json
""""
{
    "builds": [
        {
            "src": "push/wsgi.py",
            "use": "@vercel/python",
            "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "push/wsgi.py"
        }
    ]
}

""""
#create a requirements.txt file
pip freeze > requirements.txt
#in wsgi.py
app = application