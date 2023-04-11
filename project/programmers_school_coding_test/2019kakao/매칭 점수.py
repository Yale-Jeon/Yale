def solution(word, pages):
    word = word.lower()
    answer = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    basic_score = []
    url = {}
    link = []

    page_num = 0
    for page in pages:
        a = page.lower().split(word)
        score = 0
        if a[0] == '':
            a[0] = '@@'
        if a[-1] == '':
            a[-1] = '@@'
        for i in range(len(a) - 1):
            if a[i+1] == '' and i != (len(a)-2):
                a[i+1] = 'aa'
            if (a[i][-1] not in alphabet) and (a[i + 1][0] not in alphabet):
                score += 1

        basic_score.append(score)

        b = page.split('<meta property="og:url" content="')
        content = ''
        for w in b[1]:
            if w == '"':
                break
            content += w
        url[content] = page_num
        page_num += 1

    for page in pages:
        c = page.split('<a href="')
        x = []
        for i in range(len(c) - 1):
            content = ''
            for w in c[i + 1]:
                if w == '"':
                    break
                content += w
            if content in url.keys():
                x.append(url[content])
        link.append(x)

    matching_score = basic_score[:]

    for i in range(len(link)):
        for j in link[i]:
            matching_score[j] += basic_score[i]/len(link[i])

    max = -99
    for i in range(len(matching_score)):
        if matching_score[i] > max:
            answer = i
            max = matching_score[i]

    print(basic_score)
    print(matching_score)

    return answer
print(solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
