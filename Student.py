import sys


class Student:

    def __init__(self, name, age, sex, phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone

    def __delete__(self, instance):
        del self.name
        del self.age
        del self.sex
        del self.phone

    def set_name(self, name: str):
        self.name = name

    def set_age(self, age: str):
        self.age = age

    def set_sex(self, sex: str):
        self.sex = sex

    def set_phone(self, phone: str):
        self.phone = phone

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> str:
        return self.age

    def get_sex(self) -> str:
        return self.sex

    def get_phone(self) -> str:
        return self.phone


class Actions:

    def __init__(self):
        self.student_list = list()
        self.menu()

    def add(self):
        name = str(input("Enter name: "))
        age = str(input("Enter age: "))
        sex = str(input("Enter sex: "))
        phone = str(input("Enter phone: "))
        student = Student(name, age, sex, phone)
        print("Student added")
        self.student_list.append(student)
        self.menu()

    def print_all(self):
        print("Students")
        for num, val in enumerate(self.student_list):
            print("\tName: ", val.get_name())
            print("\tAge: ", val.get_age())
            print("\tSex: ", val.get_sex())
            print("\tPhone: ", val.get_phone())
        self.menu()

    def exit(self):
        sys.exit(0)

    def edit_name(self, name):
        new_name = input('Enter new name: ')
        for num, val in enumerate(self.student_list):
            if name in val.get_name():
                val.set_name(new_name)
        self.menu()

    def edit_age(self, name):
        new_age = input('Enter new age: ')
        for num, val in enumerate(self.student_list):
            if name in val.get_name():
                val.set_age(new_age)
        self.menu()

    def edit_sex(self, name):
        new_sex = input('Enter new sex: ')
        for num, val in enumerate(self.student_list):
            if name in val.get_name():
                val.set_name(new_sex)
        self.menu()

    def edit_phone(self, name):
        new_phone = input('Enter new phone: ')
        for num, val in enumerate(self.student_list):
            if name in val.get_name():
                val.set_name(new_phone)
        self.menu()

    def editing(self):
        name = input('Enter name of editing student: ')
        print("\nEditing menu:")
        print("1-Name\n2-Age\n3-Sex\n4-Phone\n5-Back to menu")
        choice = input("Choose action: ")
        choice_menu = {'1': self.edit_name(name),
                       '2': self.edit_age(name),
                       '3': self.edit_sex(name),
                       '4': self.edit_phone(name),
                       '5': self.menu}
        if choice not in choice_menu.keys():
            print("Please enter correct number")
            self.editing()
        else:
            choice_menu[choice]()

    def menu(self):
        print("\nMenu\n")
        print("1-Read\n2-Add\n3-Edit\n4-Exit\n")
        choice = input("Choose action: ")
        choice_menu = {'1': self.print_all,
                       '2': self.add,
                       '3': self.editing,
                       '4': self.exit}
        if choice not in choice_menu.keys():
            print("Please enter correct number")
            self.menu()
        else:
            choice_menu[choice]()


Actions()
