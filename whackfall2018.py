from flask import Flask, render_template, request
import json, os

app = Flask(__name__)


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/missionstatement')
def missionstatement():
    return render_template('missionstatement.html')


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
    return render_template('profile.html', name="Jane Doe", tagline="Testing", about="I am performing a test",
                           imgsrc="../images/" + "img.png", causes="more testing whipeee yay!",
                           socialmedia=["https://www.w3schools.com/tags/att_textarea_form.asp", "https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask"],
                           keywords=["test1", "test2", "test3"])

@app.route('/createprofile')
def createprofile():
    return render_template('createprofile.html')


@app.route('/makeprofile', methods=['POST'])
def makeprofile():
    filename = request.form['firstname'] + request.form['lastname']
    socialmedia=request.form['socialmedia'].split("\n")
    d = {'name': request.form['firstname'] + " " + request.form['lastname'],
         'tagline': request.form['tagline'],
         'about': request.form['about'],
         'causes': request.form['causes'],
         'keywords': [request.form['firstname'], request.form['lastname'], request.form['firstname'] + " " + request.form['lastname'], request.form['tagline']],
         'socialmedia': socialmedia}
    with open("./" + filename + ".json", "w") as file:
        file.write(json.dumps(d))
    return(render_template('index.html'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=port)
