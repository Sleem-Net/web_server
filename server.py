from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# ? Page Routing


@app.route("/index.html")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_pages(page_name):
    return render_template(page_name)

# ? Write to Data Base (txt)


def write_to_file(data):
    with open('db.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# ? Write to Data Base(csv)


def write_to_csv(data):
    with open('db.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# ? Form Submission


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return 'some thing went wrong'
    else:
        return 'Something went wrong'
