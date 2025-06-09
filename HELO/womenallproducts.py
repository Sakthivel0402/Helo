#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
userid=store.getvalue("id")
q=f"""select * from userregistration where id='{userid}'"""
cur.execute(q)
query=cur.fetchall()
username=query[0][1]

q2 = """select * from product where type='women'"""
cur.execute(q2)
productdetails = cur.fetchall()


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>women products</title>
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
body{
    background-color: #f8f9fa;
}
    .add2{
        background-color: rgb(248, 252, 252);
        transition: all ease 0.6s;
    }
    .add2:hover{
        background-color: rgb(189, 192, 192);
        transition: all ease 0.6s;
    }
    .image{
        cursor: pointer;
        transition: all ease 0.6s;

    }
    .image:hover{
        scale: 1.02;
        transition: all ease 0.6s;
    }
</style>
</head>
<body>

    <div class="d-flex justify-content-center mb-4"><h1>Women Products</h1></div>
  <a href="./userLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

 <li class="nav-item ">""")

print(f"""  <a class="nav-link " href="./userDashboard.py?id={userid}" >
                      Dashboard
                  </a>
              </li>
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./menProducts.py?id={userid}">Mens</a></li>
                      <li><a class="dropdown-item" href="#">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link" href="./userCart.py?id={userid}" >
                            Cart
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./Or-ongoing.html">New orders</a></li>
                      <li><a class="dropdown-item" href="Or-completed.html">Old orders</a></li>
                      <li><a class="dropdown-item" href="Or-completed.html">Cancelled orders</a></li>

                  </ul>
              </li>
                    </ul>
            </div>

      <div class="col-md-9 d-flex flex-row p-3">""")
for i in productdetails:
    print(f""" <div class="container"> <div class="row" > 
       <a style="text-decoration:none; color:black;" href="./womenProducts.py?id={userid}&productid={i[0]}&cname={i[16]}">  <div class="col-md-3 border rounded-2 p-2" style="height:500px; width:283px; cursor:pointer;">
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
