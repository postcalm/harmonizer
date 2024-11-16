from pathlib import Path

from harmonizer.core.size import FrameSize

# -- COMMON --
PROJECT_NAME = "harmonizer"

# -- DIRECTORIES --
ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "configs"
STORAGE_DIR = Path("~").expanduser() / f".{PROJECT_NAME}"
TMP_DIR = STORAGE_DIR / ".tmp"

# -- WINDOW SIZE --
MAIN_WINDOW_SIZE = FrameSize(800, 470)

QQC_WINDOW_SIZE = FrameSize(600, 600)

NEW_TUNE_WINDOW_SIZE = FrameSize(600, 500)

# -- CONFIGS --
TUNING_FILE = CONFIG_DIR / "tuning.json"
USER_TUNE_FILE = STORAGE_DIR / "tuning.json"
TONALITY_CONFIG = CONFIG_DIR / "tonality.json"
