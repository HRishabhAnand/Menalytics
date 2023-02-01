from config import db

class Restaurant(db.Model):                                     
    __tablename__ = 'restaurant'                   
    id = db.Column(db.Integer, primary_key=True)
    menu_items = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    item_rating = db.Column(db.Integer, nullable=False)



    
    


