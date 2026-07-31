# importing required modules
#import port module
import addition
# importing function
from subtraction import sub

# importing module with alias name
import multiplication as MUL
# importing function with alias name
from division import div as DIV
if __name__=="__main__":
    print("welcome to small calculator")
    while True:
        print("1.addition \n 2. subtraction \n 3. multiplication \n 4.division \n 5. exit")
        choice=int(input())
 if choice ==1:
     a,b=map(int,input("enter two numbers with seperated by space":).split())
     res=addition.add(x=a,y=b)
     print(f"addition of {a} and {b} is: {res}")
  elif choice==2:
        a,b=map(int,input("enter two numbers with seperated by space"))
        res=sub(x=a,y=b)
        print(f"subtraction of {a} and {b} is: {res}")
 elif choice==3:
     a,b=map(int,input("enter two numbers"))
 res=multiplication.mul(x=a,y=b)
 print(f"multiplication of {a} and {b} is: {res}")
 elif choice==4:
    a,b=map(int,input("enter two numbers seperated by space:"))
    res=DIV(x=a,y=b)
    print(f"division of {a} and {b} is : {res}")
elif choice==5:
    print("Thank for using this small calculator app")
    exit()
else:
    print("invalid choice")



