<?php 
  include "../db.php";
?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>Review</title>
<link rel="stylesheet" type="text/css" href="review/css/style.css">
</head>
<body bgcolor="#FFFBF0">
<div style="width: 700px; position: relative;"> 
  <h1>공지 사항</h1>
  <h4>동방박사 사이트의 공지사항 게시판 입니다.</h4>
    <table class="list-table">
    <thead>
      <tr>
        <th width="70">번호</th>
        <th width="200">제목</th>
        <th width="200">내용</th>
        <th width="120">날짜</th>
      </tr>
    </thead>
      <?php
          if(isset($_GET['page'])){
            $page = $_GET['page'];
              }else{
                $page = 1;
              }
                ##
                if(isset($_GET['search_type'])){
                  $search_type = $_GET['search_type'];
                  $search = $_GET['search'];
                  $sql = mq("select * from notice where $search_type like '%$search%'");
                }else{
                  $sql = mq("select * from notice");
                }

                $row_num = mysqli_num_rows($sql);
                $list = 5;
                $block_ct = 5;

                $block_num = ceil($page/$block_ct);
                $block_start = (($block_num - 1) * $block_ct) + 1;
                $block_end = $block_start + $block_ct - 1;

                $total_page = ceil($row_num / $list);
                if($block_end > $total_page) $block_end = $total_page;
                $total_block = ceil($total_page/$block_ct);
                $start_num = ($page-1) * $list;

                ##
                if(isset($_GET['search_type'])){
                  $search_type = $_GET['search_type'];
                  $search = $_GET['search'];
                  $sql2 = mq("select * from notice where $search_type like '%$search%' order by noticenum desc limit $start_num, $list");
                }else{
                  $sql2 = mq("select * from notice order by noticenum desc limit $start_num, $list");
                }

                while($data = $sql2->fetch_array()){
                	$title=$data["title"]; 
		            if(strlen($title)>10)
		            { 
		              $title=str_replace($data["title"],mb_substr($data["title"],0,10,"utf-8")."...",$data["title"]);
		            }
		            $notice=$data["notice"]; 
		            if(strlen($title)>10)
		            { 
		              $notice=str_replace($data["notice"],mb_substr($data["notice"],0,10,"utf-8")."...",$data["notice"]);
		            }
                ?>
    <tbody>
      <tr>
        <td width="70"><?php echo $data['noticenum']; ?></td>
        <td width="200"><b><a href="read.php?noticenum=<?php echo $data["noticenum"];?>"><?php echo "$title"; ?></a></b></td>
        <td width="200"><?php echo "$notice";?></td>
        <td width="120"><?php echo $data['date'];?></td>
      </tr>
    </tbody>
    <?php } ?>
  </table>
  <div id="page_num">
    <ul>
      <?php
        if($page <= 1)
        {
        	##
        }else{
          echo "<li class='fo_re'>처음</li>";
          if(isset($_GET['search_type'])){
            echo "<li><a href='?page=1&search_type=$search_type&search=$search'>처음</a></li>";
          }else{
            echo "<li><a href='?page=1'>처음</a></li>";
          }
        }
        if($page <= 1)
        {
          ##
        }else{
          $pre = $page-1;
          if(isset($_GET['search_type'])){
            echo "<li><a href='?page=$pre&search_type=$search_type&search=$search'>이전</a></li>";
          }else{
            echo "<li><a href='?page=$pre'>이전</a></li>";
          }
        }
        for($i=$block_start; $i<=$block_end; $i++){ 
          if($page == $i){
            echo "<li class='fo_re'>[$i]</li>";
          }else{
            if(isset($_GET['search_type'])){
              echo "<li><a href='?page=$i&search_type=$search_type&search=$search'>[$i]</a></li>";
            }else{
              echo "<li><a href='?page=$i'>[$i]</a></li>";
            }
          }
        }
        if($page >= $total_page)
        {

        }else{
          $next = $page + 1;
          if(isset($_GET['search_type'])){
            echo "<li><a href='?page=$next&search_type=$search_type&search=$search'>다음</a></li>";
          }else{
            echo "<li><a href='?page=$next'>다음</a></li>";
          }
        }
        if($page >= $total_page){
          echo "<li class='fo_re'>마지막</li>";
        }else{
          if(isset($_GET['search_type'])){
            echo "<li><a href='?page=$total_page&search_type=$search_type&search=$search'>마지막</a></li>";
          }else{
            echo "<li><a href='?page=$total_page'>마지막</a></li>";
          }
        }
      ?>
    </ul>
  </div>
  </div>

  <form method="get" action="notice.php">
    <p align="center">
      <select name="search_type">
        <option value="title">제목</option>
        <option value="notice">내용</option>
      </select>
      <input type="search" name="search" size="25">  <input type="submit" value="검색">
    </p>
  </form>
</body>
</html>