from abc import ABC, abstractmethod


class Fees(ABC):
    def print_slip(amount):
        print("Fees submitted : ", amount)


    @staticmethod
    @abstractmethod
    def fees(amount):
        pass


class Class10(Fees):
    # @staticmethod
    def fees(amount):
        print("Total Fees of Class 10th: ", amount)

class Class12(Fees):
    @staticmethod
    def fees(amount):
        print("Total Fees of Class 12th:", amount)


# obj = Class10()
# obj.fees(20000)
# # obj.print_slip(20000)
# # obj1= Class12()
# # obj1.fees(50000)
# # obj1.print_slip(50000)
Class10.fees(20)
# Class12.fees(60)
