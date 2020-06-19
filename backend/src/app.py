from flask import Flask, request
from flask_cors import CORS


import numpy as np
from scipy import fft, ifft

app = Flask(__name__)

CORS(app)

def validate(olistt):
    # Lista temporal sin comas 
    otemp = [n for n in olistt.split (",") if n != '']
    strPart = "1"
    signPart = "1"

    # Checar si tiene letras
    flag = 0 # si es correcta la cadena
    i = 0
    for n in otemp:
        if '*' in n:
            nTemp = n.replace('*','')
            i += 1
        else:
            nTemp = n
        if '-' in nTemp:
            nTemp = nTemp.replace('-','')
        if '.' in nTemp:
            nTemp = nTemp.replace('.','')
        if not (nTemp.isnumeric()):
            strPart = "0"
    
    
    # Checar cuantos ** tiene
    if i != 1:
        signPart = "0"
    flag = signPart + strPart
    if not otemp:
        flag = "00"
    print(flag)
    return flag

def transformList(listt):
    temp = [n for n in listt.split (",") if n != '']
    listt = []
    i = 1
    for n in temp:
        if '*' in n:
            listt.append(float(n.replace('*','')))
            origin = i
        else:
            listt.append(float(n))
        i += 1
    return listt, origin



@app.route('/', methods=['POST'])
def getSecuence():
    sec = request.json['sec']
    operation = request.json['ope']

    
    # validar

    origin = 0
    sec, origin = transformList(sec)
    sec = np.array(sec)
    y = fft(sec)
    return "<h1>Secuencia:</h1>" + str(sec) + "<h1>Origin:</h1>" + str(origin)+ "<h1>FFT:</h1>" + str(y)

@app.route('/', methods=['GET'])
def index():
    return '<h1>hello</h1>'

if __name__ == "__main__":
    app.run(debug=True)

