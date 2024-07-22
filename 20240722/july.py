age = 18
name = "이여원"
print('안녕, 나는 '+name+'이야. 나이는 '+str(age)+ '살이야')
print('안녕, 나는 {}이야, 나이는 {}살이야.'.format(name,age))
print(f'안녕, 나는{name}이야, 나이는 {age}살이야.')

엔드림 = ['마크','제노','해찬','재민','런쥔','천러','지성'] #하민, 밤비, 은호, 예준, 노아
print(엔드림)
for i in range(len(엔드림), 1):
    print(엔드림[i])

for name in 엔드림:
    print(name)

print('구구단 2~9단 출력하기')
단 = 2
# 2~9까지 2~9+1전까지
for 단 in range(2, 9+1 ):  #for 단 in range(2, 9+1, 2)
    # if 단 == 2 or 4 or 6 or 8:
    if 단 % 2 == 0:
        for num in range(1, 9 + 1):
            print(f'{단} X {num} = {단 * num}')
    print('-' * 10)

중식 = [{'menu':'자장면','price':'7000'},{'menu':'짬뽕','price':'8000'},{'menu':'양장피','price':'15000'}]
print(중식)
print(중식[0]['price'])

for 음식 in 중식:
    print(음식.get('manu'))   #print(음식['menu'])
    print(음식['price'])

def get_total_price(dictionary):  #getTotalPrice()<java>
    total = 0
    for 하나씩 in dictionary:
        total += 하나씩['price']
    return total
print(get_total_price(중식))