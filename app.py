#!/usr/bin/env python

import urllib
import json
import os
import beatbox
import psycopg2 as p


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

    con = p.connect("dbname"='dcf8dpgo20qc84' user='udbunywtjpldqr' host ='ec2-23-21-238-246.compute-1.amazonaws.com'")
                    cur = con.cursor()
                    cur.execute(select cost from shipping_zones where id=3)
                    rows.cur.fetachall()
                    
                    #for r in rows:
                    #cost = r["cost"]
    
    cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':5000, 'Africa':500}

    speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

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
    app.run(debug=True, use_reloader=True)
    #port = int(os.getenv('PORT', 5000))

    #print "Starting app on port %d" % port

    #app.run(debug=True, port=port, host='0.0.0.0')
