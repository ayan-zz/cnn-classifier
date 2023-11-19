import os
import yaml
from CNNClassifier import logger
import json
import joblib
from typing import Any
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(Path_to_yaml:Path)->ConfigBox:
    with open(Path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
        return ConfigBox(content)
    
@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass

@ensure_annotations
def load_model():
    pass

@ensure_annotations
def get_size():
    pass


@ensure_annotations
def create_directory(path_to_directory:list,verbose=True):
    for path in path_to_directory:
        os.makedirs(Path,exist_ok=True)
        if verbose:
            logger.info(f"create directory at: {Path}")


