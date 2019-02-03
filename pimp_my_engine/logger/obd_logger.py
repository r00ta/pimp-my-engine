import obd
import logging 

logger = logging.getLogger(__name__)

class ObdRecorder:
    def __init__(self, obd_collector):
        self.obd_collector = obd_collector
        self.connection = None

    def connect(self, portstr = None, baudrate = None):
        '''
        Connects to the obdii device and returns the connection status
        '''
        logger.info('Start obd connection')
        self.connection = obd.Asyc(portstr = portstr, baudrate = baudrate)
        logger.info('Connection status: {}'.format(self.connection.status()))
        return self.connection.status()

    def _callback(r):
        self.obd_collector.update(r.command.name, r.value.magnitude)

    def register_callbacks(commands):
        for cmd in commands:
            logger.info('Logging command: {}'.format(cmd))
            self.connection.watch(obd.commands[cmd], callback = _callback)

