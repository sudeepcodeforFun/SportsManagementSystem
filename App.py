from flask import Flask, render_template, flash, request, session, send_file
from datetime import datetime
import mysql.connector


app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = 'sdssdsds15154545'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html',data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where UserName='"+ uname +"' ")
    data = cur.fetchall()
    return render_template('UserHome.html',data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['pas'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()

            flash("Your are Logged In...!")
            return render_template('AdminHome.html', data=data)

        else:
            flash("Username or Password is wrong")
            return render_template('AdminLogin.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name = request.form['name']
        gender= request.form['gender']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        pas = request.form['pas']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + uname + "' and Password='" + pas + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + gender + "','" + mobile + "','" + email + "','" + address + "','" + uname + "','" + pas + "')")
            conn.commit()
            conn.close()
            flash('New User Registered successfully')
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            return render_template('UserLogin.html', data=data)
        else:
            flash('Already registered')
            return render_template('NewUser.html')


@app.route("/userLogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        uname = request.form['uname']
        pas = request.form['pas']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + uname + "' and Password='" + pas + "'")
        data = cursor.fetchone()
        if data is None:

            flash("RegisterNo or Name is wrong...!")
            return render_template('UserLogin.html')
        else:
            session['mob'] = data[2]
            session['add'] = data[4]
            session['cname'] = data[2]
            session['department'] = data[7]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where UserName='" + uname + "' and Password='" + pas + "'")
            data = cur.fetchall()
            flash("Your are Logged In...!")

            return render_template('UserHome.html', data=data)


@app.route("/AddCategory")
def AddCategory():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM categorytb ")
    data = cur.fetchall()
    return render_template('AddCategory.html', data=data)

    return render_template('AddCategory.html')


@app.route("/newcategory", methods=['GET', 'POST'])
def newcategory():
    if request.method == 'POST':

        cat = request.form['cat']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute("SELECT * from categorytb where category='" + cat + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO categorytb VALUES ('','" + cat + "')")
            conn.commit()
            conn.close()
            flash('New Category Registered successfully')
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
            cur = conn.cursor()
            cur.execute("SELECT * FROM categorytb ")
            data = cur.fetchall()
            return render_template('AddCategory.html', data=data)
        else:
            flash('Already Added')
            return render_template('AddCategory.html')


@app.route("/ARemove")
def ARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute(
        "delete from categorytb where cid='" + id + "'")
    conn.commit()
    conn.close()

    flash('Category Removed Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM categorytb  ")
    data = cur.fetchall()
    return render_template('AddCategory.html', data=data)



@app.route("/NewEvent")
def NewEvent():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT distinct category FROM categorytb")
    data = cur.fetchall()
    return render_template('NewEvent.html',data=data)



@app.route("/newevent", methods=['GET', 'POST'])
def newevent():
    if request.method == 'POST':

        ename = request.form['ename']
        cat = request.form['cat']
        place = request.form['place']
        date = request.form['date']
        time = request.form['time']
        date1 = request.form['date1']
        time1 = request.form['time1']
        file = request.files['file']
        file.save("static/uploads/" + file.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO eventtb VALUES ('','" + ename + "','" + cat + "','" + place + "','" + date + "','" + time + "',"
                                         "'" + date1 + "','" + time1 + "','" + file.filename + "')")
        conn.commit()
        conn.close()
        flash('New Event Registered successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cur = conn.cursor()
        cur.execute("SELECT * FROM eventtb ")
        data = cur.fetchall()
        return render_template('AViewEvent.html', data=data)


@app.route("/AviewEvent")
def AviewEvent():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventtb ")
    data = cur.fetchall()
    return render_template('AviewEvent.html',data=data)


@app.route("/AERemove")
def AERemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute(
        "delete from eventtb where cid='" + id + "'")
    conn.commit()
    conn.close()

    flash('eventtb Removed Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventtb  ")
    data = cur.fetchall()
    return render_template('AviewEvent.html', data=data)


@app.route("/UviewEvent")
def UviewEvent():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventtb ")
    data = cur.fetchall()
    return render_template('UviewEvent.html',data=data)

@app.route("/Add")
def Add():
    id = request.args.get('id')
    session['pid'] = id
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventtb  where eid='" + id + "' ")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM regtb  where  UserName='" + uname + "'")
    data1 = cursor.fetchone()

    if data1:
        name = data1[1]
        gender = data1[2]
        mobile = data1[3]
        email = data1[4]
        address = data1[5]

    else:
        return 'No Record Found!'
    return render_template('UApply.html', data=data,name=name,gender=gender,mobile=mobile,email=email,address=address)


@app.route("/uapply", methods=['GET', 'POST'])
def uapply():
    if request.method == 'POST':
        pid = session['pid']
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        pin = request.form['pin']
        height = request.form['height']
        weight = request.form['weight']
        file = request.files['profile']
        file.save("static/uploads/" + file.filename)
        file1 = request.files['proof']
        file1.save("static/uploads/" + file1.filename)
        uname = session['uname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM eventtb  where  eid='" + pid + "'")
        data = cursor.fetchone()

        if data:
            EName = data[1]
            cat = data[2]
            Place = data[3]

        else:
            return 'No Record Found!'


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO applytb VALUES ('','" + EName + "','" + Place + "','" + name + "','" + gender + "','" + dob + "','" + mobile + "','" + email + "',"
                                        "'" + address + "','" + pin + "','" + height + "','" + weight + "','" + file.filename + "','" + file1.filename + "','waiting','"+ uname +"','"+ cat +"')")
        conn.commit()
        conn.close()
        flash('Registered successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cur = conn.cursor()
        cur.execute("SELECT * FROM eventtb ")
        data = cur.fetchall()
        return render_template('UApply.html', data=data)


@app.route("/AApplyInfo")
def AApplyInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='waiting'")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='Accepted'")
    data1 = cur.fetchall()
    return render_template('AApplyInfo.html',data=data,data1=data1)


@app.route("/VAdd")
def VAdd():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb  where aid='" + id + "' ")
    data = cur.fetchall()
    return render_template('APersonal.html', data=data)


@app.route("/VAdd1")
def VAdd1():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb  where aid='" + id + "' ")
    data = cur.fetchall()
    return render_template('APersonal1.html', data=data)


@app.route('/download')
def download():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM applytb where  aid = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:
        filename = "static\\uploads\\"+data[13]
        return send_file(filename, as_attachment=True)
    else:
        return 'Incorrect username / password !'


@app.route("/Reject")
def Reject():
    id = request.args.get('id')


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute(
        "update applytb set Status='Rejected' where aid='" + id + "'")
    conn.commit()
    conn.close()
    flash('Player Application is Rejected...!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='waiting'")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='Accepted'")
    data1 = cur.fetchall()
    return render_template('AApplyInfo.html', data=data, data1=data1)


@app.route("/Accept")
def Accept():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cursor = conn.cursor()
    cursor.execute(
        "update applytb set Status='Accepted' where aid='" + id + "'")
    conn.commit()
    conn.close()
    flash('Player Application is Accepted...!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='waiting'")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where Status='Accepted'")
    data1 = cur.fetchall()
    return render_template('AApplyInfo.html', data=data, data1=data1)


@app.route("/UApplyinfo")
def UApplyinfo():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM applytb where UserName='"+ uname +"' ")
    data = cur.fetchall()
    return render_template('UApplyinfo.html',data=data)

@app.route("/NewWinner")
def NewWinner():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT distinct Name FROM applytb where Status='Accepted'")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT distinct Ename FROM applytb where Status='Accepted'")
    data1 = cur.fetchall()

    return render_template('NewWinner.html',data=data,data1=data1)



@app.route("/newwinner", methods=['GET', 'POST'])
def newwinner():
    if request.method == 'POST':

        player = request.form['player']
        cat = request.form['cat']
        pos = request.form['pose']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO winnertb VALUES ('','" + player + "','" + cat + "','" + pos + "')")
        conn.commit()
        conn.close()
        flash('New List Added successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
        cur = conn.cursor()
        cur.execute("SELECT * FROM winnertb ")
        data = cur.fetchall()
        return render_template('NewWinner.html', data=data)


@app.route("/AWinnerList")
def AWinnerList():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM winnertb")
    data = cur.fetchall()
    return render_template('AWinnerList.html',data=data)

@app.route("/UWinnerList")
def UWinnerList():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1sportsmanagement')
    cur = conn.cursor()
    cur.execute("SELECT * FROM winnertb")
    data = cur.fetchall()
    return render_template('UWinnerList.html',data=data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)