#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, random
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
shirt=f"""select * from product where productname='shirt' """
cur.execute(shirt)
shirts=cur.fetchall()
shirtcaption=(shirts[0][4])
shirtprice=(shirts[0][5])
shirt=(shirts[0][7],shirts[0][8],shirts[0][9],shirts[0][10],shirts[0][11],shirts[0][12],shirts[0][13],shirts[0][14],shirts[0][15])
random_index = random.randint(0, len(shirt) - 1)

skirt=f"""select * from product where productname='skirt' """
cur.execute(skirt)
skirts=cur.fetchall()
skirtcaption=(skirts[0][4])
skirtprice=(skirts[0][5])
skirt=(skirts[0][7],skirts[0][8],skirts[0][9],skirts[0][10],skirts[0][11],skirts[0][12],skirts[0][13],skirts[0][14],skirts[0][15])
random_index2 = random.randint(0, len(skirt) - 1)

pant=f"""select * from product where productname='pant' """
cur.execute(pant)
pants=cur.fetchall()
pantcaption=(pants[0][4])
pantprice=(pants[0][5])
pant=(pants[0][7],pants[0][8],pants[0][9],pants[0][10],pants[0][11],pants[0][12],pants[0][13],pants[0][14],pants[0][15])
random_index3 = random.randint(0, len(pant) - 1)

hoodie=f"""select * from product where productname='hoodie' """
cur.execute(hoodie)
hoodies=cur.fetchall()
hoodiecaption=(hoodies[0][4])
hoodieprice=(hoodies[0][5])
hoodie=(hoodies[0][7],hoodies[0][8],hoodies[0][9],hoodies[0][10],hoodies[0][11],hoodies[0][12],hoodies[0][13],hoodies[0][14],hoodies[0][15])
random_index4 = random.randint(0, len(hoodie) - 1)



print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecommerce</title>
    <link rel="stylesheet" href="./style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
<style>
.product-image {
  width: 280px;
  height: 350px;
  object-fit: cover; 
}
</style>
</head>
<body >
 <nav class="navbar navbar-expand-md position-fixed w-100" style="background-color: aliceblue; z-index: 10;" >
    <div class="container"><a href="#" class="navbar-brand">Helo</a>
    <button type="button" class="navbar-toggler" data-bs-toggle="collaps" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span></button>
        
        <div class="collapse navbar-collapse "   id="navbarNav">
            <ul class="navbar-nav " >
                <li class="nav-item"><a href="#" class="nav-link active">Home</a> </li>
                <li class="nav-item"><a href="./userLogin.py" class="nav-link">Men</a> </li>
                <li class="nav-item"><a href="./userLogin.py" class="nav-link">Women</a> </li>
                <li class="nav-item dropdown" style="margin-left: 300px;">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      LogIn
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                      <li><a class="dropdown-item" href="./userLogin.py">User</a></li>
                      <li><a class="dropdown-item" href="./AdminLogin.py">Admin</a></li>
                      <li><a class="dropdown-item" href="./whLogin.py">Wholesaler</a></li>
                      <li><a class="dropdown-item" href="./companyLogin.py">Company</a></li>
                      <li><a class="dropdown-item" href="./employeeLogin.py">Employee</a></li>
                      

                    </ul>
                  </li>
                  <span class="hi">|</span>
                  <li class="nav-item dropdown" style="margin-left: -1px;" >
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Register
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                      <li><a class="dropdown-item" href="./userRegistration.py">User</a></li>
                      <li><a class="dropdown-item" href="./companyRegistration.py">Company</a></li>
                      <li><a class="dropdown-item" href="./whRegistration.py">Wholesaler</a></li>
                    </ul>
                  </li></ul>
        </div>
    
    </div>
 </nav>

 <section>
    <div class="container mb-5">
        <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
              <div class="carousel-item active row position-relative"> 
                <img src="./Assets/b1.webp" style="margin-top: 90px;" class=" d-block mt-5 ms-auto col-sm-1 col-lg-5" alt="...">
                <h2 class="heading">Hello <br>  Everyone!</h2>
              </div>
              <div class="carousel-item w-50 row position-relative">
                <img style="margin-top: 90px;" src="./Assets/b2.webp" class="d-block col-sm-1 col-lg-10" alt="...">
                <h2 class="heading3">Winter is here!</h2>
              </div>
              <div class="carousel-item row ">
                <img src="./Assets/b3.png" style="margin-top: 90px;" class="d-block w-75 col-sm-1 col-lg-12" alt="...">
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden ">Next</span>
            </button>
          </div>
    </div>
 </section>

 

 <section>
    <div class="container">
        <div class="row" style="display: flex; justify-content: space-around; margin-bottom: 60px;">
        <div  style="cursor:pointer; background-image:url(./Assets/h1-banner1.webp); background-size:cover; height:330px;width: 300px; border-radius: 10px;" class=" hole col-md-4 p-5"><h4 class="fw-bold"> POLO T-SHIRT </h4> <br><p class="sale" style="color: aliceblue;">SALE</p>  <br> <p class="off" style="margin-left: 20px;">OFF 25%</p> <br> <button style="height: 40px; border: none; margin-left: 20%; padding: 5px; border-radius: 5px; background-color: rgb(203, 216, 228); display: none;"> ShopNow <box-icon name='right-arrow-alt'></box-icon></button></div>
            <div style="cursor:pointer; background-image:url(./Assets/h1-banner2.webp); background-size:cover; height:330px;width: 300px; border-radius: 10px;" class=" hole col-md-4 p-5"><h4 class="fw-bold">  SKIRT </h4> <br><p class="sale" style="color: aliceblue;">SALE</p>  <br> <p class="off" style="margin-left: 20px;">OFF 25%</p> <br> <button style="height: 40px; border: none; margin-left: 20%; padding: 5px; border-radius: 5px; background-color:rgb(203, 216, 228); display: none;">ShopNow <box-icon name='right-arrow-alt'></box-icon></button></div>
            <div style="cursor:pointer; background-image:url(./Assets/h1-banner3.webp); background-size:cover; height:330px;width: 300px; border-radius: 10px;" class=" hole col-md-4 p-5"><h4 class="fw-bold"> MEN'S SHIRT </h4> <br><p class="sale" style="color: aliceblue;">SALE</p>  <br> <p class="off" style="margin-left: 20px;">OFF 25%</p> <br> <button style="height: 40px; border: none; margin-left: 20%; padding: 5px; border-radius: 5px; background-color:rgb(203, 216, 228); display: none;">ShopNow<box-icon name='right-arrow-alt'></box-icon></button></div>
        </div>
    </div>
 </section>""")
print(f"""
 <h1 class="d-flex justify-content-around mb-5">Must Have</h1> 
<div class="container-fluid p-5  ">
  <div class="row d-flex justify-content-around">
    <div class="  col-md-3 d-flex flex-column    w-25 h-25 justify-content-around">
      <img src="./Assets/images/{hoodie[random_index4]}"  style="cursor:pointer;" class="product-image rounded-4" alt="" >
      <h6 class="mt-3">{hoodiecaption}</h6>
      <h5>Rs.{hoodieprice}.00</h5>
     <a href="./userLogin.py" class="mt-1  btn btn-primary w-50 d-flex justify-content-center p-2">  Buy now</a>
    </div>
    
    <div class="  col-md-3 d-flex flex-column  w-25 h-25 justify-content-around">
      <img src="./Assets/images/{pant[random_index3]}"  style="cursor:pointer;" class="product-image rounded-4" alt="">
      <h6 class="mt-3">{pantcaption}</h6>
      <h5>Rs.{pantprice}.00</h5>
     <a  href="./userLogin.py"  class="mt-1  btn btn-primary w-50 d-flex justify-content-center   p-2 ">  Buy now</a>
    </div>
    
    <div class="  col-md-3 d-flex flex-column    rounded-4 w-25 h-25 justify-content-around">
      <img src="./Assets/images/{skirt[random_index2]}"  style="cursor:pointer;" class="product-image rounded-4" alt="">
      <h6 class="mt-3">{skirtcaption}</h6>
      <h5>Rs.{skirtprice}.00</h5>
    <a  href="./userLogin.py" class="mt-1  btn btn-primary w-50 d-flex justify-content-center   p-2 ">  Buy now</a>
    </div>
    
    <div class="  col-md-3 d-flex flex-column    rounded-4 w-25 h-25 justify-content-around">
      <img src="./Assets/images/{shirt[random_index]}"   style="cursor:pointer;" class="product-image rounded-4" alt="">
      <h6 class="mt-3">{shirtcaption}</h6>
      <h5>Rs.{shirtprice}.00</h5>
     <a  href="./userLogin.py" class="mt-1  btn btn-primary w-50 d-flex justify-content-center   p-2 ">  Buy now</a>
    </div>
  </div>
</div>

 <footer class="d-block d-flex justify-content-around mt-5">CopyRight 2024 By Helo.Co</footer>
</body>
</html>""")