from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="root",
    hostname="localhost",
    databasename="clicks",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ButtonClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5))


@app.route('/')
def index():
    '''
    direc = request.args.get('direction')
    print()
    print('Direction:', direc)
    print()
    '''
    return render_template('index.html')

@app.route('/clicks', methods=['POST', 'GET'])
def clicks():
    if request.method == 'POST':
        direc = ButtonClick(content=request.form.get('direction'))
        db.session.add(direc)
        db.session.commit()
        button_direction = ButtonClick.query.order_by(ButtonClick.id.desc()).first()
        return jsonify(button_direction.content)

if __name__ == '__main__':
    app.run()   

