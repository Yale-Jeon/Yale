<?php
$club_name=$_POST["cname"];
$part_name=$_POST["part_name"];
$devi_name=$_POST["devi_name"];
$club_intro=$_POST["club_introduction"];
$phone=$_POST["pnum"];
$email=$_POST["mail"];
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}
$presi="select std_num from project.login";
$result_presi = mysqli_query($conn, $presi);
while ($db=mysqli_fetch_array($result_presi)) {
	$presi_name=$db[std_num];
}
$change_name="UPDATE project.club SET clubname='".$club_name."' WHERE president_president_id='".$presi_name."'";
if ($conn->query($change_name) === FALSE) {
    echo "Name Error: " . $conn->error;
}
$change_part="UPDATE project.club SET part='".$part_name."' WHERE president_president_id='".$presi_name."'";
if ($conn->query($change_part) === FALSE) {
    echo "Part Error: " . $conn->error;
}
$change_devi="UPDATE project.club SET devision='".$devi_name."' WHERE president_president_id='".$presi_name."'";
if ($conn->query($change_devi) === FALSE) {
    echo "Devision Error: " . $conn->error;
}
$change_club_intro="UPDATE project.club SET club_intro='".$club_intro."' WHERE president_president_id='".$presi_name."'";
if ($conn->query($change_club_intro) === FALSE) {
    echo "Club Introduction Error: " . $conn->error;
}
$change_phone="UPDATE project.president SET phone='".$phone."' WHERE president_id='".$presi_name."'";
if ($conn->query($change_phone) === FALSE) {
    echo "Phone Error: " . $conn->error;
}
$change_mail="UPDATE project.president SET email='".$email."' WHERE president_id='".$presi_name."'";
if ($conn->query($change_mail) === FALSE) {
    echo "Email Error: " . $conn->error;
}
?>

<html>
<body bgcolor="#FFFBF0">
<script language="Javascript">
	alert("정보수정이 완료되었습니다!");
</script>
<meta http-equiv="refresh" content="0; url=club_information.php">