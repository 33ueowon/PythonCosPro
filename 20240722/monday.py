#숫자가 들어있는 리스트의 합계
scores = [2024, 7, 22, 3, 4]
sum_list =sum(scores)
print(sum_list)   #2060

#2. 최댓값
scores = [2024, 7, 22, 3, 4]
max_list = max(scores)
print(max_list)   #2024
#3. 최솟값
scores = [2024, 7, 22, 3, 4]
min_list = min(scores)
print(min_list)   #3
#4. 평균
scores = [2024, 7, 22, 3, 4]
average_list = sum(scores)/len(scores)
print(round(average_list,1))   #412.0
#5. 홀수인 것만 세기
scores = [2024, 7, 22, 3, 4]
for count_odd in scores:
    if count_odd % 2 == 0:
        continue
    print(count_odd)   #10
#6. N개의 0을 가진 리스트 만들기
scores = [2024, 7, 22, 3, 4]

print(make_list(6))   #[0, 0, 0, 0, 0, 0]