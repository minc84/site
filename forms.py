from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators

 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")