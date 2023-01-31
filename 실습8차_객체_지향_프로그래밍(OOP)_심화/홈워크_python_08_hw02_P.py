class Stack:
    
    def __init__(self): # 인스턴스 생성 시 빈 리스트를 각 인스턴스의 namespace에 할당
        self.lst = []

    def empty(self): 
        if self.lst == []: # 스택이 비었으면
            return True 
        else: 
            return False
    
    def top(self):
        # if Stack.empty(self) == True: , empty 함수는 인스턴스 함수이기에
        if self.empty() == True: # 좀 더 보편적인 표현법, self : 인스턴스의 모든 정보를 포함
            return 'None'
        else:
            return self.lst[-1] # 마지막 데이터 반환
    
    def pop(self):
        if self.empty() == True:
            return 'None'
        else:
            return self.lst.pop() # 마지막 데이터 반환 & 해당 데이터 삭제
    
    def push(self, x):
        self.lst.append(x) # 스택 가장 마지막 데이터 뒤에 값 추가, 반환값 X

    def __repr__(self):
        return f'{self.lst}' # 현재 스택 요소 표시

stk = Stack()  # stack 객체 생성
print(stk)  # stack object 생성 확인

print(stk.empty())  # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(7)  # stk 에 7 넣음 : [7]
stk.push(8)  # stk 에 8 넣음 : [7,8]
stk.push(9)  # stk 에 9 넣음 : [7,8,9]
print(stk) #= > [7, 8, 9]
print(stk.empty())

print(stk.pop())  # stk 맨 마지막 값을 꺼내온다. 9를 꺼냈으니 출력 : 9
print(stk)  # [7, 8] 꺼내지고 남은 값들

print(stk.top())  # stk 맨 마지막 값을 꺼내지 않고 출력만한다 출력 : 8
print(stk)  # [7, 8] 아무 값도 사라지지 않은걸 알 수 있다

print(stk.pop())  # stk 마지막 값 8 꺼내지면서 출력 : 8
print(stk.pop())  # stk 마지막 값 7 꺼내지면서 출력 : 7

print(stk.empty())  # 객체에 아무것도 들어있지 않으므로 True 출력
print(stk)  # 비어 있으므로 [] 출력
print(stk.pop())
print(stk.top())
