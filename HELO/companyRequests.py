#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,smtplib
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
query2 = """ select * from companyregistration where status='pending'"""
cur.execute(query2)
compdetails = cur.fetchall()

import random


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Requests</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
    }
  span{
    color: rgb(49, 124, 209);
    font-weight: 400;
    margin-left: 6px;
  }
</style>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1> Company Requests</h1></div>
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
                        <a class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Employee
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./EmpReg.py">Create</a></li>
                            <li><a class="dropdown-item" href="./OldEmployee.py">Old Employee</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Wholesalers
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./whRequests.py">Requests</a></li>
                            <li><a class="dropdown-item" href="./whOld.py">Old Wholesalers</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Company
                      </a>
                      <ul class="dropdown-menu">
                          <li><a class="dropdown-item active" href="./companyRequests.py">Requests</a></li>
                          <li><a class="dropdown-item" href="./companyOld.py">Old Company's</a></li>
                      </ul>
                  </li>
                  <li class="nav-item ">
                    <a class="nav-link" href="./adminProduct.py">
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
""")
if compdetails:
    print(f"""
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">
              <div class="">
                 <table class="table mt-5 table-bordered ">
                     <thead class="thead-dark">
                       <tr class="table-dark">
                         <th scope="col">ID</th>
                         <th scope="col">company name</th>
                         <th scope="col">Email</th>
                         <th scope="col">Type of company</th>
                         <th scope="col">Annual revenue</th>
                         <th scope="col">Business website</th>                        
                         <th scope="col">Action</th>
                        </tr>
                     </thead>
                     <tbody>""")

    for i in compdetails:
        print(f""" <form method="post" ><tr><td>{i[0]}</td> <td>{i[1]}</td> <td>{i[4]}</td> <td>{i[12]}</td> <td>{i[15]}</td> <td>{i[13]}</td> <td><button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">
  View more
</button>
</form>
</td>
</tr>
<div class="modal fade" id="exampleModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Employee details</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class=" d-flex p-5 "><form>
      <div > <h5>Company name: <span>{i[1]} <input type="hidden" name="rowcompany" value="{i[1]}"></span></h5> <h5>Contact person name: <span>{i[2]}</span></h5> <h5>Contact person number: <span>{i[3]}</span></h5>  <h5>Company email: <span><input type="hidden" name="rowemail" value="{i[4]}">{i[4]}</span></h5> <h5>Company phone: <span>{i[5]}</span></h5> <h5>Address line1: <span>{i[6]}</span></h5> <h5>Address line2: <span>{i[7]}</span></h5> <h5>city: <span>{i[8]}</span></h5> 
             <h5>Zipcode: <span>{i[9]}</span></h5> <h5>State: <span>{i[10]}</span></h5> <h5>Country: <span>{i[11]}</span></h5> <h5>Type of company: <span>{i[12]}</span></h5> <h5>Company website: <span>{i[13]}</span></h5> <h5>Years in business: <span>{i[14]}</span></h5> <h5>Annual revenue: <span>{i[15]}</span></h5> 
             <h5>ISO certificate: <span><img src="./proofs/{i[16]}" alt="" width="100px" height="100px"> {i[16]} </span></h5> <h5>Tax ID number: <span>{i[17]}</span></h5>  <h5>Business licensenumber number: <span>{i[18]}</span></h5> <h5>Pan proof: <span> <img src="./proofs/{i[19]}" alt="" width="100px" height="100px"> {i[19]}</span></h5>   	
            <h5>COMPANY ID: <span>{i[20]}<input type="hidden" name="rowcompanyid" value="{i[20]}"></span></h5>
             </div>         
   </div>
      <div class="modal-footer">
      <input type="submit" value="accept" name="accept" class="btn btn-success"> 
      <input type="hidden" name="rowaccept" value="{i[0]}">
      <input type="submit" name="decline" value="Decline" class="btn btn-danger">
      <input type="hidden" name="rowdecline" value="{i[0]}">
      </form>  
      </div>
    </div>
  </div>
</div>   </tbody>
         </table>
         </div>
         </div>
         </div>
         """)
else:
    print("""</div><h2> No requests found</h2>
    
         </body>
         </html>""")

accept=store.getvalue("accept")
if accept !=None:
        rowaccept=store.getvalue("rowaccept")
        rowemail=store.getvalue("rowemail")
        rowcompany=store.getvalue("rowcompany")
        rowcompanyid=store.getvalue("rowcompanyid")
        r = random.randint(1000, 9999)
        slymail = rowemail[0:4]
        password = slymail + str(r)
        fromadd = 'sakthivelsubash0402@gmail.com'
        password2 = 'wmob kavj zalb mxoj'
        toadd = rowemail
        subject = """Company registration process"""
        body = f"Congratulations {rowcompany}!. You are successfully registered with our company. This is your Company ID: {rowcompanyid}\n and password:{password}"
        msg = f"""Subject: {subject}\n\n{body}"""
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromadd, password2)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        q=f"""UPDATE `companyregistration` SET `password`='{password}',`status`='accepted' where id='{rowaccept}'"""
        cur.execute(q)
        con.commit()
        print("""<script> location.href="companyRequests.py"
                        alert("Accepted!")</script>""")

decline=store.getvalue("decline")
if decline !=None:
    rowdecline=store.getvalue("rowdecline")
    rowemail = store.getvalue("rowemail")
    rowcompany = store.getvalue("rowcompany")
    fromadd = 'sakthivelsubash0402@gmail.com'
    password2 = 'wmob kavj zalb mxoj'
    toadd = rowemail
    subject = """Company registration process"""
    body = f"Hello, {rowcompany}!. Your company does not met with our qualifications. So it has been declined. "
    msg = f"""Subject: {subject}\n\n{body}"""
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromadd, password2)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    q=f"""UPDATE `companyregistration` SET `status`='declined' where id='{rowdecline}'"""
    cur.execute(q)
    con.commit()
    print("""<script> location.href="companyRequests.py"
        alert("Declined!!")</script>""")