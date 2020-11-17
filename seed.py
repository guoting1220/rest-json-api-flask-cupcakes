from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://images.unsplash.com/photo-1599785209796-786432b228bc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=666&q=80"
)

db.session.add_all([c1, c2])
db.session.commit()
