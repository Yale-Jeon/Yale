<html>
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 30px; font-size: 25px;"><b>동아리원 수정/삭제</b></div><br>
<form method="post" action="delete_club_student.php">
<table align="center" style="width: 90%;">
	<tr>
		<td colspan="5" bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">멤버</div>
		</td>
	</tr>
	<tr align="center" bgcolor="#E4C198" style="height: 25px; font-size: 17px;">
		<b><td style="width: 10%;">선택</td>
		<td style="width: 10%; margin-top: 5px; margin-bottom: 5px;">학 번</td>
		<td style="margin-top: 5px; margin-bottom: 5px;">이 름</td>
		<td style="width: 25%; margin-top: 5px; margin-bottom: 5px;">phone</td>
		<td style="width: 40%; margin-top: 5px; margin-bottom: 5px;">이메일</td></b>
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
		echo "<tr align='center'><td><input type='checkbox' name='choice[]' value='$db[SNum]'></td><td>$db[SNum]</td><td>$db[Name]</td><td>$db[phone]</td><td>$db[email]</td></tr>";
	}
	?>
	<tr align="right">
		<td colspan="5"><input type="submit" style="width: 70px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="삭제"></td>
	</tr>
</table>
</form>
</body>
</html>