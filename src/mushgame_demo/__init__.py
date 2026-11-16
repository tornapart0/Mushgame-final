"""Distribution launcher; gameplay remains in main.mylang."""

import argparse
import os
import sys
from pathlib import Path

__version__ = "0.1.0"


def default_save_directory():
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Mushgame"
    if os.name == "nt":
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "Mushgame"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "mushgame"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Mushgame: The Last Little Sun — playable demo")
    parser.add_argument("--version", action="version", version=f"mushgame-demo {__version__}")
    parser.add_argument("--smoke-test", action="store_true", help="Render eight frames and exit")
    parser.add_argument("--screenshot", type=Path, help="Save a title screenshot during a smoke test")
    parser.add_argument("--save-dir", type=Path, help="Override the user save directory")
    args = parser.parse_args(argv)
    if args.screenshot and not args.smoke_test:
        parser.error("--screenshot requires --smoke-test")
    from .interpreter import run
    from .mylang.compiler import LanguageError

    source = Path(__file__).with_name("main.mylang")
    previous_save = os.environ.get("MUSHGAME_SAVE_DIR")
    save_dir = args.save_dir or (Path(previous_save) if previous_save else default_save_directory())
    try:
        save_dir.mkdir(parents=True, exist_ok=True)
        os.environ["MUSHGAME_SAVE_DIR"] = str(save_dir.resolve())
        game_args = ["--smoke-test"] if args.smoke_test else []
        if args.screenshot:
            game_args.extend(["--screenshot", str(args.screenshot.resolve())])
        run(source.read_text(encoding="utf-8"), filename=str(source), arguments=game_args)
    except (OSError, LanguageError) as error:
        parser.exit(1, f"Mushgame: {error}\n")
    finally:
        if previous_save is None:
            os.environ.pop("MUSHGAME_SAVE_DIR", None)
        else:
            os.environ["MUSHGAME_SAVE_DIR"] = previous_save

