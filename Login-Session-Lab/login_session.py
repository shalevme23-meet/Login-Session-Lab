from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		try:
			login_session["quote"] = request.form["quote"]
			login_session["author"] = request.form["author"]
			login_session["age"] = int(request.form["age"])
			return render_template('thanks.html')
		except:
			return redirect(url_for('error'))
	else:
		return render_template('home.html')


@app.route('/error')
def error():
	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', q=login_session["quote"], a=login_session["author"], age=login_session["age"])


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)