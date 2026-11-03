# Portfolio

Portfolio site of Wenjuan (Joerica) Zou, Learning Experience Designer.
Deployed by Cloudflare on every push to `main`.

## Structure
- `index.html`, `work/`, `insights/`, `lab/`, `about/`: generated pages
- `work/satellica-client-education/`: hand-built case study (not generated)
- `assets/site.css`: shared styles; `assets/img/`: local images
- `tools/content.py`: all text for projects, insights and Lab entries
- `tools/build.py`: regenerates the pages

## Add a project or Lab entry
1. Add an entry to `WORK` or `LAB` in `tools/content.py` (and a body in `CASE_BODIES` for a full case study).
2. Run `python3 tools/build.py`.
3. Commit and push.
