<?php
$id=$_POST['id'];
$pw=$_POST['pw'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
	echo "<body bgcolor='#FFF2CC'>";
    die("Connection failed: ".mysqli_connect_error());
}

$select_query="select password from project.student where SNum = $id";
$result = mysqli_query($conn, $select_query);
if (!$result) {
    die("Select query failed: ".mysqli_error($conn));
}

while ($db=mysqli_fetch_array($result)) {
	$PW[]=$db[password];
}

if (in_array($pw, $PW)) {
    $insert_login = "UPDATE project.login SET std_num='$id' WHERE login=1";
	if ($conn->query($insert_login) === FALSE) {
    	echo "Login Error(MySql): " . $conn->error;
	}
	echo "<script language='javascript'>parent.location.replace('../main.html');</script>";
}
else {
	echo "<script language='javascript'>alert('Check your ID or Password');history.go(-1);</script>";
}
?>

<html>
<body bgcolor='#FFF2CC'>
</body>
</html>