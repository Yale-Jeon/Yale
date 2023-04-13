<html>
<body bgcolor="#FFFBF0">
<div style="margin-top: 40px; margin-left: 50px; font-size: 25px;"><b>리뷰 상세 보기</b></div><br>
<div style="margin-left: 55px; margin-bottom: 20px; font-size: 15px;">동방박사 사이트에서 해당 동아리에 작성된 모든 리뷰를 표시합니다</div>
<table align="center" style="width: 90%;">
	<tr align="center" bgcolor="#FFF2CC" style="font-size: 15px; "><b>
		<td style="width: 10%;"><div style="margin-top: 10px; margin-bottom: 10px; ">리뷰제목</div></td>
		<td style="width: 5%;">날짜</td>
		<td style="width: 10%;">이름</td>
		<td style="width: 10%;">점수표시</td>
		<td>리뷰내용</td></b>
	</tr>
	<?php
	require('../data_mysql.php');
	$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
	if (!$conn) {
    	die("Connection failed: ".mysqli_connect_error());
	}
	$query_club = "select ClubID,clubname from project.club, project.login where project.club.president_president_id=project.login.std_num";
	$result_club = mysqli_query($conn, $query_club);
	while ($data=mysqli_fetch_array($result_club)) {
		$clubid=$data[ClubID];
	}

	$query_review="select review_name,review_date,student_SNum,writer,club_ClubID,time_must,mood,time_spend,willing,friendliness,review from project.review where project.review.club_ClubID = $clubid";
	$time_must=0;
	$mood=0;
	$time_spend=0;
	$willing-0;
	$friendliness=0;
	$result_review = mysqli_query($conn, $query_review);
	while ($db=mysqli_fetch_array($result_review)) {
		echo "<tr align='center' style='height:20px;'><td>$db[review_name]</td>";
		echo "<td>$db[review_date]</td>";
		echo "<td>$db[writer]</td>";
		echo "<td>$db[time_must]|$db[mood]|$db[time_spend]|$db[willing]|$db[friendliness]</td>";
		$time_must+=$db[time_must];
		$mood+=$db[mood];
		$time_spend+=$db[time_spend];
		$willing+=$db[willing];
		$friendliness=$db[friendliness];
		echo "<td align='left'>$db[review]</td></tr>";
	}
	?>
</table>
</body>
</html>