import numpy as np
import pandas as pd
import pickle
import json
import config

class CarPricePred():
    def __init__(self, Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner):
        self.Year= Year
        self.Present_Price = Present_Price
        self.Kms_Driven = Kms_Driven
        self.Fuel_Type = Fuel_Type
        self.Seller_Type = Seller_Type
        self.Transmission = Transmission
        self.Owner = Owner

    def load_model(self):
        with open (config.MODEL_FILE_PATH, "rb") as f:
           self.model=  pickle.load(f)

        with open (config.JSON_FILE_PATH, "r") as f:
            self.project_data = json.load(f)

    def predict_price(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data["columns"]))
        test_array[0] = self.Year
        test_array[1] = self.Present_Price
        test_array[2] = self.Kms_Driven
        test_array[3] = self.project_data["Fuel_Type"][self.Fuel_Type]
        test_array[4] = self.project_data["Seller_Type"][self.Seller_Type]
        test_array[5] = self.project_data["Transmission"][self.Transmission]
        test_array[6] = self.Owner

        car_price = self.model.predict([test_array])[0]
        print("Predicted_car_price",car_price)
        return np.around(car_price, 2)


if __name__ == "__main__":
    Year = 2015
    Present_Price = 9.83
    Kms_Driven = 42450
    Fuel_Type = "Diesel"
    Seller_Type = 'Individual'
    Transmission = 'Manual'
    Owner = 0

    car1 = CarPricePred(Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)     
    Car_price = car1.predict_price()
    print(f"Price of car is Rs.{Car_price}\- only")