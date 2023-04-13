<html>
<meta charset="utf-8">
<head>
    <?php
        $clubname = $_GET['clubname'];
    ?>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <h4><a href="index.php">돌아가기</a></h4>
    <form method="post" action="write_ok.php">
    <input type="hidden" name="club_name" value="<?php echo $clubname; ?>">
    <table align="center" style="width: 90%;" cellpadding="7" cellspacing="1" border="1">
        <tr><td align="center" colspan="4"><h2>리뷰 작성</h2></td></tr>
        <tr><td align="center" colspan="4">**리뷰는 작성자가 직접 입력한 이름으로 게시되나, 관리자는 작성자 정보를 보유합니다</td></tr>
        <tr>
            <td align="center" style="width: 10%;">제 목</td>
            <td><input type="text" name="title" size="30" maxlength="45" required /></td>
            <td align="center" style="width: 10%;">이 름</td>
            <td><input type="text" name="name" size="30"></td>
        </tr>
        <tr>
            <td align="center" rowspan="13">리뷰하기</td>
            <td colspan="3">1. 필수로 해야 하는 동아리 로드는 얼마나 되나요?</td>
        </tr>
        <tr>
            <td colspan="3">
                <input type="radio" name="time_must" value="1">거의 없음
                <input type="radio" name="time_must" value="2">조금
                <input type="radio" name="time_must" value="3">있는 것 같다
                <input type="radio" name="time_must" value="4">많은 편
                <input type="radio" name="time_must" value="5">매우 바쁨
            </td>
        </tr>
        <tr>
            <td colspan="3">2. 동아리 분위기는요~</td>
        </tr>
        <tr>
            <td colspan="3">
                <input type="radio" name="mood" value="1">침착하고 조용해요
                <input type="radio" name="mood" value="2">조곤조곤 얘기해요
                <input type="radio" name="mood" value="3">도란도란 노는 거 좋아해요!
                <input type="radio" name="mood" value="4">재밌어요!
                <input type="radio" name="mood" value="5">Ho! 엔트로피 톡톡톡!
            </td>
        </tr>
        <tr>
            <td colspan="3">3. 동아리 활동에 시간이 어느 정도 소요되나요?</td>
        </tr>
        <tr>
            <td colspan="3">
                <input type="radio" name="time_spend" value="1">주 2시간 이내
                <input type="radio" name="time_spend" value="2">3-5일에 1-3시간
                <input type="radio" name="time_spend" value="3">1-3일에 1-3시간
                <input type="radio" name="time_spend" value="4">매일 1.5~4시간
                <input type="radio" name="time_spend" value="5">연애하는 줄...
            </td>
        </tr>
        <tr>
            <td colspan="3">4. 동아리원들이 얼마나 동아리 활동에 참여적인가요?
            </td>
        </tr>
        <tr>
            <td colspan="3">
                <input type="radio" name="willing" value="1">유령회원 많죠...
                <input type="radio" name="willing" value="2">적당히..참여는 해요~
                <input type="radio" name="willing" value="3">새로운 일...해볼까요?
                <input type="radio" name="willing" value="4">하고 싶은 일 같이 해요~
                <input type="radio" name="willing" value="5">모두가 일을 못 만들어서 난리!
            </td>
        </tr>
        <tr>
            <td colspan="3">5. 동아리 분위기는 어떠한가요?(인간관계)</td>
        </tr>
        <tr>
            <td colspan="3">
                <input type="radio" name="friendliness" value="1">시선을 피한다
                <input type="radio" name="friendliness" value="2">인사 정도는 한다
                <input type="radio" name="friendliness" value="3">친하다
                <input type="radio" name="friendliness" value="4">많이 친하다
                <input type="radio" name="friendliness" value="5">모두 다 너무 친하다(동아리 내에서만 인간관계가 쌓인다)
            </td>
        </tr>
        <tr>
            <td colspan="3">6. 마지막으로 남기고 싶은 말이 있다면?</td>
        </tr>
        <tr>
            <td colspan="3"><textarea name="text_review" rows="20" style="width: 99%;"></textarea></td>
        </tr>
        <tr><td>비밀번호 <input type="password" name="pw" placeholder="비밀번호" required /></td></tr>
        <tr><td align="center" colspan="4"><input type="submit" value="제출"> <input type="reset" value="초기화"> <input type="button" value="닫기" onclick="window.close()"> </td></tr>
    </table>
    </form>
</body>
</html>