#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
# employer=(999,)
#
#
# if employer[0]!=None:
#     if employer[0]<10:
#         empnum="HELO000"+str(employer[0]+1)
#     elif employer[0]<100:
#         empnum = "HELO00" + str(employer[0]+1)
#     elif employer[0]<1000:
#         empnum = "HELO0" + str(employer[0]+1)
# else:
#     empnum="HELO0001"

# print("""
# <form method="post" enctype="multipart/form-data">
# <input type="file" name="img">
# <input type="submit" name="sub">
# </form>
# """)
# proof1 = os.path.basename("C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe")
# a=open("proofs/" + proof1,"w")
# a.write("zexfcg")


import random

# Generate a random number between 1 and 100
r = random.randint(100000, 999999)
import string

# Define the length of the random string
length = 10

# Generate a random string of lowercase letters
random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


print(random_string)

