# Python Modules
from flask import Flask, redirect, url_for, request, render_template, flash
import jinja2
import datetime


# Google Modules
from google.appengine.api import users



#################################################################################
#
# instantiate the app
#
#################################################################################

app = Flask(__name__)



#################################################################################
#
# function for landing page
#
#################################################################################

@app.route('/', methods=['GET'])
def landing_page():
	user = users.get_current_user()

	if user:
		nickname = users.nickname()
		return redirect(url_for('user_summary_page', nickname=nickname))
	else:
		login_logout_url = users.create_login_url('/')
		return "<html><body>Welcome Unkown User.  Please <a href={}>log in</a> so we know who you are.</body></html>".format(login_logout_url)





#################################################################################
#
# function for user summary page
#
#################################################################################

@app.route('/user/<nickname>', methods=['GET'])
def user_summary_page(nickname):
	user = users.get_current_user()
	date = datetime.date.today()

	if user:
		login_logout_url = users.create_logout_url('/')

		# binding condition: if current user is requesting their page allow; else redirect
		if username == nickname:
			return render_template('user_summary_page.html', nickname=nickname, login_logout_url=login_logout_url)
		else:
			flash('You are not authorized to view this page.')
			return redirect(url_for('landing_page'))
	else:
		login_logout_url = users.create_login_url('/')
		return "<html><body>Welcome Unkown User.  Please <a href={}>log in</a> so we know who you are.</body></html>".format(login_logout_url)