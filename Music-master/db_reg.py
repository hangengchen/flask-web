from db_config import UseDatebase

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'passwd': '12345678',
            'db': 'music', }


# For register Page
def register(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'insert into `user`(email, password) values(%s,%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")

def register_business(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'insert into `business`(email, password) values(%s,%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")

def del_users(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'DELETE FROM `user` WHERE `email` =' + "\"" + data + "\""
        # Execute SQL statement
        try:
            cur.execute(sql)
        except:
            print("wrong database cur")
        else:
            print("s!")
        res = cur.fetchall()
        return res

def del_business(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'DELETE FROM `business` WHERE `email` =' + "\"" + data + "\""
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def del_music(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'DELETE FROM `vinyls` WHERE `id` =' + "\"" + data + "\""
        try:
            cur.execute(sql)
            res = cur.fetchall()
            return res
        except:
            print("del :"+str(id)+"music failed")
        else:
            print("del :"+str(id)+"music success")


def all_users():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `email` FROM `user`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_business():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `email` FROM `business`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_admin():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `email` FROM `admin`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_users_id():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `id` FROM `user`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_business_id():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `id` FROM `business`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_admin_id():
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = 'SELECT `id` FROM `admin`'
        # Execute SQL statement
        cur.execute(sql)
        res = cur.fetchall()
        return res

# For login Page
def login(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = "SELECT `password` FROM user WHERE email =" + "\"" + data + "\""
        # Execute SQL statement
        cur.execute(sql)
        # save search result in a variable and convert it to string
        res = str(cur.fetchall())
        # return the string
        return res

# For compare admin user's password
def login_admin(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = "SELECT `password` FROM admin WHERE email =" + "\"" + data + "\""
        # Execute SQL statement
        cur.execute(sql)
        # save search result in a variable and convert it to string
        res = str(cur.fetchall())
        # return the string
        return res

# For compare business business user's password
def login_business(data):
    with UseDatebase(dbconfig) as cur:
        # Splicing and executing SQL statements
        sql = "SELECT `password` FROM business WHERE email =" + "\"" + data + "\""
        # Execute SQL statement
        cur.execute(sql)
        # save search result in a variable and convert it to string
        res = str(cur.fetchall())
        # return the string
        return res

def all_music_name():
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `name` FROM `vinyls`"
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_music_id():
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `id` FROM `vinyls`"
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_music_price():
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `price` FROM `vinyls`"
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_music_singer():
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `singer` FROM `vinyls`"
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_album(data):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `name` FROM `album` WHERE music_id=" + "\"" + data + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def all_music_img():
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `picture` FROM `vinyls`"
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_info(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `infomation` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_name(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `name` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_price(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `price` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_picture(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `picture` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_singer(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `singer` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_info(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `infomation` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_path(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `musicpath` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def music_lrc(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `lyric` FROM `vinyls` WHERE id =" + "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def user_id(data):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `id` FROM `user` WHERE email =" + "\"" + data + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def business_id(data):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT `id` FROM `business` WHERE email =" + "\"" + data + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def user_music_id(id):
    with UseDatebase(dbconfig) as cur:
        sql = "SELECT DISTINCT `music_id` FROM `music_list` WHERE creater_id="+ "\"" + id + "\""
        cur.execute(sql)
        res = cur.fetchall()
        return res

def add_music(data):
    with UseDatebase(dbconfig) as cur:
        sql = 'insert into `vinyls`(add_id, addtime, name, singer, price, picture, infomation, musicpath, lyric) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")


def update_music(data):
    with UseDatebase(dbconfig) as cur:
        sql = 'update `vinyls` SET add_id = %s, addtime = %s, name = %s, singer = %s, price = %s, picture = %s, infomation = %s, musicpath = %s, lyric = %s where id=(%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")

def update_album(data):
    with UseDatebase(dbconfig) as cur:
        sql = 'update `album` SET name = %s where music_id = (%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")

def add_album(name, creater_id, music_path):
    with UseDatebase(dbconfig) as cur:
        sql_music_id = "SELECT `id` FROM `vinyls` WHERE `musicpath` =" + "\'" + music_path + "\'"
        cur.execute(sql_music_id)
        music_id=str(cur.fetchall())[2:-4]
        print(music_id)
        data=[(name,creater_id,music_id),]
        sql = 'insert into `album`(name,creater_id,music_id) values(%s,%s,%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")

def add_tomymusiclist(name,creater_id,id):
    with UseDatebase(dbconfig) as cur:
        data=[(name,creater_id,id),]
        sql = 'insert into `music_list`(name,creater_id,music_id) values(%s,%s,%s);'
        try:
            # Execute SQL statement
            cur.executemany(sql, data)
        except:
            print("wrong database cur")
        else:
            print("success!")


# Query the name of the song, the artist and the album by the user's input words
def music_search(phrase):
    with UseDatebase(dbconfig) as cur:
        # sql for search the same music name
        sql1 = "SELECT `id` FROM `vinyls` WHERE `name` LIKE" + "\'%%" + phrase + "%%\'"
        # sql for search the same singer name
        sql2 = "SELECT `id` FROM `vinyls` WHERE `singer` LIKE" + "\'%%" + phrase + "%%\'"
        # sql for search the same album name
        sql3 = "SELECT `music_id` FROM `album` WHERE `name` LIKE" + "\'%%" + phrase + "%%\'"

        # Execute sql
        cur.execute(sql1)
        res1 = cur.fetchall()
        print(res1)
        cur.execute(sql2)
        res2 = cur.fetchall()
        print(res2)
        cur.execute(sql3)
        res3 = cur.fetchall()
        print(res3)

        # set a list to collect the id of search result
        res =[]

        # add the search result in the list
        for temp in res1:
            res.append(str(temp))
        for temp in res2:
            res.append(str(temp))
        for temp in res3:
            res.append(str(temp))
        print(res)

        # return the search result
        return res