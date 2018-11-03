from flask import Flask, render_template

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

@app.route('/profile')
def profile():
    return render_template('profile.html', name="Jane Doe", tagline="Testing", text1="I am performing a test",
                           imgsrc="../images/" + "img.png", text2="more testing whipeee yay!")


if __name__ == '__main__':
    app.run()
