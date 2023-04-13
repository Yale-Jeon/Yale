<?php
$list=$_POST['choice1'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
$result_club = mysqli_query($conn, $find_club);
while ($data=mysqli_fetch_array($result_club)) {
	$clubid=$data[ClubID];
}

$submit=$_POST['submit_check'];

if ($submit == 'accept') {
	for ($i=0; $i < sizeof($list); $i++) { 
		$value1=$list[$i];
		$sql = "UPDATE project.club_activity_registration SET fixed=1 WHERE idclub_activity_registration=$value1";
		if ($conn->query($sql) === FALSE) {
		    echo "Error updating: " . $conn->error;
		}
	}    
} else if ($submit == 'reject') {
    for ($i=0; $i < sizeof($list); $i++) { 
		$value2=$list[$i];
		$sql2 = "UPDATE project.club_activity_registration SET fixed=-1 WHERE idclub_activity_registration=$value2";
		if ($conn->query($sql2) === FALSE) {
			echo "Error updating: " . $conn->error;
		}
	}
}

?>

<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<script language='Javascript'>alert('성공적으로 반영되었습니다!')</script>
</body>
</html>