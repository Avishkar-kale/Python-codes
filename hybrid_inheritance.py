class A:
    def display(self):
        print("Displat from A class")


class B(A):
    def display(self):
        print("Display from B calss")


class c:
    def display(self):
        print("Display from C class")


class D(A, B):
    # def display(self):
    print("Display from D class")


d_1 = D
d_1.display()
