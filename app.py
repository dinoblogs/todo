from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = '23989231jc8cn908ncfjdshgiehsdskht97'
@app.route('/')
@app.route('/index.html')
def index():
    if 'username' in session:
        if session['username'] == 'kanha' and session['password'] == 'kali':
            return render_template('index.html')
    else:
        return redirect('/login')
    


@app.route('/login/',methods=['POST'])
def login():
    if 'username' in session:
        if session['username'] == 'kanha' and session['password'] == 'kali':
            return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username != '' or password != '':
            if username == 'kanha' and password == 'kali':
                session['username'] = 'kanha'
                session['password'] = 'kali'
                return redirect('/')
        
        return render_template('login.html', error = 'Invalid credentials. Please try again.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)
