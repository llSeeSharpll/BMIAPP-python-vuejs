# this is the bm class
class Bmi():
    def __init__(self, name, wieght, height):
        self.name = name
        self.wieght = wieght
        self.height = height

    def calculate_bmi(self):
        bmi = self.wieght/pow(self.height, 2)
        if bmi < 25:
            s1 = self.name+" bmi: "+str(bmi)+"\n"+self.name+" is not overwieght"
            return s1
        else:
            s2 = self.name+" bmi: "+str(bmi)+"\n"+self.name+" is overwieght"
            return s2