from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sdl'
app.config['MYSQL_PASSWORD'] = 'sdlpassword'
app.config['MYSQL_DB'] = 'sdldatabase'

mysql = MySQL(app)


@app.route('/data/student',methods=['GET'])
def Query():
      arg1 = request.args['arg1']
      arg2 = request.args['arg2']

      if(arg1=='null'):
            return "Bad Request"
      cur = mysql.connection.cursor()
      if(arg2 != 'null'):
            cur.execute("select count(*) from student where class_id = %s """, (arg2,))
            mysql.connection.commit()
            data = cur.fetchall()
            print('The number of students of class id ',(arg2,),'are ',data[0])
      else:
             cur.execute("select * from student where date = %s """, (arg1,))
             mysql.connection.commit()
             data = cur.fetchall()
             jsonResult = []
             for dataObj in data:
                   jsonResult.append({
                         'Date': dataObj[0],
                         'Class': dataObj[1],
                         'Student Id': dataObj[2],
                         'Student Name': dataObj[3]
                   })
             print('The student records for date ',arg1,' are ',jsonResult)


      return "ok"



if __name__=="__main__":
     app.run(debug=True)
