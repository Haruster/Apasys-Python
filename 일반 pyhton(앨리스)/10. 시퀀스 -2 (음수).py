# 인덱싱 / 슬라이싱을 할 때 음수를 넣거나, 자리를 비우는 것도 가능하다.
a = "Once" #문자열

b = ['T', 'W', 'I', 'C', 'E'] #리스트

c = (1, 2, 3, 4, 5) #튜플

print(a[-1]) #e가 출력된다. (뒤에서 1번째 원소)
print(b[:3]) # ['T', 'W', 'I']가 출력된다. (처음 ~ 3번째까지 슬라이싱한다.)
print(b[2:]) # ['I', 'C', 'E']가 출력된다. (두번째 원소이상부터 모든 원소)