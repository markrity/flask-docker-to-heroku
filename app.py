from flask import Flask
from os import environ
app = Flask(__name__)
@app.route('/')
def hello():
  return "Hello World123!"
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))
