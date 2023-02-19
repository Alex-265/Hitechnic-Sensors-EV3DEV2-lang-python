# Hitechnic-Sensors-EV3DEV2-lang-python

This python script reads the output of the Hitechnic IrSeekerV2 and the Hitechnic Compass Sensor.

**How to use**
```
from hisensors import hitechnicIrSeekerV2
from hisensors import hitechnicCompass
```
Compass Sensor
Calibrate Start
```
hisensors.hitechnicCompass.startCalibration()
```

Calibrate Stop
```
hisensors.hitechnicCompass.stopCalibration()
```

Read Data from IrSeeker
```
hitechnicIrSeekerV2.direction
```
Read Data from Compass Sensor
```
compass = hitechnicCompass.rotation
```
