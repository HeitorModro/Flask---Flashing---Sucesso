from flask import Flask, flash, render_template 

app = Flask('app')
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
  return ('/flashing')


@app.route('/hello/<name>')
def flasing(name):
  flash(f'Bem-vindo, {name}!', 'info')
  return render_template('index.html')
  

if __name__ == '__main__':
  app.run(host= '0.0.0.0', port=8080)