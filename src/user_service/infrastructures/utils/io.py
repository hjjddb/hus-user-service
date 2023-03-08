import yaml
from yaml import loader
import os


def load_config(file_path: str):
    with open(file_path) as f:
        data = yaml.load(f, Loader=loader.SafeLoader)
        return data
