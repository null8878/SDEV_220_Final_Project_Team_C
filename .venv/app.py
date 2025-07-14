from flask import Flask, render_template
from data import db

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
