def solution(my_str, n):
    answer = []
    for x in range(0, len(my_str), n):
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answers