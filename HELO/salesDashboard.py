#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
eid=store.getvalue("id")
query=f"""select * from empreg where id='{eid}' and designation='sales'"""
cur.execute(query)
query2=cur.fetchall()

print(f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>sales Dashboard</title>
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
  <div class="d-flex justify-content-center mb-4"><h1>Sales Dashboard</h1></div>
  <a href="./employeeLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

                <li class="nav-item ">
                  <a class="nav-link active" href="./salesDashboard.py?id={eid}" >
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item">
                        <a class="nav-link"  href="./salesProductRequest.py?id={eid}" >
                            Product requests
                        </a>
                    </li>
                  <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./salesOldorders.py?id={eid}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./salescancelledorders.py?id={eid}">Cancelled orders</a></li>
                  </ul>
                  </li>                

                <li class="nav-item ">
                        <a class="nav-link" href="./salesEmployeeProfile.py?id={eid}" >
                            Profile
                        </a>
                    </li>
                    </ul>
            </div>

            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">""")
print(f"""<h1>Welcome {query2[0][1]}! </h1>""")
print("""    </div>
        </div>
    </div>

  </body>
</html>
""")