from flask import Flask, render_template, request, redirect, url_for
import json, os, hashlib
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(dict(
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='songbyrdhelp',
    MAIL_PASSWORD='Whack2018'
))

mail = Mail(app)


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/whymakeprofile')
def missionstatement():
    return render_template('whymakeprofile.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/profile', methods=['GET'])
def profile():
    with open('junruanderson.json', 'r') as file:
        d = json.loads(file.read())
    return render_template('profile.html', name=d['name'], tagline=d['tagline'], about=d['about'],
                           imgsrc="../images/" + "img.png", causes=d['causes'],
                           socialmedia=d['socialmedia'],
                           keywords=d['keywords'])

@app.route('/createprofile')
def createprofile():
    return render_template('createprofile.html')


@app.route('/makeprofile', methods=['POST'])
def makeprofile():
    filename = request.form['firstname'] + request.form['lastname']
    socialmedia=request.form['socialmedia'].split("\n")
    d = {'name': request.form['firstname'] + " " + request.form['lastname'],
         'passhash': hashlib.sha3_256(request.form['firstname'] + request.form['lastname'] + request.form['password']),
         'tagline': request.form['tagline'],
         'about': request.form['about'],
         'causes': request.form['causes'],
         'keywords': [request.form['firstname'], request.form['lastname'], request.form['firstname'] + " " + request.form['lastname'], request.form['tagline']],
         'socialmedia': socialmedia}
    with open("./" + filename + ".json", "w") as file:
        file.write(json.dumps(d))
    return redirect(url_for('success'), code=302)


@app.route('/sendmail', methods=['POST'])
def sendmail():
    msg=Message('Contact', sender='songbyrdhelp@gmail.com', recipients=['songbyrdhelp@gmail.com'])
    msg.body=request.form['content'] + "\n" + request.form['name'] + "\n" + request.form['email']
    mail.send(msg)
    return redirect(url_for('success'), code=302)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/searchprofiles')
def searchprofiles():
    return render_template('searchprofiles.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=port)
