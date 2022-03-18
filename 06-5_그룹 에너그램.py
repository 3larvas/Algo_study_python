import collections
from typing import List

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

def sol_1(arr:List[str]) -> List[List[str]]:
    # dict 선언은 이렇게!
    word_dict = collections.defaultdict(list)
    for word in arr:
        # sorted 활용
        word_dict[''.join(sorted(word))].append(word)

    print(word_dict)
    return list(word_dict.values())

print(sol_1(arr))