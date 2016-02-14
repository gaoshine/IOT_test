from hello import  app
from hello import db
from hello import User,Role
print app.url_map

user_role = Role(name='user')
user_gaoshine = User(username='Gaoshine',role=user_role)
