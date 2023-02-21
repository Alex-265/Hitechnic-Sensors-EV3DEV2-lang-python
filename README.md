# Hitechnic-Sensors-EV3DEV2-lang-python

A Python library for working with Hitechnic sensors on the EV3DEV2 platform.
## Installation

This library requires the ev3dev2 Python package to be installed on your system. You can install it using the following command:
```
pip install python-ev3dev2
```
Once ev3dev2 is installed, you can download the Hitechnic-Sensors-EV3DEV2-lang-python

## Usage

To use the library in your Python script, you can import the sensor classes as follows:

```
from hisensors import HitechnicIrSeekerV2, HitechnicCompass
```
Then, you can create instances of the sensor classes and use their methods to read sensor values:


```
# create instances of the sensor classes
ir_seeker = HitechnicIrSeekerV2()
compass = HitechnicCompass()

# start calibration of the compass
compass.start_calibration()

# read the current rotation value of the compass
rotation = compass.read_rotation()

# read the current direction value of the IR seeker
direction = ir_seeker.read_direction()

# stop calibration of the compass
compass.stop_calibration()
```
Note that the HitechnicCompass class has methods to start and stop calibration. These methods must be used to calibrate the compass before using its read_rotation method.
### Support

If you have any issues with this library, please feel free to create an issue on the GitHub repository:

[https://github.com/Alex-265/Hitechnic-Sensors-EV3DEV2-lang-python](https://github.com/Alex-265/Hitechnic-Sensors-EV3DEV2-lang-python/issues)

