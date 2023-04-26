from crypt import methods
import os
import json
#import psycopg2
from flask import Flask, render_template, jsonify, request, url_for, redirect

# ...

app = Flask(__name__)

@app.route('/')
def index():
    return "iae"

# if __name__ == '__name__':
#     app.run(host="0.0.0.0", port=5000, debug=True)
