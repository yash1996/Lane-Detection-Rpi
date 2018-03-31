# Lane-Detection-Rpi using a ConvNet
Lane Detection in RPi for a RC rover or Self Driving Vehicle using Pi Camera.
This project uses a CNN model. This is an extension of the MLND Captsone Project that uses a similar approach.
This project is a part of the autonomous triwheeler college project.

Please let me know any implementable solutions of interest for the triwheeler if you have any.

## Dataset
The dataset includes 1280px X 720px video from smartphone which is scaled down to 360 px x 120 px. And labels were assigned containing two lines.
Having 3 parameters for each line. 3 times 2, making it a 6 parameterized labels.

### Usage- Resolving dependencies
```
pip install keras
```

Download openCV from 
https://packages.debian.org/buster/armhf/python3-opencv/download
Navigate to the directory and type the following on the terminal.
```
dpkg -i python3-opencv_3.2.0+dfsg-4+b4_armhf.deb
```

# Running the Lane Detection on Rpi 3 
Attach the Pi Camera to th Rpi3 board and run the followingg command.
```
python3 draw_detected_lanes.py
```

## Authors
* Yash Gupta
