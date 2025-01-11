<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEST WEB SVR</title>
    <style>
        body {
            background-color: lightgreen;
            color: black;
            text-align: center;
            font-size: 30px;
            font-family:'Times New Roman', Times, serif;
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
        <p>You have reached <?php $host=$_SERVER['HTTP_HOST']; echo $host; ?> </p>
    </div>
    <div class="footer">
        <p>The server is hosted at: <strong><?php echo gethostname(); ?></strong></p>
        <p>Remote Address: <?php $remote_addr=$_SERVER['REMOTE_ADDR']; echo $remote_addr; ?></p>
        <p>X Real IP: 
            <?php 
                if (!empty($_SERVER['HTTP_X_REAL_IP'])) {
                     $x_real_ip = $_SERVER['HTTP_X_REAL_IP'];

                } else {
                    $x_real_ip = 'NULL';

                }
                echo $x_real_ip;
            ?>
        </p>
        <p> X Forwarded For:
            <?php
                if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
                    $x_forwarded_for= $_SERVER['HTTP_X_FORWARDED_FOR'];
                
                } else {
                    $x_forwarded_for = 'NULL';

                }
                echo $x_forwarded_for;
            ?>
        </p>
    </div>
</body>
</html>