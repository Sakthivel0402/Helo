#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os,smtplib
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
query2="""select max(id) from empReg"""
cur.execute(query2)
employer=cur.fetchone()

if employer[0]!=None:
    if employer[0]<10:
        empnum="HELO000"+str(employer[0]+1)
    elif employer[0]<100:
        empnum = "HELO00" + str(employer[0]+1)
    elif employer[0]<1000:
        empnum = "HELO0" + str(employer[0]+1)
else:
    empnum="HELO0001"

import random

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
    }}
    </style>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1>Employee Registration</h1></div>
<a href="./AdminLogin.py" class="btn btn-danger h-25  me-5 float-end">Logout</a>   
    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                  
                <li class="nav-item ">
                  <a class="nav-link " href="./AdminDashboard.py">
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Employee
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./EmpReg.py">Create</a></li>
                            <li><a class="dropdown-item" href="./OldEmployee.py">Old Employee </a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Wholesalers
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./whRequests.py">Requests</a></li>
                            <li><a class="dropdown-item" href="./whOld.py">Old Wholesalers</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Company
                      </a>
                      <ul class="dropdown-menu">
                          <li><a class="dropdown-item" href="./companyRequests.py">Requests</a></li>
                          <li><a class="dropdown-item" href="./companyOld.py">Old Company's</a></li>
                      </ul>
                  </li>
                  <li class="nav-item ">
                    <a class="nav-link" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Products
                    </a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./adminNeworders.py">Ongoing orders</a></li>
                      <li><a class="dropdown-item" href="./adminCompleted.py">Old orders</a></li>
                      <li><a class="dropdown-item" href="./adminCancelled.py">Cancelled orders</a></li>

                  </ul>
              </li>
              <li class="nav-item ">
                <a class="nav-link " href="./userDetails.py">
                    User details
                </a>
            </li>
                    </ul>
            </div>

            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-5 border ">
              <h3>Personal</h3>
              <form method="post" enctype="multipart/form-data">
                <div class="row">
                  <div class="col-md-4"><input type="text" name="fname" class="form-control" placeholder="Firstname" id=""></div>
                  <div class="col-md-4"><input type="text" name="lname" class="form-control" placeholder="Lastname" id=""></div>
                  <div class="col-md-1 "><label for="">DOB</label></div>
                  <div class="col-md-3 "><input type="date" name="dob" class="form-control" placeholder="Lastname" id=""></div>
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

             <h3>Address</h3>
              <div class="row mt-4">
                <div class="col-md-4"><input type="text" name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><input type="text" name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><select class="form-select" name=city aria-label="Default select example">
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
                  <option value="Tamilnadu">Tamilnadu</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Andrapradhesh">Andrapradhesh</option>
                </select></div>
                <div class="col-md-4"><input type="text" name="country" class="form-control" placeholder="Country" id=""></div>
              </div>
    
              <h3>Education</h3>
               <div class="row"><div class="col-md-3 mt-4"><select name="edu" class="form-select" aria-label="Default select example">
                <option selected>Education</option>
                <option value="B.E">B.E</option>
                <option value="B.Sc">B.Sc</option>
                <option value="B.Tech">B.Tech</option>
              </select></div>
              <div class="mb-3 col-md-3">
                <label for="formFile" class="form-label mb-1">Degree completion certificate</label>
                <input class="form-control" type="file" name="deg" id="formFile">
              </div>
              <div class="col-md-3"><label for="">Employee ID</label><input class="form-control" value="{empnum}" disabled placeholder="Ex: 001" name="eid">
              </div>
              <div class="col-md-3">
                <select name="department" class="form-select mt-4" aria-label="Default select example">
                  <option  selected>Department</option>
                  <option  value="Service">Service</option>
                  <option value="Delivery">Delivery</option>
                </select>
              </div>
            </div>    
            <div class="row mt-3">
              <div class="col-md-4">
                <label for="formFile" class="form-label mb-1">Profile picture</label>
                <input class="form-control" name="profile" type="file" id="formFile">
              </div>
              <div class="col-md-4">
                <label for="formFile" class="form-label mb-1">Aadhar proof</label>
                <input class="form-control" name="aad" type="file" id="formFile">
              </div>
              <div class="col-md-4">
                <label for="formFile" class="form-label mb-1">PAN proof</label>
                <input class="form-control" name="pan" type="file" id="formFile">
              </div>
              </div>
              <div class="d-flex justify-content-center mt-5 ">
              <div class="btn btn-danger me-5 ">Back</div>
              <input class="btn btn-primary" type="submit" name="submit">
            </div>
            </form>
            </div>  
            </div>
            </div>
  </body>
</html>
""")


submit= store.getvalue("submit")
if submit!=None:
    if len(store)!=0:
        Eid = store.getvalue("eid")
        fname = store.getvalue("fname")
        lname = store.getvalue("lname")
        dob = store.getvalue("dob")
        gender = store.getvalue("gender")
        mail = store.getvalue("email")
        r = random.randint(1000, 9999)
        slymail=mail[0:4]
        password=slymail+str(r)
        fromadd = 'sakthivelsubash0402@gmail.com'
        password2 = 'wmob kavj zalb mxoj'
        toadd = mail
        subject = """Regarding content"""
        body = f" your employer ID is: {empnum}\n and password:{password}"
        msg = f"""Subject: {subject}\n\n{body}"""
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromadd, password2)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        phone = store.getvalue("phone")
        add1 = store.getvalue("address1")
        add2 = store.getvalue("address2")
        city = store.getvalue("city")
        zip = store.getvalue("zipcode")
        state = store.getvalue("state")
        country = store.getvalue("country")
        education = store.getvalue("edu")
        department=store.getvalue("department")
        deg = store['deg']
        profile = store['profile']
        aad=store['aad']
        pan=store['pan']
        if profile.filename and aad.filename and pan.filename and deg.filename:
            proof1 = os.path.basename(profile.filename)
            open("Assets/images" + proof1,"wb").write(profile.file.read())
            proof2 = os.path.basename(aad.filename)
            open("Assets/images" + proof2, "wb").write(aad.file.read())
            proof3 = os.path.basename(pan.filename)
            open("Assets/images" + proof3, "wb").write(pan.file.read())
            proof4 = os.path.basename(deg.filename)
            open("Assets/images" + proof4, "wb").write(deg.file.read())
            emailquery = """select mail from empreg"""
            cur.execute(emailquery)
            emailloop = cur.fetchall()
            c = 0
            for i in emailloop:
                if i[0] == mail:
                    c += 1
            if c > 0:
                print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
            else:
                query=f""" insert into empreg (fname,lname,dob,gender,mail,phone,address1,address2,city,zipcode,state,country,education,degreeCertificate,empid,profilePicture,aadhar,pan,password,designation) values ('{fname}','{lname}','{dob}','{gender}','{mail}','{phone}','{add1}','{add2}', '{city}', '{zip}', '{state}','{country}', '{education}','{proof4}','{empnum}','{proof1}','{proof2}','{proof3}','{password}','{department}')"""
                cur.execute(query)
                con.commit()
                print("""
            <script>
            alert("submitted!");
            </script>""")








