import status
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info('Runner started...')
status.main()