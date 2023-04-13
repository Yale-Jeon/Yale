<!DOCTYPE html>
<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<div style="margin-top: 40px; margin-left: 50px; font-size: 25px;"><b>동아리 리뷰 전체 보기</b></div><br>
<div style="margin-left: 55px; margin-bottom: 20px; font-size: 15px;">동방박사 사이트에서 해당 동아리에 작성된 모든 리뷰를 보실 수 있습니다</div>

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
		$clubname=$data[clubname];
	}

	$query_review="select * from review where review.club_ClubID = $clubid";
	$time_must=0;
	$mood=0;
	$time_spend=0;
	$willing=0;
	$friendliness=0;
	$review_count=0;
	$result_review = mysqli_query($conn, $query_review);
	while ($db=mysqli_fetch_array($result_review)) {
		$time_must+=$db[time_must];
		$mood+=$db[mood];
		$time_spend+=$db[time_spend];
		$willing+=$db[willing];
		$friendliness=$db[friendliness];
		$review_count+=1;
	}

	$avg_t_m=200*$time_must/$review_count;
	$avg_mood=200*$mood/$review_count;
	$avg_t_s=200*$time_spend/$review_count;
	$avg_w=200*$willing/$review_count;
	$avg_f=200*$friendliness/$review_count;
	?>
<br>
<table align="center" style="width: 80%;">
	<tr>
		<td colspan="4" bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">종합 평점</div></td>
	</tr>
	<tr>
		<td rowspan="3" align="center" style="width: 20%;">로 드</td>
		<td colspan="3"><img style="width: 1000px; height: 10px;" src="review_bar.png"></td>
	</tr>
	<tr>
		<td colspan="3">
			<?php
			for ($i=0; $i <(int)$avg_t_m ; $i++) { 
				echo"<img style='width: 1px; height: 10px;' src='bar.png'>";
			}
			$avg_t_m=$avg_t_m/200;
			echo "|$avg_t_m";
			?>
		</td>
	</tr>
	<tr>
		<td style="width: 5%; font-size: 10px;">없음</td>
		<td style="width: 90%;"></td>
		<td align="right" style="width: 5%; font-size: 10px;">많음</td>
	</tr>
	<tr>
		<td rowspan="3" align="center">분위기</td>
		<td colspan="3"><img style="width: 1000px; height: 10px;" src="review_bar.png"></td>
	</tr>
	<tr>
		<td colspan="3">
			<?php
			for ($i=0; $i <(int)$avg_mood ; $i++) { 
				echo"<img style='width: 1px; height: 10px;' src='bar.png'>";
			}
			$avg_mood=$avg_mood/200;
			echo "|$avg_mood";
			?>
		</td>
	</tr>
	<tr>
		<td style="width: 5%; font-size: 10px;">조용함</td>
		<td style="width: 90%;"></td>
		<td align="right" style="width: 5%; font-size: 10px;">활발함</td>
	</tr>
	<tr>
		<td rowspan="3" align="center">소요시간</td>
		<td colspan="3"><img style="width: 1000px; height: 10px;" src="review_bar.png"></td>
	</tr>
	<tr>
		<td colspan="3">
			<?php
			for ($i=0; $i <(int)$avg_t_s ; $i++) { 
				echo"<img style='width: 1px; height: 10px;' src='bar.png'>";
			}
			$avg_t_s=$avg_t_s/200;
			echo "|$avg_t_s";
			?>
		</td>
	</tr>
	<tr>
		<td style="width: 20%; font-size: 10px;">시간을 거의 투자하지 않음</td>
		<td style="width: 60%;"></td>
		<td align="right" style="width: 20%; font-size: 10px;">시간을 많이 투자함</td>
	</tr>
	<tr>
		<td rowspan="3" align="center">자발성</td>
		<td colspan="3"><img style="width: 1000px; height: 10px;" src="review_bar.png"></td>
	</tr>
	<tr>
		<td colspan="3">
			<?php
			for ($i=0; $i <(int)$avg_w ; $i++) { 
				echo"<img style='width: 1px; height: 10px;' src='bar.png'>";
			}
			$avg_w=$avg_w/200;
			echo "|$avg_w";
			?>
		</td>
	</tr>
	<tr>
		<td style="width: 5%; font-size: 10px;">없음</td>
		<td style="width: 90%;"></td>
		<td align="right" style="width: 5%; font-size: 10px;">자발</td>
	</tr>
	<tr>
		<td rowspan="3" align="center">친밀도</td>
		<td colspan="3"><img style="width: 1000px; height: 10px;" src="review_bar.png"></td>
	</tr>
	<tr>
		<td colspan="3">
			<?php
			for ($i=0; $i <(int)$avg_f ; $i++) { 
				echo"<img style='width: 1px; height: 10px;' src='bar.png'>";
			}
			$avg_f=$avg_f/200;
			echo "|$avg_f";
			?>
		</td>
	</tr>
	<tr>
		<td style="width: 5%; font-size: 10px;">어색</td>
		<td style="width: 90%;"></td>
		<td align="right" style="width: 5%; font-size: 10px;">과함</td>
	</tr>
</table>
<p align="left" style="margin-left: 30px;"><a href="../menu/review/index.php?search_type=club_name&search=<?php echo $clubname; ?>">내 동아리 리뷰 보러가기</a></p>
</body>
</html>