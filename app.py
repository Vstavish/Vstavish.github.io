from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

# Define your routes
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

# Initialize Freezer before running the app
freezer = Freezer(app)

# Use this block to freeze your app (for static files generation)
if __name__ == '__main__':
    # Uncomment this line if you want to freeze your app to static files
    # freezer.freeze()  
    app.run(debug=True)