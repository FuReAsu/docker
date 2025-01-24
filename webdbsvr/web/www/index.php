<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Information</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: blue; }
        .footer{
            margin-bottom: 5px;
            text-align: center;
            font-family: 'Times New Roman', Times, serif;
            font-size: 15px;
            margin: 0;
        }
    </style>
</head>
<body>

<h2>User Information</h2>

<?php
// Database connection
$servername = "dbsvr";
$username = "webadmin";
$password = "webadmin_P@ssw0rd";
$dbname = "testdb";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to retrieve data
$sql = "SELECT uc.username, ui.name, ui.email, ui.age
        FROM user_credentials AS uc
        JOIN user_info AS ui ON uc.user_id = ui.user_id";
$result = $conn->query($sql);

if ($result && $result->num_rows > 0) {
    echo "<table>
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Age</th>
                </tr>
            </thead>
            <tbody>";
    
    // Output each row as a table row
    while ($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . htmlspecialchars($row['username']) . "</td>
                <td>" . htmlspecialchars($row['name']) . "</td>
                <td>" . htmlspecialchars($row['email']) . "</td>
                <td>" . htmlspecialchars($row['age']) . "</td>
              </tr>";
    }
    
    echo "</tbody></table>";
} else {
    echo "<p>No user information found.</p>";
}

$conn->close();
?>
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

