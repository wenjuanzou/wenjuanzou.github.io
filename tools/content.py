"""Site content. Images for older projects are served from the Wix media CDN."""


def wix(name, w=1400):
    ext = name.rsplit(".", 1)[-1]
    return f"https://static.wixstatic.com/media/{name}/v1/fit/w_{w},h_{w},q_85/img.{ext}"


WIXFILES = "https://26fd8a8f-f622-4c5b-9d08-6b32d90d27cd.filesusr.com/ugd/"

WORK = [
    dict(slug="ask-first-log-it-right", href="/work/ask-first-log-it-right/", featured=True,
         title="Ask First, Log It Right", kind="Concept project",
         tags=["Sales enablement", "CRM training"],
         headline="Ramping new reps on discovery calls and the CRM record they produce",
         goal="To give sales managers deals they can coach and forecast from a rep's first month.",
         summary="A 20-minute enablement experience for new Account Executives: a branching discovery-call simulation, a HubSpot logging walkthrough, two job aids and a 30-day reinforcement plan.",
         thumb="/assets/img/northpeak-cover.svg", cover="/assets/img/northpeak-cover.svg",
         cover_alt="Ask First, Log It Right course title screen",
         links=[("Open the course", "https://ask-first-log-it-right.pages.dev/"),
                ("Play the call simulation", "https://ask-first-log-it-right.pages.dev/story/story.html")],
         meta=[("Role", "Needs analysis, action mapping, scenario writing, development"),
               ("Audience", "New Account Executives at a B2B SaaS company, first 30 days"),
               ("Format", "~20 min self-paced course, simulation, video, job aids"),
               ("Tools", "Storyline 360 · HubSpot · HTML/CSS/JS · Cloudflare Pages")]),
    dict(slug="satellica-client-education", href="/work/satellica-client-education/", featured=True,
         title="Satellica Client Education", kind="Work project",
         tags=["Customer education", "AI workflows"],
         headline="Cutting routine client questions ~80% with self-serve product education",
         goal="To let a small team support clients across a 12-hour time difference.",
         summary="Six task-based help center guides with step-by-step clips, live onboarding, and a human-in-the-loop Claude playbook for recruitment operations at an AI research startup.",
         thumb="/work/satellica-client-education/media/01ad90c745.jpg"),
    dict(slug="ai-ethics-investigation-lab", href="/work/ai-ethics-investigation-lab/", featured=True,
         title="AI Ethics Investigation Lab", kind="Harvard LDT capstone",
         tags=["Workplace AI", "Scenario simulation"],
         headline="Turning AI policy into workplace judgment",
         goal="To prepare non-technical teams for AI incidents that a list of do's and don'ts can't cover.",
         summary="A one-week Canvas course on AI tools for workplace productivity, ending in a Storyline investigation where learners weigh evidence across emails and team chats and make a defensible call.",
         thumb=wix("e26989_2ee97eb915eb47cbb341f660ef315e79~mv2.png", 1200),
         cover=wix("e26989_bcfb47d3451449f5a1fc750773093e09~mv2.jpg", 1800), cover_alt="Investigation overview screen with three evidence channels",
         links=[("Play the investigation", "https://ai-ethics-investigation-lab.pages.dev/story"),
                ("Canvas course overview (PDF)", WIXFILES + "e26989_5e59318a1a4a4e7cbe6c03da2e37d08d.pdf")],
         meta=[("Role", "End-to-end instructional designer and developer"),
               ("Audience", "Professionals who use AI tools at work: HR, ops, support, product, analytics"),
               ("Format", "One-week self-paced Canvas course with a Storyline capstone"),
               ("Tools", "Storyline 360 · Canvas · ChatGPT · Claude · ElevenLabs")]),
    dict(slug="ai-ml-everyday-life", href="/work/ai-ml-everyday-life/",
         title="AI & ML in Everyday Life", kind="Design test, 5 days",
         tags=["Financial services", "Storyline"],
         headline="Explaining AI and machine learning through one customer's banking app",
         goal="To help entry-level banking staff explain the smart features customers see every day.",
         summary="A story-based Storyline module where learners follow Alex through fraud alerts, personalized offers and a virtual assistant, built in five days for an instructional design test.",
         thumb=wix("e26989_3f69ec691bc64b1f93199974d4bdf370~mv2.png", 1200),
         cover=wix("e26989_02c089dc78cc445baf192c47ec5113ad~mv2.png", 1800), cover_alt="Mobile banking app mockups used in the module",
         links=[("Play the module", "https://ai-ml-learning-for-everyday-life.pages.dev/story")],
         meta=[("Role", "Designer and developer"), ("Audience", "Entry-level banking and support staff; non-technical learners"),
               ("Timeline", "5 days"), ("Tools", "Storyline 360 · Perplexity · Google Flow · HeyGen · Canva")]),
    dict(slug="brain-hacks", href="/work/brain-hacks/",
         title="Brain Hacks", kind="Harvard course project",
         tags=["Learner research", "Gamification"],
         headline="Using learner research to shape a course on motivation",
         goal="To help busy adults build habits for tackling hard work, based on what they told us they needed.",
         summary="A gamified Storyline course shaped by personas, an 8-person focus group and usability testing with 4 learners, revised after each round.",
         thumb=wix("e26989_378ef5e6a80e42a6b654c36034250b50~mv2.jpg", 1200),
         cover=wix("e26989_378ef5e6a80e42a6b654c36034250b50~mv2.jpg", 1800), cover_alt="Brain Hacks title screen",
         links=[("Play the course", "https://brain-hacks-the-science-of-loving-hard-work.pages.dev/story"),
                ("Focus group report (PDF)", WIXFILES + "e26989_9741e6f2820e44309aebf7e08aea9f47.pdf"),
                ("Usability test report (PDF)", WIXFILES + "e26989_f087a6f9df96420c826fa6c82a9827a6.pdf")],
         meta=[("Role", "Researcher, designer and developer"), ("Audience", "Adult learners and busy professionals"),
               ("Research", "3 personas · 8-person focus group · 4 usability testers"), ("Tools", "Storyline 360 · Canva · Meta Animated Drawings · Zoom · Google Forms")]),
    dict(slug="when-behavior-speaks", href="/work/when-behavior-speaks/",
         title="When Behavior Speaks", kind="Concept project",
         tags=["Healthcare", "Scenario-based"],
         headline="Helping clinicians recognize GI distress in autistic children",
         goal="To catch treatable pain that shows up as behavior instead of words.",
         summary="An intake-room scenario where learners observe a child, weigh caregiver input and decide when to refer, with expert insight and Insight Points feedback.",
         thumb=wix("e26989_cbadd7a6b9654715ba45fc1ed6db50bb~mv2.png", 1200),
         cover=wix("e26989_cbadd7a6b9654715ba45fc1ed6db50bb~mv2.png", 1800), cover_alt="When Behavior Speaks title screen",
         links=[("Play the module", "https://when-behavior-speaks-recognizing-gi-distress-in-asd-child.pages.dev/story"),
                ("Design document (PDF)", WIXFILES + "e26989_ce1bbfe7949b4e14989489e089639f03.pdf"),
                ("Storyboard (PDF)", WIXFILES + "e26989_663ff0de3cfc4f3db0c0ae5af5fe3a30.pdf")],
         meta=[("Role", "Designer and developer"), ("Audience", "Pediatricians, nurses, medical assistants, ABA therapists"),
               ("Format", "11-slide scenario microlearning"), ("Tools", "Storyline 360 · NotebookLM · Perplexity · ElevenLabs · Canva")]),
    dict(slug="empathetic-communication-oncology", href="/work/empathetic-communication-oncology/",
         title="Empathetic Communication in Oncology Nursing", kind="Work sample",
         tags=["Healthcare", "Branching scenarios"],
         headline="Practicing the hardest conversations before they happen",
         goal="To give new oncology nurses a safe place to rehearse emotionally charged moments.",
         summary="A branching Storyline module built over a weekend: three action-mapped scenarios with mentor feedback, from a tearful patient to \"Am I going to die?\"",
         thumb=wix("e26989_0ab85a37ab524211a52b089a3a9c3ab8~mv2.png", 1200),
         cover=wix("e26989_0ab85a37ab524211a52b089a3a9c3ab8~mv2.png", 1800), cover_alt="Empathetic Communication in Oncology Nursing title screen",
         links=[("Play the module", "https://empathetic-communication-in-oncology-nursing.pages.dev/story"),
                ("Design document", WIXFILES + "e26989_8a1ee99601a44409b4d12eb80dbf041a.docx"),
                ("Storyboard", WIXFILES + "e26989_0486fb1b32c74fe4851d129c1f58e4d2.docx")],
         meta=[("Role", "Designer and developer"), ("Audience", "Nurses new to oncology (0–2 years)"),
               ("Timeline", "One weekend"), ("Tools", "Storyline 360 · Word · ChatGPT")]),
    dict(slug="clear-the-airway", href="/work/clear-the-airway/",
         title="Clear the Airway", kind="Concept project",
         tags=["Healthcare", "360° simulation"],
         headline="Turning a lecture video into an equipment-readiness simulation",
         goal="To help early-career clinicians find and choose pediatric airway equipment quickly.",
         summary="A Storyline module built on an OPENPediatrics teaching video, with a 360° room exploration, embedded video and knowledge checks.",
         thumb=wix("e26989_cd38875745a648f1b9b36d1eb2abc0ff~mv2.png", 1200),
         cover=wix("e26989_192a1413caba42108c87eed7a7887dd6~mv2.jpg", 1800), cover_alt="Knowledge check and certificate screens",
         links=[("Play the module", "https://clear-the-airway-an-interactive-pediatric-simulation.pages.dev/story")],
         meta=[("Role", "Designer and developer"), ("Audience", "Pediatric nurses, respiratory therapists, residents"),
               ("Format", "Interactive microlearning"), ("Tools", "Storyline 360 · CapCut · Canva · ChatGPT")]),
    dict(slug="wwi-armistice-learning-guide", href="/work/wwi-armistice-learning-guide/",
         title="11.11.18 Museum Learning Guide", kind="Harvard team project",
         tags=["Curriculum design", "Backward design"],
         headline="A museum learning guide built backward from what students should create",
         goal="To help grades 6–12 connect a WWI exhibit to memory, identity and peace.",
         summary="A team-designed learning guide for the National WWI Museum's Armistice centennial exhibit: a sound-based hook, a virtual scavenger hunt and a memorial design task.",
         thumb=wix("e26989_5a79738d5e734e51b75566abefea3200~mv2.png", 1200),
         cover=wix("e26989_ce5d9d101a3c43028c1834b8208aa531~mv2.png", 1800), cover_alt="Pages from the learning guide",
         links=[("Read the guide (PDF)", WIXFILES + "e26989_e0aa964da9de4e7bb56715c2b6d2edb7.pdf")],
         meta=[("Role", "Instructional design lead on a team project"), ("Audience", "Grades 6–12 and their teachers"),
               ("Format", "Pre-visit, virtual exhibit, post-visit"), ("Tools", "Word · Google Docs")]),
]


def fig(src, cap, alt=""):
    return f'<figure class="fig"><img loading="lazy" src="{src}" alt="{alt or cap}"><figcaption>{cap}</figcaption></figure>'


def sec(num, title, inner):
    return f'<section class="cs-sec"><p class="num">{num}</p><h2>{title}</h2>{inner}</section>'


def decisions(items):
    out = []
    for n, (h, body, why) in enumerate(items, 1):
        out.append(f'<div class="decision"><span class="n">{n}</span><div><h3>{h}</h3><p>{body}</p>'
                   + (f'<p class="why">{why}</p>' if why else "") + '</div></div>')
    return '<div class="decisions">' + "".join(out) + "</div>"


CASE_BODIES = {}

CASE_BODIES["ask-first-log-it-right"] = (
    sec("01 · The business problem", "New reps lose deals in the first five minutes",
        "<p>New Account Executives rarely lose deals for lack of product knowledge. They lose them by pitching before they understand the buyer. When a buyer asks \"So what does your company do?\", a new rep starts a product tour and never learns why the buyer took the call.</p>"
        "<p>The second gap shows up after the call. Whatever the rep did learn rarely reaches the CRM. Without the buyer's pain, its cost, a deadline and a dated next step on the record, a manager can't coach the deal or forecast it.</p>"
        "<p>So the course had to fix two things at once: the conversation, and the record the conversation produces.</p>")
    + """<div class="records">
<div class="record weak"><span class="lab">Weak record · logged three days later</span><h4>Dana Lee · Brightloom</h4><dl>
<dt>Notes</dt><dd>Great call! Seems ready to buy. Interested in the platform.</dd>
<dt>Pain</dt><dd class="missing">Not captured</dd><dt>Deadline</dt><dd class="missing">Not captured</dd>
<dt>Who decides</dt><dd class="missing">Not captured</dd><dt>Next step</dt><dd>Send info, follow up.</dd></dl></div>
<div class="record strong"><span class="lab">Strong record · logged before the next meeting</span><h4>Dana Lee · Brightloom</h4><dl>
<dt>Situation</dt><dd>Took the call because research takes too long and her team is stretched.</dd>
<dt>Pain</dt><dd>~3 weeks recruiting + ~1 week synthesis per study.</dd>
<dt>Critical event</dt><dd>Q1 roadmap locks January 15.</dd>
<dt>Decision</dt><dd>2-week pilot → IT security review → VP of Product.</dd>
<dt>Next step</dt><dd>Demo with Dana + VP, Tue 10:00 (task created).</dd></dl></div>
</div>
<p class="mono muted">The course opens with this comparison: same buyer, same 20 minutes, two very different records.</p>"""
    + sec("02 · What people needed to do differently", "Seven behaviors, six on the call and one after it",
          "<p>I action-mapped the goal down to observable behaviors, using the SPICED discovery framework from Winning by Design, which is common in B2B software sales.</p>"
          "<ul><li>Start with the situation: find out why the buyer took the call today.</li><li>Quantify the pain: turn \"it's slow\" into time, volume or headcount.</li>"
          "<li>Explore the impact: what the problem costs the business.</li><li>Find the critical event: a date that makes it urgent.</li>"
          "<li>Map the decision: the steps and who signs.</li><li>Then pitch, and book a dated next step.</li>"
          "<li>Log facts, not guesses, in a five-line note before the next meeting.</li></ul>")
    + sec("03 · Constraints", "Short, realistic, and honest about the tool",
          "<ul><li><b>About 20 minutes.</b> New reps are in back-to-back onboarding; anything longer gets skipped.</li>"
          "<li><b>HubSpot changes its labels often.</b> The walkthrough teaches the intent of each step so it survives UI changes.</li>"
          "<li><b>No real customer data.</b> Northpeak, Brightloom and every character are fictional.</li></ul>")
    + sec("04 · Key decisions", "Three choices that shaped the experience", decisions([
        ("Train the conversation and the record together",
         "The notes a learner earns in the call simulation are the exact fields they log in HubSpot afterward. Good questions unlock notes; pitching early costs trust and leaves fields empty.",
         "Why: separate \"sales skills\" and \"CRM training\" courses teach two habits that never connect. Here the CRM record is the consequence of the conversation."),
        ("Model, then practice, then transfer",
         "Learners first read an expert call where every question is tagged with the SPICED field it fills. Then they play the rep in a branching Storyline call with Dana. Finally they read a new call with a different buyer, with the rep's private guesses mixed in, and write the record from scratch.",
         "Why: worked examples lower the load for novices, and a fresh scenario checks whether the skill transfers instead of the answers being memorized."),
        ("Put the support where the work happens",
         "Two one-page job aids (a discovery cheat sheet and a HubSpot quick reference), if-then plans for the next three calls, and a 30-day plan with weekly manager reviews.",
         "Why: much of what reps learn fades without use. A reference at the moment of need and a manager checking real calls keep the habit alive."),
    ]))
    + sec("05 · The solution", "A 20-minute path from why to back on the job",
          """<div class="flow"><div><span class="k">Start here</span><b>Why calls go wrong</b><span>Two records, seven behaviors, SPICED.</span></div>
<div><span class="k">Part 1</span><b>The discovery call</b><span>Expert model, then a branching call simulation.</span></div>
<div><span class="k">Part 2</span><b>Log it in HubSpot</b><span>2:41 walkthrough, five steps, write a record yourself.</span></div>
<div><span class="k">Part 3 + job</span><b>Quick reference &amp; 30 days</b><span>Job aids, if-then plan, manager reviews, knowledge check.</span></div></div>
<figure class="fig"><video controls preload="none" playsinline src="https://ask-first-log-it-right.pages.dev/media/hubspot-walkthrough.mp4"></video><figcaption>HubSpot walkthrough (2 min 41 s): create the contact, log the call with a SPICED note, set a dated task. Fictional demo data.</figcaption></figure>
<p>The Storyline simulation tracks trust, best answers and unlocked notes in variables, so every ending reflects the choices the learner made. The course site itself is custom HTML, CSS and JavaScript on Cloudflare Pages, with progress tracking and a scored knowledge check.</p>""")
    + sec("06 · Measurement", "An evaluation plan tied to the sales manager's numbers",
          """<div class="stats"><div><b>~40% → 70%</b><span>discovery calls logged with a complete SPICED note, by day 30</span></div>
<div><b>22% → 30%</b><span>discovery-to-demo conversion for new reps, within one quarter</span></div></div>
<div class="callout info"><b>Note</b>These targets come from a fictional stakeholder intake written for this concept project. They are an evaluation plan, not measured results.</div>
<p>Behavior is checked on real calls: in week 1 the manager reviews one recorded call against a four-line scorecard (questions, pain, critical event and decision, CRM note), then one call clip and one HubSpot record each week until day 30.</p>""")
    + sec("07 · What I'd do next", "Test it with real reps",
          "<p>Pilot with a small cohort of new hires, compare their CRM completeness with the previous cohort, and listen to which simulation choices people get wrong most often. Those are the moments to rewrite first.</p>")
)

CASE_BODIES["ai-ethics-investigation-lab"] = (
    sec("01 · The problem", "Ethics training stops at the policy list",
        "<p>Most AI ethics training is a list of do's and don'ts. Real workplace issues don't arrive that way. Evidence is scattered across tools and conversations, ownership is unclear (who can pause a system?), and teams disagree about what the real risk is.</p>"
        "<p>The hard part isn't defining bias. It's deciding what to do next when the impact is real and the information is incomplete.</p>")
    + fig(wix("e26989_85163b19ddf94c7a82bf445e50b7afcf~mv2.png", 1800), "The Canvas course: Modules 1–2 build responsible-use habits and AI workflows, Module 3 is the investigation, Module 4 is transfer.")
    + sec("02 · Course design", "From AI user to AI decision-maker in one week",
          "<p>I designed the full one-week, self-paced Canvas course, not just the simulation.</p>"
          "<ul><li><b>Modules 1–2:</b> responsible-use foundations and repeatable AI workflows: prompting, iteration and quality checks.</li>"
          "<li><b>Module 3:</b> the AI Ethics Investigation Lab, a Storyline capstone built around a biased hiring-system incident.</li>"
          "<li><b>Module 4:</b> transfer, turning the experience into a personal plan and a reusable decision habit.</li></ul>")
    + sec("03 · Key decisions", "How the investigation teaches judgment", decisions([
        ("Use authentic workplace artifacts",
         "Learners investigate through emails, team chats and leadership notes, the same channels where a real incident would surface.",
         "Why: anchoring practice in real work makes the skill easier to recognize on the job."),
        ("Let clarity be earned",
         "Evidence is revealed step by step. Learners gather clues across channels, notice patterns such as biased data signals and missing stop-authority, and only then make a recommendation.",
         "Why: progressive disclosure mirrors how incidents unfold and keeps the decision from being obvious too early."),
        ("Feedback as coaching",
         "The final recommendation gets feedback that explains the tradeoffs of each option, not just right or wrong.",
         "Why: in ethics there is rarely one correct answer, so the reasoning is what learners need to take away."),
        ("End with a framework they can reuse",
         "The lab closes with a simple Pause-and-Check framework for evaluating AI use in any workplace tool.",
         "Why: the scenario is one case; the framework is what transfers."),
    ]))
    + fig(wix("e26989_bcfb47d3451449f5a1fc750773093e09~mv2.jpg", 1800), "Investigation overview: three evidence channels, unlocked step by step.")
    + sec("04 · My role and tools", "End to end, with AI as an assistant",
          "<p>I designed the scenario, evidence trail and assessment logic, wrote all learner-facing copy and feedback, built the Storyline interactions with states, variables and triggers, and integrated the lab into the Canvas course.</p>"
          "<p>ChatGPT and Claude helped me brainstorm scenarios and tighten feedback copy; ElevenLabs produced voiceover and sound; an image model produced some visuals. I made the final decisions on learning flow, tone and feedback logic.</p>")
    + sec("05 · Reflection", "Ethics as a decision habit",
          "<p>Workplace reality sits between \"AI is amazing, just use it\" and \"AI is risky, follow the policy.\" People need to act with limited information while harm is possible. What I wanted learners to practice was judgment: noticing early signals, slowing down at the right moment without freezing progress, choosing a responsible next step that fits their authority, and explaining that decision in a way that builds trust.</p>")
)

CASE_BODIES["ai-ml-everyday-life"] = (
    sec("01 · The brief", "Explain AI vs. ML to people who use it every day",
        "<p>This module was my response to a full-stack instructional design test. The brief: introduce non-technical learners to the basics of artificial intelligence and machine learning, the difference between them, and their impact on daily life, in five days.</p>")
    + sec("02 · Learning objectives", "What learners can do afterward",
          "<ul><li>Explain AI vs. ML in simple, clear language.</li><li>Identify common AI- and ML-powered features in everyday digital experiences.</li>"
          "<li>Recognize both the benefits and the concerns of smart technologies.</li></ul>")
    + sec("03 · Key decisions", "Abstract concepts, familiar screens", decisions([
        ("One character, one app",
         "Learners follow Alex through a banking app: a fraud alert, a personalized credit offer and a virtual assistant. Each feature introduces one concept.",
         "Why: anchoring abstract ideas in a familiar product makes them easier to explain to a customer later."),
        ("Design the app, not just the slides",
         "I mapped realistic user interactions in Google Flow and built mobile banking UI mockups in Canva, so the scenario looks like the products learners support.",
         ""),
        ("Use AI to move fast, keep judgment human",
         "Perplexity for research and definitions, HeyGen for an avatar-led introduction. I checked content accuracy and wrote the knowledge checks myself.",
         ""),
    ]))
    + fig(wix("e26989_02c089dc78cc445baf192c47ec5113ad~mv2.png", 1800), "Mobile banking app mockups built for the scenario.")
    + sec("04 · Reflection", "Clarity under a deadline",
          "<p>Five days forced choices: one narrative, three features, short checks. It sharpened how I distill a technical topic and use AI tools across the whole process, from research to UI visuals.</p>")
)

CASE_BODIES["brain-hacks"] = (
    sec("01 · The problem", "Busy adults know what to do but can't start",
        "<p>Brain Hacks was my final project for Designing Educational Media at Harvard Extension. The audience: adult learners and professionals who struggle with procrastination and motivation, curious about brain science but with little background in it.</p>")
    + sec("02 · Research", "What learners told us before I built anything",
          "<p>I created three personas (Marcus, fitness-focused; Elena, career-driven; Alex, creatively curious), then ran a focus group with 8 adult learners. Three findings shaped the design:</p>"
          "<ul><li>They preferred short, interactive, media-rich content.</li><li>They had little neuroscience knowledge but high curiosity.</li>"
          "<li>They wanted practical application over theory.</li></ul>"
          f'<div class="links"><a class="btn" href="{WIXFILES}e26989_0294619afce14abc8ba91fec57c24194.pdf">Personas (PDF) &#8599;</a><a class="btn" href="{WIXFILES}e26989_9741e6f2820e44309aebf7e08aea9f47.pdf">Focus group report &#8599;</a></div>')
    + '<div class="figs">' + fig(wix("e26989_b6bd377be62f411195bfc1317d4da247~mv2.png", 1000), "Persona: Marcus") + fig(wix("e26989_a11041a7afd64f6296b0b8d30546ed68~mv2.png", 1000), "Persona: Elena") + "</div>"
    + sec("03 · Design", "A three-part journey", decisions([
        ("Learn the brain", "What dopamine is, how reward shapes motivation, and why it matters, told through an animated \"Brain\" narrator.", ""),
        ("Boost it wisely", "A drag-and-drop game and avatar scenarios where learners apply strategies to relatable goals.", "Why: the focus group asked for practice over theory."),
        ("Make it stick", "Twelve strategies and a personal action plan learners leave with.", ""),
    ]))
    + sec("04 · Testing and iteration", "What changed after usability testing",
          "<p>Four usability testers went through the Storyline prototype. They responded well to the color scheme, avatars and voiceover. The character stories felt less relatable than I intended, so I rewrote them. In follow-up, testers could recall strategies such as incremental goal-setting.</p>"
          "<p>All four testers reported learning something new about motivation. With four people, that is a formative signal, not proof of impact.</p>"
          f'<div class="links"><a class="btn" href="{WIXFILES}e26989_f087a6f9df96420c826fa6c82a9827a6.pdf">Usability test report &#8599;</a><a class="btn" href="{WIXFILES}e26989_698d593583d444fd9214256ef8529967.pdf">Project summary &#8599;</a></div>')
    + fig(wix("e26989_c54b37a71d2e4d978cfd39bd9afe479f~mv2.png", 1600), "Inside the course.")
    + sec("05 · What I'd do next", "Tools learners can take with them",
          "<p>Add downloadable action-plan templates, audio descriptions, and localized versions.</p>")
)

CASE_BODIES["when-behavior-speaks"] = (
    sec("01 · The problem", "Pain that looks like behavior",
        "<p>Many autistic children can't verbally express internal pain. Instead they may self-injure, seek pressure or refuse food. These signs are often read as autism traits, and treatable gastrointestinal conditions go unrecognized.</p>")
    + sec("02 · Goals", "What learners should do",
          "<ul><li>Recognize behavioral cues that may indicate GI distress.</li><li>Tell autism traits apart from pain-related behaviors.</li>"
          "<li>Refer early to the right clinician.</li><li>Reflect on what they'll watch for in their next encounter.</li></ul>")
    + sec("03 · Key decisions", "A simulated intake, not a lecture", decisions([
        ("Put the learner in the room",
         "Learners observe a child named Joey during an intake session and weigh his behavior and his caregiver's input before deciding what to do.",
         "Why: scenario practice in a low-risk space builds the observation habit the job requires."),
        ("Bring in expert thinking",
         "Commentary draws on published work by pediatric gastroenterologist Dr. Timothy Buie, synthesized from his research and talks.",
         ""),
        ("Reward evidence-informed choices",
         "Learners earn Insight Points for well-reasoned decisions and end with a reflection and a downloadable reference guide.",
         ""),
    ]))
    + fig(wix("e26989_328ffd98a0654c6b8b6ca070c855b670~mv2.png", 1600), "Expert insight inside the scenario.")
    + sec("04 · Process", "Research, design document, storyboard, build",
          "<p>I synthesized research from GI and autism experts, wrote a design document and storyboard, then built the 11-slide module in Storyline with graphics, audio, video and animation. The design used action mapping, Knowles' adult learning principles and Bloom's taxonomy (understand → apply → evaluate).</p>"
          + fig(wix("e26989_fd25b783eb95486a95fa71d46df941eb~mv2.png", 1600), "Scenario screens."))
)

CASE_BODIES["empathetic-communication-oncology"] = (
    sec("01 · The problem", "Clinical skills get trained; hard conversations don't",
        "<p>Nurse onboarding focuses on clinical skills. Emotional communication often gets less attention, and new nurses can feel unprepared for intense moments with patients and families. I built this module over one weekend as a work sample for oncology nurse onboarding.</p>")
    + sec("02 · Action mapping", "Three moments new nurses dread",
          "<ul><li>A silent or tearful patient after treatment.</li><li>A patient who asks, \"Am I going to die?\"</li><li>A family member upset about delays.</li></ul>"
          "<p>Each scenario has branching decision points and mentor pop-up feedback that explains what a response does to the patient's trust.</p>")
    + sec("03 · Key decisions", "Designing for emotional safety", decisions([
        ("Low stakes, real dialogue",
         "Learners choose responses in realistic conversations and see how the patient reacts, before they face the moment on a unit.",
         "Why: rehearsal in a safe space reduces freezing in the real one."),
        ("A mentor, not a grader",
         "Feedback comes from an experienced nurse character who coaches the choice instead of marking it wrong.",
         ""),
        ("Calm visual tone",
         "A clean, quiet visual style that keeps attention on the conversation.",
         ""),
    ]))
    + sec("04 · Process", "Research to storyboard in a weekend",
          "<p>I reviewed clinical empathy literature in oncology settings, mapped the scenarios, wrote a design document and storyboard, and built the module in Storyline, grounded in Knowles' adult learning principles, Bloom's taxonomy and situated learning.</p>"
          f'<div class="links"><a class="btn" href="{WIXFILES}e26989_c442f0df4b744b52a3e8154a42517108.pdf">Research: clinical empathy (PDF) &#8599;</a><a class="btn" href="{WIXFILES}e26989_8eeefd39659b45539a1c6ce418aade34.pdf">Research: nurses\' perceptions (PDF) &#8599;</a></div>')
)

CASE_BODIES["clear-the-airway"] = (
    sec("01 · The problem", "Hesitation costs time in a pediatric emergency",
        "<p>Early-career clinicians often lack hands-on exposure to every piece of airway equipment. In an emergency, hesitation over sizing or setup delays care. I took Dr. Traci Wolbrink's OPENPediatrics video on pediatric intubation and turned the equipment-preparation portion into an interactive primer.</p>")
    + sec("02 · Goals", "What learners practice",
          "<ul><li>Identify and select the right airway equipment.</li><li>Build spatial familiarity with where equipment sits in a patient room.</li>"
          "<li>Get feedback on sizing and usage choices.</li></ul>")
    + sec("03 · Key decisions", "From watching to doing", decisions([
        ("Explore a 360° room", "Learners search a 360° patient room to find each tool before answering questions about it.", "Why: recognition in context is closer to the real task than a list of names."),
        ("Short checks right after each clip", "Knowledge checks sit next to the video segment they test, so feedback arrives while the content is fresh.", ""),
        ("A completion certificate", "A micro-certificate closes the module so learners have a record of what they practiced.", ""),
    ]))
    + fig(wix("e26989_192a1413caba42108c87eed7a7887dd6~mv2.jpg", 1600), "Knowledge checks and completion certificate.")
    + sec("04 · What I'd do next", "Cover the whole procedure",
          "<p>Expand into a full branching simulation covering the procedure and post-intubation care.</p>")
)

CASE_BODIES["wwi-armistice-learning-guide"] = (
    sec("01 · The challenge", "Make an exhibit matter to a 12-year-old",
        "<p>For Designing Educational Media at Harvard Extension, our team responded to a museum curation challenge: an interactive learning guide for grades 6–12 based on the 11.11.18 Centennial Armistice exhibit at the National WWI Museum and Memorial. I led the instructional design decisions on our team.</p>")
    + sec("02 · Approach", "Backward design across history, ELA and art",
          "<ul><li><b>Pre-visit hook:</b> students close their eyes and listen to a recording of the guns falling silent. \"What did peace sound like in 1918?\"</li>"
          "<li><b>Virtual scavenger hunt:</b> identify three key figures, analyze two primary sources on civilian impact, explore one lasting legacy.</li>"
          "<li><b>Inquiry questions:</b> for example, \"Did the Armistice truly end the war?\"</li>"
          "<li><b>Post-visit creation:</b> design a memorial as a poster, drawing, sculpture or digital prototype.</li></ul>"
          "<p>The guide includes objectives, essential questions, assessment options and modifications for English language learners and younger students.</p>")
    + fig(wix("e26989_ce5d9d101a3c43028c1834b8208aa531~mv2.png", 1600), "Pages from the guide.")
    + sec("03 · What I learned", "Emotion as a door into history",
          "<p>Sound and creative tasks did more to make history personal than any reading. The project also taught me to scaffold one activity for very different learners.</p>")
)

INSIGHTS = [
    dict(slug="metacognition", topic="Metacognition", date="February 2025", title="How do we describe metacognition?",
         dek="Helping learners think about how they think: person, task and strategy.",
         img=wix("e26989_d4c87c16f0824ddfa5b1bae99182337d~mv2.png", 1400)),
    dict(slug="learner-attention", topic="Attention", date="March 2025", title="How do we gain and keep learners' attention?",
         dek="Five research-informed ways to earn attention, then hold it.",
         img=wix("e26989_d8f84d041d2e476bb1b44b0e489b8fe6~mv2.png", 1400)),
    dict(slug="assessment", topic="Assessment", date="April 2025", title="When should assessment happen in the learning process?",
         dek="Assessment for learning and of learning, built in from the start.",
         img=wix("e26989_b8cadf97167249e4885eedc8c82683d7~mv2.png", 1400)),
    dict(slug="learning-framework", topic="Course structure", date="March 2025", title="How do we create an effective framework for learners?",
         dek="Six components I rely on when structuring a learning journey.",
         img=wix("e26989_c0c9ea4884e04b05b187f69520903e25~mv2.png", 1400)),
    dict(slug="design-theories", topic="Learning theory", date="April 2025", title="What theories underlie effective design?",
         dek="Seven theories I use as a compass, and what each changes in a design.",
         img=wix("e26989_cb5741c933b84b0d94cddf083c4ffcbb~mv2.jpg", 1400)),
    dict(slug="learning-variety", topic="Variety", date="May 2025", title="How can strategies create variety in the learning process?",
         dek="Variety as equity: reaching more learners without overloading any of them.",
         img=wix("e26989_a812a05cef1f475ba2a2915ad064a8da~mv2.png", 1400)),
]


def h2(t):
    return f"<h2>{t}</h2>"


ARTICLE_BODIES = {
    "metacognition":
        "<p>Metacognition is \"thinking about thinking.\" It's the learner's ability to be aware of their own thought processes and regulate them. In learning design, this means helping learners pause, reflect and adapt their approach as they go. It's not just about learning content, but learning how to learn better.</p>"
        + h2("Three dimensions of metacognition")
        + "<p><b>Person.</b> Self-awareness: recognizing your own habits, strengths and emotions as a learner. As designers, we can ask learners to think back to a recent time they struggled with a task. Was it distractions, unclear instructions or lack of confidence? These reflections help learners understand their tendencies and set the stage for growth.</p>"
        + "<p><b>Task.</b> The nature and complexity of the task itself. Imagine a branching scenario in healthcare training: before learners choose how to communicate with a patient, they need to analyze a chart and interpret the situation. That pause to assess the task helps them slow down, prioritize and make more informed choices, just as they would on the job.</p>"
        + "<p><b>Strategy.</b> Stepping back to ask whether the methods you're using are working. In a microlearning module, learners might be offered several paths to solve a problem and prompted along the way: \"Why did you choose this path?\" and \"What would you try next time?\" Over time, they take ownership by adjusting strategies with intention.</p>"
        + h2("Why it matters")
        + "<p>Metacognitive strategies lead to deeper learning and better retention. They build self-regulated learners who can plan, monitor and evaluate their own progress, which matters most for busy adults learning on their own.</p>"
        + h2("How I build it into my designs")
        + "<ul><li><b>Reflective prompts</b> before and after activities: \"What do I already know?\" and later, \"What would I do differently?\"</li>"
          "<li><b>Feedback loops</b> that go beyond right or wrong, asking learners to explain why an answer is correct.</li>"
          "<li><b>Choice and strategy use:</b> optional paths and resources so learners can decide what they need based on their confidence.</li></ul>",
    "learner-attention":
        "<p>In a world full of digital noise, attention is one of the most valuable and fragile currencies in learning. If we can't first earn a learner's attention, and then hold it, we lose the chance for meaningful learning altogether. We're competing not just with short attention spans but with real pressures, screen fatigue and other priorities. Designing for attention has to be deliberate.</p>"
        + h2("1. Gaining attention: start strong")
        + "<p>Learners engage with material they see as personally meaningful, surprising or emotionally resonant. A question, a story or an unexpected fact gives the brain a reason to care. In a workplace module, I might open with a scenario that mirrors a real challenge, something that triggers a \"that's me\" moment. The goal isn't to entertain; it's to spark curiosity and signal that this is worth attention.</p>"
        + h2("2. Engaging the elephant")
        + "<p>Julie Dirksen's <i>Design for How People Learn</i> uses the metaphor of the rider and the elephant: the rider is our analytical self, the elephant our emotional brain. Most content is written for the rider, but the elephant decides whether to engage. Emotionally relevant scenarios, such as a teammate left out of a meeting or a conflict to resolve, tap into empathy and fairness. When learners feel something, they lean in.</p>"
        + h2("3. Keeping attention: structure matters")
        + "<p>Attention fades, especially in self-paced learning, so sustaining it takes active choices: short reflection moments, interactive decision points and micro-assessments that break up content. Rhythm and variation, alternating visuals, audio, text and activities, keep engagement high.</p>"
        + h2("4. Reducing cognitive overload")
        + "<p>Cognitive load theory reminds us that too much, or badly structured, content overwhelms working memory and shuts attention down. I use chunking, clear layouts and progressive disclosure, and I anticipate common misconceptions with clarifying examples before confusion takes root.</p>"
        + h2("5. Encouraging self-directed exploration")
        + "<p>Autonomy fuels engagement. Optional tracks, real-world cases and branching choices let learners follow their curiosity: novices take a guided route, experienced learners skip ahead or go deeper.</p>"
        + h2("Designing for attention is designing for respect")
        + "<p>Attention isn't a default setting; it's earned. When we treat it that way, we invite learners into an experience designed around how they actually think, feel and focus.</p>",
    "assessment":
        "<p>Assessment shouldn't be tacked on at the end; it should be built into the whole learning journey. That's why I follow backward design: before developing any activity, clarify what learners need to achieve and what evidence will show they got there. Instead of \"What content do I need to cover?\", ask \"How will I know they've learned it?\"</p>"
        + h2("Assessment for learning (formative)")
        + "<p>Formative assessment happens during learning. It works like a GPS that helps learner and instructor course-correct in real time. You wouldn't build a bridge across a canyon and only check the structure when you reach the other side. I build in:</p>"
        + "<ul><li>Quizzes and polls after short lessons</li><li>Retrieval practice, such as \"What do you remember?\" activities</li><li>Reflection prompts for self-assessment</li></ul>"
        + h2("Assessment of learning (summative)")
        + "<p>Summative assessment is the final dress rehearsal: it measures what learners have mastered. In eLearning that might be a branching simulation that mirrors job tasks, a certification quiz aligned to objectives, or a final project reviewed by an instructor.</p>"
        + h2("Why both matter")
        + "<p>Using both isn't just about tracking progress; it improves learning itself. Well-designed formative checks support retention and motivation, and help learners reflect and recalibrate.</p>"
        + h2("A design tip")
        + "<p>Treat assessment as the heartbeat of the course. Build light-touch checkpoints along the way: a quick poll after a video, a knowledge check after each module, an exit ticket asking \"What's one thing you'll apply tomorrow?\"</p>",
    "learning-framework":
        "<p>Designing learning isn't just delivering content; it's building a structure that helps learners grow. A strong framework should feel like a well-designed journey: clear, purposeful and responsive to who the learners are. These are the six components I rely on.</p>"
        + h2("1. Start with clear learning objectives")
        + "<p>Begin with the end in mind. Objectives should be specific, measurable and action-oriented, because vague goals lead to vague results. Think of it as setting the GPS before a road trip.</p>"
        + h2("2. Understand the learners")
        + "<p>Who are they? New to the topic or experienced? What misconceptions might they bring? In healthcare training, for example, tone and pacing differ for frontline staff and clinical educators.</p>"
        + h2("3. Identify and address learning gaps")
        + "<p>When learners struggle, it's often because we assumed too much. Look for gaps in knowledge, motivation, environment or digital fluency. For a team that has never used cloud tools, software onboarding should start with foundational concepts before features.</p>"
        + h2("4. Adapt for novices and experts")
        + "<p>Build in optional support and stretch: examples, definitions and guided walkthroughs for beginners; scenario-based tasks that push deeper thinking for experienced learners.</p>"
        + h2("5. Use scaffolding")
        + "<p>You wouldn't teach someone to ride a bike by pushing them down a hill. Start with step-by-step guidance, then shift to open-ended tasks, reducing support as mastery grows.</p>"
        + h2("6. Enhance retention")
        + "<p>Information alone isn't enough. I design around chunking, retrieval and association: visual groupings, metaphors for abstract ideas, and mind maps learners build themselves.</p>"
        + "<p>This framework isn't a checklist; it's a mindset: meet learners where they are, guide them with purpose, and build a structure strong enough to support change.</p>",
    "design-theories":
        "<p>Designing effective learning isn't about aesthetics or interactivity alone; it's about how the brain learns best. These seven theories shape how I design, and each one changes something concrete in a build.</p>"
        + h2("1. Bloom's taxonomy")
        + "<p>Learning is a staircase from remembering to applying, analyzing and creating. In a compliance course, for example, I'd start with key definitions, then use case-based scenarios that ask learners to apply and evaluate.</p>"
        + h2("2. Behaviorism")
        + "<p>Learners respond to rewards and consequences. Badges for completed modules and instant quiz feedback reinforce behavior and keep people moving.</p>"
        + h2("3. Cognitive load theory")
        + "<p>Working memory is a small desk. I chunk complex topics into short lessons and use visuals to reduce friction; in systems training, one walkthrough per feature.</p>"
        + h2("4. Constructivism")
        + "<p>We learn by doing. Branching scenarios that put learners in role-play situations let them decide, reflect and adapt, constructing understanding through experience.</p>"
        + h2("5. Self-determination theory")
        + "<p>Motivation thrives on autonomy, competence and connection. Offering a choice of path or challenge level, such as optional expert tips alongside a guided track, builds buy-in.</p>"
        + h2("6. The Dunning-Kruger effect")
        + "<p>The most confident learners are sometimes the least accurate. Reflection points and peer feedback help learners calibrate what they really know.</p>"
        + h2("7. Zone of proximal development and scaffolding")
        + "<p>Support learners just enough to keep them moving, then take it away: detailed feedback and modeling first, less guidance as they take on real challenges.</p>"
        + "<p>Good instructional design is behavior change rooted in how people learn. These theories are the compass I use on every project.</p>",
    "learning-variety":
        "<p>Variety isn't only about keeping things interesting. It's about equity, flexibility and impact: people process, engage with and apply information in different ways.</p>"
        + h2("1. Offer more than one way in")
        + "<p>Universal Design for Learning asks for multiple means of representation and engagement. I pair audio explanations with visuals, or let learners choose between a video walkthrough and a step-by-step guide. The goal isn't everything for everyone; it's a path every learner can follow confidently.</p>"
        + h2("2. Target different cognitive levels")
        + "<p>Using Bloom's taxonomy like a climbing wall, I layer warm-ups such as quizzes and flashcards before analytical and creative challenges like branching scenarios and reflection prompts.</p>"
        + h2("3. Build motivation through ownership")
        + "<p>Drawing on self-determination theory, I add personalized options, embedded choice and visible progress, such as badges that signal growth. Even letting learners choose the format of a project changes how they show up.</p>"
        + h2("4. Improve retention with spacing and retrieval")
        + "<p>Learning is a series of refreshes, not a single download. Short quizzes, reflection moments and recaps at intervals keep the path through the forest from disappearing.</p>"
        + h2("5. Promote real-world application")
        + "<p>Skills stick when they're tied to real stakes. In healthcare training, for instance, interactive case studies can ground compliance rules in patient-care decisions.</p>"
        + h2("6. Reduce cognitive overload")
        + "<p>Clarity, not clutter: chunking, microlearning and visual pairings let learners spend their energy on meaning rather than decoding the delivery.</p>"
        + h2("7. Scaffold based on readiness")
        + "<p>Following Vygotsky, meet learners just beyond what they can do alone: guided walkthroughs before independent application, discussion before self-assessment.</p>"
        + "<p>Variety is responsible design. Diversifying how we engage, challenge and support learners makes learning more inclusive and more durable.</p>",
}

LAB = [
    dict(title="Recruitment-ops playbook for Claude", status="live", href="/work/satellica-client-education/#workflow",
         problem="Recruiting hundreds of study participants meant days of copying data and messaging people one by one.",
         what="Four reusable prompt procedures that Claude runs in the browser, with my approval before every action. Saved about 40% of weekly coordination time."),
    dict(title="Northpeak course site", status="live", href="https://ask-first-log-it-right.pages.dev/",
         problem="Authoring-tool output is hard to wrap in a polished, trackable course experience.",
         what="A custom HTML/CSS/JS course shell around a Storyline simulation: progress tracking, flip cards, a scored knowledge check, and job-aid downloads."),
    dict(title="Socratic ID coach", status="wip",
         problem="New designers get answers from AI instead of learning to reason through a design problem.",
         what="A chatbot that coaches with questions, grounded in learning-science frameworks such as action mapping and backward design."),
    dict(title="Work-journal tool", status="wip",
         problem="Accomplishments get forgotten by the time a review or interview comes around.",
         what="A lightweight daily log, adapted from my personal diary app, that turns notes into evidence for resumes and interview stories."),
]
