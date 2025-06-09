#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
eid = store.getvalue("id")

userdetails = """select * from `userorder` where  `deliverystatus`='picked' and `finalstatus`=''"""
cur.execute(userdetails)
user = cur.fetchall()

wholesalerdetails = """select * from `whorder` where `deliverystatus`='picked' and `finalstatus`=''"""
cur.execute(wholesalerdetails)
wholesaler = cur.fetchall()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delivery Department</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
    }}
    </style>
    <script>
    function toggleOrders() {{
        var userRadio = document.getElementById('userRadio');
        var wholesalerRadio = document.getElementById('wholesalerRadio');
        var userOrders = document.getElementById('userOrders');
        var wholesalerOrders = document.getElementById('wholesalerOrders');

        console.log("User Radio Checked:", userRadio.checked);
        console.log("Wholesaler Radio Checked:", wholesalerRadio.checked);

        if (userRadio.checked) {{
            userOrders.style.display = 'block';
            wholesalerOrders.style.display = 'none';
        }} else if (wholesalerRadio.checked) {{
            userOrders.style.display = 'none';
            wholesalerOrders.style.display = 'block';
        }}
    }}

    window.onload = function() {{
        toggleOrders();
    }};
    </script>
</head>
<body>
 <div class="d-flex justify-content-center mb-4"><h1>Orders (Delivery)</h1></div>
    <a href="./AdminLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="./deliveryDashboard.py?id={eid}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./deliveryProductRequest.py?id={eid}">Product requests</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="./ondeliveryProducts.py?id={eid}">Ondelivery products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./completedOrders.py?id={eid}">Completed orders</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./deliveryEmployeeProfile.py?id={eid}">Profile</a>
                    </li>
                </ul>
            </div>

            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">
                <h3 class="mb-5">Select Order Type:</h3>
              
    <div class="container">
        <div class="form-check">
            <input type="radio" class="form-check-input" id="userRadio" name="orderType" onclick="toggleOrders()" checked>
            <label class="form-check-label" for="userRadio">User Orders</label>
        </div>
        <div class="form-check">
            <input type="radio" class="form-check-input" id="wholesalerRadio" name="orderType" onclick="toggleOrders()">
            <label class="form-check-label" for="wholesalerRadio">Wholesaler Orders</label>
        </div>

        <div id="userOrders" style="display:block;">""")

if user:
    print(f"""
                    <h3 class="mt-5">User orders:</h3>
                    <table class="table mt-3 table-bordered">
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
        print(f"""<form method="post">
                            <tr>
                                <td>{i[19]}</td>
                                <td>{i[7]}</td>
                                <td><img src="./Assets/images/{i[4]}" alt="" width="100px"></td>
                                <td>{i[8]}</td>
                                <td>{i[11]}</td>
                                <td>{i[9]}</td>
                                <td><input type="submit" name="move" value="Delivered ?" class="btn btn-secondary"></td>
                                <input type="hidden" name="oid" value="{i[0]}">
                            </tr>
                            </form>""")
    print("""
                        </tbody>
                    </table>
                </div>""")
else:
    print("""<h2 class="mt-5">No User orders found.</h2>
        </div>""")

print("""<div id="wholesalerOrders" style="display:none;">""")
if wholesaler:
    print(f"""
        <h3 class="mt-5">Wholesaler orders:</h3>
        <table class="table mt-3 table-bordered">
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

    for i in wholesaler:
        print(f"""<form method="post">
            <tr>
                <td>{i[19]}</td>
                <td>{i[7]}</td>
                <td><img src="./Assets/images/{i[4]}" alt="" width="100px"></td>
                <td>{i[8]}</td>
                <td>{i[11]}</td>
                <td>{i[9]}</td>
                <td><input type="submit" name="move2" value="Delivered ?" class="btn btn-secondary"></td>
                <input type="hidden" name="oid2" value="{i[0]}">
            </tr>
            </form>""")
    print("""
            </tbody>
        </table>
    </div>""")
else:
    print("""<h2 class="mt-5">No Wholesaler orders found.</h2>

        </div>
    </div>
</body>
</html>
""")


move = store.getvalue("move")
if move is not None:
    oid = store.getvalue("oid")
    status = f"""update `userorder` set `finalstatus`='delivered' `deliverypersonId`='{eid}' where `id`='{oid}'"""
    cur.execute(status)
    con.commit()

    status2 = f"""update `empreg` set `status`='' where `id`='{eid}'"""
    cur.execute(status2)
    con.commit()

    print(
        f"""<script>alert("Product moved out for delivery!"); location.href = "ondeliveryProducts.py?id={eid}";</script>""")

move2 = store.getvalue("move2")
if move2 is not None:
    oid2 = store.getvalue("oid2")
    status = f"""update `whorder` set `finalstatus`='delivered' where `id`='{oid2}'"""
    cur.execute(status)
    con.commit()

    status2 = f"""update `empreg` set `status`='' where `id`='{eid}'"""
    cur.execute(status2)
    con.commit()

    print(f"""<script>alert("Product delivered to the wholesaler!"); location.href = "ondeliveryProducts.py?id={eid}";</script>""")
