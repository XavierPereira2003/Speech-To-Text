import API
from flask import Flask, render_template, request, flash, redirect

app=Flask(__name__)

@app.route('/')
def index():
    durl='#'
    return render_template('index.html',durl=durl)

if __name__ == '__main__':
    app.run(debug=True)