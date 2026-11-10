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

## Quick edits from the live site (✏️ button)

Every article has a ✏️ button (top right) that opens its file in GitHub's editor. It's
hidden from visitors: open any page with `?urednik` at the end of the address once
(e.g. `https://upute.milenij.eu/?urednik`) and that browser shows it from then on.
`?urednik=off` hides it again. Do this once per browser/phone.

This only hides the button; editing still needs write access to the GitHub repository.
Saving in GitHub's editor commits to `main`, which publishes the site.

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
  Every image in an article opens full-size when clicked (glightbox), with its alt text
  as the caption — so write a short, descriptive alt text. To turn this off for one
  image, add `{: .no-zoom }` after it.
- Callouts: `!!! info "Naslov"`, `!!! tip`, `!!! warning` (indent the text 4 spaces).
- Flowcharts are written as text in a ```` ```mermaid ```` code block (works in the CMS
  too; it shows as code in the editor and as a diagram on the site). See
  `docs/sidrene-cijene/ugostiteljstvo/index.md` for an example where each box links to
  a section: `click A href "#heading-id"`. Keep it to about three boxes side by
  side, so the text stays readable on phones.
- Abbreviations get hover tooltips from `includes/abbreviations.md` —
  add a line there (`*[PDV]: Porez na dodanu vrijednost`) to explain a new one everywhere.
- `description:` in the front matter (one sentence, about 100–150 characters) is the
  text under the title in share cards and Google results. Without it, the site
  description is used.
- Share cards: see [Share cards](#share-cards) below.
- The home page "Zadnje promjene" list and the "last updated" date on each page
  come from git history automatically. The list shows the 10 latest changes: each
  with its menu section, **Novo** (the change added the article) or **Ažurirano**,
  and the date it went live on `main` (a CMS draft counts once, when it's published).

## Site-wide settings (mkdocs.yml, under `extra:`)

- **`obavijest`**: the bar at the top of every page, e.g. in December
  "Nova godina {godina}: …" with a link. To hide it, set `tekst: ""`. Readers can
  close it; it comes back for them when the text changes.
- **`podrska`**: the "Niste pronašli odgovor?" box at the end of every article
  (email, and a phone number if you fill one in).
- Search also works without č/ć/š/ž/đ ("racun" finds "račun"). This is automatic
  (`hooks/hooks.py`), nothing to maintain.
- On GitHub, fonts and scripts are downloaded during the build and served from our own
  site (privacy plugin), so visitors' browsers don't contact Google. Local builds skip this.

## Share cards

When a page link is pasted into Viber, WhatsApp, email, Teams..., the app shows a preview
card: a 1200×630 picture plus the title and description. GitHub makes one picture per page
on every publish (local builds skip them, because Windows lacks the Cairo library).

- See a page's card: add `assets/images/social/` after the domain and `index.png` at the
  end, e.g. https://upute.milenij.eu/assets/images/social/sidrene-cijene/uvod/index.png
- The card shows the menu section, the article title, its `description:` and the web address.
- The design is in `social-cards/`: `milenij.yml` places the logo and text,
  `background.png` is the background (drawn by `make_background.py`; run it after changing
  colours or shapes there).
- Chat apps keep a card they've already fetched for a while, so a changed card can take
  time to show up there.

## Easter egg

Typing **snake** or **zmija** into the search box opens a snake game
(`docs/javascripts/snake.js`).

**Milenij Tim record:** the game shows the team's record (score and date, no names,
since this repository is public) to everyone. It's kept in `snake-rekord.json` (top of
the repository). A new record is saved only while playing on `mkdocs serve` on your own
computer: beat it and it's written to `snake-rekord.json` automatically. Commit and push
that file to show the new record on the live site (`git pull` first, in case someone else
beat it in the meantime). The live site itself can't save anything, but when a visitor
beats the team record there they get confetti and *"Bolji ste od Milenij tima!"*.

**Playing together on the office network:** one computer runs the site for everyone:

```bash
mkdocs serve -a 0.0.0.0:8001
```

The others open `http://<that computer's IP>:8001` (find the IPv4 address with `ipconfig`,
e.g. `http://192.168.1.103:8001`). Records they set are saved on the computer running
`mkdocs serve`. If nobody can connect, Windows Firewall is blocking it: when Windows asks,
allow Python, or set that computer's network to *Private* (Settings › Network & internet).
Stop it with Ctrl+C when you're done. While it runs, anyone on the network can open the site.

To remove the game: delete `docs/javascripts/snake.js`, `hooks/snake.py` and
`snake-rekord.json`, and their lines under `extra_javascript:` and `hooks:` in `mkdocs.yml`.

## Yearly: Nova godina

The Nova godina articles don't contain hard-coded years. They use `{{ godina }}`
(the new year) and `{{ godina - 1 }}` (the year before). Once a year, change
`godina:` under `extra:` in `mkdocs.yml` — that updates every page (and the top bar).

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
