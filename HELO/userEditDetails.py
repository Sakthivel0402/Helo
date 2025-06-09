#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
id=store.getvalue("id")
query=f""" select * from userregistration where id='{id}'"""
cur.execute(query)
userdetails=cur.fetchall()
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit user details</title>
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
  <div class="d-flex justify-content-center mb-4"><h1>Edit user details </h1></div>
<a href="./AdminLogin.py" class="btn btn-danger h-25  me-5 float-end">Logout</a>   

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                  
                <li class="nav-item ">
                  <a class="nav-link " href="./AdminDashboard.py" >
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
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
                            <li><a class="dropdown-item" href="./wh-Requests.html">Requests</a></li>
                            <li><a class="dropdown-item" href="Wh-Old.html">Old Wholesalers</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Company
                      </a>
                      <ul class="dropdown-menu">
                          <li><a class="dropdown-item" href="#">Requests</a></li>
                          <li><a class="dropdown-item" href="#">Old Company's</a></li>
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
                  <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./adminNeworders.py">Ongoing orders</a></li>
                      <li><a class="dropdown-item" href="./adminCompleted.py">Old orders</a></li>
                      <li><a class="dropdown-item " href="./adminCancelled.py">Cancelled orders</a></li>

                  </ul>
              </li>
              <li class="nav-item  ">
                <a class="nav-link active" href="./userDetails.py">
                    User details
                </a>
            </li>
                    </ul>
            </div>

            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-5 border ">
              <h3>Personal</h3>
              <form method="post" enctype="multipart/form-data">
                <div class="row">
                  <div class="col-md-4"><label for="">First name</label><input type="text" name="fname" value="{userdetails[0][1]}" class="form-control" placeholder="Firstname" id=""></div>
                  <div class="col-md-4"><label for="">Last name</label><input type="text" name="lname"  value="{userdetails[0][2]}" class="form-control" placeholder="Lastname" id=""></div>
                  <div class="col-md-4 "><label for="">DOB</label><input type="date"  value="{userdetails[0][3]}"  name="dob" class="form-control" placeholder="" id=""></div>
                </div>
                <div class="row mt-5 mb-5">
                 <div class="col-md-4"><label for="">Gender</label><input name="gender" class="form-control"  value="{userdetails[0][4]}" type="text" >
                  </div>
                <div class="col-md-4"><label for="">Email</label><input type="text"  value="{userdetails[0][5]}"  name="email" class="form-control" placeholder="Email" id=""></div>
                <div class="col-md-4"><label for="">Phone</label><input type="text" value="{userdetails[0][6]}"  name="phone" class="form-control" placeholder="Phone" id=""></div>
              </div>

             <h3>Address</h3>
              <div class="row mt-4">
                <div class="col-md-4"><label for="">Address line1</label><input type="text" value="{userdetails[0][7]}"  name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><label for="">Address line2</label><input type="text"  value="{userdetails[0][8]}"  name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><label for="">City</label><input value="{userdetails[0][9]}"  class="form-control" name="city">
                  </div>
              </div>
              <div class="row mt-3 mb-5 ">
                <div class="col-md-4"><label for="">Zipcode</label><input type="text" value="{userdetails[0][10]}"  name="zipcode" class="form-control" placeholder="Zipcode" id=""></div>
                <div class="col-md-4"><label for="">State</label><input type="text" name="state" value="{userdetails[0][11]}"   class="form-control">
                  </div>
                <div class="col-md-4"><label for="">Country</label><input type="text" value="{userdetails[0][12]}"  name="country" class="form-control" placeholder="Country" id=""></div>
              </div>

              
               <div class="row">
              <div class="col-md-3">
                            <label for="">User ID</label><input class="form-control" value="{userdetails[0][13]}"   name="idd">
                 </div>
              <div class="col-md-3">
              <label  mb-1">Password</label>
                <input class="form-control" value="******"  name="pwd">    
              </div>    
            </div>    
              <div class="d-flex justify-content-center mt-5 ">
              <a href="./AdminDashboard.py" class="btn btn-danger me-5 ">Back</a>
              <input class="btn btn-primary" value="Update" type="submit" name="submit" >
            </div>
            </form>
            </div>  
            </div>
            </div>
  </body>
</html>
""")

submit = store.getvalue("submit")
if submit != None:
    if len(store) != 0:
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
        userid = store.getvalue("idd")
        pwd = store.getvalue("pwd")
        update = f"""UPDATE userregistration SET firstname='{fname}',lastname='{lname}',dob='{dob}',gender='{gender}',email='{mail}',phone='{phone}',address1='{add1}',address2='{add2}',city='{city}',zipcode='{zip}',state='{state}',country='{country}',username='{userid}',password='{pwd}' WHERE id='{id}' """
        cur.execute(update)
        con.commit()
        print(f"""
        <script>alert("Updated!")
        location.href="userEditDetails.py?id={id}"
        </script>""")