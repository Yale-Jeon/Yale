<?php
$phone=$_POST["pnum"];
$email=$_POST["mail"];
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$student="select std_num from project.login";
$result = mysqli_query($conn, $student);
while ($db=mysqli_fetch_array($result)) {
	$name=$db[std_num];
}

$change_phone="UPDATE project.student SET phone='$phone' WHERE SNum=$name";
if ($conn->query($change_phone) === FALSE) {
    echo "Phone Error: " . $conn->error;
}
$change_mail="UPDATE project.student SET email='$email' WHERE SNum=$name";
if ($conn->query($change_mail) === FALSE) {
    echo "Email Error: " . $conn->error;
}
?>

<script type="text/javascript">
alert("수정되었습니다.");
</script>
<meta http-equiv="refresh" content="0; url=my_information.php">