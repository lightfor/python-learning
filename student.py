class Student:
    __name = ""

    def __init__(self, name):
        self.__name=name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    student = Student("borphi")
    print(student.get_name())
