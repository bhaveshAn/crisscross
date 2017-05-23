'''
TTS
====

The :class:`TTS` provides provides access to public methods to
use text to speech of your device.

Simple Examples
---------------

To speak::

    >>> from crisscross import tts
    >>> tts.speak(message=message)

'''


class TTS(object):
    '''
    TextToSpeech facade.
    '''

    def speak(self, message=''):
        '''Use text to speech capabilities to speak the message.

        :param message: What to speak
        :type message: str
        '''
        self._speak(message=message)

    # private

    def _speak(self, **kwargs):
        raise NotImplementedError()
