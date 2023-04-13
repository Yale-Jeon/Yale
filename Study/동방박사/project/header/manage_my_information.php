<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$query="select SNum,Name,phone,email from project.student,project.login where project.login.std_num=project.student.SNum";
$result = mysqli_query($conn, $query);
while ($data=mysqli_fetch_array($result)) {
	$std_num=$data[SNum];
	$std_name=$data[Name];
	$phone=$data[phone];
	$email=$data[email];
}
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>정보 수정</title>
</head>
<body bgcolor="#FFFBF0">
	<form method="post" action="manage_my_information_result.php">
	<div style="margin-top: 50px; margin-left: 50px; font-size: 25px;"><b>프로필 수정</b></div><br>
	<table align="center" style="width: 60%;">
		<tr style='height:50px;'>
			<td align="center" style="width: 15%; background-color: #FFF2CC;">학 번</td>
			<td style="width: 5%;"></td>
			<td>  <?php echo "$std_num"; ?></td>
		</tr>
		<tr style='height:50px;'>
			<td align="center" style="background-color: #FFF2CC;">이 름</td>
			<td style="width: 5%;"></td>
			<td>  <?php echo "$std_name"; ?></td>
		</tr>
		<tr style='height:50px;'>
			<td align="center" style="background-color: #FFF2CC;">전화번호</td>
			<td style="width: 5%;"></td>
			<td>  <input type="tel" maxlength="11" style="height: 25px; background-color: #FFFBF0;" name="pnum" value="<?php echo "$phone"; ?>"></td>
		</tr>
		<tr style='height:50px;'>
			<td align="center" style="background-color: #FFF2CC;">이메일</td>
			<td style="width: 5%;"></td>
			<td>  <input type="email" style="height: 25px; background-color: #FFFBF0;" name="mail" value="<?php echo "$email"; ?>"></td>
		</tr>
		<tr>
			<td align="center" colspan="3">
				<p>*정보수정시 빈칸을 모두 채워주셔야 정상적으로 반영됩니다</p>
				<input type="submit" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="수정하기">
				<input type="reset" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="초기화">
			</td>
		</tr>
	</table>
	</form>
</body>
</html>