wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
echo "installed geckodriver in usr/local/bin/"
rm geckodriver-v0.26.0-linux64.tar.gz
echo "removing geckodriver files"
sudo pip install selenium
echo "installed selenium"
sudo pip install -U googlemaps
echo "installed google maps API"

