<?php
	include "db.php"; /* db load */
?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	<?php
		$bno = $_GET['idx']; /* bno함수에 idx값을 받아와 넣음*/
		$hit = mysqli_fetch_array(mq("select * from review where idx ='".$bno."'"));
		$hit = $hit['hit'] + 1;
		$fet = mq("update review set hit = '".$hit."' where idx = '".$bno."'");
		$sql = mq("select * from review where idx='".$bno."'"); /* 받아온 idx값을 선택 */
		$data = $sql->fetch_array();
	?>
<!-- 글 불러오기 -->
<div id="board_read">
	<h2><?php echo $data['title']; ?></h2>
		<div id="user_info">
			<?php echo $data['name']; ?> <?php echo $data['date']; ?> 조회:<?php echo $data['hit']; ?>
				<div id="bo_line"></div>
			</div>
			<div id="bo_content">
				<?php 
					### review 점수 표시
					$time_must=['응답없음','거의없음','조금','있는 것 같다','많은 편','매우 바쁨'];
					$mood=['응답없음','침착하고 조용해요','조곤조곤 얘기해요','도란도란 노는 거 좋아해요!','재밌어요!','Ho! 엔트로피 톡톡톡!'];
					$time_spend=['응답없음','주 2시간 이내','3-5일에 1-3시간','1-3일에 1-3시간','매일 1.5~4시간','연애하는 줄...'];
					$willing=['응답없음','유령회원 많죠...','적당히..참여는 해요~','새로운 일...해볼까요?','하고 싶은 일 같이 해요~','모두가 일을 못 만들어서 난리!'];
					$friendliness=['응답없음','시선을 피한다','인사 정도는 한다','친하다','많이 친하다','모두 다 너무 친하다(동아리 내에서만 인간관계가 쌓인다)'];

					echo "<table border='1'>";
					echo "<tr><td>질문</td><td>점수</td><td>내용</td></tr>";
					echo "<tr><td>로드</td><td>".$data['time_must']."</td><td>".$time_must[$data['time_must']]."</td></tr>";
					echo "<tr><td>분위기</td><td>".$data['time_must']."</td><td>".$mood[$data['mood']]."</td></tr>";
					echo "<tr><td>활동시간</td><td>".$data['time_must']."</td><td>".$time_spend[$data['time_spend']]."</td></tr>";
					echo "<tr><td>적극성</td><td>".$data['time_must']."</td><td>".$willing[$data['willing']]."</td></tr>";
					echo "<tr><td>친밀함</td><td>".$data['time_must']."</td><td>".$friendliness[$data['friendliness']]."</td></tr></table>";

					echo nl2br("$data[review]");

					### 동아리 전반적인 내용 보여주기
				?>
			</div>
	<?php
		$std = mq("select * from login");
		while($std_sql = $std->fetch_array()){
			$std_num = $std_sql['std_num'];
		}


		$like = mq("select * from like_review where review_idx = '".$bno."'");
		$like_num = 0;
		while($data = $like->fetch_array()){
			$like_num += 1;
		}
		?>
	<!-- 목록, 수정, 삭제 -->
	<div id="bo_ser">
		<ul>
			<li><a href="read_like.php?idx=<?php echo $bno; ?>&std_num=<?php echo "$std_num"; ?>" target="_blank"> <img src="like.png" width="15" height="15"></a> <?php echo "$like_num";?></li>
			<li><a href="index.php">[목록으로]</a></li>
			<li><a href="modify.php?idx=<?php echo $bno; ?>" target="_blank">[수정]</a></li>
			<li><a href="delete.php?idx=<?php echo $bno; ?>">[삭제]</a></li>
		</ul>
	</div>
</div>
</body>
</html>