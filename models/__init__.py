from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .task import Task
from .model_info import ModelInfo
from .alarm_info import AlarmInfo

