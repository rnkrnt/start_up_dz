class MyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("calling str")
        if self.message:
            return f"MyError, {0}".format(self.message)
        else:
            return "MyError has been raised"


a = 10
b = 0
x = a * b
if x == 0:
    raise MyError("Хьюстон, у нас проблемы!")