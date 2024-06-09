from app import db, Todo, app

with app.app_context():
    db.create_all()