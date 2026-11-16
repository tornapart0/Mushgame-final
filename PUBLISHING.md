# PyPI demo release

The distribution is `mushgame-demo`, version `0.1.0`. Its command launches the complete playable five-chapter demo. The wheel bundles the original `.mylang` source and its interpreter; Pygame is the only gameplay dependency. The Python launcher only handles installation, arguments, and user save locations.

## Install the built wheel

From the directory containing the downloaded wheel:

```sh
python3 -m pip install mushgame_demo-0.1.0-py3-none-any.whl
mushgame-demo
```

You can also run `python3 -m mushgame_demo`. Papyrus must be available on your system to use the requested font.

Packaged saves live in `~/Library/Application Support/Mushgame` on macOS, `%LOCALAPPDATA%/Mushgame` on Windows, and `$XDG_DATA_HOME/mushgame` (or `~/.local/share/mushgame`) on Linux. Pass `--save-dir PATH` to use another directory. Installing or updating the package does not overwrite your save.

## Build and validate

From the source folder:

```sh
python3 -m pip install build twine
python3 -m build
python3 -m twine check dist/*
```

Test an installed wheel from outside the source folder:

```sh
python3 -m venv demo-env
demo-env/bin/python -m pip install dist/mushgame_demo-0.1.0-py3-none-any.whl
demo-env/bin/mushgame-demo --version
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy demo-env/bin/mushgame-demo --smoke-test --save-dir demo-save
```

## Publish

The release has not been uploaded by the build process. Sign in to your PyPI account and create an API token. Keep that token in your local credential store; do not put it in source code or chat.

Upload from the source folder:

```sh
python3 -m twine upload dist/*
```

Twine prompts for authentication when no credentials are configured. Use `__token__` as the username and the API token as the password. The distribution name must be available to your account. After a successful upload, users can install with `python3 -m pip install mushgame-demo` and launch with `mushgame-demo`.

For a trial release, use `python3 -m twine upload --repository testpypi dist/*` with a separate TestPyPI account and token. See the [official Python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for account and publishing instructions.
