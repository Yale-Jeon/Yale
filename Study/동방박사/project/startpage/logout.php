<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$do_logout = "UPDATE project.login SET std_num=0 WHERE login=1";
if ($conn->query($do_logout) === FALSE) {
    echo "Error updating record: " . $conn->error;
}
?>
<script>
    alert('Log Out Successfully.');
    parent.location.href = "start.html";
</script>
</body>
</html>