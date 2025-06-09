#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
wid=store.getvalue("id")
products=f"""select * from product where type='men'"""
cur.execute(products)
productdetails=cur.fetchall()


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>men products</title>
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
</style>
</head>
<body>

  <div class="d-flex justify-content-center mb-4"><h1>Men Products</h1></div>
  <a href="./userLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">""")

print(f"""  <li class="nav-item ">
                  <a class="nav-link " href="./whDashboard.py?id={wid}" >
                      Dashboard
                  </a>
              </li>

                    <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./whMenproducts.py?id={wid}">Mens</a></li>
                      <li><a class="dropdown-item" href="./whWomenallproducts.py?id={wid}">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link" href="./whCart.py?id={wid}" >
                            Cart
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./whNeworders.py?id={wid}">New orders</a></li>
                      <li><a class="dropdown-item" href="./whOldorders.py?id={wid}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./whCancelledorders.py?id={wid}">Cancelled orders</a></li>
                      <li><a class="dropdown-item" href="./whOrderStatus.py?id={wid}">Order status</a></li>


                  </ul>
              </li>
                    </ul>
            </div>

     <div class="col-md-9 d-flex flex-row p-3">""")
for i in productdetails:
    print(f""" <div class="container"> <div class="row" > 
       <a style="text-decoration:none; color:black;" href="./whmenProducts.py?id={wid}&productid={i[0]}&cname={i[16]}">  <div class="col-md-3 border rounded-2 p-2" style="height:500px; width:283px; cursor:pointer;">
         <img src="./Assets/images/{i[7]}" width="265px" title="view details">
         <div class="mt-2" style="font-size:18px"><p>{i[4]}</p></div>
         <div class="mt-1"><h5>&#8377 {i[5]}.00</h5></div></a>
         <a class="btn btn-primary mt-2" href="#">Order now</a>
         </div>
          </div>  
          </div>          
    """)

print("""
</div>  
</body>
</html>
""")