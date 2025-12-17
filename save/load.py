import json
import os

"""Simple save utilities.

Files are stored in the same folder as this module as: <name>.json
Each save contains at least: name, character
"""

SAVE_DIR = os.path.dirname(__file__)


def _save_path(name: str) -> str:
	return os.path.join(SAVE_DIR, f"{name}.json")


def create_new_save(name: str) -> str:
	"""Create a new save file with the given player name.

	Returns the path to the created save file.
	"""
	path = _save_path(name)
	data = {"name": name, "character": None}
	with open(path, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)
	return path


def update_save(name: str, updates: dict) -> str:
	"""Update an existing save with the provided key/value pairs.

	Returns the path to the save file.
	"""
	path = _save_path(name)
	if not os.path.exists(path):
		raise FileNotFoundError(f"Save not found: {path}")
	with open(path, "r", encoding="utf-8") as f:
		data = json.load(f)
	data.update(updates)
	with open(path, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)
	return path


def load_save(name: str) -> dict:
	path = _save_path(name)
	if not os.path.exists(path):
		raise FileNotFoundError(f"Save not found: {path}")
	with open(path, "r", encoding="utf-8") as f:
		return json.load(f)

