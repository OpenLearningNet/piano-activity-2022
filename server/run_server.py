import os
from flask import Flask, request, render_template, send_from_directory, jsonify
app = Flask(__name__, static_folder=None)

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

if __name__ == "__main__":
    app.debug = True
    app.run()
