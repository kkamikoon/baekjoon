def add_list(first, second):
    res = []
    res.append(first[0] + second[0])
    res.append(first[1] + second[1])

    return res


def fibonacci(num):
    answer = [[1,0], [0,1]]

    if num == 0:
        return answer[0]
    elif num == 1:
        return answer[1]
    else:
        for __ in range(num-1):
            answer.append(add_list(answer[-1], answer[-2]))

        return answer[-1]

if __name__ == "__main__":
    answers = []

    for _ in range(int(input())):
        answers.append(fibonacci(int(input())))

    for a in answers:
        print(f"{a[0]} {a[1]}")
