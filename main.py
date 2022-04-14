from flask import Flask, render_template,request,redirect
import sqlite3
con = sqlite3.connect("Login.db", check_same_thread= False)
cursor = con.cursor()
listOfTables = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='LOG' ").fetchall()
if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE LOG(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        FIRSTNAME TEXT,LASTNAME TEXT ,MOBILENUMBER TEXT,EMAILID TEXT,PASSWORD TEXT); ''')


print("Table1 has created")
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def dash():
    return render_template("dashboard.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        getemail = request.form['email']
        getpassword = request.form['passpassword']
        print(getemail)
        print(getpassword)

    try:
        query = "SELECT * FROM LOG WHERE EMAIL='" + getemail + "' AND pass='" + getpassword + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        if len(result) == 0:
            print("Invalid USER")
        else:
            return redirect("/")

    except Exception as e:
        print(e)

    return render_template("login.html")

@app.route("/registration", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        getfirstname = request.form['firstname']
        getlastname = request.form['lastname']
        getemail = request.form['email']
        getmobile= request.form['mobile']
        getpassword = request.form['password']

        print(getfirstname)
        print(getlastname)
        print(getmobile)
        print(getemail)
        print(getpassword)

    try:
        query = cursor.execute(
            "INSERT INTO LOG (FIRSTNAME,LASTNAME,MOBILENUMBER,EMAILID,PASSWORD)VALUES('"+getfirstname+"','"+getlastname+"','"+getmobile+"','"+getemail+"','"+getpassword+"')")
        print(query)
        con.commit()
        return redirect("/login")
    except Exception as e:
        print(e)

    return render_template("registration.html")

@app.route("/glocery")
def glos():
    return render_template("glocery.html")


@app.route("/mobiles")
def mob():
    return render_template("mobiles.html")


@app.route("/electronics")
def elect():
    return render_template("electronics.html")


@app.route("/decorate")
def dec():
    return render_template("decorate.html")


@app.route("/sports")
def sports():
    return render_template("sports.html")


@app.route("/books")
def books():
    return render_template("books.html")


@app.route("/toys")
def toys():
    return render_template("toys.html")

if(__name__) == "__main__":
    app.run(debug=True)
