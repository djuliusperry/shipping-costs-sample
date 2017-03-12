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
    
    
   # urlparse.uses_netloc.append("postgres")
   # url = urlparse.urlparse(os.environ["postgres://umrftdcwqqsixn:e3ffb58ad38ceb736cc2fadd041faa8cea0262ea6b29614d3f539551a91c0647@ec2-107-22-244-62.compute-1.amazonaws.com:5432/de3h20sdptjvi0"])

    #conn = psycopg2.connect(
     #   database=url.path[1:],
      #  user=url.username,
       # password=url.password,
        #host=url.hostname,
        #port=url.port
    #)
    
    #con = p.connect("dbname"='dcf8dpgo20qc84' user='udbunywtjpldqr' host ='ec2-23-21-238-246.compute-1.amazonaws.com'")
    #conn = psycopg2.connect("dbname"='dcf8dpgo20qc84' user='udbunywtjpldqr' host ='ec2-23-21-238-246.compute-1.amazonaws.com'")
     #               cur = conn.cursor()
                    #cur.execute(select cost from shipping_zones where id=3)
                    #rows = cur.fetachall()
                    
                    #for row in rows:
                    #cost = row[0]

    #cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':800, 'Africa':500}

    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."
    speech = "The cost of shipping to " + zone + " is " + "159 " + " euross."
                            
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
