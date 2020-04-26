import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
from selenium import webdriver
import time
import os
import datetime

stations =[
  {
    "latitud": 19.503664,
    "longitud": -99.13222,
    "name": "estacion1"
  },
  {
    "latitud": 19.6529727,
    "longitud": -99.1977184,
    "name":  "estacion2"
  },
]

HTML= """"
<html>
  <head>
    <title>Mapa Here</title>
    <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    <script src="https://js.api.here.com/v3/3.1/mapsjs-core.js"
    type="text/javascript" charset="utf-8"></script>
    <script src="https://js.api.here.com/v3/3.1/mapsjs-service.js"
    type="text/javascript" charset="utf-8"></script>
  </head>
  <body>
    <div style="width: 640px; height: 480px" id="mapContainer"></div>
    <script>
      // Initialize the platform object:
      var platform = new H.service.Platform({
        'apikey': 'onOejLUoojCNQB7tBRszuk0aiorm1k2tfAyvso54Kjs'
      });

      // Obtain the default map types from the platform object
      var maptypes = platform.createDefaultLayers();

      // Instantiate (and display) a map object:
      var map = new H.Map(
        document.getElementById('mapContainer'),
        maptypes.vector.normal.map,
        {
          zoom: 16,
          center: { lng: LONGITUD, lat: LATITUD }
        });
    </script>
  </body>
</html>
"""

driver = webdriver.Firefox()
driver.set_window_size(1920, 1080)
for station in stations:
  HTMLNew = HTML.replace("LATITUD",str(station["latitud"])).replace("LONGITUD",str(station["longitud"]))
  file = open(".graphStation.html","w")
  file.write(HTMLNew)
  file.close()
  driver.get("file://{}/.graphStation.html".format(os.getcwd()))
  time.sleep(5)
  
  
  filename = datetime.datetime.now().strftime("%d-%m-%YT%H-%M-%S")

  driver.save_screenshot( station["name"]+"_"+filename  +".png") 

driver.close() 