#!/usr/bin/env python

import urllib
import json
import os
#import psycopg2

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.cost":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("shipping-zone")

    cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':900, 'Africa':500}

    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."
    speech = "The cost of shipping to " + zone + " is " + "152" + " euros."
    
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
#!/usr/bin/env python

import urllib
import json
import os
import psycopg2
import urlparse

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.cost":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("shipping-zone")
    billmonth = parameters.get("billmonth")
    sin = parameters.get("sin")

    #cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':800, 'Africa':500}
    amount = {'1234567':4387, '7654321':3350}
    name = {'1234567':'Perry Dominguez', '7654321':'Carlos Garcia'}
    due = {'1234567':'March 5, 2017', '7654321':'March 6, 2017'}

    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."
    #speech = "The cost of shipping to " + zone + " is " + "159 " + " euross."
    speech = "Thank you for that information Mr. " + str(name[sin]) + ". Your bill amount for the month of " + billmonth + " is "  + str(amount[sin]) + " pesos. This is due on " + str(due[sin]) +". Do you want me to do an analysis on your electricity bill?"
    #speech = "Thank you for that information Mr. The bill amount for the month of " + billmonth + "for SIN " + sin + " is "  + str(amount[sin]) + " pesos. Do you want me to do analysis on your bill?"
                           
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "billamount": str(amount[sin]),
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
