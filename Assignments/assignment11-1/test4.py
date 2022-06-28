# def test1():
#     print('test1')
#     def test1b():
#         print('test1b')
#
# def test2():
#     print('test2')
#     # test1b()
#     test1()
#
# test1()
# test2()

class IsDuck:
    def __init__(self, floats):
        self.floats = floats

class IsWood(IsDuck):
    def __init__(self, floats, burns):
        super().__init__(floats)
        self.burns = burns

class IsWitch(IsWood):
    def __init__(self, floats, burns, wart, hat):
        super().__init__(floats,burns)
        self.wart = wart
        self.hat = hat

    def witchTest(self):
        if (self.wart and self.hat and self.burns and self.floats) == True:
            print("Burn her!")
        else:
            print("Not a witch.")

woman = IsWitch(True, True, True, True)
woman.witchTest()
