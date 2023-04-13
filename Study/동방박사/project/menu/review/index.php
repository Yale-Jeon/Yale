<?php 
  include "db.php";
?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>Review</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body bgcolor="#FFFBF0">
<div id="board_area"> 
  <h1>리뷰게시판</h1>
  <h4>동아리에 대한 리뷰글을 자유롭게 쓸 수 있는 게시판입니다.</h4>
    <table class="list-table">
    <thead>
      <tr>
        <th width="70">번호</th>
        <th width="450">제목</th>
        <th width="120">동아리</th>
        <th width="120">글쓴이</th>
        <th width="100">작성일</th>
        <th width="100">조회수</th>
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
                  $sql = mq("select * from review where $search_type like '%$search%'");
                }else{
                  $sql = mq("select * from review");
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
                  $sql2 = mq("select * from review where $search_type like '%$search%' order by idx desc limit $start_num, $list");
                }else{
                  $sql2 = mq("select * from review order by idx desc limit $start_num, $list");
                }

                while($data = $sql2->fetch_array()){
                $title=$data["title"]; 
                  if(strlen($title)>15)
                  { 
                    $title=str_replace($data["title"],mb_substr($data["title"],0,15,"utf-8")."...",$data["title"]);
                  }
                ?>
    <tbody>
      <tr>
        <td width="70"><?php echo $data['idx']; ?></td>
        <td width="500"><a href="read.php?idx=<?php echo $data["idx"];?>"><?php echo "$title"; ?></a></td>
        <td width="120"><?php echo $data['club_name'];?></td>
        <td width="120"><?php echo $data['name'];?></td>
        <td width="100"><?php echo $data['date'];?></td>
        <td width="100"><?php echo $data['hit']; ?></td>
      </tr>
    </tbody>
    <?php } ?>
  </table>
</div>
  <div id="page_num">
    <ul>
      <?php
        if($page <= 1)
        {
          echo "<li class='fo_re'>처음</li>";
        }else{
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
            ##
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
  <div id="write_btn">
    <a href="write.php"><button style="font-size: 15px;">리뷰쓰기</button></a><font color="white">..........</font>
  </div>

  <form method="get" action="index.php">
    <p align="center">
      <select name="search_type" style="font-size: 15px;">
        <option value="title">제목</option>
        <option value="name">작성자</option>
        <option value="club_name">동아리명</option>
        <option value="review">내용</option>
        <option value="date">날짜</option>
      </select>
      <input type="search" name="search" style="font-size: 15px;">  <input type="submit" value="검색" style="font-size: 15px;">
    </p>
  </form>
</body>
</html>