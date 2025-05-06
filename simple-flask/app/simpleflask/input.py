from flask import Blueprint, render_template, request
import socket
import datetime
import os
import logging

logger = logging.getLogger(__name__)
input_bp = Blueprint('input', __name__)

FILE_PATH = os.getenv('DATA_PATH','data')
FILE_NAME = os.path.join(FILE_PATH, 'data.txt')

if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass
    logger.info(f"data file created at {FILE_NAME}")
else:
    logger.info(f"data file already exists")


@input_bp.route('/input', methods=['GET', 'POST'])
def input():
    now = datetime.datetime.now()
    server_name = socket.gethostname()
    if request.headers.get('X-Forwarded-For'):
        client_ip = request.headers.get('X-Forwarded-For')
    elif request.headers.get('X-Real-IP'):
        client_ip = request.headers.get('X-Real-IP')
    else:
        client_ip = request.remote_addr
    
    button_clicked = request.form.get('button')
    count = 1
    data_file = open(FILE_NAME, 'r').read()
    if data_file:
        for c in data_file:
            if c == '\n':
                count +=1
    if request.method == 'POST':
        if button_clicked == 'submitButton':
            input_data = request.form.get('input', '')
            with open(FILE_NAME, 'a') as f:
                f.write(f'{count} '+ input_data + '\n')
            logger.info(f"{client_ip} | data inputed: {input_data}")
        elif button_clicked == 'clearButton':
            open(FILE_NAME, 'w').close()
            logger.info(f"{client_ip} | data wiped")
    with open(FILE_NAME, 'r') as f:
        content = f.read()
    
    return render_template('input.html', content=content, server_name=server_name, client_ip=client_ip)
