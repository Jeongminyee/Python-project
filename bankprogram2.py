#방법 2
#class 설정
class CAccount :
    def __init__(self, owner, amount, password) :
        self.owner = owner
        self.amount = amount
        self.password = password
    
    def passcode(self) : #비밀번호 확인
        ckpassword = input("계좌 비밀번호를 입력해주세요. : ")
        while ckpassword != self.password :
            ckpassword = input("비밀번호가 틀렸습니다. 다시 입력해주세요. : ")
        else :
            pass
    
    def check(self) : #계좌잔액확인
        print("잔액은 %d원 입니다."%self.amount)
    
    def deposit(self) : #입금하기, 입금금액 0원 이하시 오류메세지
        plus = int(input("입금하실 금액을 입력해주세요. : "))
        while plus <= 0 :
            plus = int(input("잘못된 금액을 입력하셨습니다. 입금하실 금액을 입력해주세요. : "))
        else :
            print("%d원이 입금되었습니다. 현재 계좌 잔액은 %d원입니다."%(plus, self.amount+plus))
    
    def withdrawl(self) : #출금하기
        minus = int(input("출금하실 금액을 입력해주세요. : "))
        if minus > self.amount :
            print("출금할 금액이 부족합니다. 거래가 종료됩니다.")
        else :
            print("%d원이 출금되었습니다. 잔액은 %d원 입니다."%(minus, self.amount-minus))
    
    def endprogress(self) : #종료하기
        print("계좌 거래가 종료됩니다.")

    def display(self): #초기 디스플레이 화면
        print('''%s 통장
        -----------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        -----------------------
        '''%self.owner)

#설정값
custom1 = CAccount("정민", 72835000, "1234")

print(custom1.display())
x = int(input("원하시는 메뉴의 번호를 눌러주세요. : "))

#ATM기 구동
if x == 1 :
    print(custom1.passcode())
    print(custom1.check())
elif x == 2 :
    print(custom1.passcode())
    print(custom1.deposit())
elif x == 3 :
    print(custom1.passcode())
    print(custom1.withdrawl())
else :
    print(custom1.endprogress())