from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/dataviz')
def dataviz():
    return render_template('dataviz.html')

@app.route('/automation')
def automation():
    return render_template('automation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
