<?php
$clubid=(int)$_GET['club_id'];
$clubname=$_GET['clubname'];
?>

<html>
<body bgcolor="#FFFBF0"><br>
<form method="post" action="register_student_finish.php">
	<table align="center" style="width: 90%; ">
		<input type="hidden" name="club_id" value="<?php echo $clubid; ?>">
		<tr>
			<td><h2>지원 내용</h2></td>
		</tr>
		<tr>
			<td>
				<p align="center"><textarea style="background-color: #FFFBF0; border-color: #BF9000; border-spacing: 5px; margin-top: 10px;" name="registration" rows="30" cols="100"></textarea></p>
			</td>
		</tr>
		<tr>
			<td align="center">
				<input type="submit" value="지원하기" style="font-size: 15px; width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;"> 
				<input type='reset' value="초기화" style="font-size: 15px; width: 70px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;">
			</td>
		</tr>
	</table>
</form>
</body>