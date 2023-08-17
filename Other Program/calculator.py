
class Calculator:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2
calculator = Calculator()
while True:
    while True:
        try:
            num1 = int(input("Enter the First Number:" ))
            num2 = int(input("Enter the Second Number:" ))
            break
        
        except Exception as e:
            print(e)
    
    
    
    user_choose = input('choose command')
    
    if user_choose == '+':
        print("The Addition of",num1,"and",num2,"is", calculator.add(num1,num2))
    elif user_choose == '-':
        print("The Substraction of",num1,"and",num2,"is", calculator.sub(num1,num2))
    elif user_choose == '*':
        print("The Multiply of",num1,"and",num2,"is", calculator.mul(num1,num2))
    elif user_choose == '/':
        print("The Division of",num1,"and",num2,"is", calculator.div(num1,num2))
        break
    else:
        print("Invalid Command")
    
   






