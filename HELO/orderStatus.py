#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
id2 = store.getvalue("id")

userdetails = f"""select * from `userorder` where `companystatus`='C TO A' and `userstatus`=''  """
cur.execute(userdetails)
user = cur.fetchall()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user order status </title>
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
  span{{
    color: rgb(49, 124, 209);
    font-weight: 400;
    margin-left: 6px;
  }}
</style>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1>Order status</h1></div>
<a href="./AdminLogin.py" class="btn btn-danger h-25  me-5 float-end">Logout</a>
    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

                <li class="nav-item ">

                  <a class="nav-link " href="./userDashboard.py?id={id2}" >
                      Dashboard
                  </a>
              </li>
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./menallproducts.py?id={id2}">Mens</a></li>
                      <li><a class="dropdown-item" href="./womenallproducts.py?id={id2}">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link " href="./userCart.py?id={id2}" >
                            Cart
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./newOrders.py?id={id2}">New orders</a></li>
                      <li><a class="dropdown-item" href="./oldOrders.py?id={id2}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./cancelledOrders.py?id={id2}">Cancelled orders</a></li>
                      <li><a class="dropdown-item active" href="./orderStatus.py?id={id2}">Order status</a></li>

                  </ul>
              </li>
                    </ul>
            </div>

<div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">""")
if user:
    print(f"""
              <h3>User orders:</h3>
                 <table class="table mt-3 table-bordered ">
                     <thead class="thead-dark">
                       <tr class="table-dark">
                         <th scope="col">Order ID</th>
                         <th scope="col">Product</th>
                         <th scope="col">Image</th>
                         <th scope="col">Price</th>
                         <th scope="col">Quantity</th>
                         <th scope="col">Size</th>                        
                         <th scope="col">Action</th>
                        </tr>
                     </thead>
                     <tbody>""")

    for i in user:
        print(f""" <form method="post"> 
        <tr>
        <td>{i[19]}</td> 
        <td>{i[7]}</td> 
        <td><img src="./Assets/images/{i[4]}" alt="" width="100px"></td>
        <td>{i[8]}</td>
        <td>{i[11]}</td>
        <td>{i[9]}</td>
         <td><a class="btn btn-warning" href="./viewStatus.py?id={id2}&oid={i[0]}">View status</a> </td>
             </form>""")
    print("""</tbody>
            </table>""")

else:
    print("""<h2>Users: No requests found.""")





