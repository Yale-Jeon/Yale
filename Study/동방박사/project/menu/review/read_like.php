<?php
	include "db.php";

	$idx=(int)$_GET['idx'];
	$std_num=(int)$_GET['std_num'];

	$sql = mq("select * from like_review where review_idx = '".$idx."'");
	$check_like = 0;
	while($data = $sql->fetch_array()){
		if ($data['student_SNum']==$std_num) {
			$check_like =1;
		}
	}
	if ($check_like==0) {
		$like = mq("insert into like_review (student_SNum, review_idx) values ($std_num, $idx)");
		$msg = "좋아요를 누르셨습니다!";	
	}else{
		$msg = "좋아요를 이미 누르셨습니다!";
	}
	
?>

<script type="text/javascript">
	alert("<?php echo " ".$msg." ";?>");
	window.close();
</script>