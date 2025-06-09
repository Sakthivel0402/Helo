#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cid=store.getvalue("id")
coid=f"""select * from companyregistration where id='{cid}' """
cur.execute(coid)
companyname=cur.fetchall()


print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add product</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
</head>
<body>
 <div class="d-flex justify-content-center mb-4"><h1>Add your product here</h1></div>
 <a href="./companyLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>
 
 <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

                <li class="nav-item ">
                  <a class="nav-link " href="./companyDashboard.py?id={cid}">
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item">
                        <a class="nav-link active " href="./addProduct.py?id={cid}" >
                            Add products
                        </a>
                    </li>
                    <li class="nav-item ">
                        <a class="nav-link" href="./existingProducts.py?id={cid}">
                            Existing products
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./companyneworders.py?id={cid}.html">New orders</a></li>
                      <li><a class="dropdown-item" href="./companyOldorders.py?id={cid}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./companyCancelledorders.py?id={cid}">Cancelled orders</a></li>

                  </ul>
              </li>
                    </ul>
            </div>
   
        <div class="container w-50 mt-3 w-75 bg-light col-md-9 col-lg-10 p-5">""")
print(f"""   <h1 class="mb-5" >Welcome {companyname[0][1]} ! </h1>
         <form action="" method="post" enctype="multipart/form-data">
            <div class="row">
                <div class="col-md-4"><label  for="" >Product type</label><select name="producttype"  class="form-select mt-3" aria-label="Default select example">
                    <option selected>select</option>
                    <option value="Shirt">Shirt</option>
                    <option value="pant">Pant</option>
                    <option value="hoodie">Hoodie</option>
                     <option value="skirt">Skirt</option>
                    <option value="t-shirt">t-shirt</option>
                  </select>
                </div>
                
                 <div class="col-md-4">
                <label class="mt-2" for="">Size</label>
                <select name="size"  class="form-select mt-2" aria-label="Default select example">
                    <option selected>select</option>
                    <option value="M">M</option>
                    <option value="L">L</option>
                    <option value="XL">XL</option>
                      </select>
                      </div>
            
                <div class="col-md-4 "> <label class="mt-2" for="">Quantity</label>
                <input type="text" class="form-control mt-2" name="quantity" id=""></div>
            
                <div class="col-md-4"> <label class="mt-5" for="">caption</label>
                <input type="text" class="form-control mt-2" name="caption" id=""></div>
          
            <div class="col-md-4">
                <label class="mt-5" for="">Price in Rs.</label>
                <input type="number" class="form-control mt-2" name="price" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">type</label>
                <select name="type"  class="form-select mt-2" aria-label="Default select example">
                    <option selected>select</option>
                    <option value="men">Men</option>
                    <option value="women">Women</option>
                      </select>
                      </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image(Black)</label>
                <input type="file" class="form-control mt-2" name="b1" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 2(Black)</label>
                <input type="file" class="form-control mt-2" name="b2" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 3(Black)</label>
                <input type="file" class="form-control mt-2" name="b3" id="">
            </div>
            
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image(blue)</label>
                <input type="file" class="form-control mt-2" name="s1" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 2(blue)</label>
                <input type="file" class="form-control mt-2" name="s2" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 3(blue)</label>
                <input type="file" class="form-control mt-2" name="s3" id="">
            </div>
            
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image(brown)</label>
                <input type="file" class="form-control mt-2" name="br1" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 2(brown)</label>
                <input type="file" class="form-control mt-2" name="br2" id="">
            </div>
            <div class="col-md-4">
                <label class="mt-5" for="">Product Image 3(brown)</label>
                <input type="file" class="form-control mt-2" name="br3" id="">
            </div>
            <div class="row d-flex justify-content-center">
             <div class="col-md-4 ">
            <input type="submit" class="btn btn-primary mt-5 ms-5 " name="submit" value="Add Product">
        </div>
    </form>
</body>
</html>

""")


submit=store.getvalue("submit")
if submit!=None:
    name=store.getvalue("producttype")
    size=store.getvalue("size")
    quantity=store.getvalue("quantity")
    caption=store.getvalue("caption")
    price=store.getvalue("price")
    type=store.getvalue("type")
    b1=store['b1']
    b2=store['b2']
    b3=store['b3']
    s1=store['s1']
    s2=store['s2']
    s3=store['s3']
    br1=store['br1']
    br2=store['br2']
    br3=store['br3']
    if b1.filename and b2.filename and b3.filename and s1.filename and s2.filename and s3.filename and br1.filename and br2.filename and br3.filename:
        black1 = os.path.basename(b1.filename)
        open("../products" + black1, "wb").write(b1.file.read())
        black2 = os.path.basename(b2.filename)
        open("../products" + black2, "wb").write(b2.file.read())
        black3 = os.path.basename(b3.filename)
        open("../products" + black3, "wb").write(b3.file.read())
        blue1 = os.path.basename(s1.filename)
        open("../products" + blue1, "wb").write(s1.file.read())
        blue2 = os.path.basename(s2.filename)
        open("../products" + blue2, "wb").write(s2.file.read())
        blue3 = os.path.basename(s3.filename)
        open("../products" + blue3, "wb").write(s3.file.read())
        brown1 = os.path.basename(br1.filename)
        open("../products" + brown1, "wb").write(br1.file.read())
        brown2 = os.path.basename(br2.filename)
        open("../products" + brown2, "wb").write(br2.file.read())
        brown3 = os.path.basename(br3.filename)
        open("../products" + brown3, "wb").write(br3.file.read())

        query= f"""INSERT INTO `product`( `productname`, `size`, `quantity`, `caption`, `price`, `type`,`imageblack`, `imageblack2`, 
        `imageblack3`, `imageblue`, `imageblue2`, `imageblue3`,  `imagebrown`, `imagebrown2`, `imagebrown3`, `companyname`) 
        VALUES  ('{name}','{size}','{quantity}','{caption}','{price}','{type}','{black1}','{black2}','{black3}','{blue1}','{blue2}',
        '{blue3}','{brown1}','{brown2}','{brown3}','{companyname[0][1]}')"""
        cur.execute(query)
        con.commit()
        print(""" <script>
                    alert("Product added successfully!");
                    </script>""")

