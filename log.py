import shutil
import os
from itertools import cycle
import logging.config
from datetime import datetime
import json
from bokeh.io import output_file, save, show
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import Div
import pandas as pd

try:
    import hyperdash
    HYPERDASH_AVAILABLE = True
except ImportError:
    HYPERDASH_AVAILABLE = False


def export_args_namespace(args, filename):
    with open(filename,'w')as fp:
        json.dump(dict(args.get_kwargs),fp,sort_keys=True,indent=4)


def setup_logging(log_file='log.txt', resume=False, dummy=False):
    """
    Setup logging configuration
    """
    if dummy:
        logging.getLogger('dummy')
    else:
        if os.path.isfile(log_file) and resume:
            file_mode = 'a'
        else:
            file_mode = 'w'

        root_logger = logging.getLogger()
        if root_logger.handlers:
            root_logger.removeHandler(root_logger.handlers[0])
        logging.basicConfig(level=logging.DEBUG,
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            filename=log_file,
                            filemode=file_mode)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)


'''
测试样例
'''
time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

save_path = time_stamp
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

setup_logging(os.path.join('./', 'log.txt'),
                  resume=True,
                  dummy=False)

logging.info("saving to %s"% save_path)
logging.debug("run arguments: %s"% save_path)

