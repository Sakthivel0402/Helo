#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cname = store.getvalue("cname")

id2 = store.getvalue("id")
productid = store.getvalue("productid")
q = f"""select * from userregistration where id='{id2}'"""
cur.execute(q)
query = cur.fetchall()
username = query[0][1]

q2 = f"""select * from product where type='women' and id='{productid}'"""
cur.execute(q2)
query2 = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>women products</title>

</head>
<body>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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
        background-color: rgb(32, 26, 26); color:white; 
        transition: all ease 1s;
    }
    .add3{
        background-color: rgb(248, 252, 252);
        transition: all ease 0.6s;
    }
    .add3:hover{
       background-color: #3B71CA; color: white;
        transition: all ease 1s;
    }

    .sizes{
        width: 45px; height: 30px; border: none; border-radius: 10px; margin-right: 7px; 
        transition: all ease 0.6s;
    }
    .sizes:hover{
        background-color: rgb(32, 26, 26); color:white;  transition: all ease 1s;

        }

    .button1{
        width: 25px;
        height: 25px;
        border-radius: 50%;
        border: none;
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

 <li class="nav-item ">
""")
print(f"""
  <a class="nav-link " href="./userDashboard.py?id={id2}" >
                      Dashboard
                  </a>
              </li>
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./menallProducts.py?id={id2}">Mens</a></li>
                      <li><a class="dropdown-item" href="./womenallroducts.py?id={id2}">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link" href="./userCart.py?id={id2}" >
                            Cart
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./newOrders.py?id={id2}">New orders</a></li>
                      <li><a class="dropdown-item" href="./oldOrders.py?id={id2}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./cancelledOrders.py?id={id2}">Cancelled orders</a></li>

                  </ul>
              </li>
                    </ul>
            </div>

 <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">

<div class="container-fluid p-5">
    <div class="row">""")

for i in query2:
    print(f""" <div class="d-flex flex-column border p-2 rounded-2 col-md-4 me-5" >
    <form method="post">    

   <div id="black{i[0]}" class="carousel slide"  data-bs-ride="carousel" >
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./Assets/images/{i[7]}" name="black1" class="d-block w-100" style="height:450px" alt="">
      <input type="hidden"  name="black1" value={i[7]}>
    </div>
    <div class="carousel-item">
      <img src="./Assets/images/{i[8]}" name="black2" class="d-block w-100" style="height:450px" alt="">
      <input type="hidden"  name="black2" value={i[8]}>
    </div>
    <div class="carousel-item">
      <img src="./Assets/images/{i[9]}" name="black3" class="d-block w-100" style="height:450px" alt="">
       <input type="hidden"  name="black3" value={i[9]}>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#black{i[0]}" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#black{i[0]}" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>


<div id="blue{i[0]}" class="carousel slide"  style="display: none;" data-bs-ride="carousel" >
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="./Assets/images/{i[10]}" name="blue1"  class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="blue1" value={i[10]}>

      </div>
      <div class="carousel-item">
        <img src="./Assets/images/{i[11]}" name="blue2" class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="blue2" value={i[11]}>
      </div>
      <div class="carousel-item">
        <img src="./Assets/images/{i[12]}" name="blue3" class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="blue3" value={i[12]}>

      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#blue{i[0]}" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#blue{i[0]}" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>


  <div id="brown{i[0]}" class="carousel slide" style="display: none;" data-bs-ride="carousel" >
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="./Assets/images/{i[13]}"  class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="brown1" value={i[13]}>
    </div>
      <div class="carousel-item">
        <img src="./Assets/images/{i[14]}" name="brown2" class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="brown2" value={i[14]}>
      </div>
      <div class="carousel-item">
        <img src="./Assets/images/{i[15]}" name="brown3" class="d-block w-100" style="height:450px" alt="">
         <input type="hidden"  name="brown3" value={i[15]}>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#brown" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#brown{i[0]}" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div> 

         <input type="submit" name="cart" class="add2 form-control mt-4" value="add to cart"> 
         <input type="submit" name="buy" class="add3 form-control mt-2" value="Buy now">

         <input type="hidden" id="color{i[0]}" name="color">
         <input type="hidden" id="size{i[0]}" name="size">

         </form>    
        </div> 
        <div class="col-md-7 " style="height: 180px;">
            <div class="border rounded-2 p-3"> <p name="caption"> women skirts</p><p  style="font-weight: 500; font-size: 25px; margin-bottom: 10px; margin-top: 10px;"> """)
    print(f"""<p>&#8377 {i[5]}.00</p>

    <p style="height: 20px; width: 100px;" class="badge rounded-pill text-bg-secondary rounded-3 justify-content-center">Free Delivery</p> </div>
        <div class=" d-flex rounded-2  mt-2 gap-3" style="font-weight:500;"> 
        <div class=" border rounded-2 p-3 mt-4" style="font-weight:500; width:50%"><p>Select color :</p>
        <button class="button1" id="blackbtn{i[0]}" style="background-color: black;" onclick="blackColor()"></button>
        <button class="button1" id="bluebtn{i[0]}" style="background-color: rgb(16, 151, 205);" onclick="blueColor()"></button>
        <button class="button1" id="brownbtn{i[0]}" style="background-color: brown;" onclick="brownColor()"></button>
         </div>  
        <div class="border rounded-2 p-3 mt-4" style="font-weight:500; width:50%"> <p>Select size :</p>
            <input type="submit" id="msize{i[0]}" class="sizes" name="M" onclick="sizem()"  value="M">
            <input type="submit" id="lsize{i[0]}" class="sizes" name="L" onclick="sizel()"  value="L">
            <input type="submit" id="xlsize{i[0]}" class="sizes" name="XL" onclick="sizexl()" value="XL">
        </div>  
        </div>  



        <div class="border rounded-2 p-3 mt-4" style="font-weight:500;"> <p>Product details :</p>
           <p class="d-block fw-light">
            Name : women skirts  <br>
            Fabric : Cotton <br>
            Pattern : Solid <br>
            Net Quantity (N) : 1 <br>
              
</div>
</div>
</div>
""")
    print(f"""
<script>
const brown{i[0]}=document.getElementById('brown{i[0]}')
const black{i[0]}=document.getElementById('black{i[0]}')
const blue{i[0]}=document.getElementById('blue{i[0]}')
const color{i[0]}=document.getElementById('color{i[0]}')
const size{i[0]}=document.getElementById('size{i[0]}')

const blackbtn{i[0]}=document.getElementById('blackbtn{i[0]}')
const brownbtn{i[0]}=document.getElementById('brownbtn{i[0]}')
const bluebtn{i[0]}=document.getElementById('bluebtn{i[0]}')

const msize{i[0]}=document.getElementById('msize{i[0]}')
const lsize{i[0]}=document.getElementById('lsize{i[0]}')
const xlsize{i[0]}=document.getElementById('xlsize{i[0]}')

function sizem(){{
msize{i[0]}.style.backgroundColor="black"
msize{i[0]}.style.color="white"
lsize{i[0]}.style.backgroundColor="white"
lsize{i[0]}.style.color="Black"
xlsize{i[0]}.style.backgroundColor="white"
xlsize{i[0]}.style.color="Black"
size{i[0]}.value="M"
console.log("hello")
}}
function sizel(){{
msize{i[0]}.style.backgroundColor="white"
msize{i[0]}.style.color="Black"
lsize{i[0]}.style.backgroundColor="Black"
lsize{i[0]}.style.color="white"
xlsize{i[0]}.style.backgroundColor="white"
xlsize{i[0]}.style.color="Black"
 size{i[0]}.value="L"
}}
function sizexl(){{
msize{i[0]}.style.backgroundColor="white"
msize{i[0]}.style.color="Black"
lsize{i[0]}.style.backgroundColor="white"
lsize{i[0]}.style.color="Black"
xlsize{i[0]}.style.backgroundColor="Black"
xlsize{i[0]}.style.color="white"
 size{i[0]}.value="XL"
}}

function blackColor(){{
    black{i[0]}.style.display='block'
    blackbtn{i[0]}.style.border="2px solid black"
    brownbtn{i[0]}.style.border="2px solid white"
    bluebtn{i[0]}.style.border="2px solid white"
    blue{i[0]}.style.display='none'
    brown{i[0]}.style.display='none'
    color{i[0]}.value="black" 
}}

function blueColor(){{
    blue{i[0]}.style.display='block'
    bluebtn{i[0]}.style.border="2px solid black"
    brownbtn{i[0]}.style.border="2px solid white"
    blackbtn{i[0]}.style.border="2px solid white"
    black{i[0]}.style.display='none'
    brown{i[0]}.style.display='none'
    color{i[0]}.value="blue"    
}}

function brownColor(){{
    brown{i[0]}.style.display='block'
    brownbtn{i[0]}.style.border="2px solid black"
    bluebtn{i[0]}.style.border="2px solid white"
    blackbtn{i[0]}.style.border="2px solid white"
    black{i[0]}.style.display='none'
    blue{i[0]}.style.display='none'
    color{i[0]}.value="brown"
}}


</script>
</body>
</html>
""")

order = store.getvalue("order")
cart = store.getvalue("cart")
if cart != None:
    color = store.getvalue("color")
    size = store.getvalue("size")
    caption = store.getvalue("caption")
    price = store.getvalue("price")
    black1 = store.getvalue("black1")
    black2 = store.getvalue("black2")
    black3 = store.getvalue("black3")
    blue1 = store.getvalue("blue1")
    blue2 = store.getvalue("blue2")
    blue3 = store.getvalue("blue3")
    brown1 = store.getvalue("brown1")
    brown2 = store.getvalue("brown2")
    brown3 = store.getvalue("brown3")

    if color == "black":
        q3 = f"""insert into userorder (`image`,`image2`,`image3`,`caption`,`price`,`color`,`size`,`username`,`cname`) values('{black1}','{black2}','{black3}','{i[4]}','{i[5]}','{color}','{size}','{username}','{cname}')"""
        cur.execute(q3)
        con.commit()
        print(f"""
        <script>alert("Product added to cart successfully!"); 
        location.href="userCart.py?id={id2}&cname={cname}"</script>""")
    if color == "blue":
        q3 = f"""insert into userorder (`image`,`image2`,`image3`,`caption`,`price`,`color`,`size`,`username`,`cname`) values('{blue1}','{blue2}','{blue3}','{i[4]}','{i[5]}','{color}','{size}','{username}','{cname}')"""
        cur.execute(q3)
        con.commit()
        print(f"""
                <script>alert("Product added to cart successfully!"); 
                location.href="userCart.py?id={id2}&cname={cname}"</script>""")
    if color == "brown":
        q3 = f"""insert into userorder (`image`,`image2`,`image3`,`caption`,`price`,`color`,`size`,`username`,`cname`,`productid`) values('{brown1}','{brown2}','{brown3}','{i[4]}','{i[5]}','{color}','{size}','{username}','{cname}','{productid}')"""
        cur.execute(q3)
        con.commit()
        print(f"""
                    <script>alert("Product added to cart successfully!"); 
                    location.href="userCart.py?id={id2}&cname={cname}&pid={productid}"</script>""")
    else:
        print(f"""
                           <script>alert("Please select product size & color"); 
                           location.href="wommenProducts.py?id={id2}&cname={cname}"</script>""")



