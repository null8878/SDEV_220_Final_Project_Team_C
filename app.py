from flask import Flask, render_template
from data import db

app = Flask(__name__)
app.config['DATABASE'] = 'data.database'
app.app_context().push()
db.init_app(app)

@app.route('/')
def index():
    # return all data from the database
    database = db.get_db()
    return render_template('index.html', database=database)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
