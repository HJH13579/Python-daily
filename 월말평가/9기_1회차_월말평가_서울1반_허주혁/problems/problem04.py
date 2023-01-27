# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 len 사용 금지
def title_length(movie):
    
    movie_words_lst = list(movie["title"]) # str 타입의 딕셔너리 "title"이 value값을 list로 전환, 띄어쓰기까지 리스트 요소로 할당

    movie_words_count = 0

    for i in movie_words_lst: # 리스트 요소 하나 당 for 구문 한번 씩 돌리면서 횟수 count, count 횟수 = title 글자 갯수
        movie_words_count = movie_words_count + 1
    
    return movie_words_count
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(title_length(movie))  # 6 (공백 포함 길이)