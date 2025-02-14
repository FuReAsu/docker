from flask import Flask, render_template_string, request
from werkzeug.middleware.proxy_fix import ProxyFix
import socket
import datetime
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)
FILE_PATH = os.getenv('DATA_PATH','data/data.txt')

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask File I/O</title>
    <h1> Flask File Test </h1>
    <p> Flask App to test persistent storage </p>
    <p>Server Name:[ {{server_name}} ]</p>
    <p>Client IP: [ {{client_ip}} ]</p>
    <style>
        body {
            background-color: white;
            color: black;
            font-family:'Times New Roman', Times, serif;
            font-size: 20px;
            height: 100vh;
            margin: 0;
        }
    </style>
    <script>
        function submitData(event, action) {
            event.preventDefault();
            let inputValue = document.getElementById('inputBox').value;
            let formData = new URLSearchParams();
            if (action === 'submit') {
                formData.append('input', inputValue);
                formData.append('button', 'submitButton');
            } else if (action === 'clear') {
                formData.append('button', 'clearButton');
            }
            
            fetch('/', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: formData.toString()
            })
            .then(() => {
                document.getElementById('inputBox').value = '';
                location.reload();
            });
        }
    </script>
</head>
<body>
    <input type="text" id="inputBox" placeholder="Enter something">
    <button onclick="submitData(event, 'submit')">Submit</button>
    <button onclick="submitData(event, 'clear')">Clear</button>
    <pre id="outputBox">{{ content }}</pre>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
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
    data_file = open(FILE_PATH, 'r').read()
    if data_file:
        for c in data_file:
            if c == '\n':
                count +=1
    if button_clicked == 'submitButton' and request.method == 'POST':
        input_data = request.form.get('input', '')
        with open(FILE_PATH, 'a') as f:
            f.write(f'{count} '+ input_data + '\n')
        print(f"{client_ip} - - [{now}] data inputed: {input_data}")
    elif button_clicked == 'clearButton':
        open(FILE_PATH, 'w').close()
        print(f"{client_ip} - - [{now}] data wiped")
    with open(FILE_PATH, 'r') as f:
        content = f.read()
    
    return render_template_string(HTML_PAGE, content=content, server_name=server_name, client_ip=client_ip)

if __name__ == '__main__':
    app.run(debug=True)
