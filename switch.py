# not recommend
class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fail = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fail or not args:
            return True
        elif self.value in args:
            self.fail = True
            return True
        else:
            return False


operator = "+"
x = 1
y = 2
for case in Switch(operator):
    if case("+"):
        print(x+y)
        break
    if case("-"):
        print(x-y)
        break
    if case("*"):
        print(x*y)
        break
    if case("/"):
        print(x/y)
        break
    if case():
        print("")
        break
