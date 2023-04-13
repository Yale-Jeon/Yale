<html>
<meta charset="utf-8">
<head>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <h4><a href="index.php">돌아가기</a></h4>
    <p align="center"><font size="20">동아리 선택</font></p>
    <form action="write2.php" method="get">
    <table border="1"><tr>
    <?php
        include "db.php";

        $sql = mq("select * from club");
        $tmp = 0;  

        while($data = $sql->fetch_array()){
            $club = $data["clubname"];
            if ($tmp > 5) {
                $tmp = 0;
                echo "</tr><tr>";
            }
            else {
                $tmp += 1;
            }
            ?>
            <td width="50"><a href="write2.php?clubname=<?php echo $club; ?>"> <?php echo "$club"; ?> </a></td>
    <?php } ?>
    </tr></table>
    </form>
</body>
