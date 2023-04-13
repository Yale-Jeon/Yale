<html>
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 30px; font-size: 25px;"><b>동아리지원서 삭제</b></div><br>
<div style="margin-left: 50px; margin-bottom: 5px;">동방박사 사이트에서 해당 동아리를 대상으로 작성된 동아리 지원서 삭제창입니다.
체크박스를 통해 지원서를 삭제해 주세요.</div><br>
<form method="post" action="delete_registration.php">
<table align="center" style="width: 90%;">
	<tr>
		<td colspan="5" bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">동아리 지원서 목록</div></td>
	</tr>
	<tr align="center" bgcolor="#FAD0B2" style="height: 25px; font-size: 17px;">
		<td style="width: 5%;">선택</td>
		<td colspan="2" style="width: 30%;">학생 정보</td>
		<td style="width: 5%;">지원일</td>
		<td>지원서 내용</td>
	</tr>
	<tr align="center">
		<td bgcolor="#FFF2CC" rowspan="2"></td>
		<td bgcolor="#FFF2CC">학번</td>
		<td bgcolor="#FFF2CC">이름</td>
		<td rowspan="2">*</td>
		<td rowspan="2">*</td>
	</tr>
	<tr align="center">
		<td bgcolor="#FFF2CC">전화번호</td>
		<td bgcolor="#FFF2CC">이메일</td>
	</tr>
	<?php
	require('../data_mysql.php');
	$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
	$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
	$result_club = mysqli_query($conn, $find_club);
	while ($data=mysqli_fetch_array($result_club)) {
		$clubid=$data[ClubID];
	}
	$register_query="select registrationid, student_SNum,date,content from project.registration where club_ClubID=$clubid";
	$result_rgs = mysqli_query($conn, $register_query);
	while ($db=mysqli_fetch_array($result_rgs)) {
		$regist_id=$db[registrationid];
		$student_number=$db[student_SNum];
		$date=$db[date];
		$register=$db[content];
		$student_query="select Name,phone,email from project.student where SNum=$student_number";
		$result_student=mysqli_query($conn, $student_query);
		while ($database=mysqli_fetch_array($result_student)) {
			echo "<tr align='center'><td rowspan='2'><input type='checkbox' name='choice[]' value='$regist_id'></td><td>$student_number</td><td>$database[Name]</td>";
			echo "<td rowspan='2'>$date</td><td rowspan='2'>$register</td></tr>";
			echo "<tr align='center'><td>$database[phone]</td><td>$database[email]</td></tr>";
		}
	}
	?>
	<tr align="right">
		<td colspan="5"><input type="submit" style="width: 70px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="삭제"></td>
	</tr>
</table>
</form>
</body>
</html>