from flask import Flask, render_template, request
from botSeguirHastag import *
import sys
import os
import requests


app = Flask(__name__)
@app.route('/', methods=['GET'],)
def index():
    return render_template('index.html')
@app.route('/cadastrar', methods=['POST'],)
def iniciar():
    site = "https://www.instagram.com/explore/tags/"
    hastag = request.form['hastag']
    chrome = ChromeAuto()
    chrome.acessa(site + f'{hastag}')
    chrome.login()
    sleep(10)
    chrome.agoran()
    sleep(2)
    chrome.abrircurtir()
    sleep(2)
    chrome.bot()
    return render_template("index.html")


if __name__=='__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
