# Series Bible — Valkyr

> **What this is.** The canon shared by every book in this series: the world, the rules, the
> cast, the arc that spans the books, and the settled decisions no single book may contradict.
> A per-book `STATE.yaml`, `foundation.md`, and `character-bible.md` govern ONE book; this file
> governs all of them and outranks any of them on shared canon.
>
> **Who reads it.** Every agent working on any book in this series reads this FIRST — the
> architect before outlining, the writer before drafting, the continuity-guardian when auditing,
> the entity-tracker when reconciling. Point them at it via `series.bible` in the book's
> `STATE.yaml`.
>
> **Keep it current.** When a book LOCKS something that binds later books (a death, a rule, a
> renamed place, a revealed secret), record it here in the same commit. A series bible that
> lags the manuscript is how book three contradicts book one.
>
> **Provenance.** Sections 1–6 below are the author's own series bible, transcribed from
> `valkyr-book-1/research/valkyr-source.pdf` on 2026-09-07. Everything marked **(locked)** is
> a settled author decision — the pipeline executes it, never re-litigates it.

## Setting & rights posture

Set in the **Halo universe** (UNSC / ONI black-ops tier). This is fan fiction unless and until
the author says otherwise, and that decision changes the whole delivery path: a commercial
release would need the serial numbers filed off — UNSC/ONI/SPARTAN-II/Covenant renamed and
re-grounded — before `book-packager` builds anything for sale. **Ask the author before any
publishing step. Do not file the serial numbers off on your own initiative; the Halo texture
is load-bearing for the premise as written.** See Open series-level questions.

## The books

| # (pub order) | Folder | Title | Status |
|---|---|---|---|
| 1 | `valkyr-book-1/` | Valkyr: Book One (working title) | In progress — 5 chapters drafted, architect pass done |
| 2 | — | Book Two (untitled) | Planned — outlined only in this bible |

- **Publication order:** Book One → Book Two. A two-book arc as currently conceived.
- **Chronological order:** same as publication order. The founding incident (Rx's death) sits
  four years before Book One opens and is told in retrospect, never as a prequel volume.
- **Unifying antagonist:** **Richard Jameson.** One antagonist across both books; Book Two ends
  with his fall.
- **Thematic spine:** *What do you owe an institution that has already lied to you once — and
  what does it cost to find out?* Vexx rebuilds the program that killed his brother, in good
  faith, under the man who did it.

## Series arc (the shape across books)

- **Book-level escalation ladder** — what changes in kind, not just degree:
  - **Book 1 — suspicion.** Vexx is recruited, builds the cell, and by the end privately knows
    Rx was murdered and suspects the man he reports to. He chooses to keep investigating in
    secret rather than act. **Ends on rising suspicion, not revelation.**
  - **Book 2 — confrontation.** Investigation and memory-unlock accelerate together; the full
    unlock lands near the climax; ends with Jameson's fall and the rebuilt Valkyr stepping out
    from under the original program's shadow.
- **What is answered when.**
  - Book 1 pays off: that Rx's death was not combat; that the motive is bigger than a cover-up;
    that the suspect is Vexx's own CO. It does NOT pay off the full memory or the confrontation.
  - Book 2 pays off: the complete truth of the founding incident, Jameson realizing he has been
    made, the confrontation, and whether the rebuilt Valkyr can be something other than what the
    original was.
- **The ending the series is driving at:** Jameson falls, and the cell survives him — the
  question left standing is whether a program built to judge its own can be trusted to any
  hands at all, including Vexx's.
- **Deliberately left open at the end of Book 1** (do not resolve early):
  1. Full memory unlock and the complete truth of the founding incident.
  2. Jameson realizing he has been discovered.
  3. Whether Paladin's moral objections escalate into open conflict with command.
  4. The Jameson confrontation and fall.
  5. First hint (plant late in Book One, or save entirely) of the shared AI donor-stock twist —
     a SPARTAN-II's AI who may be "kin" to a Valkyr AI.

## World rules (hard canon — never violate)

### Valkyr — the original program
- A black project so classified it has **no acknowledged existence**. Internal name "Valkyr";
  the official paper trail, where one exists at all, is a bland logistics/subsection designation.
- **Charter:** monitor SPARTAN-II operators for instability, defection, or threat, and eliminate
  if necessary. A fail-safe against the UNSC's own supersoldiers.
- **Recruitment: the presumed dead.** KIA-logged soldiers, deserters, washed-out Spartan
  candidates — people already erased from the record, easy to disappear a second time.
- Operators work in **isolated cells with no contact between cells**, insulated from the command
  tier that issues elimination orders (**"the Choosing"**).

### Timeline placement (locked)
- Valkyr founded shortly after SPARTAN-II is established, conceived directly in response to it —
  ONI's answer to the risk of fielding child-soldiers with total battlefield dominance and no
  long-term guarantee of stability.
- Rx serves several years before the founding incident. **His death occurs during the
  early-to-mid Human-Covenant War**, when a wartime UNSC has every reason not to ask hard
  questions about a classified program's internal casualties — ideal cover for Jameson.
- **Four years pass.** Jameson consolidates command; the war continues around him.
- Vexx's recruitment into the rebuilt Valkyr (Book One's opening) lands in that four-years-later
  window. **Both books unfold against the ongoing war, with Jameson's ambition as a hidden
  second front underneath it.**
- Exact calendar year relative to Reach / first contact can be pinned during copyediting against
  canon references. **Not a blocker for outlining — do not invent a hard date on the page.**

### The AI-bonding process
- Smart AIs are flash-cloned from a human donor brain; the process is **destructive** and must
  occur at or near the donor's death.
- Valkyr AIs are drawn from **the same elite donor stock as SPARTAN-II AI pairings** — meaning
  any Valkyr AI could theoretically be a genetic "sibling" to a SPARTAN-II's AI. Not publicly
  known. A live plot lever for later books.
- Two known origin types on the roster:
  - **Twin / soul-bond (Rx):** a dying donor undergoes the process specifically to become AI to
    a named, chosen partner. Believed unique — **Rx would not bond with anyone but Vexx.**
    Confirmed across Books One–Two: the process **is** repeatable intentionally (see Spector);
    it had simply never been attempted this way before Rx.
  - **Willing pre-death donation (Spector, and presumably others):** a donor signs over their
    mind before death, intending it for whoever their eventual AI partner turns out to be. No
    prior relationship required.
- **No rampancy clock is used as a plot mechanic in this series.** AI instability, where it
  exists, is driven by memory suppression, trauma and moral weight — never a ticking clock.
  (Writer warning: this is the single easiest place to import unearned Halo-canon tension.
  Don't.)

### Memory suppression (Rx-specific mechanic)
- Rx's memory of the event that killed him — refusing Jameson's order — is **sealed**. Likely a
  combination of transfer-process trauma response and a deliberate protocol baked into the
  program to keep operators "clean" of certain memories.
- **The seal is not static.** It degrades under two conditions: (1) proximity or reference to
  Jameson, and (2) Vexx's own investigation closing in on the truth externally. The two tracks
  move in parallel — external discovery and internal unlock reinforce each other.
- **Jameson believes the truth died with Rx.** He does not know Rx survived as an AI, and has no
  reason to suspect the secret is still alive. This is the source of his vulnerability.

### The four-stage memory unlock (locked structure)
1. **First leak** — an unexplained flash (name/image) during a routine op. Unsettling, not yet
   legible.
2. **Second leak** — a fragment of sound/emotion; Rx hears his own voice refusing the order.
   Surfaces as a glitch Vexx notices and Rx deflects.
3. **Third leak** — triggered specifically by Jameson's presence/voice. Proximity to Jameson
   becomes narratively dangerous for Rx.
4. **Full unlock** — forced by Vexx confronting Rx directly with external evidence. No more
   hiding.

**Placement (locked):** stages 1–2 anchor Book One's investigation thread. Stage 3 closes Book
One or opens Book Two as escalation. Stage 4 lands at or just before the Book Two climax, giving
Vexx and Rx the truth together before or during the confrontation with Jameson.

## The founding incident (locked)

The event the whole series is built on. Told in fragments; never dramatized whole in Book One.

1. Rx, on assignment for the original Valkyr, is ordered to conduct a **Choosing** against a
   SPARTAN-II operator flagged as unstable.
2. Rx's own assessment finds the target **isn't** unstable — the read is compromised by greed,
   corruption and personal gain, later revealed to belong to **Richard Jameson** himself.
3. **Rx refuses the order.**
4. Rx is killed shortly after — not in genuine combat, but as a **cleanup action disguised as
   hostile contact**, to remove a liability who wouldn't fall in line.
5. Vexx is told a cover story: KIA, classified op, hero's death, remains unrecoverable (hence the
   empty-casket burial).
6. Vexx is later approached and told Rx's mind survived the transfer and **will not bond with
   anyone but him** — pulling Vexx back into the program that killed his brother, under a
   leadership he has no reason yet to distrust.

**Locked details:**
- **Jameson's motive** — not self-preservation but **outright empire-building**. He intended to
  use control of Valkyr as a stepping stone to seize power over the military at large, and
  ultimately the UNSC itself. The Choosing order Rx refused was part of that campaign; Rx's read
  of "greed/corruption" was Rx seeing the ambition underneath.
- **Who killed Rx** — **Jameson himself, personally.** Not delegated, not disguised through a
  subordinate. He carried out the "hostile contact" cover himself.
- **The promotion** — Rx's death is the direct hinge of Jameson's rise. Killing Rx and
  successfully burying it is what cleared his path to being installed as head of command for
  Valkyr. **The murder isn't just something Jameson got away with; it is the founding act of his
  current authority.** Everything he now commands is built on top of it.
- **Timeline** — four-year gap between Rx's death and Vexx's recruitment. Jameson has had four
  years to consolidate power, grow comfortable, and build the very command structure Vexx now
  serves under.

## Cast across books

Voice cards live in each book's `character-bible.md`. This section records only what is
SERIES-level: who returns, what they know, where a book leaves them.

### The founding team of the rebuilt Valkyr

| Operator | AI | Role | Donor / origin | Core thread |
|---|---|---|---|---|
| **Vexx** (Vexxcerian) | **Rx** | Command | Vexx's twin brother; twin-bond transfer at death | Grief, memory-unlock mystery, Jameson |
| **Goliath** | **Spector** | Breach / demolitions | "Phantom" — retired veteran, demolitions/covert ops, willing pre-death donor | Protector code: "leave a message" against those who prey on the innocent |
| **Gaia** | **Echo** | Recon / infiltration | Scout-sniper, died alone behind enemy lines | Compulsion to never go silent |
| **Paladin** | **Bastion** | Heavy defense | Combat medic, died covering an evac | "Nobody gets left" — collides with Valkyr's core function |
| **Zeus** | **Hollow** | Interrogation / psych-ops | ONI intelligence officer, morally gray methods | The team's necessary discomfort; ethical residue the new Valkyr wants to purge |
| **Aglaope** | **Requiem** ("Lure") | Psych pressure / lure | Spartan who did extraction and last-contact work; stayed with the dying so none died alone | Comfort-instinct repurposed as a weapon; Vexx's off-record confidante |

**Team dynamic notes (established canon, may deepen in drafting):**
- Vexx leads **out of necessity, not ambition** — respected because he visibly hates the job.
- Goliath is Vexx's steadying counterweight; Spector and Rx have natural donor-AI rapport.
- Gaia chafes under Vexx's caution — a standing friction point.
- Paladin is the moral pressure test — likely first to question a Choosing order, echoing Rx.
- Zeus is trusted operationally, not personally — Vexx keeps him close because the work still
  needs an edge.
- Aglaope / Requiem are the quiet centre — Vexx's emotional throughline outside Rx.

**Thread to plant, not explain:** Phantom (Spector's donor) once saved Goliath's life on his
homeworld, years before either the program or the pairing existed. **Goliath does not learn this
from records — he learns it because Spector lets it slip.** (Delivered in Book One, Ch. 2.)

### Series-level state

| Character | Books | State at end of Book One | Knows | Notes |
|---|---|---|---|---|
| Vexx (Vexxcerian) | 1– | Alive, in command of the cell, investigating in secret | That Rx was murdered, not KIA; suspects Jameson; has not acted | POV for both books |
| Rx | 1– | Alive as AI; seal cracked at stages 1–3, not broken | Fragments only — a treeline, a voice, the shape of a refusal | Never a POV; the reader only ever sees him through Vexx |
| Richard Jameson | 1– | Alive, in command, **unaware he has been made** | That he killed Rx and buried it; **not** that Rx survived | Falls in Book Two |
| Aglaope | 1– | Alive; Vexx's only confidante | Vexx's suspicion, in outline — not the evidence | Told by Vexx in Ch. 5 |
| Goliath | 1– | Alive | Phantom's name; suspects the homeworld connection | — |
| Gaia | 1– | Alive; friction with Vexx suspended, not resolved | That Vexx suspects *something* and promised to tell her first | — |
| Paladin | 1– | Alive | Nothing of the Rx thread | Moral pressure test; escalation reserved for Book Two |
| Zeus | 1– | Alive | Nothing of the Rx thread | Operationally trusted, personally not |
| Corwin | 1– | Alive, reassigned to a rehabilitation track | That his own chain of command tried to kill him; not believed | Rescued Ch. 3; his evidence is in Vexx's drawer |
| Reyes | 1– | Alive, in mandatory psych evaluation | — | Spared in Ch. 4 because Paladin pushed back |
| Voss | 1– | Alive; mid-level liaison | That Vexx pulled Corwin's fragments from evidence lock, and chose not to stop him | The one institutional ally, unexplained |

**Voice carry-over rule.** A returning character keeps the voice card from the previous book.
Copy it forward into the new book's `character-bible.md` and evolve it deliberately (a book of
grief changes a voice); do NOT re-invent it from scratch, and do NOT let a new book hand them a
tic they never had.

## Naming & spelling registry (the boring file that saves the series)

| Canonical | Also appears as (accepted) | Never |
|---|---|---|
| Vexxcerian | Vexx (default on the page), "Operator Vexxcerian" (formal/institutional) | Vexcerian, Vexxcerion, Vex |
| Rx | — | R-x, RX (all caps), Rex |
| Richard Jameson | Jameson | Jamieson, Jamerson |
| Valkyr | "the program", "the rebuilt Valkyr" | Valkyrie, Valkyr Program (as a formal title) |
| the Choosing | — | The Choosing (mid-sentence caps), a Choosing-adjacent order (fine in narration) |
| Goliath / Spector | — | Specter, Spectre |
| Gaia / Echo | — | Gaea |
| Paladin / Bastion | — | — |
| Zeus / Hollow | — | — |
| Aglaope / Requiem | Requiem is also called "Lure" in program paperwork only | Aglaophe, Aglaopé |
| Phantom | "Ghost" (only in Goliath's childhood recollection, as a townsfolk name) | — |
| Corwin | "Operator Corwin" | Corwyn |
| Reyes | — | Reyez |
| Voss | — | Vos |
| SPARTAN-II | Spartan (as a common noun on the page: "a Spartan") | Spartan-2, SPARTAN II |
| UNSC / ONI | — | U.N.S.C., O.N.I. |

## Settled decisions (with the date they were settled)

- **2026-09-07** — Jameson's motive is empire-building, not self-preservation. Forecloses any
  "he panicked and covered it up" reading.
- **2026-09-07** — Jameson killed Rx personally. Forecloses a subordinate triggerman, and
  forecloses any later "he didn't know it would go that far".
- **2026-09-07** — Rx's death is the hinge of Jameson's promotion. His authority is built on the
  murder; this is why exposure destroys him rather than merely embarrassing him.
- **2026-09-07** — Four-year gap between Rx's death and Vexx's recruitment.
- **2026-09-07** — POV is Vexx, close third, throughout both books. **No Jameson POV, no Rx POV.**
  Everything the reader knows about Rx's interior is inferred from a processed voice.
- **2026-09-07** — No rampancy clock as a plot mechanic, in any book.
- **2026-09-07** — Book One ends on suspicion, not revelation. The confrontation belongs to
  Book Two.
- **2026-09-07** — Rx's twin-bond transfer was believed unique but is confirmed repeatable; it
  had simply never been attempted that way before.

## Open series-level questions (ask the author; do NOT invent)

- **Rights posture / publication intent.** Is this Halo fan fiction, or the draft of an original
  property to be filed off later? This decides the entire `book-packager` path and should be
  answered before any delivery work. It does not block drafting.
- **Book One's real title.** "Valkyr: Book One" is a working title.
- **Whether the shared-donor-stock twist is planted in Book One** or held entirely for Book Two.
  The bible allows either; the outline currently holds it back to a single unexplained line.
- **How the war is used.** The Human-Covenant War is running in the background of both books.
  How visible should it be — pressure the cell feels, or scenery they pass?
- **Corwin's fate.** He survives Book One in a rehab track holding a truth nobody believes. Does
  he return in Book Two as a witness, or is his function complete?

## Continuity carry-over checklist (run when starting the NEXT book)

1. Copy the previous book's `character-bible.md` forward; prune characters who are gone,
   keep the returning cast's voice cards, re-check the TIC BUDGET across the NEW book.
2. Seed the new book's `ENTITY_STATE.yaml` from the previous book's final one (entity-tracker
   BUILD mode, with the previous file as input) so who-knows-what survives the book boundary.
3. Re-read this bible's **Cast across books** and **Settled decisions** — everything there is
   binding on the new outline.
4. Carry the ALLOWLIST forward in `tools/style_check.py` for motifs that are genuinely
   series-level — but re-apply the motif cap PER BOOK (a motif used three times in each of
   three books is fine; three times in one book is the ceiling).
5. Record the new book's row in **The books** table above before the architect runs.
6. **Advance the memory-unlock ladder.** Book Two opens at or after stage 3 and must reach
   stage 4 near its climax. Check where Book One actually left it before outlining.
