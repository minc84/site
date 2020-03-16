from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

 
class ContactForm(FlaskForm):
  name = TextField("Ваше Имя",  [validators.Required("Please enter your name.")])
  email = TextField("e-mail",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Телефон",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Сообщение",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Отправить")
 