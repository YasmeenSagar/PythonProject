from math import *


class Calculator:
    def __init__(self):
        self.call()

    def call(self):

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        choice = 1
        while choice != 0:
            print("0. Exit")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = int(input("Enter choice: "))
            if choice == 1:
                print("Result: ", self.add(a,b))
            elif choice == 2:
                print("Result: ", self.sub(a,b))
            elif choice == 3:
                print("Result: ", self.mul(a,b))
            elif choice == 4:
                print("Result: ", round(self.div(a,b), 2))
            elif choice == 0:
                print("Exiting!")
            else:
                print("Invalid choice!!")

    def add(self,a,b):
        return a + b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b

    def sub(self,a,b):
        return a -b



class ScientficCalculator:
    def __init__(self):
        self.abc()

    def sine(self,c):
        return sin(c)

    def cosine(self,c):
        return cos(c)

    def tangent(self,c):
        return tan(c)

    def logarithm(self,c):
        return log(c)

    def abc(self):
        c = int(input("Enter number: "))

        select = 1
        while select != 0:
            print("0. Exit")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            print("4. Log")

            select = int(input("Enter choice: "))
            if select == 1:
                print("Result: ", self.sine(c))
            elif select == 2:
                print("Result: ", self.cosine(c))
            elif select == 3:
                print("Result: ", self.tangent(c))
            elif select == 4:
                print("Result: ", self.logarithm(c))
            elif select == 0:
                print("Exiting!")
            else:
                print("Invalid choice!!")


class UseCalculator:
    def __init__(self):
        user = 1
        while user != 0:
            print("1.Basic Operations")
            print("2.Scientific Operations")

            user = int(input("Enter between 1&2 ..which operation you want me to perform? :"))
            if user == 1:
                print("Performing Basic Operations")
                y=Calculator()
                break
                y.call()


            elif user == 2:
                print("Performing Scientific operation")
                z=ScientficCalculator()
                break
                z.abc()


            else:
                print("invalid choice")


t = UseCalculator()


