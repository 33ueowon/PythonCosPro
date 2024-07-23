def func_a(k):
    sum = 0
    for i in range(1,k+1):#
        sum += i#
    return sum

def solution(n,m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer


'''
1. 모든 과목 점수의 합을 구합니다.
2. 최고 점수를 구합니다.
3. 최저 점수를 구합니다.
4. (모든 과목 점수의 합) - (최고 점수) - (최저 점수)의 값을 return 합니다.
'''

def func_a(s):
    ret = 0
    for i in s:
        if i > ret: #max
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret: #min
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score


'''
1. 입력으로 주어진 배열에서 가장 많은 방문객 수를 찾습니다.
2. 1번 단계에서 찾은 값을 제외하고, 나머지 값들로 이루어진 새로운 배열을 만듭니다.
3. 2번 단계에서 만든 새로운 배열에서 가장 큰 방문객의 수를 찾습니다.
4. 1번 단계와 3번 단계에서 구한 값의 차이를 구합니다.
'''

def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x:    #max
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor,max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first,max_second)
    return answer

'''
85점 ~ 100점 : A 학점
70점 ~ 84점 : B 학점
55점 ~ 69점 : C 학점
40점 ~ 54점 : D 학점
0점 ~ 39점 : F 학점
'''
def solution(scores):
    grade_counter = [0 for i in range(5)]   #0~4 0으러 5개 채우기
    for x in scores:
        if x>=85:
            grade_counter[0] += 1   #A
        elif x>=70:
            grade_counter[1] += 1   #B
        elif x>=55:
            grade_counter[2] += 1   #c
        elif x>=40:
            grade_counter[3] += 1   #d
        else:
            grade_counter[4] += 1   #e
    return grade_counter


'''
징검다리에 적힌 숫자가 첫 번째 징검다리부터 순서대로 들어있는 배열 stones가 solution 함수의 매개변수로 주어집니다.

stones 배열의 길이는 1 이상 100 이하입니다.
stones의 원소(돌에 적혀있는 숫자)는 1 이상 5 이하의 자연수입니다.
'''

# def solution(stones):
#     cnt = 0
#     current = 0
#     n = len(stones)
#     while :
#         current +=
#         cnt += 1
#     return cnt

'''
학생들의 키가 들어있는 목록에서 키가 k보다 큰 사람은 몇 명인지 구하려합니다.
175보다 큰 사람 몇 명~
'''
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer

'''
알파벳 바꾸기
'''
def solution(s):
    s_lst = list(s) #['a','b','z']
    n = len(s)  #3
    for i in range(n):  #range(len(s)) : 0,1,2
        if s_lst[i] == 'a':
            s_lst[i] = 'z' #['z','b','z']
        elif s_lst[i] == 'z':
            s_lst[i] =  'a' #['a','b','a']
    return "".join(s_lst)


'''
k번째 작은 수
'''
a = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
for line in a:
    for num in line:
        print(num, end="\t")
    print()