<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEST WEB SVR</title>
    <style>
        body {
            background-color: green;
            color: white;
            text-align: center;
            font-size: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100vh;
            margin: 0;
        }
        .header {
            margin-top: 20px;
        }
        .footer {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>NGINX TEST WEB SERVER!</h1>
        <p>webserver hosted on nginx container</p>
    </div>
    <div class="footer">
        <p>The server is hosted at: <strong><?php echo gethostname(); ?></strong></p>
        <p>You are accessing from: <?php $client_ip = $_SERVER['REMOTE_ADDR']; echo $client_ip;?> </p>
    </div>
</body>
</html>