#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
empid=store.getvalue("id")
query2=f""" select * from empreg where id='{empid}'"""
cur.execute(query2)
empdetails=cur.fetchall()


print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit employee details</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1>Edit employee details </h1></div>
<a href="./AdminLogin.py" class="btn btn-danger h-25  me-5 float-end">Logout</a>   
    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                  <li class="nav-item ">
                    <a class="nav-link " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Greet
                    </a>
                </li>
                <li class="nav-item ">
                  <a class="nav-link " href="./adminDashboard.html" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Employee
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./empReg.html">Create</a></li>
                            <li><a class="dropdown-item" href="./oldEmployee.html">Old Employee </a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Wholesalers
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./whRequests.py">Requests</a></li>
                            <li><a class="dropdown-item" href="./WhOld.py">Old Wholesalers</a></li>
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
                      <li><a class="dropdown-item" href="#">Ongoing orders</a></li>
                      <li><a class="dropdown-item" href="#">Old orders</a></li>
                      <li><a class="dropdown-item" href="#">Cancelled orders</a></li>

                  </ul>
              </li>
              <li class="nav-item ">
        <a class="nav-link " href="./userDetails.py">  
                  User details
                </a>
            </li>
                    </ul>
            </div>""")
for i in empdetails:
    print(f"""
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-5 border ">
              <h3>Personal</h3>
              <form method="post" enctype="multipart/form-data">
                <div class="row">
                  <div class="col-md-4"><label for="">First name</label><input type="text" name="fname" value="{i[1]}" class="form-control" placeholder="Firstname" id=""></div>
                  <div class="col-md-4"><label for="">Last name</label><input type="text" name="lname"  value="{i[2]}" class="form-control" placeholder="Lastname" id=""></div>
                  <div class="col-md-4 "><label for="">DOB</label><input type="date"  value="{i[3]}"  name="dob" class="form-control" placeholder="" id=""></div>
                </div>
                <div class="row mt-5 mb-5">
                 <div class="col-md-4"><label for="">Gender</label><input name="gender" class="form-control"  value="{i[4]}" type="text" >
                  </div>
                <div class="col-md-4"><label for="">Email</label><input type="text"  value="{i[5]}"  name="email" class="form-control" placeholder="Email" id=""></div>
                <div class="col-md-4"><label for="">Phone</label><input type="text" value="{i[6]}"  name="phone" class="form-control" placeholder="Phone" id=""></div>
              </div>

             <h3>Address</h3>
              <div class="row mt-4">
                <div class="col-md-4"><label for="">Address line1</label><input type="text" value="{i[7]}"  name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><label for="">Address line2</label><input type="text"  value="{i[8]}"  name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><label for="">City</label><input value="{i[9]}"  class="form-control" name="city">
                  </div>
              </div>
              <div class="row mt-3 mb-5 ">
                <div class="col-md-4"><label for="">Zipcode</label><input type="text" value="{i[10]}"  name="zipcode" class="form-control" placeholder="Zipcode" id=""></div>
                <div class="col-md-4"><label for="">State</label><input type="text" name="state" value="{i[11]}"   class="form-control">
                  </div>
                <div class="col-md-4"><label for="">Country</label><input type="text" value="{i[12]}"  name="country" class="form-control" placeholder="Country" id=""></div>
              </div>
    
              <h3>Education</h3>
               <div class="row"><div class="col-md-3 "><label for="">Education</label><input type="text" class="form-control" value="{i[13]}"  name="edu">
                </div>
              <div class="col-md-3">
                            <label for="">Employee ID</label><input class="form-control"  value="{i[15]}"   name="idd">
                 </div>
              <div class="col-md-3">
              <label  mb-1">Password</label>
                <input class="form-control" value="****"  name="pwd">
                <input type="hidden" value="{i[16]}" name="pwd2">    
              </div>
              <div class="col-md-3">
              <label  mb-1">Department</label>
                <input type="text" name="department" class="form-control" value="{i[20]}">
              </div>
            </div>    
              <div class="d-flex justify-content-center mt-5 ">
              <div class="btn btn-danger me-5 ">Back</div>
              <input class="btn btn-primary" value="Update" type="submit" name="submit" >
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
        education = store.getvalue("edu")
        department=store.getvalue("department")
        empidd=store.getvalue("idd")
        pwd=store.getvalue("pwd")
        pwd2=store.getvalue("pwd2")
        finalpwd = ""
        if pwd != "****":
            finalpwd=pwd
        else:
            finalpwd=pwd2
        update=f"""UPDATE empreg SET fname='{fname}',lname='{lname}',dob='{dob}',gender='{gender}',mail='{mail}',phone='{phone}',address1='{add1}',address2='{add2}',city='{city}',zipcode='{zip}',state='{state}',country='{country}',education='{education}',empid='{empidd}',password='{finalpwd}',designation='{department}' WHERE id='{empid}' """
        cur.execute(update)
        con.commit()
        print(f"""
        <script>alert("Updated!")
        location.href="EditEmployee.py?id={empid}"
        </script>""")