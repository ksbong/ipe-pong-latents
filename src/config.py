from pathlib import Path
import os


def get_data_root() -> Path:
    """Return local data root.

    Set IPE_PONG_DATA_ROOT to the directory containing Pong metadata/data files.
    """
    env_path = os.getenv("IPE_PONG_DATA_ROOT")
    if env_path is None:
        raise RuntimeError(
            "IPE_PONG_DATA_ROOT is not set. "
            "Set it to the local directory containing Pong metadata/data files."
        )
    return Path(env_path).expanduser().resolve()