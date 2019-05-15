#Here are square functions
#this is for a+b whole square
class babyavi(object):
    if __name__ == "__main__":
        def apbwsqr(x,y):
            a=x*x+y*y+2*x*y
            print("The a+b whole square is ",a)
            return a


        #this is for a-b whole square
        def ambwsqr(x,y):
            b=x*x+y*y-2*x*y
            print("The a-b whole square is ",b)
            return b


        #this is for a square - b square
        def asqrmbsqr(x,y):
            c=(x-y)*(x+y)
            print("The a2-b2 is ",c)
            return c

        #this is for a square + b square
        def asqrpbsqr(x,y):
            d=x*x+y*y   #-2*x*y)+2*x*y
            print("The a2+b2 is ",d)
            return d


        #this is for a+b+c whole square
        def apbpcwsqr(a,b,c):
            e=a*a+b*b+c*c+2*a*b+2*a*c+2*b*c
            print("the Whole Square of (a+b+c)2 is ",e)
            return e


        #this is for a-b-c whole square
        def ambmcwsqr(a,b,c):
            f0=a*a+b*b+c*c
            f1=(2*a*b)
            f2=(2*a*c)
            f3=(2*b*c)
            f=f0-f1-f2+f3
            print("The Whole square of (a-b-c)2 is ",f)
            return f

        ############Here Whole Cube Function are Started

        #this is the function for a +b whole cube
        def apbwcube(a,b):
            g=a*a*a+3*a*a*b+3*a*b*b+b*b*b
            print("The Whole cube of a+b is ",g)
            return g

        #this is the function for a-b whole cube
        def ambwcube(a,b):
            h=a*a*a-3*a*a*b+3*a*b*b-b*b*b
            print("The Whole Cube Of a-b is ",h)
            return h

        #This is the function for a cube - b cube
        def acubembcube(a,b):
            i=(a-b)*(a*a+a*b+b*b)
            print("The a cube - b cube of your argument is ",i)
            return i


        #this is the function for a cube + b cube
        def acubembcube(a,b):
            j=(a+b)*(a*a-a*b+b*b)
            print("The a cube + b cube is  ",j)
            return j


        #Here 4th Function is Started

        #this is the function for a+b raise to 4

        def apbwfour(a,b):
            k0=a*a*a*a
            k1=4*a*a*a*b
            k2=6*a*a*b*b
            k3=4*a*b*b*b
            k4=4*a*b*b*b
            k5=b*b*b*b
            
            k=k0+k1+k2+k3+k4+k5
            
            print("The a+b raise to Whole 4 is ",k)
            
            return k

        #this is the function for a-b raise to 4

        def ambwfour(a,b):
            
            l1=a*a*a*a
            l2=4*a*a*a*b
            l3=6*a*a*b*b
            l4=4*a*b*b*b
            l5=b*b*b*b
            
            l=l1+l2+l3+l4+l5
            
            print("The a-b raise to 4 is ",l)
            return l


        #this is the function for a raise to 4-b raise to 4
        def afourmbfour(a,b):
            
            m0=a-b
            m1=a+b
            m2=a*a+b*b
            
            m=m0*m1*m2
            print("The a raise to 4 - b raise to 4 ",m)
            return m



        #this is function for a raise to 5 - b raise to 5

        def afivembfive(a,b):
            
            n0=a-b
            n1=a*a*a*a
            n2=a*a*a*b
            n3=a*a*b*b
            n4=a*b*b*b
            n5=b*b*b*b
            
            n=n0+n1+n2+n3+n4+n5
            
            print("The a raise to 5 - b raise to 5 is ",n)
            return n




        #this is calander program
        def babycal():
            a=int(input("Enter the no of days in a month: "))
            b=int(input("Enter which day will month start(with SUNDAY=0): "))

            print("Su Mo Tu We Th Fr Sa")
            temp=b
            d=1
            i=0
            while d<=a:
                if(d==1):
                    print("  "*b,end="  ")
                if(temp%7==0):
                    print()
                if(d<=9):
                    print(" "+str(d),end=" ")
                else:
                    print(d,end=" ")
                d=d+1
                temp=temp+1



        #This is Prime Number Or Not Program
        def isprime():
            num=int(input("Enter a number   "))
            i=2
            while i<num:
                if num%i==0:
                    print("Entered Number is not PRIME.")
                    break
                i=i+1
            else:
                print("Entered Number is PRIME.")
                    

        #This is Factorial Program
        def factorial(n):
            fact=1
            for i in range(2,n+1):
                fact=fact*i
            return fact


        #This is natural number from 1 to n
        def naturalnumber():
            
            num=int(input("enter number  "))
            for i in range(1,num+1):
                    print(i,end=" ")



        #This is Natural number in reverse manner


        def reversenatural():
            num=int(input("enter number"))
            while num>0:
                print(num,end=" ")
                num-=1



        # This is Abcd

        def atoz():
            for i in range(97,123):
                print(chr(i),end=" ")




        #This is number between function


        def numberbetween():
            a=int(input("Enter Start Number"))
            b=int(input("Enter end Number"))
            for i in range(a,b):
                print(i,end=" ")



                

        #This is 1 to n even number

        def evennumber():
            a=int(input("Enter Start Number"))
            b=int(input("Enter end Number"))
            for i in range(a,b):
                if i%2==0:
                    print(i,end=" ")        



        #This is oddnumber function 1 to n
                    
        def oddnumber():
            a=int(input("Enter Start Number"))
            b=int(input("Enter end Number"))
            for i in range(a,b):
                if i%2==1:
                    print(i,end=" ")



        #This is sum of n numbers


        def sumofnnumber():
            
            n=int(input("enter number"))
            ans=(n*n+n)/2
            print(ans)




        #This is for Sum of even number

        def sumofevennumber():
            n=int(input("enter number"))
            ans=0
            for i in range(0,n+1,2):
                    ans=ans+i
            print(ans)




        #this is function for sum of odd numbers

            
        def sumofoddnumber():
            n=int(input("enter number"))
            ans=0
            for i in range(1,n,2):
                if i%2==1:
                    ans=ans+i
            print(ans)




        # This is function for multiplication table

        def multitable():
            n=int(input("enter number"))
            for i in range(1,11):
                 print(n,"X",i,"=",n*i)


                


        #This Function for Total Number of Digit

                 
        def numberofdigit():
            n=int(input("Enter number:"))
            count=0
            while(n>0):
                    count=count+1
                    n=n//10
            print("The number of digits in the number are:",count)



            
        #the sum of first and last numbers

        def sumoffl():
            num=int(input('Enter a number '))
            num1=num%10;
            num2=num
            while num2>=10:
                num2=num2/10;
            print (int(num1+num2))


            


        #Swap a number in list after printing list


        def swapnumber():
            a=[]
            n= int(input("Enter the number of elements in list:"))
            for x in range(0,n):
                element=int(input("Enter element" + str(x+1) + ":"))
                a.append(element)
            
            temp=a[0]
            a[0]=a[n-1]
            a[n-1]=temp
            print("New list is:")
            print(a)

            


            

        #Sum Of the number


        def sumofnumber():
            

            num = int(input("Enter a Number: "))
            result = 0
            hold = num


            while num > 0:
                rem = num % 10
                result = result + rem
                num = int(num/10)


            print("Sum of all digits of", hold, "is: ", result)





        #Product Of The Digit

        def productofdigit():
            n = input("Enter A Number")
            l= str(n)
            ls= list(l)
            product = 1

            for i in l:
                product = product * int(i)
            print (product)




            
        #This Function for Palindrome


            
        def ispalindrome():
            n=int(input("Enter number:"))
            temp=n
            rev=0
            while(n>0):
                dig=n%10
                rev=rev*10+dig
                n=n//10
            if(temp==rev):
                print("The number is a palindrome!")
            else:
                print("The number isn't a palindrome!")



            




















                
            





        

        







