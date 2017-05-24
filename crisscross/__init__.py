'''
Crisscross
==========

'''

__all__ = ('accelerometer', 'audio', 'barometer', 'battery', 'call', 'camera',
           'compass', 'email', 'filechooser', 'flash', 'gps', 'gravity',
           'gyroscope', 'irblaster', 'light', 'orientation', 'notification',
           'proximity', 'sms', 'tts', 'uniqueid', 'vibrator', 'wifi',
           'temperature', 'bluetooth')

__version__ = '1.0.0dev'


from crisscross import facades
from crisscross.utils import Proxy

#: Accelerometer proxy to :class:`crisscross.facades.Accelerometer`
accelerometer = Proxy('accelerometer', facades.Accelerometer)

#: Audio proxy to :class:`crisscross.facades.Audio`
audio = Proxy('audio', facades.Audio)

#: Barometer proxy to :class:`crisscross.facades.Barometer`
barometer = Proxy('barometer', facades.Barometer)

#: Battery proxy to :class:`crisscross.facades.Battery`
battery = Proxy('battery', facades.Battery)

#: Call proxy to  :class `crisscross.facades.Call`
call = Proxy('call', facades.Call)

#: Compass proxy to :class:`crisscross.facades.Compass`
compass = Proxy('compass', facades.Compass)

#: Camera proxy to :class:`crisscross.facades.Camera`
camera = Proxy('camera', facades.Camera)

#: Email proxy to :class:`crisscross.facades.Email`
email = Proxy('email', facades.Email)

#: FileChooser proxy to :class:`crisscross.facades.FileChooser`
filechooser = Proxy('filechooser', facades.FileChooser)

#: GPS proxy to :class:`crisscross.facades.GPS`
gps = Proxy('gps', facades.GPS)

#: Gravity proxy to :class:`crisscross.facades.Gravity`
gravity = Proxy('gravity', facades.Gravity)

#: Gyroscope proxy to :class:`crisscross.facades.Gyroscope`
gyroscope = Proxy('gyroscope', facades.Gyroscope)

#: IrBlaster proxy to :class:`crisscross.facades.IrBlaster`
irblaster = Proxy('irblaster', facades.IrBlaster)

#: Light proxy to :class:`crisscross.facades.Light`
light = Proxy('light', facades.Light)

#: Orientation proxy to :class:`crisscross.facades.Orientation`
orientation = Proxy('orientation', facades.Orientation)

#: Notification proxy to :class:`crisscross.facades.Notification`
notification = Proxy('notification', facades.Notification)

#: Proximity proxy to :class:`crisscross.facades.Proximity`
proximity = Proxy('proximity', facades.Proximity)

#: Sms proxy to :class:`crisscross.facades.Sms`
sms = Proxy('sms', facades.Sms)

#: TTS proxy to :class:`crisscross.facades.TTS`
tts = Proxy('tts', facades.TTS)

#: UniqueID proxy to :class:`crisscross.facades.UniqueID`
uniqueid = Proxy('uniqueid', facades.UniqueID)

#: Vibrator proxy to :class:`crisscross.facades.Vibrator`
vibrator = Proxy('vibrator', facades.Vibrator)

#: Flash proxy to :class:`crisscross.facades.Flash`
flash = Proxy('flash', facades.Flash)

#: Wifi proxy to :class:`plyer.facades.Wifi`
wifi = Proxy('wifi', facades.Wifi)

#: Temperature proxy to :class:`crisscross.facades.Temperature`
temperature = Proxy('temperature', facades.Temperature)

#: Bluetooth proxy to :class:`crisscross.facades.Bluetooth`
bluetooth = Proxy('bluetooth', facades.Bluetooth)
