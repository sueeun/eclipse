from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/AnomalyDetection')
def AnomalyDetection():
    return render_template('AnomalyDetection.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/goaccess')
def goaccess():
    return render_template('goAccess.html')

@app.route('/ml_dashboard')
def ml_dashboard():
    return render_template('Flask.html')

@app.route('/cloudwatch')
def cloudwatch():
    return render_template('Cloudwatch.html')

@app.route('/member1')
def member1():
    return render_template('member1.html')

@app.route('/member2')
def member2():
    return render_template('member2.html')

@app.route('/member3')
def member3():
    return render_template('member3.html')

@app.route('/member4')
def member4():
    return render_template('member4.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
