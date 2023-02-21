
# -----------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

from ev3dev2.sensor import Sensor

class HitechnicIrSeekerV2:
    def __init__(self):
        self.seeker = Sensor(driver_name='ht-nxt-ir-seek-v2')
        self.seeker.mode = 'DC'
        # direction is 0 for no signal, or 1-9 for left-right direction
        self.direction = 0

    def read_direction(self):
        self.direction = self.seeker.value(0)
        return self.direction
        
class HitechnicCompass:
    def __init__(self):
        self.compass = Sensor(driver_name='ht-nxt-compass')
        self.compass.mode = 'COMPASS'
        
    def start_calibration(self):
        self.compass.command('BEGIN-CAL')

    def stop_calibration(self):
        self.compass.command('END-CAL')

    def read_rotation(self):
        return self.compass.value(0)

    
