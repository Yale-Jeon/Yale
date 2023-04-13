<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$list=$_POST['choice'];
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
$result_club = mysqli_query($conn, $find_club);
while ($data=mysqli_fetch_array($result_club)) {
	$clubid=$data[ClubID];
}

for ($i=0; $i < sizeof($list); $i++) { 
	$value3=$list[$i];
	$sql = "DELETE FROM project.student_has_club WHERE student_SNum=$value3 and club_ClubID=$clubid";
	if ($conn->query($sql) === TRUE) {
    	echo "<script language='Javascript'>	alert('동아리원 삭제가 성공적으로 진행되었습니다!')</script>";
	} else {
    	echo "Error deleting record: " . $conn->error;
	}
}
?>

<html>
<body bgcolor="#FFFBFO"><br>
<p align="right"><input type="button" style="width: 70px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" onclick="window.close();" value="닫기"></p>
</body>
</html>