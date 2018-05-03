from flask import Flask
from flask import render_template,jsonify,request
import requests
import random

#this is for cross origin
from flask_cors import CORS



#for JSON
import json
from pprint import pprint

app=Flask(__name__)


@app.route('/')
def index():
    print("Here at least")    
    return render_template('home.html')



def get_weather_forecast(loc):
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    
    # Lookup via location name.

    location = weather.lookup_by_location(loc)
    condition = location.condition
    print(condition.text)

    forecast_line="Weather today, in "+loc+"- "+ condition.text+".\n"
    # Get weather forecasts for the upcoming days.

    forecasts = location.forecast

    
    forecast_line=forecast_line+"For "+forecasts[1].date+", weather will be "+forecasts[1].text
    print(forecast_line)
    return forecast_line

def format_entities(entities):
    """
    formats entities to key value pairs
    """
    ## Should be formatted to handle multiple entity values
    # e = {"location":None}
    e = {}
    for entity in entities:
        e[entity["entity"]] = entity["value"]
    return e


@app.route('/chat',methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        response = requests.get("http://localhost:5003/parse",params={"q":request.form["text"]})

        print("Sending "+ request.form["text"])        
        print("Response is "+str(response))
        response = response.json()
        print("The response is "+str(response))
        intent = response["intent"]["name"]
        print("Intent of the message was "+intent)
        entities = format_entities(response["entities"])
        pprint(entities)

#introduction
        if intent == "intro":
            response_text="Hello! How may I be of help?"
#get weather
        elif intent == "weather_request":            
            loc="Hyderabad"
            if len(entities)>0 and "location" in entities:
                loc=entities["location"]
            print("looking fr weather in "+str(loc))
            response_text=get_weather_forecast(loc)
            #clean userrequirements
        else:
            response_text = "Sorry I do not have an answer to that yet..."
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})



if __name__ == '__main__':
    print("#main")
    app.debug=True
    app.run(host='0.0.0.0', port=5050)
    