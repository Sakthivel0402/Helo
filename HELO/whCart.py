#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cname = store.getvalue("cname")
wid = store.getvalue("id")
productid = store.getvalue("pid")
q = f"""select * from whoregistration where id='{wid}'"""
cur.execute(q)
query = cur.fetchall()
wholesalername = (query[0][1])

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>wholesaler's cart</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
     *{
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
     }
.discount-info {
    margin-left:10px !important;
}

.fun{
margin-left:50px !important
}
</style>
</head>
<body>""")
print(f"""  <div class="d-flex justify-content-center mb-4"><h1>{wholesalername}'s Cart</h1></div>
  <a href="./userLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-2 flex-column flex-shrink-0 p-3 bg-light" id="sidebar" style="min-height:100%;">
                <ul class="nav nav-pills flex-column ">

 <li class="nav-item ">
    <a class="nav-link " href="./whDashboard.py?id={wid}" >
                      Dashboard
                  </a>
              </li>
                    <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./whMenproducts.py?id={wid}">Mens</a></li>
                      <li><a class="dropdown-item" href="./womenallproducts.py?id={wid}">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link active" href="./whCart.py?id={wid}" >
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
                      <li><a class="dropdown-item" href="./whOrderstatus.py?id={wid}">Order status</a></li>


                  </ul>
              </li>
                </ul>
            </div>""")

q1query = f"""select quantity from product where `id`='{productid}'"""
cur.execute(q1query)
q1 = cur.fetchone()

q2 = f"""select * from whorder where wholesalername='{wholesalername}' AND cartstatus=''"""
cur.execute(q2)
query2 = cur.fetchall()

if query2:
    orderid = query2[0][0]
    print("""
    <div class="col-md-8 d-flex flex-column flex-grow-1 p-3">
    <div class="container">
        <div class="row fw-light">
            <div class="col-md-7">PRODUCT</div>
            <div class="col-md-3">QUANTITY</div>
            <div class=" col-md-2 ">TOTAL
            </div>
        </div>""")
    for i in query2:
        print(f"""<form method="post"> 
        <div class="row mt-3 d-flex" id="container{i[0]}" >
<div id="carouselExampleAutoplaying{i[0]}"  class="carousel slide" data-bs-ride="carousel rounded-2" style="height:300px; width:250px">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./Assets/images/{i[4]}" class="d-block" style="height:300px; width:250px">      
    </div>
    <div class="carousel-item">
      <img src="./Assets/images/{i[5]}" class="d-block" style="height:300px; width:250px">
    </div>
    <div class="carousel-item">
      <img src="./Assets/images/{i[6]}" class="d-block" style="height:300px; width:250px">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying{i[0]}" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying{i[0]}" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>            <div class="col-md-3 ml-1 mt-3"><h5 >{i[7]}</h5>&#8377<span class="price{i[0]} mt-3">{i[8]}.00 </span>
                    <div class="col-md-3 ml-1 mt-3"><h6>Size: {i[9]} </h6> </div>
            <div> <input type="submit" name="order" class="btn btn-primary mt-4" value="Order now"> 
            <input type="hidden" name="order3" value='{i[0]}'>
            </div></div>
            <div class="col-md-1"><input type="hidden" name="delete" value='{i[0]}'> <input type="submit" value="&#128465;" title="remove" style="border:none; background-color: #f8f9fa;  height: 40px; width: 40px;font-weight: 600;" name="trash1"> </div>
            <div class="col-md-2" style="display: flex; flex-direction: row;"><div class=" btn1{i[0]} border me-2" style="cursor: pointer; width: 50px; height: 40px; font-weight: 500; font-size: 25px; text-align: center;" onclick="subtraction()">-</div>
            <input type="text" value="1"  style="cursor: pointer; width: 60px; height: 40px; font-size: 20px; text-align: center;" name="quantity" class="calc form-control mb-5" id="calc{i[0]}">
            <div  style="cursor: pointer; width: 50px; height: 40px;font-weight: 500; font-size: 25px; text-align: center;" class="btn2{i[0]} border ms-2">+</div>
             </div> 
            <div class="col-md-2 d-flex justify-content-center fun  mx-5  ">&#8377  <div id="total{i[0]}"></div> <input type="hidden" id="total2{i[0]}"  name="total"> </div>
             <div  class="discount-info col-md-3 mt-5 "></div> 
             <div class="discount-info col-md-3 mt-5 "></div> 
             <div  class="discount-info col-md-3 mt-5 "></div> 
             <div  id="discount{i[0]}" class=" col-md-12 mt-5 helo fw-bold "></div> 
            

            <input type="hidden" name="image" value='{i[4]}'>
            <input type="hidden" name="caption" value='{i[7]}'>
            <input type="hidden" name="price" value='{i[8]}'>
            <input type="hidden" name="color" value='{i[9]}'>
            <input type="hidden" name="size" value='{i[10]}'> 
             <input type="hidden" name="order2" value='{wid}'> 
            </div> 
            </div>        
            </div>
           </form>

       <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const price{i[0]} = parseFloat(document.querySelector('.price{i[0]}').innerText);
        const plus{i[0]} = document.querySelector('.btn2{i[0]}');
        const minus{i[0]} = document.querySelector('.btn1{i[0]}');
        const input{i[0]} = document.querySelector('#calc{i[0]}');
        const totalprice{i[0]} = document.querySelector('#total{i[0]}');
        const totalprice2{i[0]} = document.querySelector('#total2{i[0]}');
        const discountElement{i[0]} = document.querySelector('#discount{i[0]}');
        
        input{i[0]}.value = 25;
        let discountRate{i[0]} = 0; 

        function updateTotal{i[0]}() {{
            let quantity{i[0]} = parseInt(input{i[0]}.value);
            let baseTotal{i[0]} = price{i[0]} * quantity{i[0]};
            
            let discountAmount{i[0]} = baseTotal{i[0]} * (discountRate{i[0]} / 100);
            let totalWithDiscount{i[0]} = baseTotal{i[0]} - discountAmount{i[0]};

            totalprice{i[0]}.innerText = totalWithDiscount{i[0]}.toFixed(2);    
            totalprice2{i[0]}.value = totalWithDiscount{i[0]};

            discountElement{i[0]}.innerHTML = `<br>Percentage : ${{discountRate{i[0]}}}% <br> Amount : ${{discountAmount{i[0]}}}`;
        }}

        plus{i[0]}.addEventListener('click', function() {{
            let currentQuantity{i[0]} = parseInt(input{i[0]}.value);
            if (currentQuantity{i[0]} + 25 <= 200) {{
                input{i[0]}.value = currentQuantity{i[0]} + 25;

                discountRate{i[0]} += 2.5;
                if (discountRate{i[0]} > 50) discountRate{i[0]} = 50; 
                
                updateTotal{i[0]}();
            }} else {{
                alert("Maximum quantity limit is 200");
            }}
        }});

        minus{i[0]}.addEventListener('click', function() {{
            let currentQuantity{i[0]} = parseInt(input{i[0]}.value);
            if (currentQuantity{i[0]} > 25) {{
                input{i[0]}.value = currentQuantity{i[0]} - 25;

                discountRate{i[0]} -= 2.5;
                if (discountRate{i[0]} < 0) discountRate{i[0]} = 0;

                updateTotal{i[0]}();
            }}
        }});

        updateTotal{i[0]}();  
    }});
</script>

""")
else:
    print(f"""<h2 class="text-warning" style="color: black; text-align: center;">No active orders found for {wholesalername}.</h2> """)
print("""</div>
  </div>
  </div>
  </div>
  </div>
</body>
</html>
 """)

order = store.getvalue("order")
order2 = store.getvalue("order2")
order3 = store.getvalue("order3")
trash1 = store.getvalue("trash1")

if trash1 is not None:
    delete = f"""DELETE FROM whorder WHERE id='{order3}'"""
    cur.execute(delete)
    con.commit()
    print(f"""<script>alert("Product removed!"); location.href = "whCart.py?id={wid}&cname={cname}"</script>""")

if order is not None:
    quantity = store.getvalue("quantity")
    total = store.getvalue("total")
    image = store.getvalue("image")
    caption = store.getvalue("caption")
    price = store.getvalue("price")
    color = store.getvalue("color")
    size = store.getvalue("size")

    if q1 is None or q1[0] is None:
        print("<script>alert('Product not found or no quantity available.');</script>")
    else:
        totalquantity = int(q1[0])

        if quantity is None:
            print("<script>alert('Invalid quantity entered.');</script>")
        else:
            if totalquantity >= int(quantity):
                calc = totalquantity - int(quantity)
                values = f"""update `product` set `quantity`='{calc}' where `id`='{productid}'"""
                cur.execute(values)
                con.commit()
                add = f"""UPDATE  `whorder` SET  `image`='{image}', `caption`='{caption}', `price`='{price}', `quantity`='{quantity}', `total`='{total}', `wholesalername`='{wholesalername}' ,`cartstatus`='moved' where `wholesalername`='{wholesalername}' AND id={order3}"""
                cur.execute(add)
                con.commit()
                print(f"""<script>  alert("Product moved to order page!"); 
                    location.href="whNeworders.py?id={wid}&cname={cname}&pid={productid}&oid={orderid}"</script>""")

            else:
                outofstock = f"""delete from `whorder` where id='{orderid}'"""
                cur.execute(outofstock)
                con.commit()
                print(f"""<script> alert("Not enough stock available. {totalquantity} items left. Shop other products"); 
                                                  location.href = "whMenallproducts.py?id={wid}&cname={cname}"; </script>""")

