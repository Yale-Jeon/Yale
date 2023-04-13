<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
	<div style="margin-top: 40px; margin-left: 50px; font-size: 25px;"><b>동아리 및 대표 계정 정보 보기</b></div><br>
	<div style="margin-left: 55px; margin-bottom: 20px;">동방박사 동아리 정보 조회/수정창입니다</div>
	<table align="center" style="width: 80%;">
		<tr>
			<td colspan="2" bgcolor="#BF9000" style="height: 30px; color: white;"><div style="margin-left: 10px; font-size: 20px;">동아리 정보</div></td>
		</tr>
		<?php
		require('../data_mysql.php');
		$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
		$query="select clubname,part,devision,club_intro,president_president_id from project.club, project.login where project.login.std_num = project.club.president_president_id";
		$result = mysqli_query($conn, $query);
		while ($data=mysqli_fetch_array($result)) {
			echo "<tr><td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>동아리이름</td><td>".$data[clubname]."</td></tr>";
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>분 과</td><td>".$data[part]."</td></tr>";
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>분 류</td><td>".$data[devision]."</td></tr>"; 
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>동아리소개</td><td>".$data[club_intro]."</td></tr>";
		}
		?>
		<tr>
			<td colspan="2" bgcolor="#BF9000" style="height: 30px; color: white;"><div style="margin-left: 10px; font-size: 20px;">대표 정보</div></td>
		</tr>
		<?php
		require('../data_mysql.php');
		$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
		if (!$conn) {
    		die("Connection failed: ".mysqli_connect_error());
		}
		$query_presi="select name,phone,email from project.president, project.login where project.login.std_num = project.president.president_id";
		$result_presi = mysqli_query($conn, $query_presi);
		while ($data=mysqli_fetch_array($result_presi)) {
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>대표아이디</td><td>$data[name]</td></tr>";
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>전화번호</td><td>$data[phone]</td></tr>";
			echo "<tr><td align='center' style='height:30px; background-color:#FFF2CC;'>이메일</td><td>$data[email]</td></tr>"; 
		}
		?>
		<tr>
			<td colspan="2" align="right">
				<a href="manage_club_information.php"><input type="button" value="수정하기" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;"></a>
				<a href="../contents_presi.html" target="content"><button style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;">홈으로</button></a>
			</td>
		</tr>
	</table>
</body>
</html>

