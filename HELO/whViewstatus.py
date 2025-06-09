#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime, timedelta
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
id2 = store.getvalue("id")
oid = store.getvalue("oid")

userdetails = f"""select * from `whorder` where `companystatus`='C TO W' and id='{oid}'"""
cur.execute(userdetails)
user = cur.fetchall()
ordered = user[0][20]
shipped = user[0][21]
ontheway = user[0][22]
delivered = user[0][23]

date = user[0][24]
ordernum = user[0][19]
caption = user[0][7]
price = user[0][14]
delivery = user[0][12]
total = user[0][15]
date = date[0:10]

order_date = datetime.strptime(date, "%Y-%m-%d")
expected_delivery_date = order_date + timedelta(days=5)
expected_delivery_date_str = expected_delivery_date.strftime("%d-%m-%y")

cancel_button_disabled = 'disabled' if ontheway == 'picked' else ''

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wholesaler view status </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
        }
        span{
            color: rgb(49, 124, 209);
            font-weight: 400;
            margin-left: 6px;
        }
        body{
            background-color: #f8f9fa;
            height: 100vh;
            font-size: 14px;    
        }
        .card{
            margin: auto;
            width: 38%;
            max-width:600px;
            padding: 4vh 0;
            box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            color: #000000;
            border-left: none;
            border-right: none;
        }
        @media(max-width:768px){
            .card{
                width: 90%;
            }
        }
        .title{
            color: #3B71CA;
            font-weight: 600;
            margin-bottom: 2vh;
            padding: 0 8%;
            font-size: initial;
        }
        #details{
            font-weight: 400;
            color:#000000;
        }
        #name{
            color:#000000;
        }
        .info{
            padding: 5% 8%;
        }
        .info .col-5{
            padding: 0;
        }
        #heading{
            color: grey;
            line-height: 6vh;
        }
        .pricing{
            background-color: #ddd3;
            padding: 2vh 8%;
            font-weight: 400;
            line-height: 2.5;
        }
        .pricing .col-3{
            padding: 0;
        }
        .total{
            padding: 2vh 8%;
            color: rgb(252, 103, 49); 
            font-weight: bold;
        }
        .total .col-3{
            padding: 0;
        }
        #progressbar {
            margin-bottom: 3vh;
            overflow: hidden;
            color: #3B71CA;
            padding-left: 0px;
            margin-top: 3vh
        }
        #progressbar li {
            position: relative;
            width: 25%;
            float: left;
            list-style-type: none;
            font-size: x-small;
            color: rgb(160, 159, 159);
            text-align: center;
            transition: all 0.5s ease-in-out;
        }
        #progressbar #step1:before {
            content: "";
            color: #3B71CA;
            width: 5px;
            height: 5px;
            margin-left: 0px !important;
        }
        #progressbar #step2:before {
            content: "";
            color: #fff;
            width: 5px;
            height: 5px;
            margin-left: 32%;
        }
        #progressbar #step3:before {
            content: "";
            color: #fff;
            width: 5px;
            height: 5px;
            margin-right: 32%; 
        }
        #progressbar #step4:before {
            content: "";
            color: #fff;
            width: 5px;
            height: 5px;
            margin-right: 0px !important;
        }
        #progressbar li:before {
            line-height: 29px;
            display: block;
            font-size: 12px;
            background: #ddd;
            border-radius: 50%;
            margin: auto;
            z-index: -1;
            margin-bottom: 1vh;
        }
        #progressbar li:after {
            content: '';
            height: 2px;
            background: #ddd;
            position: absolute;
            left: 0%;
            right: 0%;
            margin-bottom: 2vh;
            top: 1px;
            z-index: 1;
        }
        .progress-track{
            padding: 0 8%;
        }
        #progressbar li:nth-child(2):after {
            margin-right: auto;
        }
        #progressbar li:nth-child(1):after {
            margin: auto;
        }
        #progressbar li:nth-child(3):after {
            float: left;
            width: 68%;
        }
        #progressbar li:nth-child(4):after {
            margin-left: auto;
            width: 132%;
        }
        #progressbar  li.active{
            color: black;
        }
        #progressbar li.active:before,
        #progressbar li.active:after {
            background: rgb(252, 103, 49);
            transition: all 0.6s ease-in-out;
        }
        #progressbar  li.active2{
            color: black;
        }
        #progressbar li.active2:before,
        #progressbar li.active2:after {
            background: green;
            transition: all 0.6s ease-in-out;
        }
        @keyframes progress {
            0% {
                width: 0%;
                background-color: #ddd;
            }
            100% {
                width: 100%;
                background-color: rgb(252, 103, 49);
            }
        }
        #progressbar li.active:after {
            animation: progress 1s ease-in-out;
        }
        #progressbar li.active:after {
            background: rgb(252, 103, 49); /* Orange color for active steps */
        }
        #progressbar li.active2:after {
            animation: progress 1s ease-in-out;
        }
        #progressbar li.active2:after {
            background: green; /* Green color for active steps */
        }
        #progressbar li.completed:after {
            background: #28a745; /* Green color for completed steps */
        }
        #progressbar li.completed:before {
            background: #28a745; /* Green color for completed step indicator */
        }
        #progressbar li:nth-child(1).completed:after {
            width: 33%;
        }
        #progressbar li:nth-child(2).completed:after {
            width: 67%;
        }
        #progressbar li:nth-child(3).completed:after {
            width: 100%;
        }
         .btn:disabled {
            background-color: grey;
            border-color: grey;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
""")
print(f"""
  <div class="d-flex justify-content-center mb-4"><h1>Wholesaler order status</h1></div>
<a href="./index.py" class="btn btn-danger  me-5 float-end">Logout</a>
    <div class="container-fluid mt-5">
        <div class="row">
            <div class="col-md-3 col-lg-2 d-flex flex-column flex-shrink-0 p-3 bg-light" id="sidebar">
                <ul class="nav nav-pills flex-column mb-auto">
                <li class="nav-item">
                  <a class="nav-link" href="./whDashboard.py?id={id2}" >
                      Dashboard
                  </a>
              </li>
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Products
                  </a>
                     <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./whmenallproducts.py?id={id2}">Mens</a></li>
                      <li><a class="dropdown-item" href="./whwomenProducts.py?id={id2}">Womens</a></li>
                  </ul>
                  </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./whCart.py?id={id2}" >
                            Cart
                        </a>
                    </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Orders
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="./whNeworders.py?id={id2}">New orders</a></li>
                      <li><a class="dropdown-item" href="./wholdOrder.py?id={id2}">Old orders</a></li>
                      <li><a class="dropdown-item" href="./whcancelledOrders.py?id={id2}">Cancelled orders</a></li>
                      <li><a class="dropdown-item" href="./whOrderstatus.py?id={id2}">Order status</a></li>
                  </ul>
              </li>
                </ul>
            </div>
            <div class="col-md-9 col-lg-10 d-flex flex-column flex-grow-1 p-3">
                <div class="card">
                    <div class="title">Purchase Receipt</div>
                    <div class="info">
                        <div class="row">
                            <div class="col-7">
                                <span id="heading">Date</span><br>
                                <span id="details">{date}</span>
                            </div>
                            <div class="col-5 pull-right">
                                <span id="heading">Order No.</span><br>
                                <span id="details">{ordernum}</span>
                            </div>
                        </div>      
                    </div>      
                    <div class="pricing">
                        <div class="row">
                            <div class="col-9">
                                <span id="name">{caption}</span>  
                            </div>
                            <div class="col-3">
                                <span id="price">&#x20b9 {price}.00</span>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-9">
                                <span id="name">Shipping</span>
                            </div>
                            <div class="col-3">
                                <span id="price">&#x20b9 {delivery}.00</span>
                            </div>
                        </div>
                    </div>
                    <div class="total">
                        <div class="row">
                            <div class="col-9"></div>
                            <div class="col-3"><big>&#x20b9; {total}.00</big></div>
                        </div>
                    </div>
                    <div class="tracking">
                        <div class="title">Tracking Order</div>
                    </div>
                    <div class="progress-track">
                        <ul id="progressbar">
    """)
if delivered != 'delivered':
    print(f"""
        <li class="step0 {'active' if ordered == 'C TO W' or shipped == 'delivery' or ontheway == 'picked' or delivered == 'delivered' else ''}" id="step1">Ordered</li>
        <li class="step0 {'active' if shipped == 'delivery' or ontheway == 'picked' or delivered == 'delivered' else ''}" id="step2">Shipped</li>
        <li class="step0 {'active' if ontheway == 'picked' or delivered == 'delivered' else ''}" id="step3">On the way</li>
        <li class="step0 {'active' if delivered == 'delivered' else ''}" id="step4">Delivered</li>""")
else:
    print(f"""
        <li class="step0 {'active2' if ordered == 'C TO W' or shipped == 'delivery' or ontheway == 'picked' or delivered == 'delivered' else ''}" id="step1">Ordered</li>
        <li class="step0 {'active2' if shipped == 'delivery' or ontheway == 'picked' or delivered == 'delivered' else ''}" id="step2">Shipped</li>
        <li class="step0 {'active2' if ontheway == 'picked' or delivered == 'delivered' else ''}" id="step3">On the way</li>
        <li class="step0 {'active2' if delivered == 'delivered' else ''}" id="step4">Delivered</li>""")
print(f"""
                        </ul>
                    </div>
                    <div class="mt-3 ms-5">
                        <span id="heading">Expected Delivery Date</span><br>
                        <span id="details">{expected_delivery_date_str}</span>
                    </div>
                    <form method="post" id="cancelForm">
                        <input type="submit" value="Cancel order" name="trash" class="mt-5 btn btn-danger w-50 mx-auto d-flex justify-content-center" {cancel_button_disabled}>
                        <div id="cancelReasons" class="mt-3 d-none">
                            <h4 class="mt-4"> <label for="reason">Reason for cancellation:</label></h4>
                            <select id="reason" name="reason" class="form-select mb-3">
                                <option value="Size mismatched">Size was mismatched</option>
                                <option value="Expected delivery time too long">Expected delivery time too long</option>
                                <option value="Color mismatched">Color was mismatched</option>
                                <option value="changed-mind">Changed my mind</option>
                            </select>
                            <h4 class="mt-4">  <label for="comments">Additional comments:</label></h4>
                            <textarea id="comments" name="comments" class="form-control" rows="3" placeholder="Enter your comments here..."></textarea>
                            <input type="submit" value="Submit Cancellation" name="trash1" class="btn btn-primary mt-3">
                        </div>
                    </form>
                    <script>
                        document.querySelector('input[name="trash"]').addEventListener('click', function(event) {{
                            event.preventDefault();
                            document.getElementById('cancelReasons').classList.remove('d-none'); 
                        }});
                    </script>
    """)

trash1 = store.getvalue("trash1")

if trash1 is not None:
    reason = store.getvalue("reason")
    comments = store.getvalue("comments")
    cancelledtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if reason and comments:
        cancel = f"UPDATE `whorder` SET `wholesalerstatus`='cancelled', `cancelreason`='{reason}', `cancelcomments`='{comments}', `cancelledtime`='{cancelledtime}' WHERE id={oid}"
        cur.execute(cancel)
        con.commit()
        print(f"<script>alert('Your order was cancelled for {reason}.'); location.href = 'whmenallproducts.py?id={id2}'</script>")
    else:
        print(f"<script>alert('Please provide a reason and comments for cancellation.');</script>")
