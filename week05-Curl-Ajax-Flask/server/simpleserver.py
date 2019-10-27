#!flask/bin/python
from flask import Flask, request, send_from_directory

'''
from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
'''


# Need to define app before using it...
app = Flask(__name__, 
            static_url_path='', 
            static_folder='../')
# Flask(__name__, static url path='', static_folder='../')
#app Flask(static url path='', static_folder='../')
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__' :
    app.run(debug=True)