<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$query="select clubname,club_intro from project.club, project.login where project.login.std_num = project.club.president_president_id";
$result = mysqli_query($conn, $query);
while ($data=mysqli_fetch_array($result)) {
	$clubname=$data[clubname];
	$club_intro=$data[club_intro];
}
$query_presi="select name, phone, email from project.president, project.login where project.login.std_num = project.president.president_id";
$result_presi = mysqli_query($conn, $query_presi);
while ($db=mysqli_fetch_array($result_presi)) {
	$presi_name=$db[name];
	$phone=$db[phone];
	$email=$db[email]; 
}
?>

<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
	<div style="margin-top: 40px; margin-left: 50px; font-size: 25px;"><b>동아리 및 대표 계정 정보 수정</b></div><br>
	<div style="margin-left: 55px; margin-bottom: 20px;">*정보수정시 빈칸을 모두 채워주셔야 정상적으로 반영됩니다</div>
<body>
	<form method="post" action="manage_club_information_result.php">
	<table align="center" style="width: 80%;">
		<tr>
			<td colspan="2" bgcolor="#BF9000" style="height: 30px; color: white;"><div style="margin-left: 10px; font-size: 20px;">동아리 정보</div></td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>동아리이름</td>
			<td><input type="text" name="cname" style="margin-left: 10px; background-color: #FFFBF0;" value="<?php echo $clubname; ?>"></td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>분 과</td>
			<td>
				<input type="radio" value="생활문화" name="part_name">생활문화
				<input type="radio" value="사회" name="part_name">사회
				<input type="radio" value="연행예술" name="part_name">연행예술
				<input type="radio" value="종교" name="part_name">종교
				<input type="radio" value="전시창작" name="part_name">전시창작
				<input type="radio" value="구기체육" name="part_name">구기체육
				<input type="radio" value="밴드음악" name="part_name">밴드음악
				<input type="radio" value="생활체육" name="part_name">생활체육
				<input type="radio" value="이공학술" name="part_name">이공학술
				<input type="radio" value="연주음악" name="part_name">연주음악
				<input type="radio" value="인문학술" name="part_name">인문학술
			</td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>분 류</td>
			<td>
				<input type="radio" value="정동아리" name="devi_name">정동아리
				<input type="radio" value="상임동아리" name="devi_name">상임동아리
				<input type="radio" value="가동아리" name="devi_name">가동아리
			</td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>동아리소개</td>
			<td>
				<div style="margin-left: 10px; margin-bottom: 10px;"><textarea name="club_introduction" rows="5" cols="100" style="background-color: #FFFBF0; border-color:#BF9000;"><?php echo $club_intro; ?></textarea></div><br>
			</td>
		</tr>
		<tr>
			<td colspan="2" bgcolor="#BF9000" style="height: 30px; color: white;"><div style="margin-left: 10px; font-size: 20px;">대표 정보</div></td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>대표아이디</td>
			<td><?php echo "$presi_name"; ?> | *대표아이디는 수정이 불가합니다.</td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>전화번호</td>
			<td><input type="tel" name="pnum" style="background-color:#FFFBF0;" value="<?php echo $phone; ?>"></td>
		</tr>
		<tr>
			<td align='center' style='width:12%; height:30px; background-color:#FFF2CC;'>이메일</td>
			<td><input type="email" name="mail" style="background-color:#FFFBF0;" value="<?php echo $email; ?>"></td>
		</tr>
		<tr>
			<td align="center" colspan="2">
				<input type="submit" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="수정하기">
				<input type="reset" style="width: 90px; height: 30px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="초기화">
			</td>
		</tr>
	</table>
	</form>
</body>
</html>