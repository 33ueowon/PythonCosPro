unit = ["S","XS","M","L","XL","XXL""XXXL""XXXXL"]
def solution(shirt_size):
    answer = []
    answer = [0 for _ in range(8)]
    answer = [0] * 8

    for size in shirt_size:
        #unit에 있는 size의 index를 갖고와라
        index = unit.index(size)
        answer[index] += 1
        # if size == "XS":
        #     answer[0] += 1
        # elif size == "S":
        #     answer[1] += 1
        # elif size == "M":
        #     answer[2] += 1
        # elif size == "L":
        #     answer[3] += 1
        # elif size == "XL":
        #     answer[4] += 1
        # elif size == "XXL":
        #     answer[5] += 1
        # elif size == "XXXL":
        #     answer[6] += 1
        # elif size == "XXXXL":
        #     answer[7] += 1
    return answer
shirt_size = ["M","XL","XXL","S","XXXL","M","L","XXXXL","XL","XL","XS","M","L","S"]
print(solution(shirt_size))