<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>회장 등록</title>
</head>
<body bgcolor="#FFFBF0"><br>
<div style="margin-top: 50px; margin-left: 50px; font-size: 25px;"><b>새로이 등록하고자 하는 동아리의 대표정보를 알려주세요</b></div><br>
<div style="margin-left: 55px;">*작성해주신 자료를 기반으로 동아리 관리 대표 계정을 관리자 측에서 만들어 드립니다</div><br>
<form method="post" action="club_register.php">
	<table align="center" style="width: 80%;">
		<tr>
			<td align="center" style="width: 20%; height: 35px; background-color: #FFF2CC;">이름</td>
			<td><input type="text" name="presi_name" style="margin-left: 10px; background-color: #FFFBF0; height: 25px;" required /></td>
		</tr>
		<tr>
			<td align="center" style="height: 55px; background-color: #FFF2CC;">연락처<br>(phone)</td>
			<td><input style="margin-left: 10px; background-color: #FFFBF0; height: 25px;" type="tel" name="phone" size="30" maxlength="13"></td>
		</tr>
		<tr>
			<td align="center" style="height: 55px; background-color: #FFF2CC;">연락처<br>(email)</td>
			<td><input style="margin-left: 10px; background-color: #FFFBF0; height: 25px;" type="email" name="email" size="50"> </td>
		</tr>
		<tr>
			<td colspan="2" align="right">
				<input type="submit" value="입력완료" style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;"> 
				<input type='reset' value="초기화" style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;"> 
				<input type="button" value="닫기" style="background-color: #FFFBF0; border-width: 1px; font-size: 17px;" onclick="window.close()">
			</td>
		</tr>
	</table>
</body>
</html>