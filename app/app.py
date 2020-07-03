from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
from scipy import fft as fft

app = Flask(__name__, static_folder='../build/', static_url_path='/')

CORS(app)

def validate_sec(original_sec):
    """ Valida que la secuencia de entrada sea correcta"""
    # Lista temporal sin comas 
    temp_list = [n for n in original_sec.split (",") if n != '']
    flag = ''

    # Checar si es potencia de 2
    list_size = len(temp_list)
    if (list_size and (not(list_size & (list_size - 1))) ):
        flag += '1'
    else:
        flag += '0'
    

    # Checar si tiene letras
    flag2 = '1'
    for n in temp_list:
        n_temp = n
        try:
            n_temp = complex(n)
        except ValueError:
            flag2 = '0'
    
    # Organiza mi bandera final 
    if flag2 == '0':
        flag += '0'
    else: 
        flag += '1'

    return flag

def transform_list(original_list):
    '''Transforma el String en una lista de numeros Complejos'''
    temp_list = [n for n in original_list.split (",") if n != '']
    new_list = []
    i = 1
    for n in temp_list:
        new_list.append(complex(n))
        i += 1
    return new_list

# Obtiene la llamada POST desde el back
@app.route('/api/calculate', methods=['POST'])
def get_sequence():
    '''Obtiene la secuencia desde el Front, hace la operacion y 
    regresa el resultado '''
    sequence = request.json['sec']
    operation = request.json['ope']

    # Validar
    flag =  validate_sec(sequence)
    if (flag == '11'):
        # Hace la operacion
        if operation == 'FFT':
            y = fft.fft(transform_list(sequence))
        elif operation == 'IFFT':
            y = fft.ifft(transform_list(sequence))
        # Redondea y convierte en String
        y = np.array_str(np.around(y,2))
    elif flag == '01':
        y = 'La secuencia no es de tamaño n^2'
    elif flag == '10':
        y = 'La secuencia no es correcta'
    else:
        y = 'La secuencia no es de tamaño n^2 y tampoco esta escrita correctamente'

    # Regresa el resultado
    return jsonify(y)
    
@app.route('/')
def index():
    return app.send_static_file('index.html')

