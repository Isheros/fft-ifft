from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
from scipy import fft as fft

app = Flask(__name__, static_folder='../build/', static_url_path='/')

CORS(app)

def validate_sec(original_sec):
    """ Valida que la secuencia de entrada sea correcta"""
    # Lista temporal sin comas 
    list_temp = [n for n in original_sec.split (",") if n != '']
    flag = ''

    # Checar si es potencia de 2
    list_size = len(list_temp)
    if (list_size and (not(list_size & (list_size - 1))) ):
        flag += '1'
        #print(list_size, ' es potencia de 2')
    else:
        flag += '0'
        #print(list_size, ' no es potencia de 2')
    

    # Checar si tiene letras
    flag2 = '1'
    for n in list_temp:
        n_temp = n
        try:
            n_temp = complex(n)
            #print(n_temp, ' es complejo')
        except ValueError:
            #print(n_temp, ' no es complejo')
            flag2 = '0'
    
    # Organiza mi bandera final 
    if flag2 == '0':
        flag += '0'
    else: 
        flag += '1'

    return flag

def transformList(listt):
    '''Transforma el String en una lista de numeros Complejos'''
    temp = [n for n in listt.split (",") if n != '']
    listt = []
    i = 1
    for n in temp:
        listt.append(complex(n))
        i += 1
    return listt


# Obtiene la llamada POST desde el back
@app.route('/api/calculate', methods=['POST'])
def getSecuence():
    '''Obtiene la secuencia desde el Front, hace la operacion y regresa el resultado '''
    sec = request.json['sec']
    operation = request.json['ope']

    # Validar
    flag =  validate_sec(sec)
    if (flag == '11'):
        # Hace la operacion
        if operation == 'FFT':
            y = fft.fft(transformList(sec))
        elif operation == 'IFFT':
            y = fft.ifft(transformList(sec))
        # Redondea y convierte en String
        y = np.array_str(np.around(y,2))
    elif flag == '01':
        y = 'La secuencia no es de tamaño n^2'
    elif flag == '10':
        y = 'La secuencia no es correcta'
    else:
        y = 'La secuencia no es de tamaño n^2 y tampoco esta escrita correctamente'
    # Debug
    # print(sec)
    # print(operation)
    # print(y)

    # Regresa el resultado
    return jsonify(y)
    
@app.route('/')
def index():
    return app.send_static_file('index.html')

