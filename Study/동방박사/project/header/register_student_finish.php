<?php

$club_id=(int)$_POST['club_id'];
$contents=$_POST['registration'];
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$date = date("Y-m-d");

$login="select std_num from project.login";
$login_result = mysqli_query($conn, $login);
while ($data=mysqli_fetch_array($login_result)) {
	$std_num = $data[std_num];
}

$insert_regist = "insert into project.registration (student_SNum, club_ClubID, date, content) values ($std_num, $club_id, '$date', '$contents')";
$result_query = mysqli_query($conn, $insert_regist);

if (!$result_query) {
    die("Insert registration failed: ".mysqli_error($conn));
}

?>

<script language="Javascript">
	alert("동아리 지원이 완료되었습니다!");	
</script>
<meta http-equiv="refresh" content="0; url=../contents.html">

