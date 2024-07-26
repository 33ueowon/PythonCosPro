# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(time_table, n):
	answer = 0
	sum_list = [0] * n
	index = 0
	for time in time_table:
		sum_list[index % n] += time
		index += 1
		# if index == n:
		# 	index = 0
	answer = max(sum_list)
	return answer


time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
