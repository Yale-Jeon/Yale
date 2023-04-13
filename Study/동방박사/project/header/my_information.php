<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 100px; font-size: 25px;"><b>프로필 보기</b></div><br>
<div style="margin-left: 100px;">동방박사 프로필 조회/수정창입니다</div>
<p align="right">
	<a href="manage_my_information.php"><input type="button" value="수정하기" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;"></a>
</p>

<table align="center" style="width: 70%;" bgcolor="#FFFBF0">
	<tr>
		<?php
		require('../data_mysql.php');
		$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
		$query="select SNum,Name,phone,email from project.student,project.login where project.login.std_num=project.student.SNum";
		$result = mysqli_query($conn, $query);
		while ($data=mysqli_fetch_array($result)) {
			echo "<tr style='height:50px;'><td bgcolor='#FFF2CC' align='center' style='width:12%;'>학 번</td><td><div style='margin-left:10px;'>".$data[SNum]."</div></td></tr>";
			echo "<tr style='height:50px;'><td bgcolor='#FFF2CC' align='center'>이 름</td><td><div style='margin-left:10px;'>".$data[Name]."</div></td></tr>";
			echo "<tr style='height:50px;'><td bgcolor='#FFF2CC' align='center'>전화번호</td><td><div style='margin-left:10px;'>".$data[phone]."</div></td></tr>";
			echo "<tr style='height:50px;'><td bgcolor='#FFF2CC' align='center'>이메일</td><td><div style='margin-left:10px;'>".$data[email]."</div></td></tr>";
		}
		?>
	</tr>
</table>
</body>
</html>