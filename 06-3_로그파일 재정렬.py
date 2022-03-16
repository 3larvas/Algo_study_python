from typing import List

logs = ["dig1 8 1 5 1","let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

def sol_1(logs:List[str]) -> List[str]:
    letters, digs = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digs.append(log)
        else:
            letters.append(log)
    # lamda 표현식 - 정렬 시 우선순위를 매길 수 있다.
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    return letters+digs

print(sol_1(logs))

# lamda 표현식