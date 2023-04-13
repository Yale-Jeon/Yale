<?php
$value1=$_POST['choice'];
$value2=$_POST['month'];
$value3=$_POST['day'];
$value4=$_POST['time'];
$value5=$_POST['place'];
$title=$_POST['title'];
$event=$_POST['new_event'];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$sql_mon = "UPDATE project.club_activity SET month=$value2 WHERE info_num=$value1";
if ($conn->query($sql_mon) === FALSE) {
    echo "Error updating month: " . $conn->error;
}

$sql_day = "UPDATE project.club_activity SET day=$value3 WHERE info_num=$value1";
if ($conn->query($sql_day) === FALSE) {
    echo "Error updating day: " . $conn->error;
}

$sql_time = "update project.club_activity set project.club_activity.time='$value4' WHERE info_num=$value1";
if ($conn->query($sql_time) === FALSE) {
    echo "Error updating time: " . $conn->error;
}

$sql_place = "UPDATE project.club_activity SET place='$value5' WHERE info_num=$value1";
if ($conn->query($sql_place) === FALSE) {
    echo "Error updating place: " . $conn->error;
}

$sql_title = "UPDATE project.club_activity SET title='$title' WHERE info_num=$value1";
if ($conn->query($sql_title) === FALSE) {
    echo "Error updating title: " . $conn->error;
}

$sql_event = "UPDATE project.club_activity SET information='$event' WHERE info_num=$value1";
if ($conn->query($sql_event) === TRUE) {
    echo "<script language='Javascript'>alert('선택한 활동 수정이 성공적으로 완료되었습니다!')</script>";
} else {
    echo "Error updating event: " . $conn->error;
}
?>

<html>
<body bgcolor="#FFFBFO">
</body>
</html>