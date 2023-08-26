from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import modhi as md
import thadi as th

def get_connection():
    cnx = mysql.connector.connect(
        user='root',
        password='Samitha@15',
        host='localhost',
        port='3308',
        database='course_finder_db'
    )
    return cnx

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_books():
    return 'hello world'


@app.route('/get_courses', methods=['GET'])
def get_courses():
    results = []
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM course_details"
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        data = {}
        data['c_id'] = row[0]
        data['name'] = row[1]
        data['specialization'] = row[1]
        data['campus'] = row[2]
        data['duration'] = row[3]
        data['desc'] = row[4]
        data['req'] = row[5]
        data['al_status'] = row[6]
        data['link'] = row[7]
        data['budget'] = row[8]
        results.append(data)
    a= {"results":results}
    cursor.close()
    conn.close()
    return a

@app.route('/get_courses_filter', methods=['GET'])
def get_courses_filter():
    budget =  request.args.get('budget')
    duration =  request.args.get('duration')
    al_result = request.args.get('result')
    stream = request.args.get('stream')
    intrest = request.args.get('intrest')
    print(budget,duration,stream)
    
    if al_result != 'default':
        if intrest != 'default':
            if duration=='0' and budget=='0':
                if al_result == 'failed':
                    query = "select a.* from (SELECT * FROM course_details where al_status = 'no need') a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == 's':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need') a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '1c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need') a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '2c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need') a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            elif duration=='0':
                if al_result == 'failed':
                    query = f"select a.* from (SELECT * FROM course_details where al_status = 'no need' and budget < {budget}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == 's':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '1c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '2c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            elif budget=='0':
                if al_result == 'failed':
                    query = f"select a.* from (SELECT * FROM course_details where al_status = 'no need' and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == 's':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '1c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '2c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            else:
                if al_result == 'failed':
                    query = f"select a.* from (SELECT * FROM course_details where al_status = 'no need' and budget < {budget} and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == 's':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '1c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
                elif al_result == '2c':
                    query = f"select a.* from (select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
        else:
            if duration=='0' and budget=='0':
                if al_result == 'failed':
                    query = "SELECT * FROM course_details where al_status = 'no need'"
                elif al_result == 's':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need'"
                elif al_result == '1c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need'"
                elif al_result == '2c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need'"
            elif duration=='0':
                if al_result == 'failed':
                    query = f"SELECT * FROM course_details where al_status = 'no need' and budget < {budget}"
                elif al_result == 's':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}"
                elif al_result == '1c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}"
                elif al_result == '2c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget}"
            elif budget=='0':
                if al_result == 'failed':
                    query = f"SELECT * FROM course_details where al_status = 'no need' and duration = {duration}"
                elif al_result == 's':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}"
                elif al_result == '1c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}"
                elif al_result == '2c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and duration = {duration}"
            else:
                if al_result == 'failed':
                    query = f"SELECT * FROM course_details where al_status = 'no need' and budget < {budget} and duration = {duration}"
                elif al_result == 's':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s') and sub2 in ('s') and sub3 in ('s')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}"
                elif al_result == '1c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}"
                elif al_result == '2c':
                    query = f"select cd.* from course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any') and sub1 in ('s','c') and sub2 in ('s','c') and sub3 in ('s','c')) cr on cd.c_id = cr.c_id where al_status = 'need' and budget < {budget} and duration = {duration}"
    
    else:
        if intrest != 'default':
            if duration=='0' and budget=='0':
                query = f"select a.* from (SELECT cd.* FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            elif duration=='0':
                query = f"select a.* from (SELECT cd.* FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where budget < {budget}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            elif budget=='0':
                query = f"select a.* from (SELECT cd.* FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
            else:
                query = f"select a.* from (SELECT cd.* FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where budget < {budget} and duration = {duration}) a inner join (select c.c_id from course_details c inner join (select c_id from course_job where job like '%{intrest}%' group by c_id) cj on c.c_id = cj.c_id) b on a.c_id = b.c_id"
        else:
            if duration=='0' and budget=='0':
                query = f"SELECT * FROM course_details cd (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id"
            elif duration=='0':
                query = f"SELECT * FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where budget < {budget}"
            elif budget=='0':
                query = f"SELECT * FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where duration = {duration}"
            else:
                query = f"SELECT * FROM course_details cd inner join (select c_id from course_al_need where ( stream = '{stream}' or stream = 'any')) cr on cd.c_id = cr.c_id where budget < {budget} and duration = {duration}"
    print(query)
    results = []
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        data = {}
        data['c_id'] = row[0]
        data['name'] = row[1]
        data['specialization'] = row[1]
        data['campus'] = row[2]
        data['duration'] = row[3]
        data['desc'] = row[4]
        data['req'] = row[5]
        data['al_status'] = row[6]
        data['link'] = row[7]
        data['budget'] = row[8]
        results.append(data)
    a= {"results":results}
    cursor.close()
    conn.close()
    return a

@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    course =  request.args.get('course')
    results = []
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM course_job where c_id = {course} group by job"
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        data = {}
        data['id'] = row[0]
        data['c_id'] = row[1]
        data['job'] = row[2]
        results.append(data)
    a= {"results":results}
    cursor.close()
    conn.close()
    return a

@app.route('/get_salary', methods=['GET'])
def get_salary():
    job =  request.args.get('job')
    c_id =  request.args.get('course')
    
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT c_name,campus FROM course_details where c_id = {c_id}"
    cursor.execute(query)
    
    result = cursor.fetchall()
    new_data = {
      'University': [result[0][1]],
      'Specialization': [result[0][0]],
      'Employability': ['Internship / Traniee'],
      'Job_Role': [job]
    }
    
    prediction1 = md.get_salary(new_data)
    
    new_data = {
      'University': [result[0][1]],
      'Specialization': [result[0][0]],
      'Employability': ['Associate'],
      'Job_Role': [job]
    }
    
    prediction2 = md.get_salary(new_data)
    
    new_data = {
      'University': [result[0][1]],
      'Specialization': [result[0][0]],
      'Employability': ['Engineer'],
      'Job_Role': [job]
    }
    
    prediction3 = md.get_salary(new_data)
    
    new_data = {
      'University': [result[0][1]],
      'Specialization': [result[0][0]],
      'Employability': ['Senior Engineer'],
      'Job_Role': [job]
    }
    
    prediction4 = md.get_salary(new_data)
    return {
        'Internship / Traniee':prediction1,
        'Associate':prediction2,
        'Engineer':prediction3,
        'Senior Engineer':prediction4
    }

@app.route('/get_scholarships', methods=['GET'])
def get_scholarships():
    results = []
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM scholarship"
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        data = {}
        data['id'] = row[0]
        data['tittle'] = row[1]
        data['campus'] = row[2]
        data['sub_tittle'] = row[3]
        data['description'] = row[4]
        results.append(data)
    a= {"results":results}
    cursor.close()
    conn.close()
    print(a)
    return a


@app.route('/get_loan', methods=['GET'])
def get_loan():
    data = {
      'University': [request.args.get('university')],
      'eligible_borrower': [request.args.get('borrower')],
      'Borrowers_Monthly_Income': [request.args.get('income')],
      'Contribution_of_borrower': [request.args.get('borrower')],
      'Citizenship': [request.args.get('amount')],
      'Applied_Loan_Amount': [request.args.get('job')],
      'Mortgage_Status': [request.args.get('mortage')],

    }
    result = th.getloan(data)
    return result

    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
