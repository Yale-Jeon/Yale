<?php
$numb=$_GET['num'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
$result_club = mysqli_query($conn, $find_club);
while ($data=mysqli_fetch_array($result_club)) {
	$clubid=$data[ClubID];
}
?>

<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 50px; font-size: 25px;"><b>동아리원 신청 내역 조회/관리</b></div><br>
<div style="margin-left: 50px;">해당 이벤트를 신청한 동아리원 조회 및 이벤트 참석을 승인할 수 있습니다</div><br>

<div style="margin-left: 50px; width: 30%; float: left;">
<table style="width: 99%;">
	<tr bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;">
		<td colspan="4"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">신청 동아리원</div></td>
	</tr>
	<tr>
		<td>선 택</td>
		<td>이 름</td>
		<td>전화번호</td>
		<td>email</td>
	</tr>
	<form method="post" action="event_read_change.php">
	<?php
	$find_new="select idclub_activity_registration, student_SNum from project.club_activity_registration where project.club_activity_registration.club_activity_info_num=$numb and project.club_activity_registration.fixed=0";
	$result_new = mysqli_query($conn, $find_new);
	while ($data=mysqli_fetch_array($result_new)) {
		$number=$data[idclub_activity_registration];
		$std_new=$data[student_SNum];
		$show_std="select Name, phone, email from project.student where project.student.SNum=$std_new";
		$result_std = mysqli_query($conn, $show_std);
		while ($db=mysqli_fetch_array($result_std)) {
			echo "<tr><td><input type='checkbox' name='choice1[]' value='$number'></td>";
			echo "<td>$db[Name]</td>";
			echo "<td>$db[phone]</td>";
			echo "<td>$db[email]</td></tr>";
		}
	}
	?>
	<tr align="center">
		<td colspan="4">
			<input style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" type="submit" name="submit_check" value="accept">
			<input style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" type="submit" name="submit_check" value="reject">
		</td>
	</tr>
</form>
</table>
</div>

<div style="width: 30%; float: left;">
<table style="width: 99%;">
	<tr bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;">
		<td colspan="4"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">승인 동아리원</div></td>
	</tr>
	<tr>
		<td>선 택</td>
		<td>이 름</td>
		<td>전화번호</td>
		<td>email</td>
	</tr>
	<form method="post" action="event_read_change_cancel.php">
	<?php
	$find="select idclub_activity_registration, student_SNum from project.club_activity_registration where project.club_activity_registration.club_activity_info_num=$numb and project.club_activity_registration.fixed=1";
	$result = mysqli_query($conn, $find);
	while ($data2=mysqli_fetch_array($result)) {
		$can_num=$data2[idclub_activity_registration];
		$std=$data2[student_SNum];
		$show_stud="select Name, phone, email from project.student where project.student.SNum=$std";
		$result_stud = mysqli_query($conn, $show_stud);
		while ($db=mysqli_fetch_array($result_stud)) {
			echo "<tr><td><input type='checkbox' name='choice2[]' value='$can_num'></td>";
			echo "<td>$db[Name]</td>";
			echo "<td>$db[phone]</td>";
			echo "<td>$db[email]</td></tr>";
		}
	}
	?>
	<tr align="center">
		<td colspan="4">
			<input style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" type="submit" value="cancel">
		</td>
	</tr>
</form>
</table>
</div>

<div style="width: 30%; float: left;">
<table style="width: 99%;">
	<tr bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;">
		<td colspan="4"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">거부 동아리원</div></td>
	</tr>
	<tr>
		<td>선 택</td>
		<td>이 름</td>
		<td>전화번호</td>
		<td>email</td>
	</tr>
	<form method="post" action="event_read_reject_cancel.php">
	<?php
	$find_new="select idclub_activity_registration, student_SNum from project.club_activity_registration where project.club_activity_registration.club_activity_info_num=$numb and project.club_activity_registration.fixed=-1";
	$result_new = mysqli_query($conn, $find_new);
	while ($data3=mysqli_fetch_array($result_new)) {
		$rej_num=$data3[idclub_activity_registration];
		$std_rej=$data3[student_SNum];
		$show_rej="select Name, phone, email from project.student where project.student.SNum=$std_rej";
		$result_rej = mysqli_query($conn, $show_rej);
		while ($db=mysqli_fetch_array($result_rej)) {
			echo "<tr><td><input type='checkbox' name='choice3[]' value='$rej_num'></td>";
			echo "<td>$db[Name]</td>";
			echo "<td>$db[phone]</td>";
			echo "<td>$db[email]</td></tr>";
		}
	}
	?>
	<tr align="center">
		<td colspan="4">
			<input style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" type="submit" value="reset">
		</td>
	</tr>
</form>
</table>
</div>
</body>
</html>