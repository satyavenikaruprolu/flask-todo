from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "xxxxxxxxxxx"

app.config['MYSQL_HOST'] = 'xxxxxxxxxxxx'
app.config['MYSQL_USER'] = 'xxxxxxxxxxxxxx'
app.config['MYSQL_PASSWORD'] = 'xxxxxxxxxxxxxx'
app.config['MYSQL_DB'] = 'xxxxxxxxxx'

mysql = MySQL(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    if request.method == 'GET':
        return render_template('signup.html', error=error)
    else:        
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')        
        cursor = mysql.connection.cursor()
        cursor.execute('select username from user;')
        usernames = [row[0] for row in cursor.fetchall()]
        msg = None
        if username in usernames:            
            error = 'username already exists'
            return render_template('signup.html', error=error)
        else:            
            query = 'insert into user(first_name, last_name, username, password) values("%s", "%s", "%s", "%s")'%(first_name, last_name, username, password)
            cursor.execute(query)
            mysql.connection.commit()
            return redirect(url_for('login'))
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':                
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        query = 'select username, password from user where username="%s"'%username
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            error = 'user does not exist'
        elif data[0][1] != password:
            error = 'incorrect passwoord'
        else:
            session['username'] = username
            return redirect(url_for('dashboard'))
    return render_template('login.html', error= error)

@app.route('/delete', methods=['POST'])
def delete():    
    cursor = mysql.connection.cursor()
    title = request.form['title']
    query = 'delete from todo where title="%s";'%title
    cursor.execute(query)            
    mysql.connection.commit()                
    return redirect('todos')


@app.route('/dashboard')
def dashboard():
    if session.get('username'):
        username = session.get('username')
        query = 'select first_name, last_name from user where username="%s"'%username
        cursor = mysql.connection.cursor()
        cursor.execute(query)    
        data = cursor.fetchall()[0]             
        return render_template('dashboard.html', data=data)
    else:
        return render_template('error.html')
    
@app.route('/todos', methods=['POST', 'GET'])
def todos():
    if session.get('username'):
        username = session.get('username')
        cursor = mysql.connection.cursor()        
        cursor.execute('select title, description from todo where uname="%s"'%username)
        data = cursor.fetchall()        
        if len(data) == 0:            
            return render_template('todos.html', todos=None)
        else:
            return render_template('todos.html', todos=data)            
    else:
        return render_template('error.html')

@app.route('/add', methods=['POST', 'GET'])
def addtodo():
    if session.get('username'):
        if request.method == 'POST':        
            cursor = mysql.connection.cursor()
            username = session.get('username')
            title = request.form['title']
            description = request.form['description']
            print(username, title, description)
            print(request)
            query = 'insert into todo values ("%s", "%s","%s");'%(title, description, username)            
            cursor.execute(query)             
            mysql.connection.commit()                        
            return redirect(url_for('todos'))
        else:
            return render_template('addtodo.html')                  
    else:
        return render_template('error.html')  
        

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
