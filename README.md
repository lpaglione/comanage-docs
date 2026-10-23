# comanage-docs

[![Documentation Status](https://readthedocs.org/projects/comanage-docs/badge/?version=latest)](https://comanage-docs.readthedocs.io/en/latest/)

Source for the **COmanage Registry User Guide**, published at **https://comanage-docs.readthedocs.io/**.

## Description

The User Guide is administrative documentation for COmanage Registry v5. It covers context, concepts, configuration recipes and case studies, and complements the [Registry Technical Manual](https://spaces.at.internet2.edu/display/COmanage/Technical+Manual), which remains the reference for detailed configuration.

The guide is written in reStructuredText, built with [Sphinx](https://www.sphinx-doc.org/), and hosted on [Read the Docs](https://readthedocs.org/). Read the Docs rebuilds the site on every push.

## Repository layout

| Path | What's there |
|---|---|
| `registry/` | The Registry User Guide: `conf.py`, `index.rst`, `requirements.txt`, and one folder per section |
| `registry/about/`, `understanding/`, `using/`, `transitioning/` | Published sections |
| `registry/getting-started/`, `recipes/`, `case-studies/`, `community/` | Sections still under development |
| `registry/comanage-files/` | Git submodule with the screenshots and images the guide uses (see below) |
| `match/` | Reserved for a future COmanage Match User Guide |
| `.readthedocs.yaml` | Read the Docs build configuration |

### Images submodule

Images live in a separate repository, [InCommon-Training/comanage-files](https://github.internet2.edu/InCommon-Training/comanage-files), included here as a submodule at `registry/comanage-files`. It's public, so no credentials are needed to clone it. Read the Docs pulls it in automatically (`submodules: include: all`).

## Building locally

Requirements: Git and Python 3.11 (the version Read the Docs uses).

```bash
# Clone with the images submodule
git clone --recurse-submodules https://github.com/lpaglione/comanage-docs.git
cd comanage-docs

# If you already cloned without it:
git submodule update --init

# Install Sphinx and the theme, ideally in a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r registry/requirements.txt

# Build the HTML
sphinx-build -b html registry _build/html
```

Then open `_build/html/index.html` in a browser. `_build/` is ignored by Git.

To update the images to the latest from the comanage-files repo:

```bash
git submodule update --remote registry/comanage-files
```

Commit the updated submodule pointer afterwards.

## Branches

- `main` is what's published as `latest` on Read the Docs.
- Feature branches (such as `Getting-Started-Guide`) hold work in progress and are merged into `main` when ready.

## Support

For questions about COmanage Registry itself, see the COmanage community resources described in the guide's [Community](https://comanage-docs.readthedocs.io/en/latest/community/index.html) section. For problems with this documentation, open an issue in this repository.

## Roadmap

- Complete the Getting Started lessons, Configuration Recipes, Case Studies and Community sections.
- Add a COmanage Match User Guide under `match/`, published as a second Read the Docs project.

## Contributing

Corrections and suggestions are welcome. Open an issue, or fork the repo and send a pull request against `main`. Before submitting, build locally and check that your pages render without new Sphinx warnings.

## Authors and acknowledgment

Written by Laura Paglione for The COmanage Project, drawing on the COmanage Registry Technical Manual and Internet2/InCommon training materials.

## License

Not yet specified.

## Project status

Active. This repository moved from GitLab to GitHub in October 2026.
