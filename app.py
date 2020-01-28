from flask import Flask, render_template, request, flash
from config import Configuration
from forms import ContactForm
import os

app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = '1580208980-7d702e450c96ee352e41d401c014b0d07b9124de'


@app.route('/')
@app.route('/blog')
def index():
    return render_template('index.html')

@app.route('/foto')
def foto():
    return render_template('foto.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)



if __name__ == '__main__':
      app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 5000)))