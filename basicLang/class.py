class a:
    def init(self):
        self.__pri1=1
        self._pri2=2
        self.pri3=3
    def setV(self):
        self.pri3+=1
        self._pri2+=1
        self.__pri1+=1
    def printall(self):
        print self.pri3
        print self._pri2
        print self.__pri1

b=a()
b.init()
b.printall()
b.setV()
b.printall()
b
