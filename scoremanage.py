#성적관리 프로그램
file = {'홍길동':[90, 88, 55], '김기영': [77, 66, 100], '곽진수':[88, 99, 98]}

class Scores() :
    def __init__(self, name, score) :
        self.name = name
        self.score = score
    
    def sumbyname(self) : #개인에 대한 총점
        sum = 0
        for i in range(10):
            sum = sum + file[self.name][i]
        return sum

    def avgbyname(self) : #개인에 대한 평균
        pass

    def sumbysub(self) : #과목에 대한 총점
        pass

    def avgbyshb(self) : #과목에 대한 평균
        pass

    def sumtotal() : #전과목 총점
        pass

    def avgtotal() : #전과목 평균
        pass