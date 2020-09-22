from flask import Flask
from wsgiref.simple_server import make_server

dest_path = r'E:\wjmhd'

app = Flask(__name__)
app.debug=True
@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/<int:folder_id>')
def show_post(folder_id):
    
    return 

if __name__ == '__main__':
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run()