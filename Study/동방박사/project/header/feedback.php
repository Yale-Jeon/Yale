<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$query="select std_num from project.login";
$result = mysqli_query($conn, $query);
while ($db=mysqli_fetch_array($result)) {
	$student=(int)$db[std_num];
}

$feedback=$_POST['feedback'];
$insert_fb = "INSERT into project.feedback (feedback, student_SNum) values ('$feedback', $student)";
$result_query = mysqli_query($conn, $insert_fb);

if (!$result_query) {
    die("Insert query failed: ".mysqli_error($conn));
}
?>

<script language="Javascript">
	alert("피드백이 접수되었습니다!");
	window.close();
</script>
