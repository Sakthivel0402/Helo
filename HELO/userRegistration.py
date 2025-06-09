#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user registration</title>
    <link rel="stylesheet" href="boxicons.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<style>
   @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cedarville+Cursive&family=Edu+AU+VIC+WA+NT+Hand:wght@400..700&family=Pacifico&family=Playwrite+CU:wght@100..400&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'); 
  
 
*{
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
    font-weight: 400 !important;
}

.navbar-brand{
    font-family: "Playwrite CU", cursive;
    font-size: 1.7rem !important;
    font-weight: 900 !important;
    color: black;
    animation: color-change 20s  infinite;
}

@keyframes color-change {
  0% { color: yellow; }
  10% { color: blue; }
  20% { color: rgb(179, 104, 104); }
  30% { color: rgb(27, 222, 82); }
  40% { color: rgb(183, 235, 28); }
  50% { color: rgb(250, 93, 174); }
  60% { color: rgb(6, 165, 209); }
  70% { color: rgb(59, 32, 193); }
  80% { color: rgb(179, 104, 104); }
  90% { color: rgb(132, 8, 255); }
  100% { color: rgb(255, 255, 0); }
}

form{
        display: block;
    }   
</style>

<body>
    <nav class="navbar navbar-expand-md bg-light">
        <div class="container"><a href="./index.py" class="navbar-brand">Helo</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            </div>
     </nav>
     <form action="" class=" mt-3 rounded" method="post">
     <div class="container p-4 " style="background-color: aliceblue;">
        <h1 class="d-flex justify-content-center mb-5">User Registration</h1>
        <div class="row">
            <div class="col-md-4"><input type="text" name="fname" class="form-control" placeholder="Firstname" id=""></div>
            <div class="col-md-4"><input type="text" name="lname" class="form-control" placeholder="Lastname" id=""></div>
            <div class="col-md-1 "><label for="">DOB</label></div>
            <div class="col-md-3 "><input type="date" name="dob" class="form-control" id=""></div>
          </div>
          <div class="row mt-5 mb-5">
            <div class="col-md-4"><select name="gender"  class="form-select" aria-label="Default select example">
             <option selected>Gender</option>
             <option value="male">Male</option>
             <option value="female">Female</option>
           </select></div>
          <div class="col-md-4"><input type="text" name="email" class="form-control" placeholder="Email" id=""></div>
          <div class="col-md-4"><input type="text" name="phone" class="form-control" placeholder="Phone" id=""></div>
        </div>
        <div class="row mt-4">
            <div class="col-md-4"><input type="text" name="address1" class="form-control" placeholder="Address line1" id=""></div>
            <div class="col-md-4"><input type="text" name="address2" class="form-control" placeholder="Address line2" id=""></div>
            <div class="col-md-4"><select class="form-select" name="city" aria-label="Default select example">
              <option selected>City</option>
              <option value="Chennai">Chennai</option>
              <option value="Coimbatore">Coimbatore</option>
              <option value="Erode">Erode</option>
            </select></div>
          </div>
          <div class="row mt-3 mb-5 ">
            <div class="col-md-4"><input type="text" name="zipcode" class="form-control" placeholder="Zipcode" id=""></div>
            <div class="col-md-4"><select name="state"  class="form-select" aria-label="Default select example">
              <option selected>State</option>
              <option value="1">Tamilnadu</option>
              <option value="2">Kerala</option>
              <option value="3">Andrapradhesh</option>
            </select></div>
            <div class="col-md-4"><input type="text" name="country" class="form-control" placeholder="Country" id=""></div>
          </div>
          <div class="row">
            <h5 class="col-md-2">Create username:</h5> <div class="col-md-4"><input class="form-control" type="text" name="username" id=""></div>
          </div>
          <div class="row">
            <h5 class="col-md-2 mt-3">Create password:</h5> <div class="col-md-4"><input class="form-control mt-3" type="password" name="password" id=""></div>
          </div>
          <div class="d-flex justify-content-center mt-5 ">
            <a class="btn btn-danger me-5 " href="./index.py">Cancel</a>
            <input type="submit" class="btn btn-primary" value="Register" name="submit" >
          </div>
          <a href="./userLogin.py" class="me-5" style="text-decoration: none;">Already have an account?(Login)</a>
    </div>
     </div>
    </form>
""")

submit= store.getvalue("submit")
if submit!=None:
        fname = store.getvalue("fname")
        lname = store.getvalue("lname")
        dob = store.getvalue("dob")
        gender = store.getvalue("gender")
        mail = store.getvalue("email")
        phone = store.getvalue("phone")
        add1 = store.getvalue("address1")
        add2 = store.getvalue("address2")
        city = store.getvalue("city")
        zip = store.getvalue("zipcode")
        state = store.getvalue("state")
        country = store.getvalue("country")
        username=store.getvalue("username")
        password=store.getvalue("password")
        emailquery = """select email from userregistration"""
        cur.execute(emailquery)
        emailloop = cur.fetchall()
        c = 0
        for i in emailloop:
                if i[0] == mail:
                        c += 1
        if c > 0:
                print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
        else:
                query2 = f""" insert into userregistration (firstname,lastname,dob,gender,email,phone,address1,address2,city,zipcode,state,country,username,password)  values ('{fname}','{lname}','{dob}','{gender}','{mail}','{phone}','{add1}','{add2}', '{city}', '{zip}', '{state}','{country}','{username}','{password}')"""
                cur.execute(query2)
                con.commit()
                print(""" <script>
                    alert("submitted!");
                    </script>""")

