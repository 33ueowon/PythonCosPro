numbers = [3,5,1,4,2,5,3,1,3,5,2,1,2]
count_array = [0 for i in range(5)]
for number in numbers:
    count_array[number - 1] += 1
print(count_array)

#가장 많이 나온 숫자 몇 ?ㅋ
max_ = max(count_array)
#가장 적게 나온 숫자 몇 ?ㅋ
min_ = min(count_array)
print(int(max_ / min_))