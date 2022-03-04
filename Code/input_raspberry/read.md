The XML files were taken from the classifiers on the following link:
https://github.com/adobe/SimpleSensor/tree/master/simplesensor/collection_modules/demographic_camera/classifiers/haarcascades

The mqtt.config file comes with the installation of MQTT. Because the default configuration limits connection by external microcontrollers, the configuration file we used added lines to allow for permission. 
If necessary, SSH into the raspberry and replace the existing mqtt.config file with the one provided here. 
