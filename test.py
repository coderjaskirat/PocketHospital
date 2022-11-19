import mysql.connector as mysql
import uuid
from collections import Counter
from datetime import datetime,timedelta
db = mysql.connect(
host = "localhost",
user = "root",
passwd = "8130"
)
cursor = db.cursor()
cursor.execute("use login")
forP = [[" " for i in range(5)] for j in range(5)]
forO = [[" " for i in range(5)] for j in range(5)]
forC = [[" " for i in range(5)] for j in range(5)]
forK = [[" " for i in range(5)] for j in range(5)]
forE = [[" " for i in range(5)] for j in range(5)]
forT = [[" " for i in range(5)] for j in range(5)]
forH = [[" " for i in range(5)] for j in range(5)]
forS = [[" " for i in range(5)] for j in range(5)]
forI = [[" " for i in range(5)] for j in range(5)]
forA = [[" " for i in range(5)] for j in range(5)]
forL = [[" " for i in range(5)] for j in range(5)]
#P
for row in range(5):
for col in range(5):
if (row==0 or row==2) and (col!=4) or (col==0) or (col==4 and row ==1):
forP[row][col]="#"

#O
for row in range(5):
for col in range(5):
if (row==0 or row ==4) and (col!=0 and col!=4) or (col==0 or col==4) and (row!=0 and
row!=4):
forO[row][col]="#"

#C
for row in range(5):
for col in range(5):
if (row==0 or row ==4) and (col!=0) or (col==0)and (row!=0 and row!=4):
forC[row][col]="#"

#K
for row in range(5):
for col in range(5):
if (col==0) or (row==2) and (col<3) or (col==3) and (row ==1 or row ==3) or (col==4)
and (row ==0 or row==4):
forK[row][col]="#"

#E
for row in range(5):
for col in range(5):
if (row==0 or row ==4) or (col==0) or (row ==2) and (col<3):
forE[row][col]="#"

#T
for row in range(5):
for col in range(5):
if (row==0) or (col==2):
forT[row][col]="#"

#H
for row in range(5):
for col in range(5):
if (col==0 or col==4) or (row==2):
forH[row][col]="#"

#S
for row in range(5):
for col in range(5):
if (row==0 and col!=0) or (row==2) and (col!=0 and col!=4) or (row==4 and col!=4) or
(row==1 and col==0) or (row==3 and col==4):

forS[row][col]="#"

#I
for row in range(5):
for col in range(5):
if (row==0 or row==4) or (col==2):
forI[row][col]="#"

#A
for row in range(5):
for col in range(5):
if (row==0) and (col!=0 and col!=4) or (row==2) and (col!=0 or col!=4) or (col==0 or
col==4) and (row!=0):
forA[row][col]="#"

#L
for row in range(5):
for col in range(5):
if (row==4) or (col==0):
forL[row][col]="#"

for n in range(87):
print("*",end="")
print()
print()
for i in range(5):
for j in range(5):
print(forP[i][j],end="")
print(end=" ")
for j in range(5):
print(forO[i][j],end="")
print(end=" ")
for j in range(5):
print(forC[i][j],end="")
print(end=" ")
for j in range(5):
print(forK[i][j],end="")
print(end=" ")
for j in range(5):
print(forE[i][j],end="")
print(end=" ")
for j in range(5):
print(forT[i][j],end="")
print(end=" ")
print(end=" ")
print(end=" ")
print(end=" ")
print(end=" ")
for j in range(5):
print(forH[i][j],end="")
print(end=" ")
for j in range(5):
print(forO[i][j],end="")
print(end=" ")
for j in range(5):
print(forS[i][j],end="")
print(end=" ")
for j in range(5):
print(forP[i][j],end="")
print(end=" ")
for j in range(5):
print(forI[i][j],end="")
print(end=" ")
for j in range(5):
print(forT[i][j],end="")
print(end=" ")
for j in range(5):
print(forA[i][j],end="")
print(end=" ")
for j in range(5):

print(forL[i][j],end="")
print()
print()
print()
for n in range(87):
print("*",end="")
print("")
print("")
dmd='''select parameters,details from hospdet where details<>"POCKET HOSPITAL"'''
print()
cursor.execute(dmd)
mmm=cursor.fetchall()
for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
print()
print("***************************************************************************************")
print()
def exit():
while True:
fgg=input("ENTER Y TO EXIT")
fgg=fgg.upper()
if fgg=="Y":
break
else:
continue
def admin_menu():
while True:
print()
print("1 - COVID")
print(" 1.1 - SHOW QUESTIONS")
print(" 1.2 - MODIFY QUESTIONS ")
print(" 1.3 - ADD QUESTIONS ")
print(" 1.4 - USER COVID RESULT ")
print("2 - REMEDIES")
print(" 2.1 - MODIFY DATA ")
print(" 2.2 - ADD DATA ")
print("3 - BLOODBANK")
print(" 3.1 - SHOW USER DATA ")
print(" 3.2 - CHECK AVAILABLE BLOOD GROUP UNITS ")
print(" 3.3 - UPDATE BLOOD UNITS ")
print(" 3.4 - RESET NO. OF REQ OF BLOOD UNITS")
print("4 - APPOINTMENT")
print(" 4.1 - DOCTORS INFORMATION")
print(" 4.1.1 - VIEW DOCTORS INFO")
print(" 4.1.2 - ADD DOCTOR")
print(" 4.1.3 - UPDATE EXISTING DOCTOR'S NAME")
print(" 4.1.4 - UPDATE EXISTING DOCTOR'S TIMINGS")
print(" 4.1.5 - UPDATE EXISTING DOCTOR'S PHONE NUMBER")
print(" 4.2 - VIEW PATIENT APPOINTMENT BOOKINGS ")
print(" 4.3 - RESET NUMBER OF APPOINTMENTS BOOKED")
print("5 - UPDATE PATIENT DETAILS")
print(" 5.1 - UPDATE PATIENT'S NAME")
print(" 5.2 - UPDATE PATIENT'S AGE")
print(" 5.3 - UPDATE PATIENT'S PHONE NUMBER")
print(" 5.4 - RESET PATIENT'S PASSWORD")
print("6 - UPDATE HOSPITAL DETAILS")
print(" 6.1 - UPDATE HOSPITAL'S ADDRESS")
print(" 6.2 - UPDATE HOSPITAL'S PHONE NUMBER")
print("7 - LOGOUT")

print()
cursor.execute("select doc_id from doctordet")
res=cursor.fetchall()
w=[]
for i in res:
w.append(i[0])
cursor.execute('''select username from registration where desig="USER"''')
lmn=cursor.fetchall()
b=[]
for kl in lmn:
b.append(kl[0])
def rem():
cursor.execute("select count(*) from remedies")
m1 = cursor.fetchone()
n=int(m1[0])
cursor.execute("select disease from remedies")
abf=""
for i in range(n):
abd=cursor.fetchone()
abe = abd[0]
if abf==abe:
pass
else:
print(abe)
abf=abe
ol=input("ENTER:")
if ol=="1.1":
print()
print("1 - COVID")
print("1.1 - SHOW QUESTIONS")
print()
cursor.execute("SELECT QUES FROM COVIDQ")
for i in cursor:
print(i[0])
exit()
continue
elif ol=="1.2":
print()
print("1 - COVID")
print("1.2 - MODIFY QUESTIONS ")
print()
cursor.execute("select count(*) from COVIDQ")
m1 = cursor.fetchone()
n=int(m1[0])
j=1
for i in range(1,n+1):
cursor.execute("SELECT QUES FROM COVIDQ WHERE SNO='"+str(i)+"'")
azz1= cursor.fetchone()
azz2=azz1[0]
print(j,azz2)
j=j+1
abcd = int(input("ENTER THE CHOICE OF QUESTION YOU WANT TO MODIFY"))
for i in range(1,n+1):
if abcd==i:
abcd1 = input("ENTER THE NEW QUES")
cursor.execute("update covidq set ques='"+abcd1+"' where
SNO='"+str(abcd)+"'")
print("QUESTION UPDATED")
db.commit()
exit()
continue
elif ol=="1.3":
print()

print("1 - COVID")
print("1.3 - ADD QUESTIONS ")
print()
abcd3 = input("ENTER THE QUESTION YOU WANT TO ADD")
cursor.execute("insert into COVIDQ(QUES) values('"+abcd3+"')")
print("QUESTION ADDED")
db.commit()
exit()
continue
elif ol=="1.4":
print()
print("1 - COVID")
print("1.4 - USER COVID RESULT")
print()
Nmd='''SELECT*from COVIDSTATUS'''
cursor.execute(Nmd)
mmm=cursor.fetchall()
m = [("USERNAME","COVID STATUS")]
m=m+mmm
for i in m:
for j in i:
a=''
a=a+str(j)
while len(a)<22:
a=a+' '
print(a,end='')
print()
db.commit()
print()
exit()
continue
elif ol=="2.1":
print()
print("2 - REMEDIES")
print("2.1 - MODIFY DATA ")
print()
rem()
abcd3 = input("ENTER THE DISEASE WHOSE HOME REMEDY YOU WANT TO MODIFY")
abcd4=abcd3.upper()
cursor.execute("select SNO from remedies where disease='"+abcd4+"'")
abcd5 = cursor.fetchall()
abcd6 = abcd5[0]
abcd11=abcd6[0]
for i in range(1,500):
if abcd11==i:
abcd7 = input("ENTER THE REMEDY")
cursor.execute("UPDATE REMEDIES SET HOMEREMEDIES='"+abcd7+"' WHERE
SNO='"+str(abcd11)+"'")
print("REMEDY UPDATED")
db.commit()
elif ol=="2.2":
print()
print("2 - REMEDIES")
print("2.2 - ADD DATA ")
print()
rem()
abcd8 = input("ENTER THE DISEASE WHOSE HOME REMEDY YOU WANT TO ADD")
abcd9=abcd8.upper()
abcd10= input("ENTER THE HOME REMEDY")
cursor.execute("insert into remedies(disease,homeremedies)
values('"+abcd9+"','"+abcd10+"')")
print("HOME REMEDY ADDED")
db.commit()
exit()
continue
elif ol=="3.1":

print()
print("3 - BLOODBANK")
print("3.1 - SHOW USER DATA ")
print()
cmd='''SELECT U_NAME, F_NAME ,L_NAME,BLOOD_GROUP, UNIQUE_CODE ,DATE ,N_REQ from
bloodbank'''
cursor.execute(cmd)
lll=cursor.fetchall()
l = [("USERNAME","FIRST NAME","LAST NAME","BLOOD GROUP","UNIQUE CODE","DATE","UNITS
TAKEN")]
l=l+lll
for i in l:
for j in i:
a=''
a=a+str(j)
while len(a)<21:
a=a+' '
print(a,end='')
print()
db.commit()
exit()
continue
elif ol=="3.2":
print()
print("3 - BLOODBANK")
print("3.2 - CHECK AVAILABLE BLOOD GROUP UNITS ")
print()
dmd='''SELECT*from blood_units'''
cursor.execute(dmd)
mmm=cursor.fetchall()
m = [("BLOOD GROUP","UNITS","LAST UPDATED ON")]
m=m+mmm
for i in m:
for j in i:
a=''
a=a+str(j)
while len(a)<22:
a=a+' '
print(a,end='')
print()
db.commit()
exit()
continue
elif ol=="3.3":
print()
print("3 - BLOODBANK")
print("3.3 - UPDATE BLOOD UNITS ")
print()
choice=input("ENTER BLOOD GROUP WHOSE UNITS NEED TO BE UPDATED:")
units=input("ENTER UNITS TO BE ADDED:")
choice=choice.upper()
if choice=="A+":
BLOOD_GROUP=choice
elif choice=="A-":
BLOOD_GROUP=choice
elif choice=="B+":
BLOOD_GROUP=choice
elif choice=="B-":
BLOOD_GROUP=choice
elif choice=="O+":
BLOOD_GROUP=choice
elif choice=="O-":
BLOOD_GROUP=choice
elif choice=="AB+":
BLOOD_GROUP=choice
elif choice=="AB-":
BLOOD_GROUP=choice

else:
print("INVALID INPUT")
print()
H="UPDATE BLOOD_UNITS SET UNITS=%s where BLOOD_GROUP=%s"
T=[units,choice]
cursor.execute(H,T)
db.commit()
exit()
continue
elif ol=="3.4":
print()
print("3 - BLOODBANK")
print("3.4 - RESET NO. OF REQ OF BLOOD UNITS")
print()
u_name=input("ENTER THE USERNAME WHOSE BLOOD REQUEST IS TO BE RESET:")
f=[u_name]
cursor.execute("SELECT U_NAME from bloodbank")
b=[]
d=str(datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
for j in cursor:
b.append(j[0])
if u_name in b:
print("YOU ARE GOING TO RESET THE NUMBER OF REQUESTS FOR BLOOD FOR THE ENTERED
USERNAME")
while True:
yuy=input("ENTER 1-PROCEED ,2- ABORT")
if yuy=="1":
iu='''UPDATE BLOODBANK SET N_REQ=0 where U_NAME=%s and
DON_or_REQ="REQUEST"'''
cursor.execute(iu,f)
zu='''UPDATE BLOODBANK SET DATE=%s where U_NAME=%s and
DON_or_REQ="REQUEST"'''
cursor.execute(zu,d,f)
db.commit()
break
elif yuy=="2":
print("ABORTING")
break
else:
print()
print("ENTER A VALID QUERY")
print()
continue
elif ol=="4.1.1":
print()
print("4 - APPOINTMENT")
print("4.1 - DOCTORS INFORMATION")
print("4.1.1 - VIEW DOCTORS INFO")
print()
dmd='''SELECT doctor_name, doc_id,phone_no, dept , time1 , time2 from doctordet'''
cursor.execute(dmd)
mmm=cursor.fetchall()
m = [("DOCTOR NAME","DOCTOR ID","PHONE NUMBER","DEPARTMENT","TIME SLOT 1","TIME
SLOT 2")]
m=m+mmm
for i in m:
for j in i:
a=''
a=a+str(j)
while len(a)<28:
a=a+' '
print(a,end='')
print()
exit()
continue
elif ol=="4.1.2":
print("4 - APPOINTMENT")

print("4.1 - DOCTORS INFORMATION")
print("4.1.2 - ADD DOCTOR")
print()
doc=input("DOCTOR NAME:")
print()
dep=input("ENTER DEPARTMENT NAME:")
print()
dep,doc=dep.upper(),doc.upper()
print()
pno=input("ENTER PHONE NUMBER:")
print()
t1=input("SHIFT 1 TIMINGS(HH:MM AM/PM - HH:MM AM/PM):")
t2=input("SHIFT 2 TIMINGS(HH:MM AM/PM - HH:MM AM/PM):")
cod=str(uuid.uuid4().hex[:6].upper())
h=[doc,cod,pno,dep,t1,t2]
j="insert into doctordet(DOCTOR_NAME,Doc_id ,Phone_No,DEPT,Time1,Time2)
values(%s,%s,%s,%s,%s,%s)"
cursor.execute(j,h)
db.commit()
print()
print("DOCTOR ADDED TO THE LIST SUCCESSFULLY")
exit()
continue
elif ol=="4.1.3":
print("4 - APPOINTMENT")
print("4.1 - DOCTORS INFORMATION")
print("4.1.3 - UPDATE EXISTING DOCTOR'S NAME")
print()
dcid=input("ENTER DOCTER ID:")
dcid=dcid.upper()
if dcid in w:
nnew=input("ENTER NEW NAME OF DOCTOR")
cursor.execute("update doctordet set DOCTOR_NAME='"+nnew+"' where
doc_id='"+dcid+"'")
print("DOCTOR INFORMATION UPDATED SUCESSFULLY")
db.commit()
print()
else:
print("DOCTOR FOR ENTERED DOCTOR_ID DOES NOT EXIST")
exit()
continue
elif ol=="4.1.4":
print("4 - APPOINTMENT")
print("4.1 - DOCTORS INFORMATION")
print("4.1.4 - UPDATE EXISTING DOCTOR'S TIMINGS")
print()
dcid=input("ENTER DOCTER ID:")
print()
dcid=dcid.upper()
if dcid in w:
print("ENTER 1 for TIME SLOT 1 UPDATION")
print("ENTER 2 for TIME SLOT 2 UPDATION")
print()
cc=input("ENTER:")
print()
if cc=="1":
t1=input("ENTER NEW TIMINGS - SLOT 1(HH:MM AM/PM - HH:MM AM/PM):")
print()
cursor.execute("update doctordet set time1='"+t1+"' where doc_id='"+dcid+"'")
print("TIMINGS IN SLOT 1 UPDATED SUCCESSFULLY")
db.commit()
print()
elif cc=="2":
t1=input("ENTER NEW TIMINGS - SLOT 2(HH:MM AM/PM - HH:MM AM/PM):")
cursor.execute("update doctordet set time1='"+t1+"' where doc_id='"+dcid+"'")
db.commit()
print()

print("TIMINGS IN SLOT 2 UPDATED SUCCESSFULLY")
print()
else:
print()
else:
print("DOCTOR FOR ENTERED DOCTOR_ID DOES NOT EXIST")
exit()
continue
elif ol=="4.1.5":
print("4 - APPOINTMENT")
print("4.1 - DOCTORS INFORMATION")
print("4.1.5 - UPDATE EXISTING DOCTOR'S PHONE NUMBER")
print()
dcid=input("ENTER DOCTER ID:")
dcid=dcid.upper()
if dcid in w:
lul=input("ENTER NEW NUMBER:")
cursor.execute("update doctordet set phone_no='"+lul+"' where doc_id='"+dcid+"'")
db.commit()
print()
print("PHONE NUMBER UPDATED SUCCESSFULLY")
print()
else:
print("DOCTOR FOR ENTERED DOCTOR_ID DOES NOT EXIST")
exit()
continue
elif ol=="4.2":
print("4 - APPOINTMENT")
print("4.2 - VIEW PATIENT APPOINTMENT BOOKINGS ")
print()
dmd='''SELECT * from patientdet'''
cursor.execute(dmd)
mmm=cursor.fetchall()
m = [("USERNAME","FIRST NAME","LAST NAME","DEPARTMENT","DOCTOR","TIME SLOT")]
m=m+mmm
for i in m:
for j in i:
a=''
a=a+str(j)
while len(a)<28:
a=a+' '
print(a,end='')
print()
exit()
continue
elif ol=="4.3":
print("4 - APPOINTMENT")
print("4.3 - RESET NUMBER OF APPOINTMENTS BOOKED")
print()
dcid=input("ENTER DOCTOR ID:")
dcid=dcid.upper()
if dcid in w:
print("ENTER 1 TO UPDATE THE NUMBER OF APPOINTMENTS IN TIME SLOT 1")
print("ENTER 2 TO UPDATE THE NUMBER OF APPOINTMENTS IN TIME SLOT 2")
cc=input("ENTER:")
if cc=="1":
dd=input("ENTER NUMBER OF PATIENT DOCTOR CAN ATTEND")
cursor.execute("update doctordet set no_t1='"+dd+"' where doc_id='"+dcid+"'")
db.commit()
print()
print("SUCCESSFULLY UPDATED")
elif cc=="2":
dd=input("ENTER NUMBER OF PATIENT DOCTOR CAN ATTEND")
cursor.execute("update doctordet set no_t2='"+dd+"' where doc_id='"+dcid+"'")
print()
print("SUCCESSFULLY UPDATED")
print()

else:
print()
else:
print("DOCTOR FOR ENTERED DOCTOR_ID DOES NOT EXIST")
exit()
continue
elif ol=="5.1":
print("5 - UPDATE PATIENT DETAILS")
print("5.1 - UPDATE PATIENT'S NAME")
iun=input("ENTER USERNAME OF THE PATIENT WHOSE NAME IS TO BE UPDATED")
if iun in b:
fn=input("ENTER NEW FIRST NAME OF PATIENT")
ln=input("ENTER NEW LAST NAME OF PATIENT")
fn,ln=fn.upper(),ln.upper()
cursor.execute("update registration set last_name='"+ln+"' where
username='"+iun+"'")
cursor.execute("update registration set first_name='"+fn+"' where
username='"+iun+"'")
print("SUCCESSFULLY UPDATED")
else:
print("PATIENT WITH ENTERED USERNAME DOES NOT EXIST")
elif ol=="5.2":
print("5 - UPDATE PATIENT DETAILS")
print("5.2 - UPDATE PATIENT'S AGE")
iun=input("ENTER USERNAME OF THE PATIENT WHOSE AGE IS TO BE UPDATED")
if iun in b:
ag=input("ENTER NEW AGE OF PATIENT")
cursor.execute("update registration set AGE='"+ag+"' where username='"+iun+"'")
print("SUCCESSFULLY UPDATED")
else:
print("PATIENT WITH ENTERED USERNAME DOES NOT EXIST")
elif ol=="5.3":
print("5 - UPDATE PATIENT DETAILS")
print("5.3 - UPDATE PATIENT'S PHONE NUMBER")
iun=input("ENTER USERNAME OF THE PATIENT WHOSE PHONE NUMBER IS TO BE UPDATED")
if iun in b:
ag=input("ENTER NEW PHONE NUMBER OF PATIENT")
cursor.execute("update registration set PHONE_NUMBER='"+ag+"' where
username='"+iun+"'")
print("SUCCESSFULLY UPDATED")
else:
print("PATIENT WITH ENTERED USERNAME DOES NOT EXIST")
elif ol=="5.4":
print("5 - UPDATE PATIENT DETAILS")
print("5.4 - RESET PATIENT'S PASSWORD")
iun=input("ENTER USERNAME OF THE PATIENT WHOSE PASSWORD IS TO BE RESET")
if iun in b:
t=UNIQUE_CODE=str(uuid.uuid4().hex[:9].upper())
cursor.execute("update registration set PASSWORD='"+t+"' where
username='"+iun+"'")
print("SUCCESSFULLY UPDATED")
print("NEW PASSWORD = ",t)
else:
print("PATIENT WITH ENTERED USERNAME DOES NOT EXIST")
elif ol=="6.1":
print("6 - UPDATE HOSPITAL DETAILS")
print("6.1 - UPDATE HOSPITAL'S ADDRESS")
lg="ADDRESS : "
df=input("ENTER NEW ADDRESS")
cursor.execute("update hospdet set details='"+df+"' where parameters='"+lg+"' ")
print("SUCCESSFULLY UPDATED")
elif ol=="6.2":
print("6 - UPDATE HOSPITAL DETAILS")
print("6.2 - UPDATE HOSPITAL'S PHONE NUMBER")
lg="PHONE NUMBER : "
df=input("ENTER NEW PHONE NUMBER")
cursor.execute("update hospdet set details='"+df+"' where parameters='"+lg+"' ")

print("SUCCESSFULLY UPDATED")
elif ol=="7":
break
else:
continue
db.commit()
def for_admin():
cursor.execute("create table if not exists blood_units(BLOOD_GROUP varchar(255),UNITS
integer, LAST_UPDATED_ON varchar(255))")
db.commit()
cursor.execute("select*from blood_units")
count = cursor.fetchall()
if len(count)==0:
d=str(datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
rec1=["A+",5,d]
cmd1="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd1,rec1)
rec2=["A-",5,d]
cmd2="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd2,rec2)
rec3=["B+",5,d]
cmd3="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd3,rec3)
rec4=["B-",5,d]
cmd4="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd4,rec4)
rec5=["AB+",5,d]
cmd5="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd5,rec5)
rec6=["AB-",5,d]
cmd6="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd6,rec6)
rec7=["O+",5,d]
cmd7="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd7,rec7)
rec8=["O-",5,d]
cmd8="insert into blood_units values(%s,%s,%s)"
cursor.execute(cmd8,rec8)
db.commit()
cursor.execute("CREATE table if not exists BLOODBANK(U_NAME varchar(255),F_NAME
varchar(255),L_NAME varchar(255), BLOOD_GROUP varchar(255) , DON_or_REQ varchar(255) ,
UNIQUE_CODE varchar(255), DATE varchar(255) , N_REQ integer DEFAULT 0)")
cursor.execute("select*from BLOODBANK")
count =cursor.fetchall()
if len(count)==0:
cursor.execute('''insert into bloodbank
values("CHECK","CHECK","CHECK","CHECK","REQUEST","CHECK","CHECK",0)''')
cursor.execute("create table if not exists hospdet(PARAMETERS varchar(255) , DETAILS
varchar(255))")
cursor.execute("select*from hospdet")
lok=cursor.fetchall()
if len(lok)==0:
cursor.execute('''insert into hospdet values("HOSPITAL NAME : ","POCKET HOSPITAL")''')
cursor.execute('''insert into hospdet values("ADDRESS : ","PRASHANT VIHAR , ROHINI ,
DELHI - 110085")''')
cursor.execute('''insert into hospdet values("PHONE NUMBER : ","8130899991")''')
db.commit()

for_admin()
dis=""
while True:
print("ENTER 1 TO SIGNUP")
print("ENTER 2 TO LOGIN")
print("ENTER 3 TO EXIT")
print("")
print("")
entry=input("ENTER YOUR CHOICE")
cursor.execute("CREATE TABLE if not exists registration (FIRST_NAME varchar(255) NOT
NULL,LAST_NAME varchar(255),AGE varchar(255),GENDER varchar(255),PHONE_NUMBER
varchar(255),USERNAME varchar(255) PRIMARY KEY,PASSWORD varchar(255),DESIG varchar(255))")
if entry=="1":#for signup
while True:
print()
print("ENTER 1 TO SIGNUP AS ADMIN")
print("ENTER 2 TO SIGNUP AS USER")
ec=input("")
if ec=="1":
org_code="admin@123"
o_c=input("ENTER ORGANISATION CODE PROVIDED:")
if o_c==org_code:
DESIG="ADMIN"
print("VERYFYING ORGANISATION CODE")
print(".")
print(".")
print(".")
print("ORGANIZATION CODE VERIFIED")
print("PROCEED TO SIGN UP")
else:
print("VERYFYING ORGANISATION CODE")
print(".")
print(".")
print(".")
print("WRONG ORGANISATION CODE")
continue
elif ec=="2":
DESIG="USER"
else:
print()
print("ENTER A VALID INPUT")
print()
continue
print("")
FIRST_NAME=input("ENTER YOUR FIRST NAME:")
print("")
LAST_NAME=input("ENTER YOUR LAST NAME:")
print()
AGE=input("ENTER AGE:")
print("")
GENDER=input("ENTER YOUR GENDER:")
print("")
PHONE_NUMBER=input("ENTER MOBILE NUMBER:")
print("")
USERNAME=input("ENTER UNIQUE USERNAME:")
print("")
PASSWORD=input("ENTER A STRONG PASSWORD:")
print("")
s="insert into registration
values('"+FIRST_NAME+"','"+LAST_NAME+"','"+AGE+"','"+GENDER+"','"+PHONE_NUMBER+"','"+
USERNAME+"','"+PASSWORD+"','"+DESIG+"')"
cursor.execute(s)
db.commit()
print("LOGIN USING THE USERNAME AND PASSWORD BY ENTERING 2")

break
elif entry=="2":#for login
cursor.execute("drop table if exists entryvalues")
cursor.execute("drop table if exists admin")
h='''create table if not exists entryvalues as(SELECT USERNAME,PASSWORD from
registration where DESIG="USER" )'''#table for login
cursor.execute(h)
t='''create table if not exists admin as(SELECT USERNAME,PASSWORD from registration
where DESIG="ADMIN")'''
cursor.execute(t)
while True:
print()
print("USERNAME AND PASSWORD IS CASE SENSITIVE")
print()
print("ENTER 1 TO LOGIN AS AN ADMIN")
print("ENTER 2 TO LOGIN AS AN USER")
ec=input("")
if ec=="1":
u_name=input("ENTER USERNAME:")
print("")
passwdd=input("ENTER PASSWORD:")
M=u_name,passwdd
T=tuple(M)
print()
cursor.execute("select*from admin")
data=cursor.fetchall()
L=[]
for i in data:
L.append(i)
F=False
for j in range(len(L)):
if L[j]==T:
F=True
if F==False:
print("")
print("WRONG LOGIN/PASSWORD")
elif F==True:
print("")
print("SUCCESFUL LOGIN")
print()
op="select FIRST_NAME,LAST_NAME from registration where USERNAME=%s"
un=(u_name,)
cursor.execute(op, un)
result = cursor.fetchall()
for x in result:
gb,kk=x[0],x[1]
cursor.execute('''select details FROM hospdet where PARAMETERS="HOSPITAL
NAME : "''')
lm=cursor.fetchall()
print()
print("**********************************************************************
********************************************************************")
print()
print("
",lm[0][0],"
")
print()
print("**********************************************************************
********************************************************************")
dmd='''select parameters,details from hospdet where details<>"POCKET
HOSPITAL"'''
print()

cursor.execute(dmd)
mmm=cursor.fetchall()
for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
print()
print("**********************************************************************
********************************************************************")
print()
print("WELCOME",x[0],x[1])
print()
admin_menu()
break
elif ec=="2":#foruser
u_name=input("ENTER USERNAME:")
print("")
passwdd=input("ENTER PASSWORD:")
print("")
M=u_name,passwdd
T=tuple(M)
cursor.execute("select*from entryvalues")
data=cursor.fetchall()
L=[]
for i in data:
L.append(i)
F=False
for j in range(len(L)):
if L[j]==T:
F=True
if F==False:
print("")
print("WRONG LOGIN/PASSWORD")
elif F==True:
print("")
print("SUCCESFUL LOGIN")
op="select FIRST_NAME,LAST_NAME from registration where USERNAME=%s"
un=(u_name,)
cursor.execute(op, un)
result = cursor.fetchall()
for x in result:
gb,kk=x[0],x[1]
while True:
cursor.execute('''select details FROM hospdet where
PARAMETERS="HOSPITAL NAME : "''')
lm=cursor.fetchall()
print()
print("**************************************************************
*********************************************************************
*******")
print()
print("
",lm[0][0],"
")
print()
print("**************************************************************
*********************************************************************
*******")
print()
dmd='''select parameters,details from hospdet where

details<>"POCKET HOSPITAL"'''
print()
cursor.execute(dmd)
mmm=cursor.fetchall()
for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
print()
print("**************************************************************
*********************************************************************
*******")
print()
print("WELCOME",x[0],x[1])
print()
print()
print("1)COVID-19 TEST")
print("")
print("2)DISEASE DETECTOR")
print()
print("3)HOME REMEDIES")
print()
print("4)BLOOD BANK")
print()
print("5)BOOK AN APPOINTMENT")
print()
print("6)LOGOUT")
print()
c=input("ENTER CHOICE")
if c=="1":
print()
print("**********************************************************
*****************************************************************
***************")
print()
print("
COVID-19 TEST ")
print()
print("**********************************************************
*****************************************************************
***************")
print()
print("This program is not meant to take the place of
consultation with your health care provider or to ",end="")
print("diagnose or to treat any conditions."+"\n"+"If you're in
an emergency medical situation, call 011-22307145 (Delhi,
India) or your local emergency number.")
cursor.execute("create table if not exists COVIDSTATUS(USERNAME
varchar(255), STATUS varchar(255) )")
def call(b):
cursor.execute("select QUES from COVID where
SNO='"+b+"'")
az1 = cursor.fetchone()
for i in az1:
print(i)

def COVID(b):
cursor.execute("select QUES from COVIDQ where
SNO='"+str(b)+"'")

az1 = cursor.fetchone()
for i in az1:
print(i)
while True:
ac1 = input("Enter Your Choice(YES/NO)")
ac2 = ac1.upper()
if ac2=="YES" or ac2=="NO":
cursor.execute("update COVIDQ set
YN='"+ac2+"' where SNO='"+str(b)+"'")
break
else:
print()
print("PLEASE ENTER A VALID CHOICE")
print()
continue

print()
while True:
call("1")
ab1 = input("Enter Your Choice(YES/NO)")
ab2 = ab1.upper()
if ab2=="YES" or ab2=="NO":
break
else:
print()
print("PLEASE ENTER A VALID CHOICE")
print()
continue

cursor.execute("select count(*) from COVIDQ")
m1 = cursor.fetchone()
n=int(m1[0])
while True:
if ab2=="YES":
for i in range(1,n+1):
print()
COVID(i)
print()
cursor.execute("select YN,count(*) from COVIDQ
where YN='YES'")
az = cursor.fetchall()
for i in az:
if i[1]>=4:
cr="POSITIVE"
call("2")
elif i[1]==3:
cr="PRONE"
call("3")
elif i[1]<=2:
cr="NEGATIVE"
call("4")
cursor.execute('''SELECT USERNAME from
COVIDSTATUS''')
jk=[]
for j in cursor:
jk.append(j[0])
if u_name in jk:
cursor.execute("UPDATE COVIDSTATUS SET
STATUS='"+cr+"'where USERNAME='"+u_name+"' ")
db.commit()
else:
cursor.execute("insert into COVIDSTATUS
values('"+u_name+"','"+cr+"')")
db.commit()
print()
call("5")
call("6")

while True:
az3 = input("Enter Your Choice")
if az3=="1" or az3=="2":
break
else:
print()
print("PLEASE ENTER A VALID CHOICE")
print()
continue

if az3=="1":
break
elif az3=="2":
continue
elif ab2=="NO":
print()
call("7")
print()
print("EXIITING TO MAIN MENU")
print()
break

continue
db.commit()
elif c=="2":
print()
print("**********************************************************
*****************************************************************
***************")
print()
print("
DISEASE
DETECTOR
")
print()
print("**********************************************************
*****************************************************************
***************")
print()
f=open("disease.txt","r")
z=open("diseaseonlyread.txt","r")
print(z.read())
f.seek(0,0)
l1= f.read().splitlines()
print()
ch1= input("Enter the serial no. of the symptoms you are
suffering:")
choice= ch1.split( )
dict1 = {1:'Cataract', 2:'Night blindness,Cataract',
3:'Cataract,Common Cold', 4:'High Blood Pressure',
5:'Diabetes,Cataract', 6:'Sinnitus,COVID-19',
7:'Sinnitus', 8:'Sinnitus', 9:'Common Cold',
10:'Common Cold', 11:'Common Cold',
12:'Epiglottis,Asthma',
13:'Asthma,Bronchitis,Pneumonia,Heart Attack,High
Blood Pressure',
14:'Pneumonia', 15:'High Blood Pressure',
16:'Typhoid', 17:'COVID-19',
18:'Influenza,Bronchitis,Typhoid,COVID-19',
19:'Tonsillitis,COVID-19',20:'Tonsillitis',21:'Tonsillit
is',22:'Epiglottis',23:'Epigottis',24:'Asthma',25:'Bronc
hitis',
26:'Influenza,Epiglottis,Bronchitis,Pneumonia,Malaria,Ja
undice,COVID-19', 27:'Influenza,Typhoid,High Blood

Pressure,COVID-19', 28:'Sinnitus',
29:'Bronchitis,Heart Attack,Typhoid,Malaria,COVID-19',
30:'Flu,Pneumonia,Heart Attack,Malaria,Gastric,Kidney
Stone', 31:'Flu,Pneumonia,Malaria,COVID-19',
32:'Bronchitis,Pneumonia,Malaria', 33:'Pneumonia,Heart
Attack,Malaria,Gastric,Kidney Stone', 34:'Heart
Attack,Kidney Stone',35:'Malaria',
36:'High Blood Pressure', 37:'Diabetes',
38:'Diabetes', 39:'Diabetes', 40:'Typhoid',
41:'COVID-19', 42:'Asthma,High Blood Pressure,COVID-19',
43:'Bronchitis', 44:'Pneumonia', 45:'Heart Attack',
46:'Heart Attack', 47:'Malaria', 48:'Heart
Attack,Gastric', 49:'Heart
Attack,Malaria,Jaundice,Gastric',
50:'Typhoid', 51:'Gastric', 52:'Typhoid',
53:'Typhoid,Gastric', 54:'Kidney Stone', 55:'Typhoid',
56:'Gastric', 57:'Gastric',
58:'Diabetes', 59:' ', 60:'Jaundice', 61:'Typhoid',
62:'COVID-19', 63:'High Blood Pressure',
64:'Diabetes', 65:'Jaundice', 66:'Kidney Stone'}

disease = [ ]
find= [ ]
for i in choice:
a= int(i)
sym= l1[a-1]
find.append(sym)
disease.append(dict1[a])
dis_total = [ ]
for i in disease:
lis = i.split(",")
dis_total += lis
dis_count = Counter(dis_total)
max_symptoms = 1
fin_dis = 'aaa'
for i,j in dis_count.items():
if j >= max_symptoms:
max_symptoms = j
fin_dis = i
print()
print("You have symptoms of:", fin_dis)
print()
dis=fin_dis
while True:
print("ENTER 1 TO EXIT TO MAIN MENU")
nnn=input()
if nnn=="1":
break
else:
print("INVALID CHOICE")
continue
continue
if c=="3":
print()
a1 = dis.upper()
print("**********************************************************
*****************************************************************
***************")
print()
print("

HOME
REMEDIES ")
print()
print("**********************************************************
*****************************************************************
***************")
print()
print(" THIS PROGRAM SHOWS
THE HOME REMEDIES FOR THE DISEASE YOU CONCLUDED IN DISEASE
DETECTOR")
print()
print("**********************************************************
*****************************************************************
***************")
print()
if a1=="":
print("PLEASE GO TO DISEASE DETECTOR FIRST")
else:
print("HOME REMEDIES/PREVENTION OF",a1,"ARE:")
print()
cursor.execute("select homeremedies from remedies where
disease='"+a1+"'")
for i in cursor:
print(i[0])
db.commit()
continue
if c=="4":
while True:
print()
print("******************************************************
*************************************************************
***********************")
print()
print("
BLOOD
BANK ")
print()
print("******************************************************
*************************************************************
***********************")
print()
print("Regular blood donations by a sufficient number of
healthy people are needed to ensure that safe blood\nwill
be available whenever and wherever it is needed. Blood is
the most precious gift that anyone can\ngive to another
person — the gift of life.")
print()
print("ENTER 1 TO DONATE BLOOD")
print("ENTER 2 TO REQUEST FOR BLOOD")
print("ENTER 3 TO EXIT")
nzm=input("ENTER CHOICE:")
if nzm=="1":
choice=input("ENTER BLOOD GROUP:")
choice=choice.upper()
if choice=="A+":
BLOOD_GROUP=choice
elif choice=="A-":
BLOOD_GROUP=choice
elif choice=="B+":
BLOOD_GROUP=choice
elif choice=="B-":

BLOOD_GROUP=choice
elif choice=="O+":
BLOOD_GROUP=choice
elif choice=="O-":
BLOOD_GROUP=choice
elif choice=="AB+":
BLOOD_GROUP=choice
elif choice=="AB-":
BLOOD_GROUP=choice
else:
print("INVALID INPUT")
print()
print()
dr="DONATE"
UNIQUE_CODE=str(uuid.uuid4().hex[:6].upper())
d=str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
H="UPDATE BLOOD_UNITS SET UNITS=UNITS+1 where
BLOOD_GROUP='"+choice+"'"
cursor.execute(H)
p="insert into
bloodbank(U_NAME,F_NAME,L_NAME,BLOOD_GROUP,DON_or_REQ,UNI
QUE_CODE,DATE)values(%s,%s,%s,%s,%s,%s,%s)"
q=(u_name,gb,kk,choice,dr,UNIQUE_CODE,d)
cursor.execute(p,q)
db.commit()
print()
print("YOU CAN DONATE THE BLOOD AT THIS LOCATION")
print()
dmd='''SELECT * from hospdet'''
cursor.execute(dmd)
mmm=cursor.fetchall()
for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
continue
elif nzm=="2":
choice=input("ENTER BLOOD GROUP REQUIRED:")
choice=choice.upper()
if choice=="A+":
BLOOD_GROUP=choice
elif choice=="A-":
BLOOD_GROUP=choice
elif choice=="B+":
BLOOD_GROUP=choice
elif choice=="B-":
BLOOD_GROUP=choice
elif choice=="O+":
BLOOD_GROUP=choice
elif choice=="O-":
BLOOD_GROUP=choice
elif choice=="AB+":
BLOOD_GROUP=choice
elif choice=="AB-":
BLOOD_GROUP=choice
else:
print("INVALID INPUT")
print()
dr="REQUEST"
jko=[u_name]
UNIQUE_CODE=str(uuid.uuid4().hex[:6].upper())
d=str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
m="select*from bloodbank where DON_or_REQ='"+dr+"'"

cursor.execute(m)
result=cursor.fetchall()
cursor.execute("SELECT U_NAME from bloodbank where
DON_or_REQ='"+dr+"'")
b=[]
for j in cursor:
b.append(j[0])
for i in range(len(result)):
if u_name==result[i][0]:
x=result[i]
break
cursor.execute("SELECT UNITS from BLOOD_UNITS where
BLOOD_GROUP='"+choice+"'")
oiu=cursor.fetchone()
if oiu[0]>1:
if u_name in b:
if (x[7]==0 or x[7]==1):
yu=x[3]+"," +choice
f=[yu,u_name]
p='''update bloodbank SET BLOOD_GROUP=%s
where U_NAME=%s and DON_or_REQ="REQUEST" '''
cursor.execute(p,f)
pop='''update bloodbank SET N_REQ=N_REQ+1
where U_NAME=%s and DON_or_REQ="REQUEST" '''
print()
print("YOU CAN COLLECT THE BLOOD FROM THIS
LOCATION")
print()
dmd='''SELECT * from hospdet'''
cursor.execute(dmd)
mmm=cursor.fetchall()
for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
cursor.execute(pop,jko)
db.commit()
else:
print("ALREADY REQUESTED TWICE")
else:
w="insert into
bloodbank(U_NAME,F_NAME,L_NAME,BLOOD_GROUP,DON_or
_REQ,UNIQUE_CODE,DATE)values(%s,%s,%s,%s,%s,%s,%s
)"
f=[u_name]
g=(u_name,gb,kk,choice,dr,UNIQUE_CODE,d)
cursor.execute(w,g)
H="UPDATE BLOOD_UNITS SET UNITS=UNITS-1 where
BLOOD_GROUP='"+choice+"'"
cursor.execute(H)
iu='''UPDATE BLOODBANK SET N_REQ=N_REQ+1 where
U_NAME=%s and DON_or_REQ="REQUEST"'''
cursor.execute(iu,f)
print()
print("YOU CAN COLLECT THE BLOOD FROM THIS
LOCATION")
print()
dmd='''SELECT * from hospdet'''
cursor.execute(dmd)
mmm=cursor.fetchall()

for i in mmm:
for j in i:
a=''
a=a+str(j)
while len(a)<17:
a=a+' '
print(a,end='')
print()
db.commit()
else:
print("BLOOD NOT AVAILABLE")
continue
db.commit()
elif nzm=="3":
break
continue
elif c=="5":
print()
print("**********************************************************
*****************************************************************
***************")
print()
print("
BOOK AN
APPOINMENT ")
print()
print("**********************************************************
*****************************************************************
***************")
print()
def rem1():
cursor.execute("select distinct dept from doctordet")
mg=cursor.fetchall()
k=1
for i in mg:
print(k,i[0])
k=k+1
while True:
rem1()
print()
a10=input("ENTER DEPARTMENT NUMBER")
cursor.execute("select distinct dept from doctordet")
opo=len(cursor.fetchall())
if int(a10) in range(opo+1):
cursor.execute("select dept from doctordet where
sno='"+a10+"'")
hm=cursor.fetchall()
for i in hm:
lo=i[0]#dept
cursor.execute("select doctor_name,dept from doctordet
where sno='"+a10+"'")
ab = cursor.fetchall()
cursor.execute("select doctor_name,time1,time2 from
doctordet where sno='"+a10+"'")
a11 = cursor.fetchall()
l = ["SNO. ","DOCTOR NAME \t \t"," TIMESLOT1
\t\t"," TIMESLOT2 \t\t"]
print()
for i in l:
print(i,end='')
print()
count=1
for i in a11:

print(str(count)+' ',end='')
count+=1
for j in i:
a=''
a=a+str(j)
while len(a)<27:
a=a+' '
print(a,end='')
print()
print()
else:
print()
print("### PLEASE ENTER A VALID DEPARTMENT NUMBER ###")
print()
continue
while True:
a12=int(input("ENTER DOCTOR SERIAL NUMBER"))
cursor.execute("select doctor_name from doctordet where
dept='"+ab[0][1]+"'")
t=cursor.fetchall()
if a12 in range(len(t)+1):
cursor.execute("select time1,time2 from doctordet
where doctor_name ='"+ab[a12-1][0]+"'")
a13 = cursor.fetchall()
l = [("TIMESLOT 1","TIMESLOT 2")]
l=l+a13
print()
for i in l:
for j in i:
a=''
a=a+str(j)
while len(a)<27:
a=a+' '
print(a,end='')
print()
break
else:
print()
print("### ENTER CORRECT DOCTOR SERIAL NUMBER ###")
print()
continue
while True:
cursor.execute("select no_t1,no_t2 from doctordet where
doctor_name='"+ab[a12-1][0]+"'")
abb=cursor.fetchall()
if abb[0][0] or abb[0][1]!=0:
print()
a14=input("ENTER TIMESLOT NUMBER")
print()
if a14=='1':
cursor.execute("select No_T1 from doctordet
where doctor_name='"+ab[a12-1][0]+"'")
a15 = cursor.fetchone()
if int(a15[0])>0:
cursor.execute("select time1 from doctordet
where doctor_name='"+ab[a12-1][0]+"'")
abb=cursor.fetchone()
cursor.execute("UPDATE doctordet SET No_T1
= No_T1-1 where
doctor_name='"+ab[a12-1][0]+"'")
cursor.execute("insert into patientdet
values('"+u_name+"','"+gb+"','"+kk+"','"+lo+"
','"+ab[a12-1][0]+"','"+abb[0]+"')")
F = datetime.now()+timedelta(1)
print("YOUR APPOINTMENT WITH THE DOCTOR IS
TOMORROW i.e:",F.strftime('%d-%m-%Y'))
db.commit()

break
else:
print("THIS TIME SLOT IS NOT
AVAILABE,PLEASE SELECT ANOTHER TIME SLOT")
continue
elif a14=='2':
cursor.execute("select No_T2 from doctordet
where doctor_name='"+ab[a12-1][0]+"'")
a15 = cursor.fetchone()
if int(a15[0])>0:
cursor.execute("select time2 from doctordet
where doctor_name='"+ab[a12-1][0]+"'")
abb=cursor.fetchone()
cursor.execute("UPDATE doctordet SET No_T2
= No_T2-1 where
doctor_name='"+ab[a12-1][0]+"'")
cursor.execute("insert into patientdet
values('"+u_name+"','"+gb+"','"+kk+"','"+lo+"
','"+ab[a12-1][0]+"','"+abb[0]+"')")
F = datetime.now()+timedelta(1)
print("YOUR APPOINTMENT WITH THE DOCTOR IS
TOMORROW i.e:",F.strftime('%d-%m-%Y'))
db.commit()
break
else:
print("THIS TIME SLOT IS NOT
AVAILABE,PLEASE SELECT ANOTHER TIME SLOT")
continue
else:
print("### PLEASE ENTER A VALID NUMBER ###")
continue
else:
print()
print("BOTH THE TIME SLOTS ARE ALREADY BOOKED FOR
TOMORROW")
print()
break
while True:
abbbbb = input("DO YOU WANT TO BOOK MORE
APPOINTMENTS?(Y/N)")
abbbbb=abbbbb.upper()
if abbbbb=="Y" or abbbbb=="N":
break
else:
print()
print("### PLEASE ENTER A VALID CHOICE ###")
continue
if abbbbb=="N":
break
db.commit()
elif c=="6":
print()
print("LOGGING OUT")
print(".")
print(".")
print(".")
break
if c=="6":
break
if c=="6":
break
break
elif entry=="3":
print()
print("ABORTING")
print(".")
print(".")

print(".")
break
else:
print()
print("ENTER A VALID INPUT")
print()
continue
db.commit()