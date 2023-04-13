<?php
	include "../../db.php"; /* db load */
?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	<?php
		$bno = $_GET['idx'];
		$sql = mq("select * from club where ClubID='".$bno."'");
		$data = $sql->fetch_array();
	?>

<div style="margin-top: 20px; width:900px;">
	<h2><?php echo "$data[clubname]"; ?></h2>
	<h4><a href="index.php">[목록으로]</a></h4>
	<div id="bo_line"></div><br>
	<table>
		<tr><td>분과</td><td><?php echo $data[part]; ?></td></tr>
		<tr><td>구분</td><td><?php echo $data[devision]; ?></td></tr>
		<tr><td colspan="2">동아리 소개글</td></tr>
		<tr><td colspan="2"><?php echo $data[club_intro]; ?></td></tr>
	</table>		
	<br><div style="width:880px; height:2px; background: gray;"></div><br>

	<?php
		$presi = $data['president_president_id'];
		$sql2 = mq("select * from president where president_id='".$presi."'");
		$data2 = $sql2->fetch_array();
	?>
	<p align="left">
	<table>
		<tr><td>이름</td><td><?php echo $data2['name']; ?></td></tr>
		<tr><td>연락처</td><td><?php echo $data2['phone']; ?></td></tr>
		<tr><td>e-mail</td><td><?php echo $data2['email']; ?></td></tr>
	</table>
	</p><div style="width:880px; height:2px; background: gray;"></div><br>

	<?php
		$query_review = mq("select * from review where club_ClubID='".$bno."'");
		$time_must=0;
		$mood=0;
		$time_spend=0;
		$willing=0;
		$friendliness=0;
		$review_count=0;
		while($db = $query_review->fetch_array()){
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
	<br><div id="bo_line"></div>
</div>
</body>
</html>