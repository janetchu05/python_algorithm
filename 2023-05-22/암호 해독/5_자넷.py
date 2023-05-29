def solution(cipher, code):
    answer = ''
    divideByCode = len(cipher)//code
    j = -1
    
    for i in range(0, divideByCode):
        j += code
        answer += cipher[j]
        
    return answer
