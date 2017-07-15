from flask import g, Flask, redirect, Response
app = Flask(__name__)

cache = {}
cache['url'] = "https://google.co.uk"
    
@app.route('/')
def index():
    return redirect(cache['url'])

@app.route('/ping')
def ping():
    cache['url'] = "https://community.rs"
    return Response(status=202)
