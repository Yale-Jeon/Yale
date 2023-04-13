<?php
$value1 = $_POST["club_name"];
$value2 = $_POST["part_name"];
$value3 = $_POST["devi_num"];
$value4 = $_POST["club_intro"];
$presi = $_POST["presi"];
$phone = $_POST["phone"];
$email = $_POST["email"];

require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$insert_club = "insert into project.president_new (name, phone, email) values
('$presi', '$phone', '$email')";
$result_query = mysqli_query($conn, $insert_club);
if (!$result_query) {
    die("Insert query failed: ".mysqli_error($conn));
}

$find_presi = "select * from president_new where name='".$presi."'";
$result_query = mysqli_query($conn, $find_presi);
while ($db=mysqli_fetch_array($result_query)) {
	$presi_id = $db[president_id];
}

$insert_club2 = "insert into project.club_new (clubname, part, devision, club_intro, president_president_id) values
('$value1', '$value2', '$value3', '$value4', '$presi_id')";
$result_query = mysqli_query($conn, $insert_club2);
if (!$result_query) {
    die("Insert query failed: ".mysqli_error($conn));
}

?>

<script language="Javascript">
	alert("동아리 신청이 완료되었습니다!");
	window.close();
</script>
