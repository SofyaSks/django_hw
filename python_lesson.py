class Fraction:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def __gt__(self, other):
        return (self.__num1 / self.__num2) > (other.__num1 / other.__num2)
    
    def __lt__(self, other):
        return (self.__num1 / self.__num2) < (other.__num1 / other.__num2)
    
    def __add__(self, other):
        return Fraction(self.__num1 * other.__num2 + self.__num2 *other.__num1, self.__num2 * other.__num2)
    
    def __sub__(self, other):
        return (self.__num1 / self.__num2) - (other.__num1 / other.__num2)
    
    def __mul__(self, other):
        return (self.__num1 / self.__num2) * (other.__num1 / other.__num2)
    
    def __str__(self):
        return str(self.__num1) + '/' + str(self.__num2)

first = Fraction(1,2)
second = Fraction (2,4)

print (first > second)
print (first < second)
print (first + second)
print (first - second)
print (first * second)