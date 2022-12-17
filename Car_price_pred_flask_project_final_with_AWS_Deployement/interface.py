from flask import Flask, request, render_template, jsonify
from utils import CarPricePred
import config


app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Car Price Prediction")
    return render_template("page.html")

@app.route("/predict_car_price", methods = ["POST", "GET"])
def predict_car_price():
    if request.method == 'POST':
        user_data = request.form
        Year = eval(user_data['Year'])
        Present_Price = eval(user_data['Present_Price'])
        Kms_Driven = eval(user_data['Kms_Driven'])
        Fuel_Type = user_data['Fuel_Type']
        Seller_Type = user_data['Seller_Type']
        Transmission = user_data['Transmission']
        Owner = eval(user_data['Owner'])
        print("Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner\n",Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)

        car2 = CarPricePred(Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
        charges = car2.predict_price()
        # wreturn jsonify({"Result" : f"Predicted Charges for Car is {charges}/- Rs. Only"})
        return render_template("page.html", prediction = charges)


    # if request.method == "GET":
    #     print("We are using GET Method")
    #     Year = int(request.args.get("Year"))
    #     Present_Price = float(request.args.get("Present_Price"))
    #     Kms_Driven = int(request.args.get("Kms_Driven"))
    #     Fuel_Type = request.args.get("Fuel_Type")
    #     Seller_Type = request.args.get("Seller_Type")
    #     Transmission = request.args.get("Transmission")
    #     Owner = int(request.args.get("Owner"))

    #     print("Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner\n",Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)

    #     car2 = CarPricePred(Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
    #     charges = car2.predict_price()
    #     return jsonify({"Result" : f"Predicted Charges for Car is {charges}/- Rs. Only"})

    # else:
    #     print("We are using POST Method")

    #     Year = int(request.form.get("Year"))
    #     Present_Price = float(request.form.get("Present_Price"))
    #     Kms_Driven = int(request.form.get("Kms_Driven"))
    #     Fuel_Type = request.form.get("Fuel_Type")
    #     Seller_Type = request.form.get("Seller_Type")
    #     Transmission = request.form.get("Transmission")
    #     Owner = request.form.get("Owner")

        
    # 
        

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)