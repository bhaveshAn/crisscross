import subprocess
from crisscross.facades import TTS
from crisscross.utils import whereis_exe


class EspeakTextToSpeech(TTS):
    ''' Speaks using the espeak program
    '''
    def _speak(self, **kwargs):
        subprocess.call(["espeak", kwargs.get('message')])


class FliteTextToSpeech(TTS):
    ''' Speaks using the flite program
    '''
    def _speak(self):
        subprocess.call(["flite", "-t", kwargs.get('message'), "play"])


def instance():
    if whereis_exe('espeak'):
        return EspeakTextToSpeech()
    elif whereis_exe('flite'):
        return FlitetextToSpeech()
    return TTS()
