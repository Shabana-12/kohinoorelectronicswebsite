from flask import Flask, render_template, request, redirect, url_for, session, flash
import re
from flask_mail import Mail, Message
mail = Mail()
app = Flask(__name__)
app.secret_key = 'your secret key'

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'apexinfotechexcellenceco@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Fs@Da@25$7'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)
# # key=API_KEY
# AIzaSyDkxEx1kmjj62v5yriRA4z3G3sJBxml14g
@app.route("/")
def homepage():
    return render_template("kohinoor_web.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(
            subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender='apexinfotechexcellenceco@gmail.com', recipients=['kohinoorelect01@gmail.com'])
        mail.send(msg)
        flash("Your response is sent successfully!! Our team will get back You soon, Thank You 😊")
        return render_template("kohinoor_web.html", success=True)

    return render_template("kohinoor_web.html")


if __name__ == "__main__":
    app.run()
