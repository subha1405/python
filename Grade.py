a=int(input("Enter the marks of subject 1"))
b=int(input("Enter the marks of subject 2"))
c=int(input("Enter the marks of subject 3"))
d=int(input("Enter the marks of subject 4"))
e=int(input("Enter the marks of subject 5"))
sum=a+b+c+d+e
per=sum/5
if(per>=90):
    print("Grade A")
elif(per<90 and per>=75):
    print("Grade B")
elif(per<75 and per>=65):
    print("Grade C")
elif (per<65 and per>=50):
    print("Grade D")
else:
    print("Grade E")
