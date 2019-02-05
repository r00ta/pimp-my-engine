from pimp_my_engine.logger.obd_logger import ObdRecorder
from pimp_my_engine.core.dtypes.obd_collector import ObdCollector
from threading import Thread, Condition
import obd
import logging

logging.basicConfig(filename='autotag_service.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def data_collection_thread(obd_collector, condition):
    logger.info('Data collection thread running')
    obd_recorder = ObdRecorder(obd_collector)
    commands = ['RPM']
    obd_recorder.connect()
    obd_recorder.register_callbacks(commands)
    obd_recorder.start_recording()
    
    # wait to stop recording
    logger.info('Data collection is running')
    condition.acquire()
    condition.wait() 
    condition.release()

    logger.info('Data collection thread dies now')
    obd_recorder.stop_recording()


def main():
    obd_collector = ObdCollector()
    condition = Condition()
    dcthread = Thread(
            target = data_collection_thread, 
            args = [obd_collector,condition]
            )
    dcthread.start()

if __name__ == '__main__':
    main()
