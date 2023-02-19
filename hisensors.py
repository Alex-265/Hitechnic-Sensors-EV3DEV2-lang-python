#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Copyright (c) 2023 Alexander Neumeier <alexneuprill@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

from ev3dev2.sensor import Sensor

class hitechnicIrSeekerV2:
    seeker = Sensor(driver_name='ht-nxt-ir-seek-v2')
    seeker.mode = 'DC'
    # direction 0 kein signal, 1-9 für Ball ist Hier. 1=Ganz links, 5=Mitte, 9=Ganz Rechts
    direction = seeker.value(0)


class hitechnicCompass:
    global compass
    compass = Sensor(driver_name='ht-nxt-compass')
    compass.mode = 'COMPASS'

    def startCalibration():
        compass.command('BEGIN-CAL')
    
    def stopCalibration():
        compass.command('END-CAL')