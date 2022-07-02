from models import db, User, Post
from app import app

db.drop_all()
db.create_all()

User.query.delete()

alan = User(first_name='Alan', last_name='Alda',
            image_url='https://t4.ftcdn.net/jpg/02/19/63/31/360_F_219633151_BW6TD8D1EA9OqZu4JgdmeJGg4JBaiAHj.jpg')
joel = User(first_name='Joel', last_name='Burton',
            image_url='https://image.shutterstock.com/mosaic_250/698308/567772042/stock-photo-headshot-of-successful-smiling-cheerful-african-american-businessman-executive-stylish-company-567772042.jpg')
jane = User(first_name='Jane', last_name='Smith',
            image_url='https://jaysoriano.com/wp-content/uploads/2018/04/P8110606-Edit.jpg')


post1 = Post(title='Test Post 1', content='This is a test', )

db.session.add_all([alan, joel, jane])

db.session.commit()

db.session.add(post1)
db.session.commit()
