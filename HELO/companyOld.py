#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
query2 = """ select * from companyregistration where status='accepted'"""
query3 = """ select * from companyregistration where status='declined'"""
cur.execute(query3)
declineloop=cur.fetchall()
cur.execute(query2)
acceptloop = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Old Company </title>
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
<body>""")
print(f"""
  <div class="d-flex justify-content-center mb-4"><h1> Old company</h1></div>
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
                          <li><a class="dropdown-item" href="./companyRequests.py">Requests</a></li>
                          <li><a class="dropdown-item active" href="./companyOld.py">Old Company's</a></li>
                      </ul>
                  </li>
                  <li class="nav-item ">
                    <a class="nav-link" href="./adminProduct.py" >
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
            
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">
            <h3> Accepted Company details:</h3>
                 <table class="table mt-3 table-bordered ">
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

for i in acceptloop:
    print(
        f""" <form method="post" ><tr><td>{i[0]}<input type="hidden" name="rowid" value="{i[0]}"></td> <td>{i[1]}</td> <td>{i[4]}</td> <td>{i[12]}</td> <td>{i[15]}</td> <td>{i[13]}</td> <td><button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">
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
      <div class=" d-flex p-5 ">
      <div > <h5>Company name: <span>{i[1]}</span></h5> <h5>Contact person name: <span>{i[2]}</span></h5> <h5>Contact person number: <span>{i[3]}</span></h5>  <h5>Company email: <span>{i[4]}</span></h5> <h5>Company phone: <span>{i[5]}</span></h5> <h5>Address line1: <span>{i[6]}</span></h5> <h5>Address line2: <span>{i[7]}</span></h5> <h5>city: <span>{i[8]}</span></h5> 
             <h5>Zipcode: <span>{i[9]}</span></h5> <h5>State: <span>{i[10]}</span></h5> <h5>Country: <span>{i[11]}</span></h5> <h5>Type of company: <span>{i[12]}</span></h5> <h5>Company website: <span>{i[13]}</span></h5> <h5>Years in business: <span>{i[14]}</span></h5> <h5>Annual revenue: <span>{i[15]}</span></h5> <h5>ISO certificate: <span>{i[16]}</span></h5> <h5>Tax ID number: <span>{i[17]}</span></h5>  <h5>Business licensenumber number: <span>{i[18]}</span></h5> <h5>Pan proof: <span>{i[19]}</span></h5>   	
            <h5>COMPANY ID: <span>{i[20]}</span></h5>
             </div>         
   </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <a href="./EditEmployee.py?id={i[0]}" type="button" class="btn btn-primary">Edit</a>
      </div>
""")

print("""
        </table>
        <hr>
        
            <h3 class="mb-4 mt-5"> Declined Company details:</h3>
                 <table class="table  table-bordered">
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

for i in declineloop:
    print(
        f""" <form method="post" ><tr><td>{i[0]}<input type="hidden" name="rowdec" value="{i[0]}"></td> <td>{i[1]}</td> <td>{i[4]}</td> <td>{i[12]}</td> <td>{i[15]}</td> <td>{i[13]}</td> <td><button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">
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
      <div class=" d-flex p-5 ">
      <div > <h5>Company name: <span>{i[1]}</span></h5> <h5>Contact person name: <span>{i[2]}</span></h5> <h5>Contact person number: <span>{i[3]}</span></h5>  <h5>Company email: <span>{i[4]}</span></h5> <h5>Company phone: <span>{i[5]}</span></h5> <h5>Address line1: <span>{i[6]}</span></h5> <h5>Address line2: <span>{i[7]}</span></h5> <h5>city: <span>{i[8]}</span></h5> 
             <h5>Zipcode: <span>{i[9]}</span></h5> <h5>State: <span>{i[10]}</span></h5> <h5>Country: <span>{i[11]}</span></h5> <h5>Type of company: <span>{i[12]}</span></h5> <h5>Company website: <span>{i[13]}</span></h5> <h5>Years in business: <span>{i[14]}</span></h5> <h5>Annual revenue: <span>{i[15]}</span></h5> <h5>ISO certificate: <span>{i[16]}</span></h5> <h5>Tax ID number: <span>{i[17]}</span></h5>  <h5>Business licensenumber number: <span>{i[18]}</span></h5> <h5>Pan proof: <span>{i[19]}</span></h5>   	
            <h5>COMPANY ID: <span>{i[20]}</span></h5>
             </div>         
   </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <a href="./EditEmployee.py?id={i[0]}" type="button" class="btn btn-primary">Edit</a>
      </div>
""")

print("""
         </tbody>
         </table>
         </body>
         </html>
""")





