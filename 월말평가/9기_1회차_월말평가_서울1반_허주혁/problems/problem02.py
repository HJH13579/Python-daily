# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    sorted_scores = sorted(scores) # scores 리스트를 오름차순으로 정렬

    (min, max) = (sorted_scores[0], sorted_scores[len(sorted_scores)-1]) # 오름차순 시 첫번째가 최소, 마지막이 최대, 주소값으로 불러와서 튜플로 지정

    return (min,max)
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
