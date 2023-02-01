from flask import Flask, jsonify, request
from flask_cors import CORS                      
from os import environ
from config import db, SECRET_KEY
from dotenv import load_dotenv
from models.restaurant import Restaurant
from models.customer import Customer
from models.orderDetails import OrderDetails
from models.givenRating import GivenRating



 
def create_app():                              
    app = Flask(__name__)                       
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")


    with app.app_context():
        # db.drop_all()
     
        @app.route("/sign_up", methods=['POST'])
        def sign_up():
            data = request.form.to_dict(flat=True)

            new_customer = Customer(
                customer_name = data["customer_name"],
                customer_phone_no = data["customer_phone_no"]
            )
            db.session.add(new_customer)
            db.session.commit()

            return 'Customer added successfully'
        

        @app.route("/menu_items", methods=['GET'])
        def menu_items():

            menu = request.get_json()
            
            for item in menu:
                    restaurant_menu = Restaurant(
                        menu_items=menu[item]["item_name"],
                        item_price=menu[item]["item_price"],
                        item_rating=menu[item]["item_rating"]
                    )

                    db.session.add(restaurant_menu)
                    db.session.commit()
            return menu

        

        @app.route("/orderDetails", methods=['POST'])
        def orderDetails():
            customer_name = request.args.get('customer_name')
            customer = Customer.query.filter_by(customer_name=customer_name).first()
            # data = request.form.to_dict(flat=True)

            items_ordered = request.get_json()

            total_items = 0
            total_price = 0
            for item in items_ordered:
                total_items += 1
                total_price += items_ordered[item]["item_price"]

            order_Details = OrderDetails(
                customer_name = customer_name,
                quantity_of_items = total_items,
                total_amount = total_price,
                customer_id =  customer.id  
            )


            db.session.add(order_Details)
            db.session.commit() 

            return 'Order details given successfully'

        @app.route("/rating", methods=['POST'])
        def rating():
            customer_name = request.args.get('customer_name')
            customer = Customer.query.filter_by(customer_name=customer_name).first()
            data = request.form.to_dict(flat=True)

            rating = GivenRating(
                customer_name = customer_name,
                rating = data["rating"],
                customer_id =  customer.id  
            )

            db.session.add(rating)
            db.session.commit() 

            return 'Rating given successfully'
        
        db.create_all()
        db.session.commit()
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

    