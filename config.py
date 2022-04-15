import os
import logging

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(ROOT_DIR, "file")

class Config:

    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@host/table_name")
    SECRET_KEY = os.getenv("SECRET_KEY", "324bef6c5985f7ad7c8527d2")