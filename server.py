from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route ('/') # the main page work with port :5000
def index():
    return render_template('index.html') # when user enter 127.0.0.1:5000/ it will render the index template

@app.route('/<string:page_name>') #this helps to make our pages dynamic
def html_page(page_name):
    return render_template(page_name)
def write_to_file(data):
    with open('database.text', mode='a') as database: # this heleps to save our user information from contact in to database
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject},{message}')

def write_to_csv(data): # to convert the user information in to csv (comma separated value) file so it will have similar to excel file
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.write(database2, delimiter=",", newline='', quotechar='""', qouting=csv.QOUTE_MINIMAL)
        csv_writer.writerow([email, subject,message])

@app.route('/submit_form', methods=['POST', 'GET']) #this helps when user submit the message the it will write to a data and give thank you to the user
def  submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something goes wrong please try again'
