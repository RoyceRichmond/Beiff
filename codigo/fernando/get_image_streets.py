# coding: utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import datetime
path='~\Desktop\2k'
stations = [{
  "latitud": 19.272100,
  "longitud": -99.207658,
  "name": "1",
  "location":"AJM - Ajusco Medio"
}, {
  "latitud": 19.393734,
  "longitud": -99.028212,
  "name": "2",
  "location":"NEZ - Nezahualcoyotl"
}, {
  "latitud": 19.4827,
  "longitud": -99.094517,
  "name": "3",
  "location":"GAM - Gustavo A. Madero"
}, ]

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
          }]                    
        });
		var trafficLayer = new google.maps.TrafficLayer();
    trafficLayer.setMap(map);
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdTg2ovTM9YZ_wOJJt0aGkjfAM4wSAm3Y&callback=initMap"
    async defer></script>
  </body>
</html>
"""
HTMLPRINCIPAL = """
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
    "featureType": 'road.arterial',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#000Ffc'}]
          }]                    
        });
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdTg2ovTM9YZ_wOJJt0aGkjfAM4wSAm3Y&callback=initMap"
    async defer></script>
  </body>
</html>
"""
HTMLCARRETERA = """
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
    "featureType": 'road.highway',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#000Ffc'}]
          }]                    
        });
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdTg2ovTM9YZ_wOJJt0aGkjfAM4wSAm3Y&callback=initMap"
    async defer></script>
  </body>
</html>
"""
HTMLSECUNDARIA = """
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
    "featureType": 'road.local',
    "elementType": 'geometry',
    "stylers": [{'visibility': 'on'}, {'color': '#000Ffc'}]
          }]                    
        });
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdTg2ovTM9YZ_wOJJt0aGkjfAM4wSAm3Y&callback=initMap"
    async defer></script>
  </body>
</html>
"""
roadways=[HTML,HTMLCARRETERA,HTMLPRINCIPAL,HTMLSECUNDARIA]

def save_images():
  options = Options()
  options.set_preference("browser.download.folderList", 2)
  options.set_preference("browser.download.manager.showWhenStarting", False)
  options.set_preference("browser.download.dir", path)
  driver = webdriver.Firefox(firefox_options=options)
  driver.set_window_size(1920, 1080)
  for index,station in enumerate(stations):
    HTMLNew=roadways[0].replace("LATITUD",str(station["latitud"])).replace("LONGITUD",str(station["longitud"]))
    file = open(".graphStation.html", "w")
    file.write(HTMLNew)
    file.close()
    driver.get("file://{}/.graphStation.html".format(os.getcwd()))
    time.sleep(3)
    #filename = datetime.datetime.now().strftime("%d-%m-%YT%H-%M-%S")
    #driver.save_screenshot(station["name"] + "_" + filename + ".png")
    driver.save_screenshot(station["name"]+".png")
  driver.close()

def save_segmentation():
  options = Options()
  options.set_preference("browser.download.folderList", 2)
  options.set_preference("browser.download.manager.showWhenStarting", False)
  options.set_preference("browser.download.dir", path)
  driver = webdriver.Firefox(firefox_options=options)
  driver.set_window_size(1920, 1080) 
  for station in stations:
    for a in range(0,4):
      HTMLNew=roadways[a].replace("LATITUD",str(station["latitud"])).replace("LONGITUD",str(station["longitud"]))
      file = open(".graphStation.html", "w")
      file.write(HTMLNew)
      file.close()
      driver.get("file://{}/.graphStation.html".format(os.getcwd()))
      time.sleep(3)
      #filename = datetime.datetime.now().strftime("%d-%m-%YT%H-%M-%S")
      if a!=0:
        driver.save_screenshot(station["name"]+chr(96+a)+".png")
  driver.close()
