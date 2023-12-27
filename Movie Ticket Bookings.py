import uuid
import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost",user = "root", passwd = "sql123", database = "Movie")
global f
global movie_name
global screen_no
global x
global city_name
global ticket
global center_name
f = 0
def t_movie():
    global f
    global movie_name
    f = f+1
    print("which movie do you want to watch?")
    print("1,Intersteller")
    print("2,Spiderman : No Way Home ")
    print("3,Red Notice")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
     
      center()
      theater()
      return 0
    if movie == 1:
        movie_name = "Intersteller"
        theater()
    if movie == 2:
        movie_name = "Spiderman : No Way Home"
        theater()
    if movie == 3:
        movie_name = "Red Notice"
        theater()

def theater():
    global screen_no
    global ticket
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("choose your screen: "))
    if a == 1 :
        screen_no = "SCREEN 1 "
    if a == 2 :
        screen_no = "SCREEN 2"
    if a == 3 :
        screen_no = "SCREEN 3"
    ticket = int(input("number of ticket do you want?: "))
    timing(a)
 

def timing(a):
    global x
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successful!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
    return 0
 
 
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
 
 
def center():
    global center_name
    print("which theater do you wish to see movie? ")
    print("1,Inox")
    print("2,Cinepolis")
    print("3,PVR")
    print("4,back")
    a = int(input("choose your option: "))
    if a == 1:
        center_name = "Inox"
        t_movie()
    elif a == 2:
        center_name = "Cinepolis" 
        t_movie()
    elif a == 3:
        center_name = "PVR"
        t_movie()
    elif a == 4:
        city()
    else:
        print("wrong choice")
    return 0
 

def city():
    global city_name
    print("Hi welcome to Film O Maniac Bookings: ")
    print("where you want to watch movie?:")
    print("1,Kolkata")
    print("2,Dehli")
    print("3,Mumbai")
    place = int(input("choose your option: "))
    if place == 1:
        city_name = "Kolkata"
        center()
    elif place == 2:
        city_name = "Delhi"
        center()
    elif place == 3:
        city_name = "Mumbai"
        center()
    else:
      print("wrong choice") 

city()
Unique_ID = uuid.uuid4().hex[:8]
print("***************************************Summary Of The Ticket*********************************************")
print("City Name :", city_name)
print("Movie Name : ", movie_name)
print("Theatre Name : ", center_name)
print("Number Of Tickets : ", ticket)
print("Screen Number : ",screen_no)
print("Show Timmings : ", x)
print("*********************************************************************************************************")
cursor = mycon.cursor()
cursor.execute("INSERT INTO FOM_Booking(UNIQUE_ID, Movie_Name, Theatre, Timmings, City, Tickets) VALUES('{}','{}','{}','{}','{}',{})".format(Unique_ID,movie_name,center_name,x,city_name,ticket))
mycon.commit()
mycon.close()
