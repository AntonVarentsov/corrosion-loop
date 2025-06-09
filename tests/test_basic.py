import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from corrosion_loop.config import get_settings


def test_settings_has_url():
    settings = get_settings()
    assert settings.database_url
