# Milenij Upute

Source of the Milenij help site, **https://upute.milenij.eu** — built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/),
edited through Decap CMS (`/admin/`) and published to GitHub Pages.

## Run it locally

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
pip install -r requirements.txt
mkdocs serve                      # http://127.0.0.1:8001
```

After `requirements.txt` changes, run `pip install -r requirements.txt` again
(otherwise you'll see e.g. *The "macros" plugin is not installed*).

Before pushing, `mkdocs build --strict` should pass — that's what the PR check runs.

## How publishing works

- **Pull requests** (including the CMS's `cms/...` drafts) are built with
  `mkdocs build --strict` by `.github/workflows/check.yml`. A broken link, missing
  image or bad front matter fails the check.
- **Every push to `main`** is built and deployed by `.github/workflows/publish.yml`.
  The footer version is `1.0_<run number> (<commit>)`.

## Writing articles

- Each article is a folder with an `index.md`. Front matter:

  ```yaml
  ---
  title: Naslov članka
  tags:
    - fiskalizacija 2.0        # from cms-data/tags
  keywords:                    # optional extra search words, shown as grey badges
    - adresar
  ---
  ```

- Images go in `docs/assets/images/`. The CMS links them as `/assets/images/...`.
- Callouts: `!!! info "Naslov"`, `!!! tip`, `!!! warning` (indent the text 4 spaces).
- Abbreviations get hover tooltips from `includes/abbreviations.md` —
  add a line there (`*[PDV]: Porez na dodanu vrijednost`) to explain a new one everywhere.
- The home page "Zadnje promjene" table and the "last updated" date on each page
  come from git history automatically.

## Yearly: Nova godina

The Nova godina articles don't contain hard-coded years. They use `{{ godina }}`
(the new year) and `{{ godina - 1 }}` (the year before). Once a year, change
`godina:` under `extra:` in `mkdocs.yml` — that updates every page.

In the CMS editor these show as `{{ godina }}`; leave them as they are.

## Adding a new section

1. Create the folder under `docs/` (e.g. `docs/skladiste/`) with a `.pages` file:
   `title: Skladište`.
2. Add the folder name to the `nav:` list in `docs/.pages`.
3. Add a CMS collection in `docs/admin/config.yml` (copy an existing section block).
4. Optionally add a card for it on the home page (`docs/index.md`).

## Upgrading packages

Versions in `requirements.txt` are pinned on purpose. To upgrade, bump a version,
run `mkdocs build --strict` locally, check the site, then commit.

Material for MkDocs reaches end of life on 5 May 2027; its successor is
[Zensical](https://zensical.org/), which can read this `mkdocs.yml`.

## Commit messages

Describe the change, e.g. `Nova godina: update for 2027` or
`Sidrene cijene: add Veleprodaja screenshot`. The CMS writes its own messages.
