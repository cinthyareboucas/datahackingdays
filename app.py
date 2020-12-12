from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/app-home')
def appHome():
   return render_template('appHome.html')

@app.route('/agendamento')
def agendamento():
   return render_template('agendamento.html')

@app.route('/nova-conta')
def novaConta():
   return render_template('novaConta.html')

@app.route('/validar-email')
def validarEmail():
   return render_template('validarEmail.html')

@app.route('/final')
def final():
   return render_template('final.html')

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=5000)