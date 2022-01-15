#방법 1
#class 설정
class CAccount:
    def __init__(self, owner, amount = 0, password = '1111'):
        self.owner = owner
        self.balance = amount
        self.password = password

    def passcode(self, code):
        while code != '1111' :
            code = input("비밀번호가 틀렸습니다. 다시 입력해주세요.: ")
        else:
            pass

    def inform(self):
        print("잔액은 %d 원 입니다."%amount)

    def deposit(self, plus):
        self.result = amount + plus
        print("입금하신 금액은 %d 원 입니다. 잔액은 %d 원 입니다."%(plus, self.result))            

    def withdraw(self, minus):
        self.result = amount - minus
        if self.result < 0:
            print("잔액 부족, 거래가 중지됩니다.")
        else:
            print("출금하신 금액은 %d 원입니다. 잔액은 %d 원 입니다."%(minus, self.result))
        
    def endprogram(self):
        print("계좌 거래가 종료되었습니다.")

#설정값
cal1 = CAccount("홍길동", 1000, '1111')
amount = 1000

#초기 디스플레이 화면
print("%s 통장"%cal1)
print("-"*50)
print("1. 잔액확인\n2. 입금\n3. 출금\n4. 종료")
print("-"*50)

#비밀번호
code = input("비밀번호를 눌러주세요.: ")
print(cal1.passcode(code))

#메뉴 선택
x = int(input("원하시는 메뉴를 선택해 주세요.: "))

#ATM기 구동
if x == 1:
    print(cal1.inform())
elif x == 2:
    plus = int(input("입금하실 금액을 알려주세요.: "))
    while plus < 0:
        plus = int(input("정확한 금액을 입력하세요.: "))
    else:
        print(cal1.deposit(plus))
elif x == 3:
    minus = int(input("출금하실 금액을 알려주세요: "))
    while minus < 0:
        minus = int(input("정확한 금액을 입력하세요: "))
    else:
        print(cal1.withdraw(minus))
else:
    print(cal1.endprogram())
    