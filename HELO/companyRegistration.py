#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="ecommerce")
cur = con.cursor()
query2="""select max(id) from companyregistration"""
cur.execute(query2)
company=cur.fetchone()

if company[0]!=None:
    if company[0]<10:
        comnum="CO000"+str(company[0]+1)
    elif company[0]<100:
        comnum = "CO00" + str(company[0]+1)
    elif company[0]<1000:
        comnum = "CO0" + str(company[0]+1)
else:
    comnum="CO0001"






print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
</head>
<body>
  <div class="d-flex justify-content-center mb-4"><h1>Company Registration</h1></div>
   
    <div class="container mt-5">           
            <div class="col-md-9 col-lg-12 d-flex flex-column flex-grow-1 p-5 border ">
                <form action="" method="post" enctype="multipart/form-data">
              <h3>Company</h3>
                <div class="row mt-3">
                  <div class="col-md-4"><input type="text" name="companyname" class="form-control" placeholder="Companyname" id=""></div>
                  <div class="col-md-4"><input type="text" name="contactpersonname" class="form-control" placeholder="Contact person name" id=""></div>
                  <div class="col-md-4"><input type="text" name="contactnumber" class="form-control" placeholder="Contact person number" id=""></div>
                </div>
                <div class="row mt-5 ">
                    <div class="col-md-3"></div>
                    <div class="col-md-3"><input type="text" name="email" class="form-control" placeholder="Company mail" id=""></div>
                    <div class="col-md-3 mb-5"><input type="text" name="companynumber" class="form-control" placeholder="Company Phone" id=""></div>
                    <div class="col-md-3"></div>
            </div>

             <h3>Wholesaler Address</h3>
              <div class="row mt-4">
                <div class="col-md-4"><input type="text" name="address1" class="form-control" placeholder="Address line1" id=""></div>
                <div class="col-md-4"><input type="text" name="address2" class="form-control" placeholder="Address line2" id=""></div>
                <div class="col-md-4"><select class="form-select" name=city aria-label="Default select example">
                  <option selected>City</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Coimbatore">Coimbatore</option>
                  <option value="Erode">Erode</option>
                </select></div>
              </div>
              <div class="row mt-3 mb-5 ">
                <div class="col-md-4"><input type="text" name="zipcode" class="form-control" placeholder="Zipcode" id=""></div>
                <div class="col-md-4"><select name="state"  class="form-select" aria-label="Default select example">
                  <option selected>State</option>
                  <option value="Tamilnadu">Tamilnadu</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Andrapradhesh">Andrapradhesh</option>
                </select></div>
                <div class="col-md-4"><input type="text" name="country" class="form-control" placeholder="Country" id=""></div>
              </div>
    
              <h3>Additional Details</h3>
               <div class="row mt-3"><div class="col-md-3 mt-4"><select name="companytype" class="form-select" aria-label="Default select example">
                <option selected>Type of company</option>
                <option value="Corporation">Corporation</option>
                <option value="Partnership">Partnership</option>
                <option value="Limited Liablity Company(LLC)">Limited Liablity Company(LLC)</option>
                <option value="Sole partnership">Sole partnership</option>
              </select></div>
              <div class="mb-3 mt-4 col-md-3">
                <input type="text" name="website" class="form-control" placeholder="Business website" id=""></div>
              <div class="col-md-3"><label for="">Years in business</label><input class="form-control" placeholder="Ex: 5 years" name="years">
              </div>
              <div class="col-md-3 mt-4">
                <input type="text" name="revenue" class="form-control" placeholder="Annual revenue" id=""></div>

            </div>   
            <div class="row mt-3">
                <div class="col-md-3">
                    <label for="formFile" class="form-label " >ISO Certificate</label>
                    <input class="form-control" name="iso" type="file" id="formFile">
                </div>
                <div class="col-md-3"><label for="">Tax ID number</label><input class="form-control" placeholder="Ex: PNEV123456" name="taxid">
                </div>
              
              <div class="col-md-3"><label for="">Business License number</label><input class="form-control" placeholder="Ex: 632589741" name="license">
              </div>
              <div class="col-md-3">
                <label for="formFile" class="form-label ">PAN Proof</label>
                <input class="form-control " name="pan" type="file" id="formFile">
            </div>""")
print(f"""
            <div class="row">
                    <div class="col-md-4">
                    </div>
                    <div class="col-md-4 mt-3">
                        <label for="">Company ID</label>
                        <input type="text" class="form-control" id="" value="{comnum}" name="companyid">
                    </div>
                    <div class="col-md-4">
                    </div>
            </div>

              <div class="d-flex justify-content-center mt-5 ">
              <a href="./index.py" class="btn btn-danger me-5 ">Back</a>
              <input type="submit" class="btn btn-primary" value="Register" name="submit" >
              
            </div>
            </div> 
                 <div class=""> <a href="./companyLogin.py" class="text-primary text-decoration-none">Already have an account?</a></div>

        </form> 
            </div>
            </div>
  </body>
</html>
""")

submit= store.getvalue("submit")
if submit is not None:
    if len(store) != 0:
        companyname = store.getvalue("companyname")
        contactname = store.getvalue("contactpersonname")
        mail = store.getvalue("email")
        contactnumber = store.getvalue("contactnumber")
        companynumber = store.getvalue("companynumber")
        add1 = store.getvalue("address1")
        add2 = store.getvalue("address2")
        city = store.getvalue("city")
        zip = store.getvalue("zipcode")
        state = store.getvalue("state")
        country = store.getvalue("country")
        typeofcompany = store.getvalue("companytype")
        website = store.getvalue("website")
        yearsinbusiness = store.getvalue("years")
        revenue = store.getvalue("revenue")
        companyid = store.getvalue("companyid")
        taxid = store.getvalue("taxid")
        license = store.getvalue("license")
        iso = store['iso']
        pan = store['pan']
        if iso.filename and pan.filename:
            proof1 = os.path.basename(iso.filename)
            open("Assets/images/" + proof1,"wb").write(iso.file.read())
            proof2 = os.path.basename(pan.filename)
            open("Assets/images/" + proof2, "wb").write(pan.file.read())
            mail = store.getvalue("email")
            emailquery = """select companymail from companyregistration"""
            cur.execute(emailquery)
            emailloop = cur.fetchall()
            c = 0
            for i in emailloop:
                if i[0] == mail:
                    c += 1
            if c > 0:
                print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
            else:
                query = f""" insert into companyregistration (companyname,contactpersonname,contactpersonnumber,companymail,companyphone,address1,address2,city,zipcode,state,country,typeofcompany,businesswebsite,yearsinbusiness,annualrevenue,isocertificate,taxidnumber,businesslicensenumber,panproof, companyid,status) values ('{companyname}','{contactname}','{contactnumber}','{mail}','{companynumber}','{add1}','{add2}','{city}','{zip}','{state}','{country}','{typeofcompany}','{website}','{yearsinbusiness}','{revenue}','{proof1}','{taxid}','{license}','{proof2}','{companyid}',"pending")"""
                cur.execute(query)
                con.commit()
                print(""" 
                  <script>
                  alert("Company registered!");
                  </script>""")
