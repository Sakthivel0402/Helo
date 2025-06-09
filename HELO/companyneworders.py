#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
cid = store.getvalue("id")

query = f"""select * from companyregistration where `id`='{cid}'"""
cur.execute(query)
all = cur.fetchall()
cname=all[0][1]

products = f"""select * from userorder where `cname`='{cname}' and `orderstatus`='processed' and `companystatus`='' """
cur.execute(products)
user = cur.fetchall()

products2 = f"""select * from whorder where `cname`='{cname}' and `orderstatus`='processed' and `companystatus`='' """
cur.execute(products2)
wholesaler = cur.fetchall()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Various Company Products</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<body>
    <div class="d-flex justify-content-center mb-4">
        <h1>New Orders</h1>
    </div>
    <a href="./companyLogin.py" class="btn btn-danger h-25 me-5 float-end">Logout</a>

    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="./companyDashboard.py?id={cid}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./addProduct.py?id={cid}">Add Products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./existingProducts.py?id={cid}">Existing Products</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Orders</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./companyneworders.py?id={cid}">New Orders</a></li>
                            <li><a class="dropdown-item" href="./companyOldorders.py?id={cid}">Old Orders</a></li>
                            <li><a class="dropdown-item" href="./companyCancelledorders.py?id={cid}">Cancelled Orders</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">""")

if user:
    print(f""" <h2 class='mt-'>User orders:</h2>      
        <table class="table mt-1 table-bordered">
            <thead class="thead-dark">
                <tr class="table-dark">
                    <th scope="col">Order ID</th>
                    <th scope="col">Image</th>
                    <th scope="col">Caption</th>
                    <th scope="col">Price</th>
                    <th scope="col">Color</th>
                    <th scope="col">Size</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total</th>
                    <th scope="col">Action</th>
                </tr>
            </thead>
            <tbody>""")

    for i in user:
        print(f"""
        <tr>
            <form method="post" enctype="multipart/form-data">
                <td>{i[19]}</td>
                <td>{i[6]}</td>
                <td>{i[7]}</td>
                <td>{i[8]}</td>
                <td>{i[9]}</td>
                <td>{i[10]}</td>
                <td>{i[11]}</td>
                <td>{i[15]}</td>
                <td>
                    <input type="submit" value="Accept" class="btn btn-success" name="accept">
                    <input type="submit" value="Decline" class="btn btn-danger" name="decline">
                    <input type="hidden" name="thisid" value="{i[0]}">
                </td>
            </form>
        </tr>""")

    print("""
        </tbody>
    </table>
    """)
else:
    print("<h2 class='mb-5'>Users: No new orders found.</h2>")

accept = store.getvalue("accept")
if accept != None:
    thisid=store.getvalue("thisid")
    status=f"""update `userorder` set `companystatus`='C TO A' where `id`='{thisid}'"""
    cur.execute(status)
    con.commit()
    print(f"""<script> alert("Product ready to deliver!");
                        location.href = "companyneworders.py?id={cid}&cname={cname}&oid={thisid}"</script>""")

decline=store.getvalue("decline")
if decline!=None:
    thisid=store.getvalue("thisid")
    status2=f"""update `userorder` set `companystatus`='cancelled' where `id`='{thisid}'"""
    cur.execute(status2)
    con.commit()
    print(f"""<script> alert("Product cancelled!");
                            location.href = "companyneworders.py?id={cid}&cname={cname}&oid={thisid}"</script>""")


if wholesaler:
    print(f"""     <h2 class='mt-5'>Wholesaler orders:</h2> 
            <table class="table mt-1 table-bordered mt-">
                <thead class="thead-dark">
                    <tr class="table-dark">
                        <th scope="col">Order ID</th>
                        <th scope="col">Image</th>
                        <th scope="col">Caption</th>
                        <th scope="col">Price</th>
                        <th scope="col">Color</th>
                        <th scope="col">Size</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Total</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>""")

    for i in wholesaler:
        print(f"""
            <tr>
                <form method="post" enctype="multipart/form-data">
                    <td>{i[19]}</td>
                    <td>{i[6]}</td>
                    <td>{i[7]}</td>
                    <td>{i[8]}</td>
                    <td>{i[9]}</td>
                    <td>{i[10]}</td>
                    <td>{i[11]}</td>
                    <td>{i[15]}</td>
                    <td>
                        <input type="submit" value="Accept" class="btn btn-success" name="accept2">
                        <input type="submit" value="Decline" class="btn btn-danger" name="decline2">
                        <input type="hidden" name="oid2" value="{i[0]}">
                    </td>
                </form>
            </tr>""")
        print("""
                </tbody>
            </table>
            """)
else:
    print("<h2>Wholesalers: No new orders found.</h2>")

print("""
        </div>
    </div>
</body>
</html>""")

accept2 = store.getvalue("accept2")
if accept2 != None:
    oid2=store.getvalue("oid2")
    status3=f"""update `whorder` set `companystatus`='C TO W' where `id`='{oid2}'"""
    cur.execute(status3)
    con.commit()
    print(f"""<script> alert("Product ready to deliver!");
                        location.href = "companyneworders.py?id={cid}&cname={cname}&oid={oid2}"</script>""")

decline2=store.getvalue("decline2")
if decline2!=None:
    oid2=store.getvalue("oid2")
    status4=f"""update `whorder` set `companystatus`='cancelled' where `id`='{oid2}'"""
    cur.execute(status4)
    con.commit()
    print(f"""<script> alert("Product cancelled!");
                            location.href = "companyneworders.py?id={cid}&cname={cname}&oid={oid2}"</script>""")
