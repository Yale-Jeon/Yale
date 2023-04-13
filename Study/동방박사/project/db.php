<?php
	session_start();
	header('Content-Type: text/html; charset=utf-8'); // utf-8인코딩

	$db = new mysqli("localhost","root","sonic98","project");
	$db->set_charset("utf8");

	function mq($sql)
	{
		global $db;
		return $db->query($sql);
	}
	
	function sql($sql)
	{
		$connect = mysqli_connect("localhost","root","sonic98","test");
		$result = mysqli_query($connect,$sql);

		if (!$result){
		die("Warning : Connection to DB is failed.".mysqli_error($connect));
		#include('write.html');
		}
		return $result;
	}
?>

