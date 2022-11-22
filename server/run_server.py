import os
from flask import Flask, request, render_template, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_folder=None)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///piano.db"

db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    notes = db.Column(db.String)
    is_correct = db.Column(db.Boolean, default=False)


CLIENT_FOLDER = os.path.abspath('../client/build')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/note', methods=['GET', 'POST'])
def note():
    result = None

    if request.method == 'POST':
        notes = request.get_json()
        if 'C#' in notes:
            result = True
        else:
            result = False
    else:
        result = {'note': 'C#'}
    
    return jsonify(result)

@app.route('/piano/', methods=['GET'])
def serve_app():
    return send_from_directory(CLIENT_FOLDER, 'index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    print(path)
    return send_from_directory(CLIENT_FOLDER, path)


def create_db_tables():
    print('creating tables...')
    with app.app_context():
        db.create_all()

        db.session.add(Submission(user_id='user1', notes="C,D,E,F,G,A,B"))
        db.session.commit()

        submissions = db.session.execute(db.select(Submission)).scalars()
        print(list(submissions))


if __name__ == "__main__":
    create_db_tables()
    app.debug = True
    app.run()