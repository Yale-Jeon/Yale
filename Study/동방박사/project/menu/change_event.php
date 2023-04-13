<?php
$value1=$_POST['choice'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$find_info="select month, day, time, place, part, information, title from project.club_activity where project.club_activity.info_num=$value1";
$result_info = mysqli_query($conn, $find_info);
while ($db=mysqli_fetch_array($result_info)) {
	$mon=$db[month];
	$day=$db[day];
	$time=$db[time];
	$place=$db[place];
	$part=$db[part];
	$info=$db[information];
	$title=$db[title];
}

?>

<html>
<body bgcolor="#FFFBFO">
<form method="post" action="change_event_result.php">
	<table align="center" style="width: 90%;" cellpadding="7" cellspacing="1">
		<tr>
			<td style="width:15%;" bgcolor="#FAD0B2">Month</td>
			<td>
				<select name="month" style="height: 25px; background-color: #FFFBF0; ">
					<option style="color: white; background-color: #BF9000;" value="<?php echo "$mon";?>" selected="selected"><?php echo "$mon";?></option>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<option value="6">6</option>
					<option value="7">7</option>
					<option value="8">8</option>
					<option value="9">9</option>
					<option value="10">10</option>
					<option value="11">11</option>
					<option value="12">12</option>
				</select>
			월</td>
			<td style="width: 15%;" bgcolor="#FAD0B2">Day</td>
			<td>
				<select name="day" style="height: 25px; background-color: #FFFBF0; ">
					<option style="color: white; background-color: #BF9000;" value="<?php echo "$day";?>" selected="selected"><?php echo "$day";?></option>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<option value="6">6</option>
					<option value="7">7</option>
					<option value="8">8</option>
					<option value="9">9</option>
					<option value="10">10</option>
					<option value="11">11</option>
					<option value="12">12</option>
					<option value="13">13</option>
					<option value="14">14</option>
					<option value="15">15</option>
					<option value="16">16</option>
					<option value="17">17</option>
					<option value="18">18</option>
					<option value="19">19</option>
					<option value="20">20</option>
					<option value="21">21</option>
					<option value="22">22</option>
					<option value="23">23</option>
					<option value="24">24</option>
					<option value="25">25</option>
					<option value="26">26</option>
					<option value="27">27</option>
					<option value="28">28</option>
					<option value="29">29</option>
					<option value="30">30</option>
					<option value="31">31</option>
				</select>
			일</td>
		</tr>
		<tr>
			<td bgcolor="#FAD0B2">시간(24시)</td>
			<td><input type="text" name="time" value="<?php echo "$time"; ?>" maxlength="5"  style="height: 25px; background-color: #FFFBF0; "></td>
			<td bgcolor="#FAD0B2">장소</td>
			<td><input type="text" name="place" value="<?php echo "$place"; ?>" style="height: 25px; background-color: #FFFBF0; "></td>
		</tr>
		<tr>
			<td bgcolor="#FAD0B2">항목</td>
			<td colspan="3">
				<input type="radio" name="choice" value="신환회">신환회
				<input type="radio" name="choice" value="오픈동방">오픈동방
				<input type="radio" name="choice" value="전시">전시
				<input type="radio" name="choice" value="부스운영">부스운영
				<input type="radio" name="choice" value="공연">공연
				<input type="radio" name="choice" value="기타">기타
			</td>
		</tr>
		<tr>
			<td align="center" bgcolor="#FAD0B2">제목</td>
			<td colspan="3"><input type="text" name="title" maxlength="20" value="<?php echo "$title"; ?>" style="width: 600px; height: 25px; background-color: #FFFBF0;"></td>
		</tr>
		<tr>
			<td align="center" colspan="4" bgcolor="#FAD0B2">내용</td>
		</tr>
		<tr>
			<td align="center" colspan="4"><textarea style="background-color: #FFF2CC; border-spacing: 5px; width: 97%; height: 200px" name="new_event"></textarea></td>
		</tr>
		<tr>
			<td colspan="4" align="center">
				<input type="submit" style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="수정하기">
				<input type="text" name="choice" style="width: 1px; background-color: #FFFBF0; color: #FFFBF0; border:0;" value="<?php echo "$value1"; ?>">
				<input type='reset' style="width: 100px; height: 25px; background-color: #FFFBF0; border-color: #BF9000; border-width: 1px;" value="초기화"> 
			</td>
		</tr>
	</table>
	</form>
</body>
</html>