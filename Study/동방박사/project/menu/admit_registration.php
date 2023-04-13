<?php
$list=$_POST['choice'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
$result_club = mysqli_query($conn, $find_club);
while ($data=mysqli_fetch_array($result_club)) {
	$clubid=$data[ClubID];
}
for ($i=0; $i < sizeof($list); $i++) { 
	$sql1 = "select student_SNum from registration where registrationid='".$list[$i]."'";
	$result_query = mysqli_query($conn, $sql1);
	while ($data=mysqli_fetch_array($result_query)) {
		$std_num=$data[student_SNum];
	}

	$sql = "insert into student_has_club (student_SNum, club_ClubID) values ($std_num, $clubid)";
	if ($conn->query($sql) === TRUE) {
    	echo "<script language='Javascript'>	alert('동아리지원서 승인이 성공적으로 완료되었습니다!');</script>";
	} else {
    	echo "Error deleting record: " . $conn->error;
	}
?>

<html><body bgcolor="#FFFBFO"></body></html>