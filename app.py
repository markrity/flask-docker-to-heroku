from flask import Flask
from os import environ
app = Flask(__name__)
@app.route('/')
def hello():
  return "<h1>Hello World</h1>"
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))
