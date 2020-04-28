# coding: utf-8

from selenium import webdriver
import time
import os
import datetime

stations = [{
  "latitud": 19.503664,
  "longitud": -99.13222,
  "name": "estacion1"
}, {
  "latitud": 19.6529727,
  "longitud": -99.1977184,
  "name": "estacion2"
}, ]


modifiers =[{
    "featureType": 'road.arterial',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#fcfcfc'}]
    },{
    "featureType": 'road.highway',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#000Ffc'}]
    },{
    "featureType": 'road.local',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#fFf000'}]
    },{
    "featureType": 'road.highway.controlled_access',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#f11f00'}]
    },{		
    "featureType": '',
    "elementType": '',
    "stylers": ''
    }
]


HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: LATITUD, lng: LONGITUD },
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          disableDoubleClickZoom: true,
          draggable: false,
          scrollwheel: false,
          panControl: false,
          disableDefaultUI: true,
          styles: [{
            "stylers": [{"visibility": "off"}]
          },{
            "featureType": FEATURE,
            "elementType": ELEMENTTYPE,
            "stylers": STYLERS
          }]                    
        });
        TRAFFIC
		SETTRAFFIC
		<!--var trafficLayer = new google.maps.TrafficLayer();-->
        <!--trafficLayer.setMap(map);-->
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdTg2ovTM9YZ_wOJJt0aGkjfAM4wSAm3Y&callback=initMap"
    async defer></script>
  </body>
</html>
"""
def save_images():
  driver = webdriver.Firefox()
  driver.set_window_size(1920, 1080)
  for station in stations:
    HTMLNew = HTML.replace("LATITUD", str(station["latitud"])).replace("LONGITUD", str(station["longitud"])).replace("TRAFIC", "var trafficLayer = new google.maps.TrafficLayer();").replace("SETTRAFIC", "trafficLayer.setMap(map);")
    file = open(".graphStation.html", "w")
    file.write(HTMLNew)
    file.close()
    driver.get("file://{}/.graphStation.html".format(os.getcwd()))
    time.sleep(5)
    # filename = datetime.datetime.now().strftime("%d-%m-%YT%H-%M-%S")
    # driver.save_screenshot(station["name"] + "_" + filename + ".png")
  driver.close()

def save_segmentation():
  driver = webdriver.Firefox()
  driver.set_window_size(1920, 1080)
  for station in stations:
    HTMLNew=HTML.replace("LATITUD",str(station["latitud"])).replace("LONGITUD",str(station["longitud"])).replace("FEATURE",str(station["featureType"])).replace("ELEMENTTYPE",str(station["elementType"])).replace("STYLERS",str(station["stylers"])).replace("TRAFIC","").replace("SETTRAFIC","")
    file = open(".graphStation.html", "w")
    file.write(HTMLNew)
    file.close()
    driver.get("file://{}/.graphStation.html".format(os.getcwd()))
    time.sleep(5)
    # filename = datetime.datetime.now().strftime("%d-%m-%YT%H-%M-%S")
    # driver.save_screenshot(station["name"] + "_" + filename + ".png")
  driver.close()