from flask import Flask
import connexion
from models.database import db

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/atlas-db'
db.init_app(app.app)

@app.route('/')
def home():
  db.create_all()
  return 'hellow world!'

if __name__ == '__main__':
  app.run(debug=True)
