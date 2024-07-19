from flask import Flask
from main import main as main_blueprint

app = Flask(_name_)
app.register_blueprint(main_blueprint)

if _name_ == '_main_':
    app.run(debug=True)