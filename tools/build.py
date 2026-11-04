"""Builds the static portfolio pages.

To add a project: add an entry to WORK (and, for a full case study, a body in
tools/content.py), then run:  python3 tools/build.py
Pages are written in place; commit the generated HTML. The Satellica case
study is a hand-built page and is not generated here.
"""
import os, html
from content import WORK, INSIGHTS, LAB, CASE_BODIES, ARTICLE_BODIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "Wenjuan (Joerica) Zou"
EMAIL = "joericazou@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/wenjuanzou/"
RESUME = "/assets/Wenjuan_Zou_Resume.pdf"
PHOTO = "/assets/img/headshot.webp"
PORTRAIT = "/assets/img/about-portrait.jpg"
ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9M8.5 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
EXT = '<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3h7v7M13 3 4 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">')


def esc(s):
    return html.escape(s, quote=True)


def page(path, title, desc, body, current="", home=False):
    nav = [("/work/", "Work", ""), ("/insights/", "Insights", "hide-sm"), ("/lab/", "Lab", "hide-sm"), ("/about/", "About", "")]
    links = "".join(
        f'<a href="{h}" class="{c}"{" aria-current=\"page\"" if current == l else ""}>{l}</a>' for h, l, c in nav)
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/img/logo.png">
</head>
<body{' class="home"' if home else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="brand" href="/"><img src="/assets/img/logo.png" alt="">Wenjuan Zou <span>(Joerica)</span></a>
<nav class="nav" aria-label="Main">{links}<a class="cta" href="{RESUME}">Resume</a></nav>
</div></header>
<main id="main">
{body}
</main>
{CLOSING}
</body>
</html>
"""
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)


CLOSING = f"""<footer class="closing on-ink"><div class="wrap">
<h2>Need someone to help customers or teams adopt a complex product?</h2>
<p>I'm open to learning experience design, customer education and enablement roles, remote or in Greater Boston. I work in English and Mandarin.</p>
<div class="btns"><a class="btn primary" href="mailto:{EMAIL}">Email me</a><a class="btn" href="{LINKEDIN}">LinkedIn</a><a class="btn" href="{RESUME}">Download resume</a></div>
<div class="site-foot"><span>&copy; 2026 {SITE}, Greater Boston</span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
</div></footer>"""


def tags(w):
    t = "".join(f'<span class="tag">{esc(x)}</span>' for x in w["tags"][:2])
    return f'<div class="tags">{t}<span class="tag kind">{esc(w["kind"])}</span></div>'


def frame(src, alt=""):
    return f'<div class="frame"><img loading="lazy" src="{src}" alt="{esc(alt)}"></div>'


def card(w):
    return (f'<a class="card" href="{w["href"]}">{frame(w["thumb"])}'
            f'<div class="body">{tags(w)}<h3>{esc(w["title"])}</h3><p>{esc(w["summary"])}</p></div></a>')


def feature(w):
    return (f'<a class="feature" href="{w["href"]}">{frame(w["thumb"])}'
            f'<div>{tags(w)}<h3>{esc(w["headline"])}</h3><p class="goal">{esc(w["goal"])}</p>'
            f'<p class="sum">{esc(w["summary"])}</p><span class="more">Read the case study {ARROW}</span></div></a>')


ICONS = {
    "job": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/></svg>',
    "practice": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4v16M6 8h8a3 3 0 0 1 0 6H6M14 14l4 6"/></svg>',
    "support": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/></svg>',
    "ai": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.6L18 9l-4.2 1.4L12 15l-1.8-4.6L6 9l4.2-1.4z"/><path d="M18 15l.8 2.2L21 18l-2.2.8L18 21l-.8-2.2L15 18l2.2-.8z"/></svg>',
}


def build_home():
    featured = [w for w in WORK if w.get("featured")]
    rest = [w for w in WORK if not w.get("featured")]
    body = f"""
<section class="hero on-ink"><div class="wrap">
<div class="hero-grid">
<div>
<p class="kicker">Learning experience designer for customer education and enablement</p>
<h1>I design learning that helps people adopt complex products, and I measure whether it worked.</h1>
<p class="lede">I start from the business problem, design for the moment someone gets stuck, and build the course, job aid or AI workflow that fixes it.</p>
<div class="btns"><a class="btn primary" href="#work">See case studies</a><a class="btn" href="/about/">About me</a></div>
</div>
<figure class="hero-portrait"><img src="{PHOTO}" alt="Portrait of Wenjuan (Joerica) Zou"><figcaption>English &amp; Mandarin</figcaption></figure>
</div>
<div class="proof">
<div><b>~80%</b><span>fewer routine how-to questions after self-serve product guides at Satellica</span></div>
<div><b>~40%</b><span>of weekly coordination time saved with human-in-the-loop Claude workflows</span></div>
<div><b>+20%</b><span>course completion after rebuilding a slide-based Title IX course at Northeastern</span></div>
</div>
</div></section>

<section class="section" id="work"><div class="wrap">
<div class="section-head"><div><p class="kicker">Selected case studies</p><h2>Work that starts from a business problem</h2></div><a class="btn" href="/work/">All work</a></div>
{''.join(feature(w) for w in featured)}
</div></section>

<section class="band"><div class="wrap">
<div class="section-head"><div><p class="kicker">More projects</p><h2>Scenarios, simulations and curriculum</h2>
<p>Storyline builds, interactive video and curriculum design across healthcare, workplace AI and learning science.</p></div></div>
<div class="grid">{''.join(card(w) for w in rest)}</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><p class="kicker">How I work</p><h2>Four habits behind every project</h2></div></div>
<div class="principles">
<div class="principle"><span class="glyph">{ICONS['job']}</span><h3>Start with the job</h3><p>I find the task people are stuck on and what getting it wrong costs before I decide what to build.</p></div>
<div class="principle"><span class="glyph">{ICONS['practice']}</span><h3>Practice over content</h3><p>Learners make realistic decisions and get feedback that explains the tradeoff, not just right or wrong.</p></div>
<div class="principle"><span class="glyph">{ICONS['support']}</span><h3>Support the moment of need</h3><p>Short clips, job aids and self-serve guides do more on the job than a course people finish once.</p></div>
<div class="principle"><span class="glyph">{ICONS['ai']}</span><h3>AI with a human at the gate</h3><p>I use AI to draft, build and automate, and I review every output before it reaches a learner.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<div class="section-head"><div><p class="kicker">Insights</p><h2>How I think about learning design</h2></div><a class="btn" href="/insights/">All insights</a></div>
<div class="grid">{''.join(insight_card(i) for i in INSIGHTS[:3])}</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><p class="kicker">Lab</p><h2>Tools and AI products I'm building</h2><p>Small products that test an idea about learning or work. New ones are added as they ship.</p></div><a class="btn" href="/lab/">Visit the Lab</a></div>
<div class="grid">{''.join(lab_card(l) for l in LAB[:3])}</div>
</div></section>

<section class="section"><div class="wrap about-strip">
<div class="photo"><img loading="lazy" src="{PORTRAIT}" alt="Joerica at Harvard Yard"></div>
<div><p class="kicker">About</p><h2>A designer who learned how courses break</h2>
<p>I trained in interaction design, built clinical and university eLearning, then spent years at TransPerfect making enterprise courses work across languages and systems. After a graduate certificate in Learning Design and Technology at Harvard Extension, I joined an AI research startup to run client education and research operations.</p>
<p class="muted">That mix is why I design the way I do: I think about the interface, the learner and the system the course has to live in.</p>
<div class="btns" style="margin-top:28px"><a class="btn" href="/about/">More about me</a></div></div>
</div></section>
"""
    page("/", f"{SITE} | Learning Experience Designer",
         "Learning experience designer for customer education, enablement and AI-enabled learning workflows. Case studies, insights and tools.",
         body, home=True)


def build_work_index():
    featured = [w for w in WORK if w.get("featured")]
    rest = [w for w in WORK if not w.get("featured")]
    body = f"""<section class="page-hero"><div class="wrap">
<p class="kicker">Work</p><h1>Case studies and projects</h1>
<p class="goal">Three full case studies, then Storyline builds and curriculum projects. Each page says whether it was client work, a concept project or graduate coursework.</p>
</div></section>
<section class="section" style="padding-top:88px"><div class="wrap">{''.join(feature(w) for w in featured)}</div></section>
<section class="band"><div class="wrap"><div class="section-head"><div><p class="kicker">More projects</p><h2>Scenarios, simulations and curriculum</h2></div></div>
<div class="grid">{''.join(card(w) for w in rest)}</div></div></section>"""
    page("/work/", f"Work | {SITE}", "Case studies and eLearning projects by Wenjuan (Joerica) Zou.", body, "Work")


def build_case(w, prev_w, next_w):
    meta = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in w["meta"])
    links = "".join(f'<a class="btn{" primary" if i == 0 else ""}" href="{h}">{esc(t)} {EXT}</a>' for i, (t, h) in enumerate(w.get("links", [])))
    cover = w.get("cover_html") or f'<img src="{w["cover"]}" alt="{esc(w.get("cover_alt", ""))}">'
    pager = (f'<a href="{prev_w["href"]}"><span>Previous</span>{esc(prev_w["title"])}</a>' if prev_w else "<span></span>") + \
            (f'<a class="next-link" href="{next_w["href"]}"><span>Next</span>{esc(next_w["title"])}</a>' if next_w else '<a class="next-link" href="/work/"><span>Back to</span>All work</a>')
    body = f"""<article><section class="page-hero"><div class="wrap">
<p class="crumb"><a href="/work/">Work</a><span aria-hidden="true">/</span><span>{esc(w["title"])}</span></p>
{tags(w)}
<h1 style="margin-top:18px">{esc(w["headline"])}</h1>
<p class="goal">{esc(w["goal"])}</p>
<div class="links">{links}</div>
<div class="cover">{cover}</div>
<dl class="meta">{meta}</dl>
</div></section>
<section class="cs-body"><div class="wrap"><div class="read">
{CASE_BODIES[w["slug"]]}
</div>
<nav class="pager" aria-label="More work">{pager}</nav>
</div></section></article>"""
    page(w["href"], f'{w["title"]} | {SITE}', w["summary"], body, "Work")


def insight_card(i):
    return (f'<a class="card" href="/insights/{i["slug"]}/">{frame(i.get("thumb", i["img"]))}'
            f'<div class="body"><div class="tags"><span class="tag">{esc(i["topic"])}</span></div><h3>{esc(i["title"])}</h3><p>{esc(i["dek"])}</p></div></a>')


def build_insights():
    body = f"""<section class="page-hero"><div class="wrap"><p class="kicker">Insights</p>
<h1>How I think about learning design</h1>
<p class="goal">Short essays on the learning science I use most, each with an infographic I made during my Learning Design and Technology program.</p></div></section>
<section class="section" style="padding-top:72px"><div class="wrap"><div class="grid">{''.join(insight_card(i) for i in INSIGHTS)}</div></div></section>"""
    page("/insights/", f"Insights | {SITE}", "Essays on learning science and instructional design practice.", body, "Insights")
    for i in INSIGHTS:
        b = f"""<article class="article"><section class="page-hero"><div class="wrap"><div class="read">
<p class="crumb"><a href="/insights/">Insights</a><span aria-hidden="true">/</span><span>{esc(i["topic"])}</span></p>
<h1>{esc(i["title"])}</h1><p class="when">{esc(i["date"])}, by Wenjuan (Joerica) Zou</p>
<figure class="fig"><img src="{i["img"]}" alt="Infographic: {esc(i["title"])}"></figure>
{ARTICLE_BODIES[i["slug"]]}
<nav class="pager"><a href="/insights/"><span>Back to</span>All insights</a><a class="next-link" href="/work/"><span>See it applied</span>The work</a></nav>
</div></div></section></article>"""
        page(f'/insights/{i["slug"]}/', f'{i["title"]} | {SITE}', i["dek"], b, "Insights")


def lab_card(l):
    st = '<span class="status live">Live</span>' if l["status"] == "live" else '<span class="status wip">In progress</span>'
    inner = f'{st}<h3>{esc(l["title"])}</h3><p>{esc(l["problem"])}</p><p class="what">{esc(l["what"])}</p>'
    if l.get("href"):
        return f'<a class="lab-card" href="{l["href"]}">{inner}</a>'
    return f'<div class="lab-card">{inner}</div>'


def build_lab():
    body = f"""<section class="page-hero"><div class="wrap"><p class="kicker">Lab</p>
<h1>Tools and AI products I'm building</h1>
<p class="goal">Each one starts from a problem I kept running into. I build them with AI coding tools and review every output myself. New entries are added as they ship.</p></div></section>
<section class="section" style="padding-top:72px"><div class="wrap"><div class="grid">{''.join(lab_card(l) for l in LAB)}</div></div></section>"""
    page("/lab/", f"Lab | {SITE}", "AI-enabled tools and learning products built by Wenjuan (Joerica) Zou.", body, "Lab")


def tl(when, org, role, text):
    return f'<li><span class="when">{when}</span><div><b>{org}</b><span class="role">{role}</span><p>{text}</p></div></li>'


def build_about():
    body = f"""<section class="page-hero"><div class="wrap about-strip">
<div class="photo"><img src="{PORTRAIT}" alt="Joerica at Harvard Yard"></div>
<div>
<p class="kicker">About</p>
<h1 style="font-size:clamp(2.2rem,4.4vw,3.4rem)">I'm Wenjuan, and most people call me Joerica.</h1>
<p style="margin-top:24px">I design learning for the moment someone gets stuck: a new rep on a discovery call, a client setting up their first study at 10 p.m. in another time zone, a nurse in a hard conversation with a patient. I start from what that person needs to do differently, then build the practice, the job aid or the workflow that gets them there.</p>
<p>I came to learning design through interaction design. My M.S. at Northeastern taught me to think about the interface first, and that habit stuck. I built clinical eLearning for 350+ nurses at Commonwealth Care Alliance, rebuilt a university Title IX course that raised completion by 20%, and spent years at TransPerfect localizing and testing enterprise courses across Western European and East Asian languages. That is where I learned how courses actually break.</p>
<p>In 2023 I went back to the science with Harvard Extension's Learning Design and Technology program. Then I joined Satellica, an AI-powered UX research platform, to run client education and research operations: self-serve product guides that cut routine how-to questions by about 80%, and human-in-the-loop Claude workflows that saved about 40% of my weekly coordination time.</p>
<div class="btns" style="margin-top:28px"><a class="btn primary" href="{RESUME}">Download resume</a><a class="btn" href="{LINKEDIN}">LinkedIn</a></div>
</div></div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><p class="kicker">Experience</p><h2>Where the work happened</h2></div></div>
<ul class="timeline">
{tl("Jan 2026 &ndash; Present", "Satellica", "Operations Manager &mdash; Client Education &amp; Research Operations", "Task-based help center guides, step-by-step videos and client onboarding cut routine how-to questions by about 80%. Four human-in-the-loop Claude workflows saved about 40% of weekly coordination time. Bilingual product updates for clients and investors; recruitment for six qualitative studies.")}
{tl("Sep 2019 &ndash; Dec 2025", "TransPerfect", "E-Learning Localization Engineer, freelance", "Project-based eLearning localization in Storyline, Captivate and Adobe Creative Suite, with functional QA and LMS compatibility testing.")}
{tl("May 2016 &ndash; Aug 2019", "TransPerfect", "E-Learning Localization Engineer", "Localized and quality-tested courses for global enterprise clients in Western European and East Asian languages, catching layout, interaction and font-encoding issues before delivery.")}
{tl("Oct 2015 &ndash; May 2016", "Commonwealth Care Alliance", "E-Learning Specialist", "Interactive clinical and compliance modules in Storyline for 350+ nurses and nurse practitioners, reducing learner seat time by 30% compared with the previous modules, based on LMS time tracking. SCORM on HealthStream, refined through learner surveys and focus groups.")}
{tl("Jul 2015 &ndash; Oct 2015", "Northeastern University", "E-Learning Designer", "Rebuilt a slide-based Title IX course as interactive eLearning with the Office of Diversity, raising completion by 20%; student and faculty focus groups shaped navigation and content.")}
</ul>
</div></section>

<section class="band"><div class="wrap">
<div class="section-head"><div><p class="kicker">Education and credentials</p><h2>The foundation</h2></div></div>
<div class="creds">
<div><b>Harvard Extension School</b><span>Graduate Certificate, Learning Design and Technology, 2023&ndash;2026, GPA 4.0</span></div>
<div><b>Association for Talent Development</b><span>E-Learning Instructional Design Certificate, 2023</span></div>
<div><b>Northeastern University</b><span>M.S. Digital Media, Interactive Design, 2013&ndash;2015</span></div>
</div>
<div class="skills">
<div><h3>Learning design</h3><p>Needs analysis, action mapping, ADDIE and SAM, backward design, storyboarding, scenario-based learning, assessment design, microlearning, performance support, evaluation planning.</p></div>
<div><h3>Customer education and enablement</h3><p>Product and customer education, client onboarding, help center content, software and CRM training, SME collaboration, eLearning localization.</p></div>
<div><h3>Tools</h3><p>Articulate Storyline 360 and Rise 360, Adobe Captivate, Canvas, HealthStream, SCORM, Camtasia, Canva, Adobe Creative Suite, Claude, ChatGPT, ElevenLabs, HeyGen, HTML and CSS.</p></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><p class="kicker">Methods</p><h2>How I choose a process</h2></div></div>
<div class="principles" style="grid-template-columns:repeat(3,minmax(0,1fr))">
<div class="principle"><h3>ADDIE</h3><p>For well-defined, end-to-end builds where audience analysis, objectives and evaluation need to be planned up front.</p></div>
<div class="principle"><h3>SAM</h3><p>For tight timelines or shifting SME input: quick Storyline prototypes, reviewed early and often.</p></div>
<div class="principle"><h3>Double Diamond</h3><p>For behavior-change problems where the real need isn't clear yet: understand learners first, then design and test.</p></div>
</div>
</div></section>"""
    page("/about/", f"About | {SITE}", "About Wenjuan (Joerica) Zou, learning experience designer in Greater Boston.", body, "About")


if __name__ == "__main__":
    build_home()
    build_work_index()
    cases = [w for w in WORK if w["slug"] in CASE_BODIES]
    for n, w in enumerate(cases):
        build_case(w, cases[n - 1] if n else None, cases[n + 1] if n + 1 < len(cases) else None)
    build_insights()
    build_lab()
    build_about()
    print("built", len(cases), "case pages,", len(INSIGHTS), "insights")
