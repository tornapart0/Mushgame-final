# Mushgame: The Last Little Sun

You are **Nori**, a mushroom who inherits Grandma Luma's kitchen. A vast cyberpunk city is growing around your little shop. Feed your neighbors, install solarpunk technology, and find a place in the government so you can change the city's future.

All game logic, drawing, dialogue, sound generation, and tests are written in **Tay's Sensible Lang** (`.mylang`). **Pygame Community Edition** is the only external dependency. The included Python files are the existing language runtime. Every visual is drawn with Pygame; audio is synthesized locally. The game uses your system's **Papyrus** font throughout.

## Play on this Mac

Double-click **Play Mushgame.command**, or open this folder in VS Code and press **Cmd+Shift+B**. The prepared `.venv` in this local folder has Pygame installed.

## Installable PyPI demo

The `mushgame-demo` distribution includes the playable story and a launch command. Install the built wheel with `python3 -m pip install mushgame_demo-0.1.0-py3-none-any.whl`, then run **`mushgame-demo`** or **`python3 -m mushgame_demo`**. The wheel is ready for PyPI upload; it has not been published yet. See [PUBLISHING.md](PUBLISHING.md) for building, testing, and publishing.

Installed demos save in your user application-data directory, rather than inside the installed package. Use `mushgame-demo --save-dir PATH` to override that directory. Source-folder launches keep their existing local save location.

## Install from the ZIP

Requires Python 3.10 or newer. Extract the entire folder first, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python interpreter.py main.mylang
```

On Windows, create the environment with `py -m venv .venv`, then replace `.venv/bin/python` with `.venv\Scripts\python.exe` in the commands above. The ZIP excludes the machine-specific virtual environment. Papyrus must be installed on the destination computer; Pygame falls back to its default font when the system does not provide it.

## Controls

| Key | Action |
| --- | --- |
| WASD / arrows | Move Nori |
| Shift | Walk faster |
| E / Enter | Interact with a nearby person or station |
| 1–5, arrows + Enter, or mouse | Choose dialogue and menu options |
| J / Tab | Open the journal, kitchen guide, and map |
| Left / Right in the journal | Switch pages |
| Esc | Pause, resume, or close a conversation |
| F5 | Save |
| M | Toggle music and sound |

The game pauses when you switch away from its window. The gold arrow and **NEXT** hint guide you toward the next useful interaction. The window can be resized; artwork and mouse coordinates scale together.

## Your kitchen

1. Read the orders over customers' heads, or talk to them with E.
2. At the chopping table, choose the matching recipe.
3. At the stove, press E to start cooking.
4. Return to the stove and press E to collect the finished dish.
5. Talk to the matching customer and choose **Serve**.

Customers never abandon their orders, and ingredients are free. You can prepare a second recipe while the first cooks. If you make an unwanted dish, take it to the recipe shelf and share it with the neighborhood. Spare prepared ingredients can also be returned there.

Earn coins to install a **solar stove**, **living roof**, **rainwater loop**, and **community battery**. Each upgrade changes the shop's appearance and its abilities. Roof and water upgrades unlock additional recipes.

## A story in five chapters

- **A kitchen, a seed:** open the shop, serve three neighbors, build your first improvement.
- **When the towers rise:** gather Jun's and Mira's signatures, feed six customers, install a second improvement.
- **A place at the table:** choose a permit with Inspector Vale, then accept Sable's invitation into government.
- **The city we choose:** work with Tess, Jun, and Mira to propose energy, food, and transit reforms. Bring working examples to the committees.
- **The last little sun:** sign a city charter, then explore the transformed neighborhood and continue running your kitchen.

Your choices determine ownership, access, grants, trust, and the ending's details. A Commons Charter can replace earlier private contracts and ID gates; a Renewal Charter preserves your committee agreements. An optional delivery to the clinic gives Mira's night crew a warm meal.

## Saving

The game saves every 45 seconds of active play, at major story milestones, when resting, and when quitting normally. Choose **Continue your story** on the title screen. Progress is stored in `mushgame-save.json` beside `main.mylang`. Saves are validated before loading, and writes use a temporary file so a partial write does not replace the previous save.

## Verify

```sh
.venv/bin/python interpreter.py --check main.mylang
.venv/bin/python interpreter.py test_story.mylang
.venv/bin/python interpreter.py main.mylang --smoke-test
```

The `.mylang` tests cover both complete story routes, the economy, cooking, upgrades, wrong-dish recovery, the clinic favor, movement, interaction reachability, keyboard and mouse input, waypoint routing, saving, malformed saves, and rendering every location and game overlay. Tests use temporary saves and do not overwrite your progress.

For a headless render check, set `SDL_VIDEODRIVER=dummy` and `SDL_AUDIODRIVER=dummy`. Add `--screenshot preview.png` after `--smoke-test` to capture a title frame.

## Hackatime

`.wakatime-project` names this project **Mushgame**. The Hackatime VS Code extension tracks actual editor activity. The terminal-wakatime zsh plugin tracks commands in interactive shells; noninteractive shells do not automatically load its hooks. Use a fresh terminal after installation.

Configure your account through [Hackatime setup](https://hackatime.hackclub.com/my/wakatime_setup) and follow the [terminal documentation](https://hackatime.hackclub.com/docs/editors/terminal). Keep credentials in private user configuration, never in this repository. The game itself does not generate time-tracking entries.
