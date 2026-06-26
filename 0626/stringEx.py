 #문자열
print("hello python") 
print('hello python') 
print('''hello 
python''') 
print("""hello 
python""")
print("hello \npython") 
print("hello \f\rpython") 
print("2hello \r2python") #2python 출력
print("hello \fpython")

 #문자열 길이
a = "Life is too short, You need Python"
print(a[3]) # a의 4번째 문자 출력 (0부터 시작)
print(len(a)) # a의 길이 출력
print(a[0:4]) # a의 1번째부터 4번째까지 출력 > Life 
#a[시작_번호:끝_번호]끝 번호의 문자는 포함 x

 #대입
b=3
c=5
print("I eat %d apples" % b) #정수값 대입
print("I eat %d apples and %d oranges" % (b, c)) #정수값 여러개 대입
print("I eat %d apples and %f oranges" % ((1+2), 3.141592))
# %f : 실수값 대입
print("I eat %d apples and %.2f oranges" % ((1+2), 3.14592))
#%.2f : 소수점 2자리까지 출력 3자리에서 반올림
str1 = "sample python string"
print(str1)
print("example string: %s" % str1) #문자열 대입
# %d: 정수값 대입, %f: 실수값 대입, %s: 문자열 대입

print("I eat {} ".format(3))
print("I eat {0} apples and {1} oranges".format(3, 5)) #중괄호에 값 대입

 #f-string을 사용하여 문자열 포맷팅(사실 숫자 리터럴이라 f 없어도 됨)
print(f"I eat {3} apples and {5} oranges")
print(f"I eat {{3}} apples and {{5}} oranges") 
# f는 "변수나 계산 결과를 넣고 싶을 때" 사용하는 기능

#키보드로부터 입력 받는 함수 input()
a = int(input("Enter first number: "))    #입력값을 a에 저장
b = int(input("Enter second number: "))   #입력값을 b에 저장
print(f"You entered: {a} and {b}")
print(f"a + b = {(a) + (b)}")
print(f"a - b = {(a) - (b)}")
print(f"a * b = {(a) * (b)}")
print(f"a / b = {(a) / (b)}")
#1. 두개의 정수를 입력 받아 사칙연산의 결과를 출력하세요
#2. 5개의 정수 값을 입력받아 리스트에 저장하고 그 리스트의 합, 평균, 최소값, 최대값을 출력하세요.
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
#3. 과일명이 있는 리스트를 정의 하고 그리스트의 첫번째와 마지막 문자열을 출력하세요
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")