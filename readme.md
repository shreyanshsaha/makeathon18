# Better Automation <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/L%26T.png" width="48">


## Introduction
Our approach improves human safety in production/manufacturing by detecting the presence of humans all around the workspace. The machines change their working capacity and power depending upon that.

## How to achieve it
### Modules used
- IOT Device - Raspberry Pi
- Detection device - User Phone / User ID Card
- A Server

### Approach
We make a central server which monitors the activities of all IOT Devices. The raspberry pi's are distributed across the production mainly near automation robots. The users connect to the raspberry pi as soon as they enter their detection range, since this range usually includes the machines it is safe to say that the user is in range of a robot. This information is updated in the server.

The raspberry pi is also connected to the robots. It controls the operation of the robots (mainly speed and response time). Once a user is detected to be in range of a robot. The Server sends a signal through the pi to the robot. The signal tells the robot how much to reduce the operation speed and when to resume back.

The raspberry pi can detect presence of humans by two methods:
- Image Processing
- Wifi

Since, Image Processing would not be able to detect distance between human and robot as the pixel distance may vary and there will be need of lot of calibration; the wifi approach is better.

An access point (made by a router) can identify how many devices are connected to it, at the same time it will be able to tell the strength of the connection. We use this to detect if the user is in range. Furthermore, we live in an era of wireless communication and WiFi. Many production units will have many routers spreading throughout the manufacturing plant. This helps to reduce cost as we wont need to spend much on infrastructure.

## Befinit of our approach
- Cost Affective
- Light on processor as it is distributed
- No need to configure the user devices
- No need of machine training and user training


# Technical Information
