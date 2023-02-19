#!/usr/bin/env python3

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


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
