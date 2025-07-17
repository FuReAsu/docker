from flask import Blueprint, render_template, request, session
import secrets
import socket
import logging

cookies_bp = Blueprint('cookies', __name__)
logger = logging.getLogger(__name__)

@cookies_bp.route("/cookies", methods=["GET"])
def cookies():
    server_name = socket.gethostname()

    if request.headers.get('X-Forwarded-For'):
        client_ip = request.headers.get('X-Forwarded-For')
    elif request.headers.get('X-Real-IP'):
        client_ip = request.headers.get('X-Real-IP')
    else:
        client_ip = request.remote_addr

    host = request.host

    if request.method == 'GET':
        if 'session_id' in session:
            message = f'Your session_id is {session["session_id"]}'
        else:
            session['session_id'] = secrets.token_hex(16)
            message = 'Your session cookie has been set'
            logger.info(f"{client_ip} | cookie {session["session_id"]} set for client")
    message =""
    return render_template('cookies.html', message=message, server_name=server_name, client_ip=client_ip, host=host)

