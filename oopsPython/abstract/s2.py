from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def show(self):
        pass

    def disp(self):
        print('concrete method')

class Son(Father):
    def show(self):
        print()

s = Son()
s.show()
s.disp()







