# Project Name: Horizon team_Online_Music_Platform
# Author: Horizon Team
# Start Date:25/4/2021
# Last Fix Date:29/5/2021

# Introduce a part of flash module which in use
from flask import Flask, render_template, make_response, request, redirect, url_for, flash, send_from_directory,session
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
import os
import time
# The module to connect python to mysql
import db_reg

app = Flask(__name__)

UPLOAD_FOLDER = 'static/custom/mp3/'     # 文件下载路径
ALLOWED_EXTENSIONS = {'mp3','jpg','lrc'}   # 文件允许上传格式

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER   # 设置文件下载路径
app.config["SECRET_KEY"] = 'hangengchen'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('index.html')
      return redirect('music_list')


@app.route('/company', methods=['GET', 'POST'])
def company():
     return render_template('company.html')


# @app.route('/payment-page', methods=['GET', 'POST'])
# def company():
#      return render_template('payment-page.html')

# fault-tolerant 1
@app.route('/<int:post_id>')
def inii(post_id):
    return render_template('faq.html', post_id=post_id)

# fault-tolerant 2
@app.route('/<string:post_id>')
def inss(post_id):
    return render_template('faq.html', post_id=post_id)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if(exit()):
        return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # to set the cookie
    resp = make_response(redirect('/mysonglist'))
    resp_business = make_response(redirect('/judge_0'))
    resp_admin = make_response(redirect('/judge_0'))
    # When user Submitted
    if request.method == 'POST':
        # var to save the email form user input
        email = request.form.get('email')
        # var to save the password form user input
        password = request.form.get('password')
        # var to sve the user if they want to save the cookies
        remember = request.form.get('remember')
        # background log
        print("user input email:" + email)
        print("user input password:" + password)
        print("user input remember:" + str(remember))
        # to change the var type to string
        email = str(email)
        # In the comparison method, the user input data (user name + password)
        # are connected together and compared with the tuple after slicing
        passwd = str(db_reg.login(email))[3:-5]
        print("the password from database:" + passwd)
        passwda = str(db_reg.login_admin(email))[3:-5]
        print("the password from database:" + passwda)
        passwdb = str(db_reg.login_business(email)[3:-5])
        print("the password from database:" + passwdb)
        # when the user input the admin user email
        if passwd != "":
            print("this is user")
            # if str(passwd) == password:
            if check_password_hash(passwd,password):
                # set cookie and The expiration time is two days
                if remember == "on":
                    resp.set_cookie("email", email, max_age=172800)
                else:
                    session["email"] = email
                    return redirect('/mysonglist')
                return resp
                # when Login failed jump to the warring page
            else:
                return render_template('login.html')
        elif passwdb != "":
            print("this is business account")
            if check_password_hash(passwdb,password):
                # set cookie and The expiration time is two days
                if remember == "on":
                    resp_business.set_cookie("email", email, max_age=172800)
                else:
                    session["email"] = email
                    return redirect('/judge_0')
                return resp_business
                # when Login failed jump to the warring page
            else:
                return render_template('login.html')
        elif passwda != "":
            print("this is admin")
            if check_password_hash(passwda,password):
                # set cookie and The expiration time is two days
                if remember == "on":
                    resp_admin.set_cookie("email", email, max_age=172800)
                else:
                    session["email"] = email
                    return redirect('/judge_0')
                return resp_admin
                # when Login failed jump to the warring page
            else:
                return render_template('login.html')
        else:
            print("you are not reg")
            return render_template('faq.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def reg():
    info = "Click Sing Up To Submit Your New Account"
    info2 = "If you register success you will be jump to login page"
    info3 = ""
    # When user Submitted
    if request.method == 'POST':
        # Get role
        role = request.form['role']
        # Get User email
        email = request.form['email']
        # Get User password
        password = request.form['password']
        password_hash = generate_password_hash(password)
        # Save it to a list
        data = [
            (email, password_hash),
        ]
        getdata = [
            (role, email, password_hash),
        ]
        # save in database
        print(getdata)

        user = db_reg.all_users()
        business = db_reg.all_business()
        admin = db_reg.all_admin()

        print(user)
        print(business)
        print(admin)

        re = 0

        if role == "user":
            for temp in user:
                temp2 = str(temp)[2:-3]
                print("user_list:" + temp2)
                if temp2 == email:
                    # as same as user with user input and database
                    re = 1
                    return render_template('registration.html', info=info, info2=info2, info3="This email is used")
                    break

        elif role == "business":
            for temp in business:
                temp2 = str(temp)[2:-3]
                print("user_list:" + temp2)
                if temp2 == email:
                    # as same as user with user input and database
                    re = 1
                    return render_template('registration.html', info=info, info2=info2, info3="This email is used")
                    break
        else:
            for temp in admin:
                temp2 = str(temp)[2:-3]
                print("user_list:" + temp2)
                if temp2 == email:
                    # as same as user with user input and database
                    re = 1
                    return render_template('registration.html', info=info, info2=info2, info3="This email is used")
                    break

        if re == 0:
            print("add:"+email)
            if role == "user":
                db_reg.register(data)
            elif role == "business":
                db_reg.register_business(data)

    return render_template('registration.html', info=info, info2=info2, info3=info3)


@app.route('/music_list', methods=['GET', 'POST'])
def music_list():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    type = "All Music"
    page_info = "This is the list to display all music"
    if (email):
        exit = "Exit Account"
    else:
        exit = "You haven't login"

    music_id = db_reg.all_music_id()
    name = db_reg.all_music_name()
    singer = db_reg.all_music_singer()
    # album = db_reg.all_music_album()
    price = db_reg.all_music_price()
    picture = db_reg.all_music_img()

    music = []
    album = []

    for i in range(len(music_id)):
        album.append(str(db_reg.music_album(str(music_id[i])[1:-2]))[3:-5])

    for i in range(len(music_id)):
        musicaa = [str(music_id[i])[1:-2], str(name[i])[2:-3], str(singer[i])[2:-3], str(price[i])[10:-4], str(picture[i])[2:-3],album[i]]
        music.append(musicaa)

    for pp in music:
        print(pp)

    return render_template('/music_list.html',type=type , page_info=page_info,music=music, account=email, exit=exit)


@app.route('/music_list/<id>', methods=['GET'])
def song(id):
    print (id)
    name = str(db_reg.music_name(id))[3:-5]
    price = str(db_reg.music_price(id))[11:-6]
    picture = str(db_reg.music_picture(id))[3:-5]
    info = str(db_reg.music_info(id))[3:-5]
    singer = str(db_reg.music_singer(id))[3:-5]
    path = str(db_reg.music_path(id))[3:-5]
    lrc = str(db_reg.music_lrc(id))[3:-5]
    album = str(db_reg.music_album(id))[3:-5]

    # to search the song if it be added in the musiclist
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')

    add = "Add To My Song List"
    if (email):
        # Use user's email to search user_id
        print("email:" + email)
        user_id = str(db_reg.user_id(email))[2:-4]
        print("user_id:" + user_id)
        # Use user_id to search user's song's in music_list
        music_id = db_reg.user_music_id(user_id)
        print("music_id:" + str(music_id))

        #set the defult
        for temp in music_id:
            temp = str(temp)[1:-2]
            if temp == id:
                add = "Add To My Song List"

    return render_template('/product-page.html', id=id, add=add, name = name, price = price, picture = picture, singer = singer, info = info, path=path, lrc=lrc, album=album)

@app.route('/mysonglist', methods =['GET'])
def mysonglist():
    music = []
    type = "My Song List"
    page_info= "This is the list your music list"

    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')

    if(email):
        exit="Exit Account"
        # Use user's email to search user_id
        print("email:" + email)
        user_id = str(db_reg.user_id(email))[2:-4]
        print("user_id:" + user_id)

        # Use user_id to search user's song's in music_list
        music_id = db_reg.user_music_id(user_id)
        print("music_id:" + str(music_id))

        # infomation search by use music_id list

        name = []
        singer = []
        price = []
        picture = []
        album = []

        for temp in music_id:
            music_id_bystr = str(temp)[1:-2]

            print(str(db_reg.music_name(music_id_bystr))[3:-5])
            name.append(str(db_reg.music_name(music_id_bystr))[3:-5])

            print(str(db_reg.music_singer(music_id_bystr))[3:-5])
            singer.append(str(db_reg.music_singer(music_id_bystr))[3:-5])

            print(str(db_reg.music_price(music_id_bystr))[11:-6])
            price.append(str(db_reg.music_price(music_id_bystr))[11:-6])

            print(str(db_reg.music_picture(music_id_bystr))[3:-5])
            picture.append(str(db_reg.music_picture(music_id_bystr))[3:-5])

            print(str(db_reg.music_album(music_id_bystr))[3:-5])
            album.append(str(db_reg.music_album(music_id_bystr))[3:-5])

        for i in range(len(music_id)):
            musicaa = [str(music_id[i])[1:-2], str(name[i]), str(singer[i]), str(price[i]), str(picture[i]),str(album[i])]
            print(music_id[i])
            music.append(musicaa)
        for pp in music:
            print(pp)
    else:
        return redirect('login')
    return render_template('/music_list.html',type = type, page_info=page_info, music=music, account=email, exit=exit)

@app.route('/add_music', methods=['GET', 'POST'])
def upload_file():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        print(judge_business)
        if(judge_business==""):
            return redirect('/faq_not_business')
        else:
            add_id = str(db_reg.business_id(email))[2:-4]
            if request.method == 'POST':
                # check if the post request has the file part
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['file']
                if 'file2' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file2 = request.files['file2']
                if 'file3' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file3 = request.files['file3']

                # if user does not select file, browser also
                # submit an empty part without filename
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file2.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file3.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    # filename (this position) is the upload file name who save in your server
                    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    # I change the file name to the database code of the songs
                    song_code = str(time.time())
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], song_code+".mp3"))

                if file2 and allowed_file(file2.filename):
                    file2.save(os.path.join('static/custom/img/', song_code + ".jpg"))

                if file3 and allowed_file(file3.filename):
                    file3.save(os.path.join('static/custom/lrc/', song_code + ".lrc"))

                # Write into database
                add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                add_id = str(db_reg.business_id(email))[2:-4]
                name = request.form['name']
                singer = request.form['singer']
                price = request.form['price']
                picture_path=os.path.join("/"+'static/custom/img/', song_code + ".jpg")
                information=request.form['info']
                music_path=os.path.join("/"+'static/custom/mp3/', song_code + ".mp3")
                lyric_path=os.path.join("/"+'static/custom/lrc/', song_code + ".lrc")
                album=request.form['album']

                data=[
                    (add_id, add_time, name, singer, price, picture_path, information, music_path, lyric_path)
                    ,]
                db_reg.add_music(data)
                db_reg.add_album(album,add_id,music_path)


                # if the song will be upload the website page will jump to the file location
                return redirect('add_music')
            # return redirect(url_for('uploaded_file',filename=song_code+".mp3"))
            return render_template('/add_music.html',add_id=add_id,price=0)
    else:
        return redirect('login')


@app.route('/add_music/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/results',methods=['POST'])
def search_result():
    music = []
    type = "Search result"
    page_info = "This page list your search result"

    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')

    if (email):
        exit = "Exit Account"
    else:
        exit = "You haven't login"

    if request.method == 'POST':
        # save the Submitted thing in a variable
        phrase = request.form['phrase']
    if phrase:
        # Use database to search the result
        music_id = db_reg.music_search(phrase)
        print("music_id:" + str(music_id))

        # infomation search by use music_id list
        name = []
        singer = []
        price = []
        picture = []
        album = []

        for temp in music_id:
            music_id_bystr = str(temp)[1:-2]
            print(str(db_reg.music_name(music_id_bystr))[3:-5])
            name.append(str(db_reg.music_name(music_id_bystr))[3:-5])
            print(str(db_reg.music_singer(music_id_bystr))[3:-5])
            singer.append(str(db_reg.music_singer(music_id_bystr))[3:-5])
            print(str(db_reg.music_price(music_id_bystr))[11:-6])
            price.append(str(db_reg.music_price(music_id_bystr))[11:-6])
            print(str(db_reg.music_picture(music_id_bystr))[3:-5])
            picture.append(str(db_reg.music_picture(music_id_bystr))[3:-5])
            print(str(db_reg.music_album(music_id_bystr))[3:-5])
            album.append(str(db_reg.music_album(music_id_bystr))[3:-5])


        for i in range(len(music_id)):
            musicaa = [str(music_id[i])[1:-2], str(name[i]), str(singer[i]), str(price[i]), str(picture[i]),str(album[i])]
            print(music_id[i])
            music.append(musicaa)
        for pp in music:
            print(pp)

    return render_template('music_list.html',type=type,page_info=page_info,music=music, account=email, exit=exit)

@app.route('/user_manage',methods=['GET','POST'])
def user_manage():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        print(judge_admin)
        if(judge_admin==""):
            return redirect('/faq_not_admin')
        else:
            alluser=[]
            all_users_id=db_reg.all_users_id()
            all_business_id=db_reg.all_business_id()
            all_admin_id=db_reg.all_admin_id()
            all_users=db_reg.all_users()
            all_business=db_reg.all_business()
            all_admin=db_reg.all_admin()

            for i in range(len(all_users_id)):
                user = [str(all_users_id[i])[1:-2], str(all_users[i])[2:-3], "NO", "NO", ""]
                print(user)
                alluser.append(user)

            for i in range(len(all_business_id)):
                business = [str(all_business_id[i])[1:-2], str(all_business[i])[2:-3], "YES", "NO", ""]
                print(business)
                alluser.append(business)

            for i in range(len(all_admin_id)):
                admin = [str(all_admin_id[i])[1:-2], str(all_admin[i])[2:-3], "NO", "YES", "disabled"]
                print(admin)
                alluser.append(admin)

            return render_template('user_manage.html',alluser=alluser)
    else:
        return redirect('/login')

@app.route('/music_manage',methods=['GET','POST'])
def music_manage():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        print(judge_admin)
        if(judge_admin==""):
            return redirect('/faq_not_admin')
        else:
            allmusic=[]
            all_music_id=db_reg.all_music_id()
            all_music_name=db_reg.all_music_name()
            all_music_mp3=db_reg.all_music_img()
            all_music_price=db_reg.all_music_price()

            for i in range(len(all_music_id)):
                user = [str(all_music_id[i])[1:-2], str(all_music_name[i])[2:-3], str(all_music_mp3[i])[2:-3], "¥"+str(all_music_price[i])[10:-4], ""]
                print(user)
                allmusic.append(user)

            return render_template('music_manage.html',allmusic=allmusic)
    else:
        return redirect('/login')

@app.route('/judge_0',methods=['GET'])
def judge_0():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        judge_user = str(db_reg.login(email))[3:-5]

        print(judge_business)
        print(judge_admin)
        print(judge_user)

        if (judge_business != ""):
            return redirect('/judge_business')
        elif (judge_admin != ""):
            return redirect('/judge_admin')
        elif (judge_user != ""):
            return redirect('/login')
        else:
            return redirect('/you_are_user')

@app.route('/judge_business',methods=['GET'])
def judge_business():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        judge_user = str(db_reg.login(email))[3:-5]

        print(judge_business)
        print(judge_admin)
        print(judge_user)
    else:
        return redirect('/login')
    return render_template('/judge_b.html')

@app.route('/judge_admin',methods=['GET'])
def judge_admin():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        judge_user = str(db_reg.login(email))[3:-5]

        print(judge_business)
        print(judge_admin)
        print(judge_user)
    else:
        return redirect('/login')
    return render_template('/judge_a.html')


@app.route('/music_manage/<id>',methods=['GET','POST'])
def music_manage_del(id):
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_admin = str(db_reg.login_admin(email))[3:-5]
        print(judge_admin)
        if (judge_admin == ""):
            return redirect('/faq_not_admin')
        else:
            print(id)
            db_reg.del_music(id)
            return redirect('/music_manage')
    else:
        return redirect('/login')

@app.route('/music_update',methods=['GET','POST'])
def music_update():
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        print(judge_business)
        if(judge_business==""):
            return redirect('/faq_not_admin')
        else:
            allmusic=[]
            all_music_id=db_reg.all_music_id()
            all_music_name=db_reg.all_music_name()
            all_music_mp3=db_reg.all_music_img()
            all_music_price=db_reg.all_music_price()

            for i in range(len(all_music_id)):
                user = [str(all_music_id[i])[1:-2], str(all_music_name[i])[2:-3], str(all_music_mp3[i])[2:-3], "¥"+str(all_music_price[i])[10:-4], ""]
                print(user)
                allmusic.append(user)

            return render_template('music_update.html',allmusic=allmusic)
    else:
        return redirect('/login')

@app.route('/music_update/<id>',methods=['GET','POST'])
def music_update_do(id):
    if (request.cookies.get('email')):
        email = request.cookies.get('email')
    else:
        email = session.get('email')
    print(email)
    if (email):
        judge_business = str(db_reg.login_business(email))[3:-5]
        print(judge_business)
        if (judge_business == ""):
            return redirect('/faq_not_business')
        else:
            add_id = str(db_reg.business_id(email))[2:-4]

            read_name = str(db_reg.music_name(id))[3:-5]
            read_singer = str(db_reg.music_singer(id))[3:-5]
            read_info = str(db_reg.music_info(id))[3:-5]
            read_price = str(db_reg.music_price(id))[11:-6]
            read_album = str(db_reg.music_album(id))[3:-5]

            if request.method == 'POST':
                # check if the post request has the file part
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['file']
                if 'file2' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file2 = request.files['file2']
                if 'file3' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file3 = request.files['file3']

                # if user does not select file, browser also
                # submit an empty part without filename
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file2.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file3.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    # filename (this position) is the upload file name who save in your server
                    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    # I change the file name to the database code of the songs
                    song_code = str(time.time())
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], song_code + ".mp3"))

                if file2 and allowed_file(file2.filename):
                    file2.save(os.path.join('static/custom/img/', song_code + ".jpg"))

                if file3 and allowed_file(file3.filename):
                    file3.save(os.path.join('static/custom/lrc/', song_code + ".lrc"))

                # Write into database
                add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                add_id = str(db_reg.business_id(email))[2:-4]
                name = request.form['name']
                singer = request.form['singer']
                price = request.form['price']
                picture_path = os.path.join("/" + 'static/custom/img/', song_code + ".jpg")
                information = request.form['info']
                music_path = os.path.join("/" + 'static/custom/mp3/', song_code + ".mp3")
                lyric_path = os.path.join("/" + 'static/custom/lrc/', song_code + ".lrc")
                album = request.form['album']

                data = [
                    (add_id, add_time, name, singer, price, picture_path, information, music_path, lyric_path, id)
                    , ]

                db_reg.update_music(data)

                data2 =[(album,id),]
                db_reg.update_album(data2)

                # if the song will be upload the website page will jump to the file location
                return redirect('update_music')
            # return redirect(url_for('uploaded_file',filename=song_code+".mp3"))
            return render_template('/update_music.html', add_id=add_id, read_name=read_name,read_singer=read_singer,read_info=read_info,read_album=read_album,price = read_price)
    else:
        return redirect('login')

@app.route('/add_tomymusiclist/<id>', methods=['GET'])
def add_tomymusiclist(id):

    if (request.cookies.get('email')):
        my_email = request.cookies.get('email')
    else:
        my_email = session.get('email')

    if(my_email):
        judge_user = str(db_reg.login(my_email))[3:-5]
        user_id = db_reg.user_id(my_email)
        if (judge_user == ""):
            return redirect('/faq_not_user')
        else:
            db_reg.add_tomymusiclist(my_email,user_id,id)
            return redirect(url_for('song',id=id))
    else:
        return redirect('/login')

@app.route('/user_manage/<email>', methods=['GET'])
def user_manage_del(email):
    print ("del_email:"+email)

    if (request.cookies.get('email')):
        my_email = request.cookies.get('email')
    else:
        my_email = session.get('email')

    if (my_email):
        judge_admin = str(db_reg.login_admin(my_email))[3:-5]
        if (judge_admin == ""):
            return redirect('/faq_not_admin')
        else:
            judge_user = str(db_reg.login(email))[3:-5]
            print("judge_user:"+judge_user)
            judge_business = str(db_reg.login_business(email))[3:-5]
            print("judge_business:" + judge_business)
            if (judge_user != ""):
                print("del user")
                db_reg.del_users(email)
            elif(judge_business!=""):
                print("del business")
                db_reg.del_business(email)
            return redirect('/user_manage')
    else:
        return redirect('/login')

@app.route('/exit', methods=['GET'])
def exit():
    res = make_response(redirect('/'))
    if (request.cookies.get('email')):
        res.delete_cookie('email')
        return res
    elif(session.get('email')):
        session.pop('email')
        return redirect('/')
    return redirect('/')



if __name__ == '__main__':
    app.run(host='localhost',port='80',debug=True)
