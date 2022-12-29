from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from config import roles, users

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@auth.get_user_roles
def get_user_roles(username):
    return roles.get(username)

@app.route("/public")
def public():
    return "Este endpoint está expuesto al público. No es necesario loguearse."

@app.route("/private")
@auth.login_required(role="user")
def private():
    return "Logueado como {}".format(auth.current_user())

@app.route('/admin')
@auth.login_required(role="admin")
def admin():
    return "Logueado como {}. El usuario tiene permisos de administrador".format(auth.current_user())

if __name__ == "__main__":
    app.run(debug=True)