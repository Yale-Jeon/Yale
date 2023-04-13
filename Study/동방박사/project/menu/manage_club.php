<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 50px; font-size: 25px;"><b>동아리원 조회</b></div><br>
<div style="margin-left: 50px;">동방박사 동아리원 정보 조회/수정창입니다</div>
<div style="margin-left: 900px;">
	동아리원 수정/삭제는 여기서 해주세요
	<button style="width: 150px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" onclick="window.open('club_change.php','window_name','width=600,height=800,location=no,status=no,scrollbars=yes');">정보 수정/삭제</button>
</div>

<table align="center" style="width: 90%;">
	<tr>
		<td colspan="4" bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">멤버</div>
		</td>
	</tr>
	<tr align="center" bgcolor="#E4C198" style="height: 25px; font-size: 17px;">
		<b><td style="width: 10%; margin-top: 5px; margin-bottom: 5px;">학 번</td>
		<td style="margin-top: 5px; margin-bottom: 5px;">이 름</td>
		<td style="width: 15%; margin-top: 5px; margin-bottom: 5px;">전화번호</td>
		<td style="margin-top: 5px; margin-bottom: 5px;">이메일</td></b>
	</tr>
	<?php
	require('../data_mysql.php');
	$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
	$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
	$result_club = mysqli_query($conn, $find_club);
	while ($data=mysqli_fetch_array($result_club)) {
		$clubid=$data[ClubID];
	}
	$student_query="select SNum,Name,phone,email from project.student where SNum IN(select student_SNum from project.student_has_club where club_ClubID=$clubid)";
	$result_std = mysqli_query($conn, $student_query);
	while ($db=mysqli_fetch_array($result_std)) {
		echo "<tr align='center'><td>$db[SNum]</td><td>$db[Name]</td><td>$db[phone]</td><td>$db[email]</td></tr>";
	}
	?>
</table>
</html>