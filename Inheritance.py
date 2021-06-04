#Inheritance
class A:
    def feat1(self):
        print("feat1 working")
    def feat2(self):
        print("feat2 is working")

    def feat7(self):
        print("feat7 is working in A")
class B(A):
    def feat3(self):
        print("feat3 working")
    def feat4(self):
        print("feat4 is working")

    def feat7(self):
        print("feat7 is working in B")
class C(B):
    def feat5(self):
        print("feat5 working")
    def feat6(self):
        print("feat6 is working")
    def feat7(self):
        print("feat7 is working in C")
a1 = A()
b1= B()
c1 = C()
b1.feat1()
c1.feat1()
b1.feat7()





# call overridden method with super call ref
class A:
    def __init__(self):
        print("In A init")

    def feat1(self):
        print("feat1 working")

    def feat2(self):
        print("feat2 working")
class B:
    def __init__(self):
        print("In B init")
    def feat3(self):
        print("feat3 working")

    def feat4(self):
        print("feat4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
b=C()
b.feat1()



