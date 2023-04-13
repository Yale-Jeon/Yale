<?php
$value1 = $_POST["presi_name"];
$value2 = $_POST["phone"];
$value3 = $_POST["email"];
?>

<html>
<body bgcolor="#FFFBF0"><br>
<meta charset="utf-8">
<div style="margin-top: 20px; margin-left: 50px; font-size: 25px;"><b>새로이 등록하고자 하는 동아리 정보를 알려주세요</b></div><br>
<div style="margin-left: 55px;">*수정 사항은 관리자의 검토 후 홈페이지에 반영됩니다^^</div><br>
<form method="post" action="register_club.php">
	<input type="hidden" name="presi" value="<?php echo $value1;?>">
	<input type="hidden" name="phone" value="<?php echo $value2;?>">
	<input type="hidden" name="email" value="<?php echo $value3;?>">
	<table align="center" style="width: 70%;">
		<tr>
			<td align="center" style="width: 30%; height: 35px; background-color: #FFF2CC;">동아리 이름</td>
			<td><input type="text" name="club_name" size="40" style="margin-left: 10px; background-color: #FFFBF0; height: 25px;" required /></td>
		</tr>
		<tr>
			<td align="center" style="height: 35px; background-color: #FFF2CC;">분 과</td>
			<td>
				<input type="radio" value="생활문화" name="part_name">생활문화
				<input type="radio" value="사회" name="part_name">사회
				<input type="radio" value="연행예술" name="part_name">연행예술
				<input type="radio" value="종교" name="part_name">종교<br>
				<input type="radio" value="전시창작" name="part_name">전시창작
				<input type="radio" value="구기체육" name="part_name">구기체육
				<input type="radio" value="밴드음악" name="part_name">밴드음악
				<input type="radio" value="생활체육" name="part_name">생활체육<br>
				<input type="radio" value="이공학술" name="part_name">이공학술
				<input type="radio" value="연주음악" name="part_name">연주음악
				<input type="radio" value="인문학술" name="part_name">인문학술
			</td>
		</tr>
		<tr>
			<td align="center" style="height: 35px; background-color: #FFF2CC;">동아리 구분</td>
			<td>
				<input type="radio" value="정동아리" name="devi_num">정동아리
				<input type="radio" value="상임동아리" name="devi_num">상임동아리
				<input type="radio" value="가동아리" name="devi_num">가동아리
			</td>
		</tr>
		<tr>
			<td align="center" style="height: 35px; background-color: #FFF2CC;">동아리 소개</td>
			<td><textarea name="club_intro" rows="10" cols="55" style="background-color: #FFFBF0;"></textarea></td>
		</tr>
		<tr>
			<td align="center" style="height: 35px; background-color: #FFF2CC;">회 장</td>
			<td><font style="margin-left: 10px; background-color: #FFFBF0; height: 25px;"><?php echo "$value1";?></td>
		</tr>
		<tr>
			<td align="right" colspan="2">
				<input type="submit" value="제출" style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;">
				<input type="reset" value="초기화"style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;">
				<input type="button" value="닫기" style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;" onclick="window.close()"></td>
		</tr>
	</table>
</form>
</body>
</html>