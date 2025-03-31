# Wake the BEEP UP!
Winning the SheHacks + General Motor Challenge <a href="https://devpost.com/software/wake-the-beep-up?_gl=1*1t51oc3*_gcl_au*MTc1NjI3MDEyOC4xNzQzNDU4NzYx*_ga*OTcyODk4NDE5LjE3NDM0NTg3NjE.*_ga_0YHJK3Y10M*MTc0MzQ1ODc2MC4xLjEuMTc0MzQ1ODc2Ni4wLjAuMA">Devpost

## Inspiration
Drowsy Driving is a significant factor in a huge proportion of road accidents globally

## What it does
We present a simple real-time video monitoring application to alert drivers as they turn sleepy

## How we built it
We used OpenCV to monitor eyes of the driver and python libraries pygame to send sound alerts to wake up the driver. We used acknowledgement to confirm the driver is up, if not we used twilio to automatically call 911 for emergency

## Challenges we ran into
Integrating the python script to an actual web application was time-consuming

## Accomplishments that we're proud of
Figuring out a way to automatically call a phone number through python API

## What we learned
OpenCV for computer vision, CMake tools for development, Python API for calling, Figma for interactive design

## What's next for Wake The Beep Up
While this is just a way for us to put our step in the game, we have several ideas for the future to enhance our application:
1. Adding visual alerts to pop up/flash the phone screen
2. Adding haptic alerts in the driver seat by integrating hardware devices to create vibrations for alerting
3. Confirming state of being awake through solving a quick math question
4. Adding option to either call a cab in the application
   
## Built With:
figma, html, css, opencv, python, twilio

<img src="https://github.com/chaa-san/Snooze-Cruise/blob/main/images/Home.png" width="350" height=auto>


## To run the python Code:
Install  & import the following python libraries: opencv-python, dlib, imutils, scipy

And execute the command from python code folder path:
python DrowsinessDetection.py
