# question1 employee bonus eligibility
attendence=int(input("enter the attendence"))
perf_rating=int(input("enter the performance"))

def bonus(attendence,perf_rating):
  if(attendence>=80 and perf_rating>=4):
    print("you are eligible for bonus")
  else:
    print("you are not eligible for bonus")
bonus(attendence,perf_rating)



# Q2 login credentials
username=input("enter the username")
password=input("enter the password")
def login(username,password):
  if(username=="ADMIN" and password=="1234"):
    print("login access apporved")
  else:
    print("acess denied")
login(username,password)



# Q3 speed limit of vehicle 
vehicle=input("enter the vehicle")
limit=int(input("enter the speed"))

def speed(vehicle,limit):
  if (vehicle=="car" or vehicle=="rikshaw") and limit<=60:
    print("limit not exceed")
    if(vehicle=="truck" and limit<=50):
      print("limit not exceed for heavy vehicles")
      if(vehicle=="bike" or vehicle=="scooty") and limit<=80:
        print("speed under control")
      else:
        print("drive slow")
speed(vehicle,limit)



# Q3 ticket pricing 
age=int(input("enter age"))
def ticket(age):
  if(age<18):
    print("child ticket")
    if age <60:
      print("adult")
  else:
    print("senior")
ticket(age)



# Q4largest number
a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
def number(a,b,c):
  if a>=b and a>=c:
    return a
  elif b>=a and b>=c:
    return b
  return c
print(number(a,b,c))



# Q login maximum 3 attempts
def login(attempts=0):
  while attempts<3:
    password=(input("enter password"))
    if password == "admin":
      print("login succesful")
      return 
    attempts +=1
print("login failed")
login()




    

