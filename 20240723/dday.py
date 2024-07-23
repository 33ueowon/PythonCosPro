month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
start_month = 1
start_day = 2
end_month = 2
end_day = 2

def func_a(month, day):
    answer = 0
    #month
    for i in range(month - 1):
        answer += month_list[i]  #1 => 0, 2 => 31, 3 => 31 + 28
    #day
    answer += day - 1
    return answer

def solution(start_month,start_day,end_month,end_day):
    answer = 0
    #1월 1일 부터 정해진 날짜까지 날 수 구하긔.
    # 1월 1일 ~ end_month end_day까지 날 수 구하자
    long_day = func_a(end_month,end_day)
    #1월 1일 ~ short_month start_day까지 날 수 구하자
    short_day = func_a(start_month, start_day)
    answer = long_day - short_day
    return answer

print(solution(1,2,1,3))    #31
print(solution(start_month,start_day,end_month,end_day))    #31
print(solution(7,1))