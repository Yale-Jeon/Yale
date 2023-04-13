<?php
$title = $_POST['title'];
$date = $_POST['date'];
$club = $_POST['club_name'];
$writer = $_POST['writer'];
$time_must = (int)$_POST['time_must'];
$mood = (int)$_POST['mood'];
$time_spend = (int)$_POST['time_spend'];
$willing = (int)$_POST['willing'];
$friendliness = (int)$_POST['friendliness'];
$review = $_POST['text_review'];
#mysql 커넥션
require('../../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}
#학번 불러오기
$login="select std_num from project.login";
$result_login = mysqli_query($conn, $login);
while ($data=mysqli_fetch_array($result_login)) {
	$std_num=$data[std_num];
}
#동아리 데이터 불러오기
$club_data="select ClubID from project.club where project.club.clubname=$club";
$result_club = mysqli_query($conn, $club_data);
while ($data=mysqli_fetch_array($result_club)) {
	$club_num=$data[ClubID];
}
#리뷰 데이터 테이블에 집어넣기
$insert_review = "insert into project.review (review_name, review_date, student_SNum, writer, club_ClubID, time_must, mood, time_spend, willing, friendliness, review) values
('$title', '$date', $std_num, '$writer', $club_num, $time_must, $mood, $time_spend, $willing, $friendliness, '$review')";
$result_query = mysqli_query($conn, $insert_review);

if (!$result_query) {
    die("Insert Review failed: ".mysqli_error($conn));
}

?>
<html>
<body bgcolor="#FFF2CC">
<script language="Javascript">
	alert("리뷰가 정상적으로 작성되었습니다. 감사합니다!")
</script>
<input type="button" value="닫기" style="background-color: #CBD5BB;border:0; font-size: 20px; color: #BF9000;" onclick="window.close()">
</body>
</html>