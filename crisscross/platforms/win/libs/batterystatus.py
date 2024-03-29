__all__ = ('battery_status')


import ctypes
from crisscross.platforms.win.libs import win_api_defs


def battery_status():
    status = win_api_defs.SYSTEM_POWER_STATUS()
    if not win_api_defs.GetSystemPowerStatus(ctypes.pointer(status)):
        raise Exception('Could not get system power status.')

    return dict((field, getattr(status, field)) for field, _ in status._fields_)
