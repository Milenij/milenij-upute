"""MkDocs hook: the "Milenij Tim" high score for the snake easter egg (docs/javascripts/snake.js).

The team record lives in `snake-rekord.json` at the top of the repository: just the
score and the date. No names, because the repository is public on GitHub.
- Every build copies it to the site as assets/snake-rekord.json, where the game reads it,
  so the live site shows the team record.
- Only while `mkdocs serve` runs, the game can save a new record (also when teammates
  play on it over the local network): the served copy then says "spremanje": true, the
  game sends new records to /__snake-rekord, and this hook writes snake-rekord.json.
  The live site (GitHub Pages) can't save anything; commit and push the file to publish.

The file is outside docs/ on purpose: a change there would make `mkdocs serve`
rebuild and reload the page in the middle of the game.

To remove the easter egg, delete this file, its line under hooks: in mkdocs.yml,
docs/javascripts/snake.js and snake-rekord.json.
"""
import json
import logging
import os
import threading
from datetime import date

log = logging.getLogger("mkdocs.hooks.snake")

RECORD_FILE = "snake-rekord.json"
SITE_PATH = os.path.join("assets", "snake-rekord.json")
ENDPOINT = "/__snake-rekord"
MAX_SCORE = 20 * 20  # board size in snake.js

_lock = threading.Lock()
_serving = False  # True under `mkdocs serve`, set in on_startup


def _record_path(config):
    return os.path.join(os.path.dirname(config["config_file_path"]), RECORD_FILE)


def _read(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _public(data):
    """Only the score and date, whatever else someone may have added to the file."""
    try:
        score = int(data.get("score") or 0)
    except (TypeError, ValueError):
        score = 0
    return {"score": score, "date": str(data.get("date", ""))} if score > 0 else {}


def _write_site_copy(config, record):
    """The copy the game reads; under `mkdocs serve` it also tells the game it can save."""
    data = dict(record, spremanje=True) if _serving else record
    if data:
        _write(os.path.join(config["site_dir"], SITE_PATH), data)


def on_startup(command, dirty):
    global _serving
    _serving = command == "serve"


def on_post_build(config):
    _write_site_copy(config, _public(_read(_record_path(config))))


def on_serve(server, config, builder):
    site_app = server.get_app()

    def app(environ, start_response):
        if environ.get("PATH_INFO", "").endswith(ENDPOINT):
            return _save(environ, start_response, config)
        return site_app(environ, start_response)

    server.set_app(app)
    return server


def _save(environ, start_response, config):
    def reply(status, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        start_response(status, [("Content-Type", "application/json; charset=utf-8"),
                                ("Content-Length", str(len(body))),
                                ("Cache-Control", "no-store")])
        return [body]

    if environ.get("REQUEST_METHOD") != "POST":
        return reply("405 Method Not Allowed", {"error": "POST only"})

    try:
        length = min(int(environ.get("CONTENT_LENGTH") or 0), 2048)
        sent = json.loads(environ["wsgi.input"].read(length) or b"{}")
        score = int(sent.get("score"))
    except (ValueError, TypeError, AttributeError):
        return reply("400 Bad Request", {"error": "expected {score}"})
    if not 0 < score <= MAX_SCORE:
        return reply("400 Bad Request", {"error": "score out of range"})

    path = _record_path(config)
    with _lock:
        current = _public(_read(path))
        if score <= current.get("score", 0):
            return reply("200 OK", {"saved": False, **current})
        record = {"score": score, "date": date.today().strftime("%d.%m.%Y.")}
        _write(path, record)
        # Also update the copy the running local site serves, so the game sees it right away
        _write_site_copy(config, record)

    log.info("Snake: new Milenij Tim record %s, saved to %s; commit it to publish", score, RECORD_FILE)
    return reply("200 OK", {"saved": True, **record})
