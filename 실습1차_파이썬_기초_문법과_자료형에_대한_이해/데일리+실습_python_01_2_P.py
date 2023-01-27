script_num = int(input('게시글의 총 갯수를 입력하세요 : '))
scripts_per_page = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

if script_num % scripts_per_page == 0:
    page_num = script_num // scripts_per_page
else :
    page_num = script_num // scripts_per_page + 1

print(page_num)