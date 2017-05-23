'''
Facades
=======

Interface of all the features available.

'''

__all__ = ('Accelerometer', 'Audio', 'Barometer', 'Battery', 'Call', 'Camera',
           'Compass', 'Email', 'FileChooser', 'GPS', 'Gravity', 'Gyroscope',
           'IrBlaster', 'Light', 'Orientation', 'Notification', 'Proximity',
           'Sms', 'TTS', 'UniqueID', 'Vibrator', 'Wifi', 'Flash',
           'Temperature')

from crisscross.facades.accelerometer import Accelerometer
from crisscross.facades.audio import Audio
from crisscross.facades.barometer import Barometer
from crisscross.facades.battery import Battery
from crisscross.facades.call import Call
from crisscross.facades.camera import Camera
from crisscross.facades.compass import Compass
from crisscross.facades.email import Email
from crisscross.facades.filechooser import FileChooser
from crisscross.facades.flash import Flash
from crisscross.facades.gps import GPS
from crisscross.facades.gravity import Gravity
from crisscross.facades.gyroscope import Gyroscope
from crisscross.facades.irblaster import IrBlaster
from crisscross.facades.light import Light
from crisscross.facades.proximity import Proximity
from crisscross.facades.orientation import Orientation
from crisscross.facades.notification import Notification
from crisscross.facades.sms import Sms
from crisscross.facades.tts import TTS
from crisscross.facades.uniqueid import UniqueID
from crisscross.facades.vibrator import Vibrator
from crisscross.facades.wifi import Wifi
from crisscross.facades.temperature import Temperature
