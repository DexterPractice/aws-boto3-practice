import json
import os
import traceback
from datetime import datetime
from time import time


##LOG_STREAM = "InstanceScheduler-{:0>4d}{:0>2d}{:0>2d}"

"""
def load_models():
    cdw = os.getcwd()
    models = os.path.join(cdw, "models")
    aws_data_path = os.getenv("AWS_DATA_PATH", None)
    if aws_data_path is not None:
        aws_data_path = ":".join([aws_data_path, models])
    else:
        aws_data_path = models
    os.environ["AWS_DATA_PATH"] = aws_data_path


load_models()

"""
dt = datetime.utcnow
