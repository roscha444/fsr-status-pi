import status
import logging
from dotenv import load_dotenv

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
load_dotenv()
logging.info('Runner started...')
status.main()