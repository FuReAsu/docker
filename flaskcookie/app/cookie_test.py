from flask import Flask, session, request, render_template_string
from werkzeug.middleware.proxy_fix import ProxyFix
import secrets
import socket


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)
app.secret_key = secrets.token_hex(32)   # Replace with a secure random key

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Test</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        button {
            margin: 10px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        p {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Session Cookie Test</h1>
        <p>You have reached {{host}}</p>
        <p>{{ message }}</p>
        <p>Server Name:[ {{server_name}} ]</p>
        <p>Client IP: [ {{client_ip}} ]</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
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
    return render_template_string(HTML_TEMPLATE, message=message, server_name=server_name, client_ip=client_ip, host=host)

app.run(host='0.0.0.0',debug=True)