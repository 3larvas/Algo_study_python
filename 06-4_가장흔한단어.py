from typing import List
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def sol_1(para:str, banned:List[str]) -> str:
    # for in 문 안에 if 조건절을 넣을 수 있다. else가 있을 때, 없을 때 선언 위치 차이 기억할 것.
    # words = [word if word not in banned else '----' for word in re.sub("[^\w]", " ", para).lower().split() ]
    # ^\w -> word가 아닌 것은 모두 공백을 치환
    words = [word for word in re.sub("[^\w]", " ", para).lower().split() if word not in banned]
    print(words)
    # Counter 객체 활용법.
    count = collections.Counter(words)
    print(count)
    return count.most_common(1)[0][0]

print(sol_1(paragraph, banned))