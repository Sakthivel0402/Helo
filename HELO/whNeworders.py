#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cname = store.getvalue("cname")
wid = store.getvalue("id")
pid = store.getvalue("pid")
oid = store.getvalue("oid")

q = f"""select * from whoregistration where id='{wid}'"""
cur.execute(q)
query = cur.fetchall()
wholesaler = (query[0][1])
address = query[0][7] + " " + query[0][8] + ", " + query[0][9] + ", " + query[0][10] + ", " + query[0][11] + ", " + \
          query[0][12]

q2 = f"""select * from whorder where wholesalername='{wholesaler}' AND cartstatus='moved' and `orderstatus`=''"""
cur.execute(q2)
query2 = cur.fetchall()



stock = f"""select quantity from `whorder` where `productid`='{pid}' and id='{oid}'"""
cur.execute(stock)
stocks = cur.fetchall()

q3 = f"""select max(id) from whorder """
cur.execute(q3)
orders = cur.fetchone()

if orders != None:
    if orders[0] < 10:
        ordernum = "WORDER000" + str(orders[0])
    elif orders[0] < 100:
        ordernum = "WORDER00" + str(orders[0])
    elif orders[0] < 1000:
        ordernum = "WORDER0" + str(orders[0])
else:
    ordernum = "WORDER0001"

orderid1 = store.getvalue("orderid")

status = f"""select * from `userorder` where id='{orderid1}'"""
cur.execute(status)
changedaddress = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>new orders</title>
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
    .checkout{
        background-color: rgb(139, 219, 243);
        transition: all ease 0.6s;

    }
    .checkout:hover{
        transition: all ease 0.6s;
        background-color: rgb(37, 161, 214) !important;
    }
</style>
</head>
<body>""")

print(f"""    
         <div class="d-flex justify-content-center mb-4"><h1>Men Products</h1></div>
  <a href="./userLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">

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
                      <li><a class="dropdown-item" href="./whMenallproducts.py?id={wid}">Mens</a></li>
                      <li><a class="dropdown-item" href="./whWomenallproducts.py?id={wid}">Womens</a></li>
                  </ul>
                  </li>

                    <li class="nav-item ">
                        <a class="nav-link" href="./whCart.py?id={wid}" >
                            Cart
                        </a>
                    </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                       <li><a class="dropdown-item active" href="./whNeworders.py?id={wid}&oid={oid}">New orders</a></li>
                      <li><a class="dropdown-item" href="./whOldorders.py?id={wid}&oid={oid}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./whCancelledorders.py?id={wid}&oid={oid}">Cancelled orders</a></li>
                      <li><a class="dropdown-item" href="./whOrderstatus.py?id={wid}&oid={oid}">Order status</a></li>
                  </ul>
              </li>
                </ul>
            </div>""")
if oid is None:
    print("""<h2 class="text-warning" style="color: black; text-align: center;">No active orders found for this user.</h2>""")
else:
    q1query = f"""select quantity from product where `id`='{pid}'"""
    cur.execute(q1query)
    q1 = cur.fetchone()
    totalquantity = (int(q1[0]))
    print("""
 <div class="col-md-9 col-lg-10">
<div class="container-fluid p-2" id="container">
    <div class="row">
    <div class=" p-2 rounded-2 col-md-7 me-5" >
        <h4 class="">My Cart</h4> <hr>""")
    for i in query2:
        print(f"""  <form method="post"> <div class="container mt-4">
                <div class="row">
                <div class="col-md-4">
        <img src="./Assets/images/{i[4]}"  style="height: 200px;width: 200px; border-radius: 8px;"></div>
      <div class="col-md-4 ">  <h6 class="mt-4">{i[7]}</h6> <p class="price{i[0]} mt-4 mb-1"> {i[8]}</p>
    <p>Size: {i[9]}</p></div>        
            <div class="col-md-3 border mt-4" style="display: flex; flex-direction: row; width: 90px; height: 35px;"><div class="btn1{i[0]}"   style="cursor: pointer; height: 30px; font-weight: 500; font-size: 20px; text-align: center;">-</div>
            <input type="text" disabled value="{i[11]}" style="cursor: pointer; border: none; width: 50px; height: 25px; font-size: 15px; text-align: center; background-color:#f8f9fa;" class="calc form-control mt-1" name="quantity" id="calc{i[0]}">
            <div  style="cursor: pointer; border: none; height: 30px;font-weight: 500; font-size: 20px; text-align: center;"  class="btn2{i[0]} ms-1">+</div>
           <div class="total{i[0]} mt-5" style="margin-top: 70px !important; margin-left: -80px; font-size: 20px; font-weight: 500;"></div>
        </div> <input type="hidden" name="hidden" value="{i[8]}" >           
            <div class="col-md-2"><input type="hidden" name="delete" value='{i[0]}'> <input type="submit" value="&#128465;" title="remove" style="border:none; background-color: #f8f9fa; margin-left:50px;margin-top:20px;height: 40px; width: 40px;font-weight: 600;" name="trash1"> </div>
  <hr class="mt-4">
  <input type="hidden" name="quantity" value="{i[14]}">
  <input type="hidden" name="totalquantity" value="{totalquantity}">
</form>
    </div>
        </div> 
    """)
    print(f"""<script>
    let globaltotal=0;
    document.addEventListener('DOMContentLoaded', function() {{
        const price{i[0]} = parseFloat(document.querySelector('.price{i[0]}').innerText);
        const plus{i[0]} = document.querySelector('.btn2{i[0]}');
        const minus{i[0]} = document.querySelector('.btn1{i[0]}');
        const input{i[0]} = document.querySelector('#calc{i[0]}');
        const totalprice{i[0]} = document.querySelector('.total{i[0]}');
        const delivery{i[0]} = document.getElementById('delivery{i[0]}');
        const alltotal{i[0]} = totalprice{i[0]}.value;

        let g2{i[0]} = 0;
        let discountRate{i[0]} = 0; 

        function updateTotal{i[0]}() {{
            let quantity{i[0]} = parseInt(input{i[0]}.value);
            let baseTotal{i[0]} = price{i[0]} * quantity{i[0]};

            if (quantity{i[0]} >= 50 && quantity{i[0]} < 75) {{
                discountRate{i[0]} = 2.5;
            }} else if (quantity{i[0]} >= 75 && quantity{i[0]} < 100) {{
                discountRate{i[0]} = 5;
            }} else if (quantity{i[0]} >= 100 && quantity{i[0]} < 125) {{
                discountRate{i[0]} = 7.5;
            }} else if (quantity{i[0]} >= 125 && quantity{i[0]} < 200) {{
                discountRate{i[0]} = 10;
            }} else {{
                discountRate{i[0]} = 0;
            }}

            let discountAmount{i[0]} = baseTotal{i[0]} * (discountRate{i[0]} / 100);
            let totalWithDiscount{i[0]} = baseTotal{i[0]} - discountAmount{i[0]};
            

            totalprice{i[0]}.innerHTML = totalWithDiscount{i[0]}.toFixed(2);

            if (g2{i[0]} == 0) {{
                g2{i[0]} = totalWithDiscount{i[0]};
                globaltotal += totalWithDiscount{i[0]};
            }} else {{
                globaltotal -= g2{i[0]};
                g2{i[0]} = totalWithDiscount{i[0]};
                globaltotal += totalWithDiscount{i[0]};
            }}
            after(); 
        }}

        plus{i[0]}.addEventListener('click', function() {{
            let currentQuantity{i[0]} = parseInt(input{i[0]}.value);
            if (currentQuantity{i[0]} + 25 <= 200) {{
                input{i[0]}.value = currentQuantity{i[0]} + 25;
                updateTotal{i[0]}();
            }} else {{
                alert("Maximum quantity limit is 200");
            }}
        }});

        minus{i[0]}.addEventListener('click', function() {{
            if (input{i[0]}.value > 25) {{
                input{i[0]}.value = parseInt(input{i[0]}.value) - 25;
                updateTotal{i[0]}();
            }}
        }});

        updateTotal{i[0]}();  

       }});
</script>
""")

    print(f"""
 </div>   
        <div class=" p-2 rounded-2 col-md-4 " >
        <h4 class="">Order Summary</h4><hr>
        <div class="row mt-5 mb-3">
        <div class="col-md-6 ">Subtotal</div>
        <div class="col-md-2 "></div>
        <div id="globaltotal" class=" col-md-4 "> </div>
        </div>

        <div class="row  mb-4">
            <div class="col-md-6 ">Delivery</div>
            <div class="col-md-2 "></div>
            <div class="col-md-4 ">&#8377 50.00</div>   
        </div>
<div class="row">""")
    if changedaddress:
        for i in changedaddress:
            print(f"""
                      <div class="col-md-"><box-icon type='solid' name='map'></box-icon> <b> Deliver To:</b> <div class="col-md-">{i[13]}</div> </div>
                    <a style="color: rgb(41, 178, 219); font-size: 16px;" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Change address</a> 
              """)
    else:
        print(
            f"""<div class="col-md- "><box-icon type='solid' name='map'></box-icon> <b> Deliver To:</b> {query[0][6]}, {query[0][7]}, {query[0][8]}, {query[0][9]}, {query[0][10]}, {query[0][11]}</div>
                    <a style="color: rgb(41, 178, 219); font-size: 16px;" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Change address</a>""")

    print(f"""     
         <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Delivery Address:</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
           <form method="post">
           <input type="hidden" value="{oid}" name="orderid2">
    
           <div class="row mt-4">
            <div class="col-md-4"><input type="text" name="email" class="form-control" placeholder="Email" id=""></div>
              <div class="col-md-4"><input type="text" name="phone" class="form-control" placeholder="Phone" id=""></div> </div>
            <div class="row mt-4">
                <div class="col-md-4"><input type="text" required name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><input type="text" name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><select class="form-select" name="city" aria-label="Default select example">
                  <option selected>City</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Coimbatore">Coimbatore</option>
                  <option value="Erode">Erode</option>
                </select></div>
    
                <div class="col-md-4 mt-4 mb-5"><input type="text" name="pincode" class="form-control" placeholder="Pincode" id=""></div>
                <div class="col-md-4 mt-4 mb-5"><select name="state"  class="form-select" aria-label="Default select example">
                  <option selected>State</option>
                  <option value="Tamilnadu">Tamilnadu</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Andrapradhesh">Andrapradhesh</option>
                </select></div>
                <div class="col-md-4 mt-4 mb-5"><select name="country"  class="form-select" aria-label="Default select example">
                  <option selected>Country</option>
                  <option value="India">India</option>
                  <option value="Srilanka">Srilanka</option>
                  <option value="China">China</option>
                </select></div>
    
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
    
            <input type="submit" name="caddress" value="save" class="btn btn-primary"></form>
            </div>
            </div>
            </div>
            </div>
            </div>    
            </div>
    
    
            <div class="row mt-4 "></div>
            <hr class="mt-5">
            <div class="row mt-4">
                <div class="col-md-6 "><h5>Total</h5></div>
                <div class="col-md-2 "></div>
                <div id="gfulltotal" class="col-md-4 ">&#8377</div>
            </div>
            <div class="row" style="font-size: 14px;">(Tax included)</div>
            <div class="row d-flex justify-content-center">
    
    <form method="post"> 
                <input type="hidden" name="delicharge" value=50>
                <input type="hidden" name="deliaddress" value='{address}'>
                <input type="hidden" name="ordernum" value='{ordernum}'>
                <input type="hidden" id="ctotal" name="total">
                <input type="hidden" id="grandtotal" name="fulltotal">
                <input type="submit" value="Checkout"  class="checkout btn col-md-8 mt-4" name="checkout" >       
    </form> 
            </div>
        </div>
     <script>
                const gtotal = document.getElementById('globaltotal');
                const gfulltotal = document.getElementById('gfulltotal');
                const grandtotal= document.getElementById('grandtotal');
                const ctotal= document.getElementById('ctotal');
    
    
     setTimeout(after,600);
     function after(){{
                 g2=globaltotal;
                 gtotal.innerHTML = globaltotal;
                 gfulltotal.innerHTML= globaltotal+50;    
                 grandtotal.value=globaltotal+50; 
                 ctotal.value=globaltotal; 
    
    }}
    </script>
    </div>
    </div>
    </div> 
    
    <div class="modal fade" id="checkoutModal" tabindex="-1" aria-labelledby="checkoutModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="checkoutModalLabel">Order Confirmation</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        Your order has been placed successfully. Your order will be delivered in 3 days.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
    </body>
    </html>""")

trash1 = store.getvalue("delete")
checkout = store.getvalue("checkout")
save = store.getvalue("caddress")

if save != None:
    email = store.getvalue("email")
    phone = store.getvalue("phone")
    address1 = store.getvalue("address1")
    address2 = store.getvalue("address2")
    city = store.getvalue("city")
    pin = store.getvalue("pincode")
    state = store.getvalue("state")
    country = store.getvalue("country")
    orderid2 = store.getvalue("orderid2")
    add = f"""update `whorder` set `deliveryaddress`='{address1},{address2},{city},{pin},{state},{country},{phone},{email}', `addressstatus`='changed' where id='{orderid2}'"""
    cur.execute(add)
    con.commit()
    print(f"""<script> alert("Address updated!");
                    location.href = "whNeworders.py?orderid={orderid2}&cname={cname}&id={wid}" </script>""")

if trash1 != None:
    delete = f"""delete from `whorder` where id='{trash1}'"""
    cur.execute(delete)
    con.commit()
    print(f"""<script> alert("Product removed!");
            location.href = "whNeworders.py?id={wid}&cname={cname}" </script> """)

if checkout != None:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    deliverycharge = store.getvalue("delicharge")
    deliveryaddress = store.getvalue("deliaddress")
    total = store.getvalue("total")
    fulltotal = store.getvalue("fulltotal")
    finalorder = f"""update `whorder` set `orderDatetime`='{current_time}', `deliveryaddress`='{deliveryaddress}', `deliverycharges`='{deliverycharge}', `total`='{total}', `fulltotal`='{fulltotal}',`orderstatus`='processed',`ordernumber`='{ordernum}' where id='{oid}' """
    cur.execute(finalorder)
    con.commit()
    print(f"""<script>
                        document.addEventListener('DOMContentLoaded', function() {{
                            var checkoutModal = new bootstrap.Modal(document.getElementById('checkoutModal'));
                            checkoutModal.show();
                        }});
                        setTimeout(function() {{
                            location.href = "whmenallproducts.py?id={wid}";
                        }}, 3000); 
                    </script>""")