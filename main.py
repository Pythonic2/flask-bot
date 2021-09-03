from flask import Flask, render_template, request
from botSeguirHastag import *
import sys

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
    log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
if __name__=='__main__':
    app.run(debug=True)
