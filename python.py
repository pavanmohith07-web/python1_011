'''a="Good Morning"
print(a[7:11])
print(a[-5:-1])'''
'''a='good morning'
print(a[1:6:2])
print(a[5::3])
print(a[-1:-8:-3])
print("hello world")'''
'''a='good morinng'
print(a[-2:-8-1:-3])
print(a[10:4-1:-3])'''
'''a=eval(input("enter a nmber:"))
print(a,type(a))'''
# chr = input("enter a character :")
# if "A"<=chr<="Z":
#     print("th echaracter is uppercase :")
# elif "a"<=chr<="z":
#     print("the character is lowercase :")
# else:
#     print("the character is not a letter.")
# username = "pavan"
# password = "ps@194"
# un = input("enter the username :")
# if(un == username):
#     pw = input("enter the password :")
#     if(pw == password):
#         print("login succesfully")
#     else:
#         print("incorrect password")
#         exit()
# else: 
#     print("Incorrect username")
# exit()
# for i in range(51):
#     if i%2 == 0:
#         print(i,"is even")
# l = [10,20,30]
# for i in l:
#     print(i)
# s=input("enter a string :")
# out=''
# for i in s:
#     if"A"<=i<="Z":
#         out+=chr(ord(I)+32)
#     elif 'a'<=i<='z':
#         out+=chr(ord(i)-32)
#     else:
#         out+=i
#     print(out)

# s = input("enter a string :")
# rev =''
# for i in s:
#     rev=i+rev
# print(rev)
 
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i == j:
#             print('@',end =' ')
#         else:
#             print('0',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i<j:
#             print('*',end =' ')
#         else:
#             print(' ',end=' ')
#     print()
# print("hello word")


#args with return 

# def convert_to_uppercase(s,out ):
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     return out 
# print(convert_to_uppercase(input("enter a string:"),""))
    

#with args without return

# def convert_to_uppercase(s,out ):
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     print(out) 
# print(convert_to_uppercase(input("enter a string:"),""))

#without args without return

# def convert():
#     s=input("enter :")
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     print(out)
# convert()

#without args with return

# def convert():
#     s=input('enter :')
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     return out 
# print(convert())

# class and objects
# whatever the changes made in class it is aplicable to objects also
# class college:
#     cname="GCEM"
#     cloc="Hoodi"
# s1=college()
# print(s1.cname,s1.cloc)
# college.cloc="KR puram"
# print(college.cloc)
# print(s1.cloc)
# s1.cloc='Hoodi'
# print(s1.cloc)
# print(college.cloc)

#class college:
#     cname='GCEM'
#     cloc='Hoodi'
# s1=college()
# s1.sname='EREN'
# s1.phone=8456375890

# s2=college()
# s2.sname='MIKASA'
# s2.phone=9445425470

# print(s1.cname)
# s1.cloc='KR puram'
# print('After Changing')
# print(s1.cloc)
# print(s2.cloc)
# print(college.cloc)

class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
s1=college('EREN',8456375890,'1GD001')
s2=college('MIKASA',9445425470,'1GD002')
s1.display()
s2.display()

