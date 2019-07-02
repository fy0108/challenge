from flask import Flask, render_template
from flask import abort
import os, json

app = Flask(__name__)

new_path = '/home/shiyanlou/files'
def json_data():
    data = []
    for filename in os.listdir(new_path):
        file_path = new_path + '/' + filename
        with open(file_path) as f:
            data.append(json.load(f))
    return data

def json_hsyl(filename):
    file_path = new_path + '/' + filename + '.json'
    with open(file_path) as f:
        data = json.load(f)
    return data

@app.route('/')
def index():
    data = json_data()
    return render_template('index.html', data=data)

@app.route('/files/<filename>')
def files(filename):
    if filename == 'helloshiyanlou':
        data = json_hsyl(filename)
        return render_template('file.html', data=data)
    elif filename == 'helloworld':
        data = json_hsyl(filename)
        return render_template('file.html', data=data)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()

