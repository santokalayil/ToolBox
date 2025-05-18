
import dotenv
from pathlib import Path

dotenv.load_dotenv(Path(__file__).parent / ".env")

from . import __config
