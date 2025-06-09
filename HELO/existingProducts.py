#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cid=store.getvalue("id")
query=f"""select * from companyregistration where id='{cid}'"""
cur.execute(query)
all=cur.fetchall()
compname=all[0][1]

query2=f"""select * from product where companyname='{compname}'"""
cur.execute(query2)
all2=cur.fetchall()

q1query="""select quantity from product"""
cur.execute(q1query)
q1=cur.fetchall()

products="""select * from userorder"""
cur.execute(products)
product=cur.fetchall()
q2=product[0][10]


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>various company products</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
<style>
  span{
    color: rgb(49, 124, 209);
    font-weight: 400;
    margin-left: 6px;
  }
</style>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1>Existing Products</h1></div>
  <a href="./companyLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

                <li class="nav-item "> """)
print(f"""    <a class="nav-link " href="./companyDashboard.py?id={cid}" >
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item">
                        <a class="nav-link " href="./addProduct.py?id={cid}" >
                            Add products
                        </a>
                    </li>
                    <li class="nav-item ">
                        <a class="nav-link active" href="./existingProducts.py?id={cid}" >
                            Existing products
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./companyneworders.py?id={cid}">New orders</a></li>
                      <li><a class="dropdown-item" href="./companyOldorders.py?id={cid}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./companyCancelledorders.py?id={cid}">Cancelled orders</a></li>

                  </ul>
              </li>
                    </ul>
            </div>
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">""")
print(f"""      
                 <table class="table mt-1 table-bordered ">
                     <thead class="thead-dark">
                       <tr class="table-dark">
                         <th scope="col">Product type</th>
                         <th scope="col">Quantity</th>
                         <th scope="col">Caption</th>
                         <th scope="col">Price</th>
                         <th scope="col">Action</th>                         
                        </tr>
                     </thead>
                     <tbody>""")
for i in all2:
    print( f""" <form method="post" enctype="multipart/form-data">
         <tr><td>{i[1]} <td>{i[3]}</td> <td>{i[4]}</td> <td>{i[5]}</td> <td><button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">
  View more
</button>
</td> </tr> 
</form>

<div class="modal fade" id="exampleModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Employee details</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class=" d-flex p-5 ">
      <div >  <h5>Product name: <span>{i[1]}</span></h5> <h5>Size: <span>{i[2]}</span></h5> <h5>Quantity: <span>{i[3]}</span></h5>  <h5>Capion: <span>{i[4]}</span></h5> <h5>Price: <span>{i[5]}</span></h5> <h5>Type: <span>{i[6]}</span></h5> <h5>Image (black1): <span>{i[7]}<img src="./Assets/images/{i[7]}" width="100px" height="100px"></span></h5> <h5>Image (black2): <span>{i[8]}<img src="./Assets/images/{i[8]}" width="100px" height="100px"></span></h5> 
             <h5>Image (black3): <span>{i[9]}<img src="./Assets/images/{i[9]}" width="100px" height="100px"></span></h5> <h5>Image (blue1): <span>{i[10]}<img src="./Assets/images/{i[10]}" width="100px" height="100px"></span></h5> <h5>Image (blue2): <span>{i[11]}<img src="./Assets/images/{i[11]}" width="100px" height="100px"></span></h5> <h5>Image (blue3): <span>{i[12]}<img src="./Assets/images/{i[12]}" width="100px" height="100px"></span></h5> <h5>Image (brown1): <span>{i[13]}<img src="./Assets/images/{i[13]}" width="100px" height="100px"></span></h5> <h5>Image (brown2): <span>{i[14]}<img src="./Assets/images/{i[14]}" width="100px" height="100px"></span></h5> <h5>Image (brown3): <span>{i[15]}<img src="./Assets/images/{i[15]}" width="100px" height="100px"></span></h5>
             </div>         
   </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <a href="#" type="button" class="btn btn-primary">Edit</a>
      </div> 
""")
print("""
    </table>
    </div>
    </body>
    </html>""")
