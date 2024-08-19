from pathlib import Path

from harmonizer.win_size import WindowSize

# -- COMMON --
PROJECT_NAME = "harmonizer"

# -- DIRECTORIES --
ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "configs"
USER_DIR = Path("~").expanduser() / f".{PROJECT_NAME}"

# -- WINDOW SIZE --
MAIN_WINDOW_SIZE = WindowSize(800, 470)

QQC_WINDOW_SIZE = WindowSize(600, 600)

NEW_TUNE_WINDOW_SIZE = WindowSize(600, 500)

# -- CONFIGS --
TUNING_FILE = CONFIG_DIR / "tuning.json"
USER_TUNE_FILE = USER_DIR / "tuning.json"
