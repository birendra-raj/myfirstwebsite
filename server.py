from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Birendra!!'
# 
# @app.route('/secret')
# def secret():
#     return 'your secret is here'
# 
# @app.route('/secret/mine')
# def mine():
#     return render_template('first.html')
# 
# @app.route('/<username>/<int:post_id>')
# def usernm(username=None,post_id=None):
#     return render_template('first.html', name=username,post_id=post_id)
#     
# @app.route('/secret/song')
# def song():
#     return render_template('Second.html')
# 
# # @app.route('/secret/<username>')
# # def mine(username=None):
# #     return render_template('first.html', name=username)

#------------------------------------------------------

# @app.route('/')
# def my_home():
#     return render_template('index.html')
# 
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
# 
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
# 
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

#---------------------------------------------------

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
        from werkzeug.utils import redirect
        if request.method=='POST':
            data=request.form.to_dict()
            #save_into_txtdb(data)
            save_into_csvdb(data)
            return redirect('/thankyou.html')
        else:
            return 'there is some issue'
        
def save_into_txtdb(data):
    database=open("Database.txt", mode='a')
    database.write(f"\n {data['email']}, {data['subject']} ,{data['message']}")


def save_into_csvdb(data):
    csvfile = open('Database.csv', 'a', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(data.values())

    