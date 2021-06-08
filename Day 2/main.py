from flask import Flask, render_template, request
import logging

app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/', methods=['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		name = request.form.get("name")
		email = request.form.get("email")
		subject = request.form.get("subject")
		message = request.form.get("message")
		print(f"\n============\nNEW MESSAGE!\n\nNAME: {name}\nEMAIL: {email}\nSUBJECT: {subject}\n\nMESSAGE:\n{message}\n============\n")
		return render_template('sent.html')
	else:
		return render_template('index.html')

@app.route('/user/<username>')
def generate_user(username):
	return render_template('hello_world.html', user=username)

if __name__ == "__main__":	
    app.run(host='0.0.0.0', port=8080)