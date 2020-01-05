from pylab.devices import pyvisa_resource_manager

class KeysightB2962A():

    def __init__(self, identifier):
        self._identifier = identifier
        self._instrument = pyvisa_resource_manager.open_resource(self._identifier)
        self.reset()

    def get_idn(self):
        return self._instrument.query('*idn?')

    def reset(self):
        self._instrument.write('*rst')

    def close(self):
        self._instrument.close()

    def enable_channel(self, channel):
        write_string = ':outp'+ str(channel)  + ' on'
        self._instrument.write(write_string)

    def disable_channel(self, channel):
        write_string = ':outp' + str(channel)  + ' off'
        self._instrument.write(write_string)

    def set_channel_mode(self, channel, mode):
        mode_string = ''
        if mode == 'current':
            mode_string = 'curr'
        elif mode == 'voltage':
            mode_string = 'volt'
        write_string = ':sour' + str(channel) + ':func:mode ' + mode_string
        self._instrument.write(write_string)

    def set_current_output(self, channel, current):
        write_string = ':sour' + str(channel) + ':curr '+ str(current)
        self._instrument.write(write_string)

    def set_voltage_output(self, channel, voltage):
        write_string = ':sour' + str(channel) + ':volt '+ str(voltage)
        self._instrument.write(write_string)

    def voltage_pulse(self, channel, amplitude, width):
        self._instrument.write(':sour'+ str(channel)+':func:shap puls')
        self._instrument.write(':sour'+ str(channel)+':volt 0')
        self._instrument.write(':sour'+ str(channel)+':volt:trig ' + str(amplitude))
        self._instrument.write(':sour'+ str(channel)+':puls:widt ' + str(width))
        self._instrument.write(':init (@'+ str(channel)+')')
