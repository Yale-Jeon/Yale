<?php
require('../data_mysql.php');
$conn = mysqli_connect("localhost", ROOT_ID,PASSWORD,SCHEMA);
$value1=$_POST["std_num"];
$value2=$_POST["password"];
$value3=$_POST["std_name"];
$value4=$_POST["phone"];
$Value5=$_POST["email"];
if (!$conn) {
    die("Connection failed: ".mysqli_connect_error());
}

$insert_query = "insert into project.student (SNum, password, Name, phone, email) values
($value1, '$value2', '$value3', '$value4', '$value5')";
$result_query = mysqli_query($conn, $insert_query);

if (!$result_query) {
    die("Insert query failed: ".mysqli_error($conn));
}
?>

<script language="Javascript">
	alert("회원가입이 완료되었습니다!");
	window.close();
</script>