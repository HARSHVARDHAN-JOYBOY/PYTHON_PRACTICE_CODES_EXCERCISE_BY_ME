class Stud:
    Scname="SARASWATI VIDYA MANDIR"
    def __init__(self,name):
        self.name=name

    @classmethod
    def chngSc(cls, newsc):
        cls.Scname=newsc

    @classmethod
    def getsc(cls):
        return cls.Scname
    

print(Stud.getsc())
print(Stud.chngSc("NVP Clg"))
print(Stud.getsc())
print(Stud.__name__)
print(Stud.chngSc("KKW nsk"))
print(Stud.getsc())