def solution(temperature, A, B):
	answer = 0
	A = 0
	B = 2
	for i in range(A + 1, B):
		if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
			answer += 1
	return answer


temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution(temperature, A, B)

print("solution 함수의 반환 값은", ret, "입니다.")