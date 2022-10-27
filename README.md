## DETAILS OF THE REPO

# todo-application

### USED TECHNOLOGIES
1. python 3.9
2. flask
3. html
4. css

### SETTING UP THE PROJECT

#### 1.  create a directory 
> **mkdir dirname**

#### 2.  create a virtual environment as follows: 
> **python -m venv env**

#### 3.  activate the virtual environment:   
> **cd env/Scripts & activate**

#### 4. create a directory for the project parallel to venv and cd into that directory

#### 5. clone the repository 
> **git clone https://github.com/satyavenikaruprolu/flask-todo**

#### 6. cd in to install the requirements
> **pip install -r requirements.txt**

#### 7. install the mysql, and set up and login as root user

#### 8. create tables user and todo
> **create database todo_app;**\
> **use todo_app**\
> **create table user(first_name varchar(50) not null, last_name varchar(50) not null, username varchar(80) not null primary key, password varchar(50));**\
> **create table todo(title varchar(50) not null, description text not null, uname varchar(80) not null, foreign key(uname) references user(username) on delete cascade);**

#### 9. update the credentials of your data base in the app.py in the project and add a secret key
>  **app.config['MYSQL_HOST'] = 'localhost'**\
> **app.config['MYSQL_USER'] = 'root'**\
> **app.config['MYSQL_PASSWORD'] = 'your_mysql_password'**\
> **app.config['MYSQL_DB'] = 'todo_app'**\
> **app.secret_key = "secret key"**

#### 10. install the requirements
> **pip install -r requirements**

#### 11. run the server
>  **python app.py**


# thank you
