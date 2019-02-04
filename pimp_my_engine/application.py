from pimp_my_engine.logger.obd_logger import ObdRecorder
from pimp_my_engine.core.dtypes.obd_collector import ObdCollector
import obd
import logging

logging.basicConfig(filename='autotag_service.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    obd_collector = ObdCollector()
    obd_recorder = ObdRecorder()
    commands = ['RPM']
    obd_recorder.connect()
    obd_recorder.register_callbacks(commands)
    obd_recorder.start_recording()

if __name__ == '__main__':
    main()
