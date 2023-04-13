<?php
require('data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$query="select std_num,clubname from project.login,project.club where project.login.std_num=project.club.president_president_id";
$result = mysqli_query($conn, $query);
while ($data=mysqli_fetch_array($result)) {
	echo "<p style='size: 20px;' align='right'>$data[std_num] | $data[clubname]</p>";
}
?>

<html>
<meta charset="utf-8">
<head>
	<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic:400,700,800&subset=korean');
</style>
</head>
<body bgcolor="#FFF2CC">
<p align="right">
<a href="header/club_information.php" target="content"><button type="button" style="width: 140px; height: 15px; background-color:#FFF2CC; border: 0; font-family:Nanum Gothic; font-size: 18px;">Club Info</button></a>
<a href="header/manage_review.php" target="content"><button type="button" style="width: 160px; height: 15px; background-color:#FFF2CC; border: 0; font-family:Nanum Gothic; font-size: 18px;">동아리 리뷰 확인</button></a>
<button type="button" style="width: 160px; height: 15px; background-color:#FFF2CC; border: 0; font-family:Nanum Gothic; font-size: 18px;" onclick="window.open('header/presi_register.php','window_name','width=800,height=600,location=no,status=no,scrollbars=yes');">신규 동아리 제보</button>
<button type="button" style="width: 90px; height: 15px; background-color:#FFF2CC; border: 0; font-family:Nanum Gothic; font-size: 18px;" onclick="window.open('header/feedback.html','window_name','width=800,height=500,location=no,status=no,scrollbars=yes');">feedback</button>
<button type="button" style="width: 90px; height: 18px; background-color:#FFF2CC; border: 0; font-family:Nanum Gothic; font-size: 18px;" onclick="location.href='startpage/logout.php'">로그아웃</button></p>
</body>
</html>