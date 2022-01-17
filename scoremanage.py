#성적관리 프로그램
file = {'홍길동':[90, 88, 55], '김기영': [77, 66, 100], '곽진수':[88, 99, 98]}

class Scores() :
    def __init__(self) : #초기 설정값
        pass
    
    def sumbyname(self) : #개인에 대한 총점
        name = input("총점을 구할 사람의 이름을 입력해주세요. : ")
        sum = 0

        for i in range(len(file)):
            sum = sum + file[name][i]
        return("%s님의 총점은 %d점 입니다."%(name, sum))

    def avgbyname(self) : #개인에 대한 평균
        
        name = input("평균을 구할 사람의 이름을 입력해주세요. : ")
        sum = 0

        for i in range(len(file)):
            sum = sum + file[name][i]
        return("%s님의 평균은 %d점 입니다."%(name, sum / len(file[name])))

    def sumbysub(self) : #과목에 대한 총점
        
        a = input("총점을 구할 과목명을 입력해주세요. : ")
        if a == "국어" :
            a = 0
        elif a == "영어" :
            a = 1
        elif a == "수학" :
            a = 2
        else :
            print("Error")
        
        total = 0 #총점초기값
    
        for i in range(len(file.keys())):
            total += file[list(file.keys())[i]][a]
        return("해당 과목의 총점은 %d점 입니다."%total)

    def avgbysub(self) : #과목에 대한 평균
        a = input("평균을 구할 과목명을 입력해주세요. : ")

        if a == "국어" :
            a = 0
        elif a == "영어" :
            a = 1
        elif a == "수학" :
            a = 2
        else :
            print("Error")
        
        total = 0 #총점초기값
    
        for i in range(len(file.keys())):
            total += file[list(file.keys())[i]][a]
        return("해당 과목의 평균은 %d점 입니다."%(total / len(file.keys())))

    def sumtotal(self) : #전과목 총점
        total = sum(list(file.values()),[])
        plus = 0
        for i in range(len(total)):
            plus += total[i]
        return("전과목 총점은 %d점 입니다."%plus)

    def avgtotal(self) : #전과목 평균
        total = sum(list(file.values()),[])
        plus = 0
        for i in range(len(total)):
            plus += total[i]
        return("전과목 평균은 %d점 입니다."%(plus/len(total)))

cal1 = Scores()

print('''
1. 개인에 대한 총점
2. 개인에 대한 평균
3. 과목에 대한 총점
4. 과목에 대한 평균
5. 전체 총점
6. 전체 평균
''')

button = int(input("원하는 메뉴 선택: "))

if button == 1:
    print(cal1.sumbyname())
elif button == 2:
    print(cal1.avgbyname())
elif button == 3:
    print(cal1.sumbysub())
elif button == 4:
    print(cal1.avgbysub())
elif button == 5:
    print(cal1.sumtotal())
else :
    print(cal1.avgtotal())