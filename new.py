from flask import Flask, render_template, request
import urllib2
import xml.etree.ElementTree as ET


app=Flask(__name__)

@app.route('/')
def root():
   return render_template("submit.html")

@app.route('/results')
def results():
   track = request.args["track"]
   xml = '''
   http://production.shippingapis.com/ShippingAPI.dll?API=TrackV2&XML=<?xml version="1.0"
   encoding="UTF-8" ?>
   <TrackRequest USERID="074STUYV1630">
   <TrackID ID="'''
   xml += track + '''"></TrackID>''' + "</TrackRequest>"

   

   u = urllib2.urlopen(xml).read()
   '''u = \'''
<?xml version="1.0" encoding="UTF-8"?>
<TrackResponse><TrackInfo ID="9405509699937073048953"><TrackSummary>The item is currently in transit to the destination as of November 13, 2017 at 9:03 am. It is on its way to ZIP Code 10025.</TrackSummary><TrackDetail>In Transit to Destination, November 12, 2017, 9:08 am, On its way to ZIP Code 10025</TrackDetail><TrackDetail>Departed USPS Regional Facility, November 12, 2017, 7:03 am, DES MOINES IA DISTRIBUTION CENTER</TrackDetail><TrackDetail>Arrived at USPS Regional Origin Facility, November 11, 2017, 9:08 pm, DES MOINES IA DISTRIBUTION CENTER</TrackDetail><TrackDetail>Departed Post Office, November 11, 2017, 6:16 pm, AMES, IA 50010</TrackDetail><TrackDetail>USPS in possession of item, November 11, 2017, 4:38 pm, AMES, IA 50010</TrackDetail><TrackDetail>Shipping Label Created, USPS Awaiting Item, November 11, 2017, 8:32 am, AMES, IA 50014</TrackDetail></TrackInfo></TrackResponse>
\''''''

   return "This has yet to be formatted" + u


   
   

   #return render_template("results.html", track=request.args["track"])

if __name__ == '__main__':
   app.debug = True
   app.run()

	
