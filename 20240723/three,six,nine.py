def solution(number):
    count = 0
	for i in range(1, number + 1):
            current = i
            while current != 0:
                if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                    count +=1
			    current = current // 10
	return count

def solution2(number):
    count = 0
    for number in range(1,number + 1):
        number_str = str(number)
        count += number_str.count("3")
        count += number_str.count("6")
        count += number_str.count("9")
    #     for s in number_str:
    #         if s in "369":
    #             count += 1
    #         current = current // 10
    # return count


print(solution(10))
print(solution(20))
print(solution(40))

