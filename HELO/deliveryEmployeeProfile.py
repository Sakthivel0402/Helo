#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
eid = store.getvalue("id")
query2 = f""" select * from empreg where id='{eid}' and designation='delivery'"""
cur.execute(query2)
empdetails = cur.fetchall()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>delivery employee profile</title>
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
    body{{
    background-color: #f8f9fa;

    }}
    .profile{{
        height: 150px;
        width: 150px;
        border-radius: 50%;
        overflow: hidden; 
        display: flex;
        justify-content: center;
        align-items: center;
    }}


</style>
</head>
<body>
    <div class="d-flex justify-content-center mb-4"><h1>Employee profile</h1></div>
    <a href="./employeeLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

      <div class="container-fluid mt-5">
          <div class="row">
              <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                  <ul class="nav nav-pills flex-column mb-auto">

                <li class="nav-item ">
                  <a class="nav-link " href="./deliveryDashboard.py?id={eid}" >
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item">
                        <a class="nav-link "  href="./deliveryProductRequest.py?id={eid}" >
                            Product requests
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " href="./ondeliveryProducts.py?id={eid}">Ondelivery products</a>
                    </li>
                    <li class="nav-item ">
                        <a class="nav-link" href="./completedOrders.py?id={eid}" >
                            Completed orders
                        </a>
                    </li>
                  <li class="nav-item ">
                        <a class="nav-link active" href="./deliveryEmployeeProfile.py?id={eid}" >
                            Profile
                        </a>
                    </li>
                    </ul>
              </div>    
""")
for i in empdetails:
    print(f"""
              <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">
                  <div class="row mb-2">
                  <div class="col-md-3 profile mx-5"><img src="./Assets/images/{i[17]} "alt="" height="150px"></div>
                  <div class="col-md-4 mb-2 "> <h3 class="my-5">{i[1]} {i[2]}</h3> </div>
                  <div class="col-md-4"></div>
                </div>

              <form method="post" enctype="multipart/form-data">
                <h3 class="mt-5">Personal</h3>
                <div class="row mt-4">
                  <div class="col-md-4"><label for="">Fullname</label><input type="text" name="fname" disabled value="{i[1]}" class="form-control" placeholder="Firstname" id=""></div>
                  <div class="col-md-4 "><label for="">DOB</label><input type="date"  value="{i[3]}" disabled name="dob" class="form-control" placeholder="" id=""></div>
                  <div class="col-md-4"><label for="">Gender</label><input name="gender" class="form-control" disabled value="{i[4]}" type="text" >
                </div>
                <div class="row mt-5">
                  </div>
                <div class="col-md-4"><label for="">Email</label><input type="text"  value="{i[5]}" disabled name="email" class="form-control" placeholder="Email" id=""></div>
                <div class="col-md-4"><label for="">Phone</label><input type="text" value="{i[6]}"disabled  name="phone" class="form-control" placeholder="Phone" id=""></div>
                <div class="col-md-4"><label for="">Photo (profile)</label><input type="text" value="{i[17]}"disabled  name="picture" class="form-control" placeholder="picure" id=""></div>

            </div>

             <h3 class="mt-5">Address</h3>
              <div class="row mt-4">
                <div class="col-md-4"><label for="">Address line1</label><input type="text" value="{i[7]}" disabled name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><label for="">Address line2</label><input type="text"  value="{i[8]}" disabled name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><label for="">City</label><input value="{i[9]}"  class="form-control"disabled name="city">
                  </div>
              </div>
              <div class="row mt-3 mt-5">
                <div class="col-md-4"><label for="">Zipcode</label><input type="text" value="{i[10]}" disabled name="zipcode" class="form-control" placeholder="Zipcode" id=""></div>
                <div class="col-md-4"><label for="">State</label><input type="text" name="state" value="{i[11]}" disabled  class="form-control">
                  </div>
                <div class="col-md-4"><label for="">Country</label><input type="text" value="{i[12]}" disabled name="country" class="form-control" placeholder="Country" id=""></div>
              </div>

              <h3 class="mt-5 mb-5">Education</h3>
               <div class="row"><div class="col-md-3 "><label for="">Education</label><input type="text" class="form-control" value="{i[13]}" disabled name="edu">
                </div>
                <div class="col-md-3">
                    <label  >Department</label>
                      <input type="text" name="department" class="form-control"disabled value="{i[20]}">
                    </div>
              <div class="col-md-3">
                            <label for="">Employee ID</label><input class="form-control"  value="{i[15]}" disabled  name="idd">
                 </div>
              <div class="col-md-3">
              <label >Password</label>
                <input class="form-control" value="********"  name="pwd">
                <input type="hidden" value="{i[16]}" name="pwd2">    
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
            </div>
            </div>

</body>
</html>
""")
    submit = store.getvalue("submit")
    if submit != None:
        pwd = store.getvalue("pwd")
        pwd2 = store.getvalue("pwd2")
        finalpwd = ""
        if pwd != "********":
            finalpwd = pwd
        else:
            finalpwd = pwd2
        update = f"""UPDATE empreg SET password='{finalpwd}' WHERE id='{eid}' """
        cur.execute(update)
        con.commit()
        print(f"""
        <script>alert("Updated!")
        location.href="employeeProfile.py?id={eid}"
        </script>""")