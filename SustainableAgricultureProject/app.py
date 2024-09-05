from flask import Flask, render_template, request, redirect, flash, url_for, session
import MySQLdb
import time
import subprocess
import os

app = Flask (__name__)
app.secret_key = "secret key"

@app.route('/')
@app.route("/index")
def index1():
    return render_template('index.html')


# Admin Login
@app.route("/adminlogin", methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        uid=request.form["uid"]
        pwd=request.form["pwd"]

        if uid=="Admin" and pwd=="Admin":
            return render_template("adminhome.html")
        else:
            return render_template("adminlogin.html", msg="Your Login attempt was not successful. Please try again!!")
    return render_template("adminlogin.html")

#New Farmer Registration
@app.route("/farmerregistration", methods=["GET", "POST"])
def user_registration():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()

    if request.method == "POST" :
        if request.form["b1"] == "Register":
            uname = request.form["uname"]
            c1.execute("select * from farmertable where uname='%s'" % uname)
            row = c1.fetchone()
            if (row is not None):
                return render_template("farmerregistration.html", msg="User Name Already Found!!")

            name = request.form["name"]
            gender = request.form["gender"]
            age = int(request.form["age"])
            address = request.form["address"]
            cname = request.form["cname"]
            mno = request.form["mno"]
            pword = request.form["pword"]

            c1.execute("insert into farmertable(name,gender,age,address,cname,mno,uname,pword) values('%s','%s','%d','%s','%s','%s','%s','%s')" %(name,gender,age,address,cname,mno,uname,pword))
            db.commit()

            return render_template("farmerregistration.html", msg="User Details Inserted!!!")

    return render_template("farmerregistration.html", msg="")


# Admin View Farmer
@app.route("/adminviewfarmer")
def admin_viewuser():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("select * from farmertable")
    data = c1.fetchall()
    return render_template("adminviewfarmer.html", data=data)


# Farmer Login
@app.route("/farmerlogin", methods=["GET","POST"])
def userlogin():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "agridb")
        c1 = db.cursor()
        uname=request.form["uname"]
        pword=request.form["pword"]

        c1.execute("select * from farmertable where uname='%s' and pword='%s'"%(uname,pword))
        if c1.rowcount>=1:
            row=c1.fetchone()
            session["uname"]=uname
            return render_template("farmerhome.html", msg="")
        else:
            return render_template("farmerlogin.html", msg="Your Login attempt was not successful. Please try again!!")

    return render_template("farmerlogin.html")

#Farmer View Profile
@app.route("/farmerviewprofile")
def user_viewprofile():
    db=MySQLdb.connect("localhost","root","","agridb")
    c1 = db.cursor()
    uname=session["uname"]

    c1.execute("select * from farmertable where uname='%s'"%uname)
    if c1!=None:
        row=c1.fetchall()
        print(row)
        return render_template("farmerviewprofile.html", data=row)

#Admin Add Plant Information
@app.route("/adminaddplantinfo", methods=["GET", "POST"])
def admin_addlandinfo():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()

    if request.method == "POST" :
        if request.form["b1"] == "Add":

            pname = request.form["pname"]
            f1 = request.files['pimage']
            f1.save(os.getcwd() + "\\static\\plantimage\\" + f1.filename)
            pimage = f1.filename
            plocation = request.form["plocation"]

            devicename = request.form["devicename"]
            devicedesc = request.form["devicedesc"]

            f2 = request.files['devicevideo']
            f2.save(os.getcwd() + "\\static\\devicevideo\\" + f2.filename)
            devicevideo = f2.filename



            c1.execute("insert into planttable(pname,pimage,plocation,devicename,devicedesc,devicevideo) values('%s','%s','%s','%s','%s','%s')" %(pname,pimage,plocation,devicename,devicedesc,devicevideo))
            db.commit()

            return render_template("adminaddplantinfo.html", msg="Plant Details Successfully Inserted!!!")

    return render_template("adminaddplantinfo.html", msg="")

# Admin View Plant Information
@app.route("/adminviewplantinfo", methods=["GET", "POST"])
def admin_viewlandinfo():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("select * from planttable")
    data = c1.fetchall()
    return render_template("adminviewplantinfo.html", data=data)

#Admin Delete Plant Information
@app.route("/admindeleteplantinfo", methods=["GET", "POST"])
@app.route("/admindeleteplantinfo/<int:pid>", methods=["GET", "POST"])
def admin_deletelandinfo(pid):
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("delete from planttable where  pid='%d'" %(pid))
    db.commit()

    c1.execute("select * from planttable")
    row = c1.fetchall()
    return render_template("adminviewplantinfo.html", data=row, msg="")



#Admin Add Cost Information
@app.route("/adminaddcostinfo", methods=["GET", "POST"])
def admin_addcostinfo():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("select pid,pname from planttable where pid not in (select pid from costtable)")
    row1 = c1.fetchall()
    if request.method == "POST" :
        if request.form["b1"] == "Add":

            pid = int(request.form["pname"])
            if(pid==0):
                return render_template("adminaddcostinfo.html", data1=row1, msg="Select Plant Name!!!")

            pname =""
            for x in row1:
               if (int (x[0])==pid):
                   pname =x[1]
                   break

            nodevice =int(request.form["nodevice"])
            cost=float(request.form["cost"])
            c1.execute("insert into costtable values('%d','%s','%d','%f')" %(pid,pname,nodevice ,cost))
            db.commit()
            c1.execute("select pid,pname from planttable where pid not in (select pid from costtable)")
            row1 = c1.fetchall()
            return render_template("adminaddcostinfo.html",data1=row1 ,msg="Cost Details Successfully Inserted!!!")

    return render_template("adminaddcostinfo.html",data1=row1 , msg="")


# Admin View Cost Information
@app.route("/adminviewcostinfo", methods=["GET", "POST"])
def admin_viewcostinfo():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("select * from costtable")
    data = c1.fetchall()
    return render_template("adminviewcostinfo.html", data=data)

#Admin Delete Cost Information
@app.route("/admindeletecostinfo", methods=["GET", "POST"])
@app.route("/admindeletecostinfo/<int:pid>", methods=["GET", "POST"])
def admin_deletecostinfo(pid):
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("delete from costtable where  pid='%d'" %(pid))
    db.commit()

    c1.execute("select * from costtable")
    row = c1.fetchall()
    return render_template("adminviewcostinfo.html", data=row, msg="")






# Farmer Find Plant Device Information"
@app.route("/farmerfindplantdevice", methods=["GET", "POST"])
def farmer_findplantdevice():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    if request.method == "POST":
        if request.form["b1"] == "Find":
            f1 = request.files['pimage']
            #f1.save(os.getcwd() + "\\static\\plantimage\\" + f1.filename)
            pimage = f1.filename
            plocation = request.form["plocation"]
            c1.execute("select * from planttable where pimage='%s' and plocation='%s'" %(pimage,plocation))
            data = c1.fetchall()
            if (len(data)==0):
                return render_template("farmerfindplantdevice.html",msg="Record Not Found!!!")
            else:
                return render_template("farmerviewplantdevice.html", data=data)

    return render_template("farmerfindplantdevice.html")


#Farmer View Device Cost
@app.route("/farmerviewdevicecost", methods=["GET", "POST"])
def farmer_viewdevicecost():
    db = MySQLdb.connect("localhost", "root", "", "agridb")
    c1 = db.cursor()
    c1.execute("select pid,pname from costtable ")
    row1 = c1.fetchall()
    if request.method == "POST" :
        if request.form["b1"] == "View":

            pid = int(request.form["pname"])
            if(pid==0):
                return render_template("farmerviewdevicecost.html", data1=row1, msg="Select Plant Name!!!")

            c1.execute("select pname,nodevice,cost from costtable where pid='%d'" %(pid))
            data = c1.fetchall()
            pname=""
            nodevice=0
            cost=0
            if (len(data)!=0):
                rec =data [0]
                pname =rec [0]
                nodevice =int(rec[1])
                cost =float (rec[2])

                noacre =int(request.form["noacre"])
                nodevice1 =nodevice * noacre
                totcost=cost * noacre

                return render_template("farmerviewdevicecost1.html",msg="",pname=pname, noacre=noacre, nodevice=nodevice1, totcost=totcost)

    return render_template("farmerviewdevicecost.html",data1=row1 , msg="")





if __name__ == "__main__":
    app.run (debug=True)