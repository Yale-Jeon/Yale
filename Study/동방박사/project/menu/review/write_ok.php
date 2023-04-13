<meta charset="utf-8">

<?php
include "db.php";
$date = date('Y-m-d');
$userpw = password_hash($_POST['pw'], PASSWORD_DEFAULT);

$title = $_POST['title'];
$club = $_POST['club_name'];
$name = $_POST['name'];

$time_must = (int)$_POST['time_must'];
$mood = (int)$_POST['mood'];
$time_spend = (int)$_POST['time_spend'];
$willing = (int)$_POST['willing'];
$friendliness = (int)$_POST['friendliness'];
$review = $_POST['text_review'];

#학번 불러오기
$sql = mq("select * from login");  
while($data = $sql->fetch_array()){
	$std_num = $data['std_num'];
}

#동아리 데이터 불러오기
$sql2=mq("select * from club where clubname='$club'");
while ($data = $sql2->fetch_array()){
	$club_num = $data['ClubID'];
}

#리뷰 데이터 테이블에 집어넣기
$insert_review = mq("insert into review (title, name, date, student_SNum, club_ClubID, club_name, time_must, mood, time_spend, willing, friendliness, review) values ('$title', '$name', '$date', $std_num, $club_num, '$club', $time_must, $mood, $time_spend, $willing, $friendliness, '$review')");
?>

<script type="text/javascript">alert("리뷰가 정상적으로 작성되었습니다. 감사합니다!");</script>
<meta http-equiv="refresh" content="0; url=index.php">