<?php
require('../../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$value1 = $_POST["month"];
$value2=$_POST["day"];
$value3=$_POST["time"];
$value4=$_POST["place"];
$list=$_POST['choice'];
$title=$_POST['title'];
$value6=$_POST['new_event'];
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}
$query="select ClubID from project.club, project.login where project.club.president_president_id = project.login.std_num";
$result = mysqli_query($conn, $query);
while ($data=mysqli_fetch_array($result)) {
	$clubid=$data[ClubID];
}

for ($i=0; $i < sizeof($list); $i++) { 
	$value5=$list[$i];
	$insert = "insert into project.club_activity (club_ClubID, month, day, time, place, part, information, title) values ($clubid, '$value1','$value2','$value3','$value4','$value5','$value6', '$title')";
	$result = mysqli_query($conn, $insert);
	if (!$result) {
		die("Insert query failed: ".mysqli_error($conn));
	}
}

?>

<html>
<body bgcolor="#FFFBF0">
<script language="Javascript">
	alert("이벤트 생성이 완료되었습니다!")
</script>
</html>