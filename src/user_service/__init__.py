import pathlib
import sys
import os

PRJ_PTH = pathlib.Path(os.path.abspath(__file__)).parents[0]
sys.path.append(str(PRJ_PTH))
sys.path.append(str(PRJ_PTH.parents[1]))
sys.path.append(str(PRJ_PTH.parents[1] / "configs"))

from infrastructures.utils import io

config = io.load_config("configs/local/service_config.yaml")
