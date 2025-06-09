#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wholesaler Login</title>
    <link rel="stylesheet" href="boxicons.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<style>
   @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cedarville+Cursive&family=Edu+AU+VIC+WA+NT+Hand:wght@400..700&family=Pacifico&family=Playwrite+CU:wght@100..400&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'); 

form{
        display: block;
    }

*{
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
    font-weight: 400 !important;
  font-style: normal;
}

.navbar-brand{
    font-family: "Playwrite CU", cursive;
    font-size: 1.7rem !important;
    font-weight: 900 !important;
    color: black;
    animation: color-change 20s  infinite;
}

@keyframes color-change {
  0% { color: yellow; }
  10% { color: blue; }
  20% { color: rgb(179, 104, 104); }
  30% { color: rgb(27, 222, 82); }
  40% { color: rgb(183, 235, 28); }
  50% { color: rgb(250, 93, 174); }
  60% { color: rgb(6, 165, 209); }
  70% { color: rgb(59, 32, 193); }
  80% { color: rgb(179, 104, 104); }
  90% { color: rgb(132, 8, 255); }
  100% { color: rgb(255, 255, 0); }
}

.nav-item{
    margin-left: 160px;
    font-size: 17px;
}

.nav-item a{
    font-weight: 500 !important;
    color: black !important;
    transition: all 0.6s;
}
.nav-item a:hover{
    color: blue !important;
    transform: translateY(-5px);
    scale: 1.02;
    transition: all 0.6s;
}

.nav-item1 a{
    margin-left: 200px;
    font-weight: 500 !important;
    color: black !important;
    transition: all 0.6s;
}
.nav-item1 a:hover{
    color: salmon !important;
    scale: 1.01;
    transition: all 0.6s;
}
.nav-item2 a{
    margin-left: 10px;
    font-weight: 500 !important;
    color: black !important;
    transition: all 0.6s;
}
.nav-item2 a:hover{
    color: salmon !important;
    scale: 1.01;
    transition: all 0.6s;
}
.hi{
    margin-top: 10px;
    font-weight: 600 !important;
    font-size: 18px;
    margin-left: 4px;
}
.helo{
    margin-left: 150px;
}
</style>
<body>
    <nav class="navbar navbar-expand-md bg-light">
        <div class="container"><a href="./index.py" class="navbar-brand">Helo</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collaps" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span></button>       
        </div>
     </nav>
    <form class="container w-50 mt-5 bg-light p-5" method="post">
        <h1 class="ms-5 mb-4">Wholesaler Login</h1>
        <input  type="text" class="form-control mb-3" name="username" autocomplete="off" required  placeholder="Wholesaler ID">
        <input type="password" class="form-control mb-3" name="password" placeholder="Password" required>
        <input type="submit" class="w-100 text-white btn btn-primary border border-white rounded" name="submit" value="Login">
           <div class="mt-5"> <a href="./whForgetpwd.py" class="text-danger text-decoration-none">Forget password?</a></div>
              <div class="float-end"> <a href="./whRegistration.py" class="text-primary text-decoration-none">Didn't have an account?</a></div>


    </form>
    <footer class="d-block d-flex justify-content-around mt-5">CopyRight 2024 By Helo.Co</footer>

</body>
</html>
""")

submit = store.getvalue("submit")
if submit != None:
    wholesalerID = store.getvalue("username")
    password = store.getvalue("password")
    query=f"""select id from whoregistration where wholesalerid='{wholesalerID}' and password='{password}'"""
    cur.execute(query)
    idpwd=cur.fetchone()
    if idpwd!=None:
        print(f"""
        <script>alert("Login Successful!")
        location.href="whDashboard.py?id={idpwd[0]}"
        </script>""")
    else:
        print(f"""
            <script>alert("Please enter the correct ID or Password!") </script>""")


