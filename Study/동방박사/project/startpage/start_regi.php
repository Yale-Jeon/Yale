<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>회원가입</title>
</head>
<body bgcolor="#FFF2CC">
<form method="post" action="start_regi_result.php">
	<table style="width: 50%;" align="center" border-right=none border-left=none border-top=none border-bottom=none>
		<tr>
			<td colspan="2" align="center"><<<회원가입 창입니다>>></td>
		</tr>
		<tr>
			<td rowspan="2" align="center">학번</td>
			<td><input type="text" name="std_num" size="30" required /> </td>
		</tr>
		<tr>
			<td>*학번은 이후 아이디로 사용됩니다</td>
		</tr>
		<tr>
			<td align="center">비밀번호</td>
			<td><input type="password" name="password" size="30" required /> </td>
		</tr>
		<tr>
			<td align="center">이름</td>
			<td><input type="text" name="std_name" size="30" required /> </td>
		</tr>
		<tr>
			<td align="center">연락처</td>
			<td><input type="tel" name="phone" size="30" maxlength="13"> </td>
		</tr>
		<tr>
			<td align="center">이메일</td>
			<td><input type="email" name="email" size="30"> </td>
		</tr>
		<tr>
			<td colspan="2" align="center">
				<input type="submit" value="입력하기">
				<input type='reset' value="초기화"> 
				<input type="button" onclick="window.close();" value="홈으로">
			</td>
		</tr>
	</table>
</form>
</body>
</html>