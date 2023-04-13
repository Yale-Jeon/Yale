<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body bgcolor="#FFF4E0" style="width:330px; height: 250px">
	<form method="post" action="check.php">
	<table align="center" bgcolor="FFF4E0" style="width: 330px; height: 250px" border ="0">
		<tr height = 20>
		</tr>

		<tr height ="40">
			<td align="center"><input style="width: 250px; height: 30px" type="text" name="id" placeholder="ID" required /></td>
		</tr>
		<tr height = 20>
		</tr>
		<tr height = "40">
			<td align="center"><input style="width: 250px; height: 30px" type="PASSWORD" name="pw" placeholder="Password" required /></td>
		</tr>
		<tr>
			<td colspan="2" align="center">
				<button style="width: 120px; height: 50px; background-color:#BF9000; color: white; border: 0;" type="submit">로그인</button> 
				<button style="width: 120px; height: 50px; background-color: #BF9000; color: white; border: 0;" onclick="window.open('start_regi.php','팝업창','width=800, height=600'); return false;" >회원가입</button></td>
		</tr>
	</table>
</form>
</body>
</html>