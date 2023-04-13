<!DOCTYPE html>
<html>
<body bgcolor="#FFFBF0">
<div style="margin-top: 30px; margin-left: 50px; font-size: 25px;"><b>동아리 지원서 작성</b></div><br>
<div style="margin-left: 55px;">동방박사 사이트에 동아리 지원서를 작성할 수 있는 공간입니다</div><br>

<table align="center" style="width: 90%;">
	<tr>
		<td align="center" style="width: 15%; height: 30px; background-color: #FFF2CC;">학번 | 이름</td>
		<td colspan="4">
			<?php
			require('../data_mysql.php');
			$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
			$query="select std_num,Name from project.login,project.student where project.login.std_num=project.student.SNum";
			$result = mysqli_query($conn, $query);
			while ($data=mysqli_fetch_array($result)) {
				echo "<div style='size: 20px; margin-left: 10px;'>$data[std_num] | $data[Name]</div>";
			}
			?>
		</td>
	</tr>
	<tr>
		<td colspan="5" align="center" style="height: 40px; background-color: #FFF2CC; ">지원 동아리</td>
	</tr>
	<tr>
		<td colspan="5" align="center">
			<p align="center"><font style="font-size: 13x;">동아리 선택</font></p>
			    <p align="center"><table border="1" style="width: 80%;"><tr>
			    <?php
			        include "../db.php";

			        $sql = mq("select * from club");
			        $tmp = 0;  

			        while($data = $sql->fetch_array()){ 
			            if ($tmp > 7) {
			                $tmp = 0;
			                echo "</tr><tr>";
			            }
			            else {
			            	$club = $data["clubname"];
			                $tmp += 1;
			            }
			            ?>
			            <td width="50"><a href="register_student2.php?club_id=<?php echo $data[ClubID]; ?>&clubname=<?php echo $data["clubname"]; ?>" style="color:#333; text-decoration: none;"> <?php echo "$club"; ?></a></td>
			    <?php } ?>
			    </tr></table></p>
		</td>
	</tr>
</table>
</body>
</html>