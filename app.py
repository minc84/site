from flask import Flask, render_template, request, flash
from config import Configuration
from forms import ContactForm
from flask_mail import Message, Mail
import os


mail = Mail()
app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = '1580208980-7d702e450c96ee352e41d401c014b0d07b9124de'

app.config["MAIL_SERVER"] = "mail.greenarea.by"
app.config["MAI_PORT"] = 25
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"]= False
app.config["MAIL_USERNAME"] = 'info@greenarea.by'
app.config["MAIL_PASSWORD"] = 'Lokomotiv1'
 
mail.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('index.html', form=form)
    else:
      msg = Message(form.subject.data, sender='info@greenarea.by', recipients=['info@greenarea.by'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('foto.html', success=True)
 
  elif request.method == 'GET':
    return render_template('index.html', form=form)

@app.route('/foto', methods = ['GET', 'POST'])
def foto():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('foto.html', form=form)
    else:
      msg = Message(form.subject.data, sender='info@greenarea.by', recipients=['info@greenarea.by'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('foto.html', success=True)
 
  elif request.method == 'GET':
    return render_template('foto.html', form=form)

 






if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 5000)))