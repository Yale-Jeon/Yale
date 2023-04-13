<?php 
  include "db.php";
?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>동아리</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body bgcolor="#FFFBF0">
<p align="center" style="margin-top: 15px; font-size: 25px;">동아리 목록</p>
<div id="data_area"> 
    <table class="list-table">
    <thead>
      <tr>
        <th width="100">이름</th>
        <th width="100">구분</th>
        <th width="100">분과</th>
        <th width="450">동아리 소개글</th>
        <th width="100">회장</th>
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
                  $sql = mq("select * from club where $search_type like '%$search%'");
                }else{
                  $sql = mq("select * from club");
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
                  $sql2 = mq("select * from club where $search_type like '%$search%' order by ClubID desc limit $start_num, $list");
                }else{
                  $sql2 = mq("select * from club order by ClubID desc limit $start_num, $list");
                }

                while($data = $sql2->fetch_array()){
                $club_intro=$data["club_intro"]; 
                  if(strlen($club_intro)>30)
                  {
                    $club_intro=str_replace($data["club_intro"],mb_substr($data["club_intro"],0,30,"utf-8")."...",$data["club_intro"]);
                  }
                ?>
    <tbody>
      <tr>
        <td width="100"><a href="read.php?idx=<?php echo $data["ClubID"];?>"><?php echo $data['clubname']; ?></a></td>
        <td width="100"><?php echo $data['devision'];?></td>
        <td width="100"><?php echo $data['part'];?></td>
        <td width="450"><?php echo "$club_intro"; ?></td>
        <td width="100"><?php echo $data['president_president_id']; ?></td>
      </tr>
    </tbody>
    <?php } ?>
  </table>
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

  <form method="get" action="index.php">
    <p align="center">
      <select name="search_type">
        <option value="clubname">이름</option>
        <option value="devision">구분</option>
        <option value="part">분과</option>
        <option value="club_intro">동아리소개</option>
        <option value="president_president_id">회장</option>
      </select>
      <input type="search" name="search" size="25">  <input type="submit" value="검색">
    </p>
  </form>
</body>
</html>