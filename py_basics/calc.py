class Calculator:
    def add(self, *args):
        total = 0
        try:
            for number in args:
                total += number
            print(total)
        except TypeError:
            print("can only add integers not str")

    def sub(self, *args):
        answer = args[0]
        try:
            for number in args[1:]:
                answer -= number
                print(answer)
        except TypeError:
            print("can only subtract integers not str")

    def mul(self, *args):
        answer = args[0]
        try:
            for number in args[1:]:
                answer *= number
                print(answer)
        except TypeError:
            print("can only multiply integers not str")

    def div(self, *args):
        answer = args[0]
        try:
            for number in args[1:]:
                answer /= number
                print(answer)
        except (TypeError, ZeroDivisionError):
            print("invalid division")


# Calculator().add(45, 56, 73, 72, 95)

# Calculator().sub(90, 20)

# Calculator().mul(5, 125)

Calculator().div(100, 5)
