import os.path
import sys

sys.path.append(os.path.dirname(os.path.relpath(__file__)))
from .schema_pb2_grpc import *
sys.path.pop()

__version__ = '0.1.0'
