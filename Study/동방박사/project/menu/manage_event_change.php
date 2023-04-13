<html>
<meta charset="utf-8">
<body bgcolor="#FFFBF0">
<div style="margin-top: 50px; margin-left: 50px; font-size: 25px;"><b>동아리 Activity 수정</b></div><br>
<div style="margin-left: 50px;">동방박사 사이트에 게시되어 있는 해당 동아리의 활동 이벤트를 수정하실 수 있습니다</div>
<div style="margin-left: 680px;">
	동아리 activity 관리는 여기서 해주세요
	<a href='event/make_event.html'><button style="width: 140px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;">이벤트 만들기</button></a>
	<a href='manage_event_change.php'><button style="width: 120px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;">이벤트 수정</button></a>
	<a href='manage_event_delete.php'><button style="width: 120px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;">이벤트 삭제</button></a>
</div>
<form method="post" action="change_event.php">
<table align="center" style="width: 90%;">
	<tr>
		<td colspan="8" bgcolor="#FFF2CC" style="height: 35px; font-size: 20px;"><div style="margin-left: 10px; margin-top: 10px; margin-bottom: 10px;">동아리 이벤트 목록</div></td>
	</tr>
	<tr align="center" bgcolor="#FAD0B2">
		<td style="width: 4%;">선택</td>
		<td style="width: 2%;">월</td>
		<td style="width: 2%;">일</td>
		<td style="width: 4%;">시간</td>
		<td style="width: 8%;">장소</td>
		<td style="width: 10%;">항목</td>
		<td style="width: 15%;">제목</td>
		<td style="width: 55%;">내용</td>
	</tr>
	<?php
	require('../data_mysql.php');
	$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
	$find_club="select ClubID from project.club, project.login where project.club.president_president_id=project.login.std_num";
	$result_club = mysqli_query($conn, $find_club);
	while ($data=mysqli_fetch_array($result_club)) {
		$clubid=$data[ClubID];
	}
	$activity_query="select info_num,month,day,time,place,part,information,title from project.club_activity where club_ClubID=$clubid";
	$result_act = mysqli_query($conn, $activity_query);
	while ($db=mysqli_fetch_array($result_act)) {
		echo "<tr align='center'><td><input type='radio' name='choice' value='$db[info_num]'></td>";
		echo "<td>$db[month]</td><td>$db[day]</td><td>$db[time]</td><td>$db[place]</td><td>$db[part]</td><td>$db[title]</td><td>$db[information]</td></tr>";
	}
	?>
	<tr align="right">
		<td colspan="8"><input type="submit" style="width: 70px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="수정"></td>
	</tr>
</table>
</form>
</html>