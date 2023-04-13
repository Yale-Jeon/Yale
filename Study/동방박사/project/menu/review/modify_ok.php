<meta charset="utf-8">

<?php
include "db.php";

$bno = $_POST['idx'];

$date = date('Y-m-d');
#$pw = $_POST['pw'];

$title = $_POST['title'];
$club = $_POST['club_name'];
$name = $_POST['name'];

$time_must = (int)$_POST['time_must'];
$mood = (int)$_POST['mood'];
$time_spend = (int)$_POST['time_spend'];
$willing = (int)$_POST['willing'];
$friendliness = (int)$_POST['friendliness'];
$review = $_POST['text_review'];


#$check_pw = mq("select * from review where idx='$bno'");
#$Origin_pw = $check_pw->fetch_array();
###
#if ($pw==$Origin_pw['password']) {
	$sql = mq("update review set title='".$title."',name='".$name."', date='".$date."', time_must='".$time_must."', mood='".$mood."', time_spend='".$time_spend."', willing='".$willing."', review='".$review."', friendliness='".$friendliness."' where idx='$bno'");
	$msg = "수정되었습니다.";
#}else{
#	$msg = "비밀번호가 틀렸습니다!";
#}

?>

<script type="text/javascript">
	alert("<?php echo " ".$msg." ";?>");
	window.close();
</script>