wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
echo "installed geckodriver in usr/local/bin/"
rm geckodriver-v0.26.0-linux64.tar.gz
echo "removing geckodriver files"
sudo pip3 install selenium
echo "installed selenium"
sudo pip3 install matplotlib
echo "installed matplotlib"
sudo pip3 install opencv-python
echo "installed opencv"
sudo pip3 install Pillow
echo "installed Pillow"
