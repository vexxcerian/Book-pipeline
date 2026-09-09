# Ch.6–8 Comparison Repair — voice-match floor

Narration-only pass restoring figurative comparison to the author's measured floor
(2.0 true comparisons / 1,000 words). Sixteen comparisons added across three chapters.
No dialogue altered. No `the way X does Y` used anywhere in Ch.8.

---

## 1. Metrics — before / after

| | Ch.6 | Ch.7 | Ch.8 |
|---|---|---|---|
| comparisons/1k **before** | 0.9 | 1.3 | 0.4 |
| comparisons/1k **after** | **2.1** | **2.0** | **2.1** |
| markers before → after | 4 → 9 | 2 → 3 | 2 → 12 |
| words before → after | 4337 → 4374 | 1499 → 1505 | 5646 → 5717 |

Ch.8's other ceilings, all of which moved in the safe direction because the added
clauses carry no `and` and no em-dash:

| metric | before | after | limit |
|---|---|---|---|
| `and` /1k | 23.2 | **22.9** | ceiling 24.0 |
| em-dash /1k | 11.5 | **11.4** | ceiling 12.0 |
| `the way` / `the same way` | 5 | **5** | ceiling 5 |
| narration median | 13.5 | **13.5** | floor 13 |
| narration ≥40w | 12.0% | **13.0%** | floor 11.5% |
| `somebody`/`nobody` /1k | 5.3 | 5.4 | ceiling 6.5 |

Ch.6 narration median moved 13 → 14 and ≥40w held at 12.4%. Ch.7's punch-chapter
exemption is untouched (median 9, ≤6w 36.4%).

Gates: `style_check.py`, `grammar_check.py`, `voice_wear_check.py` all **clean**.
Ch.1–5 output byte-identical to the pre-pass run. `git diff --stat` = three files.

**One caveat the next maintainer must know.** Ch.7 passes at 3 markers in 1,505 words —
that is 1.993/1k, which the gate rounds to 2.0. It is a real pass by the gate's own
arithmetic but it has no headroom: any future edit that pushes Ch.7 past ~1,538 words
without adding a comparison will re-fail it. The brief specified "roughly one" for Ch.7
and I held to that rather than buying margin the chapter did not need. Flagging rather
than quietly over-correcting.

---

## 2. Every comparison added

### Chapter 6 — five

**6.1 — the arrival, the orchard**
- before: *"…an orchard on the south side, the trees pruned back hard for winter, a track down to a pump house…"*
- after: *"…the trees pruned back hard for winter, **the cut ends on them like knuckles**, a track down to a pump house…"*
- why here: the paragraph is a run of appositive physical facts and every one of them
  lands except the trees, which get an adjective and move on. It is also the chapter's
  establishing shot — the place has to be seen before it can be liked.

**6.2 — the clinician with the trolley**
- before: *"She poured Vexx a fresh cup, from a jug on the trolley."*
- after: *"She poured Vexx a fresh cup, from a jug on the trolley, **like it was her own table**."*
- why here: the chapter's engine is that the institution is genuinely kind. That has to
  be shown in a gesture, and the gesture was sitting there unqualified. `like it was —`
  is the author's own manner-form (*"like it settled something"*, *"like it was a fact
  of the universe"*).

**6.3 — the jigsaw, after "I think I had it backwards"**
- before: *"She was going along the border with it, trying it in one place, then in another."*
- after: *"…trying it in one place, then in another, **like a key in one door after another**."*
- why here: a deliberate cutaway from Corwin at the highest point in the scene — a
  texture beat, not a working emotional beat, so a comparison there holds the camera off
  him a moment longer instead of deflating him.

**6.4 — Corwin and the empty casing**
- before: *"Corwin laid two fingers flat on the wood, moved them across it a little way."*
- after: *"…moved them across it a little way, **like a man checking a table for dust**."*
- why here: the gesture was vague — "a little way" is the prose settling. This is the
  emotional centre of the chapter and it is the one addition I am least certain of. See §4.

**6.5 — the clinician's ready answer about the daughter**
- before: *"…and the answer was out of her, before he had got to the question."*
- after: *"…before he had got to the question, **like a door coming back on its spring**."*
- why here: the horror of the beat is her fluency, and fluency is a mechanism. The
  sentence was describing a mechanism without showing one.

### Chapter 7 — one

**7.1 — the tag under the lamp**
- before: *"…and the D had worn shallower than the rest of it, and Vexx had been reading it…"*
- after: *"…and the D had worn shallower than the rest of it, **rubbed down like a stair tread**, and Vexx had been reading it…"*
- why here: one clause, inside an existing chain, in the chapter's texture register
  rather than at either of its two flat peaks (*"Eleven months after the file closed."*
  / *"The left one was not flat."*), both of which were left alone. It says *many hands,
  long time* about an object whose whole meaning is that it was handled by somebody who
  has been dead seven years.

### Chapter 8 — ten (all `like`; no `the way` construction used)

**8.1 — the flag summary**
- before: *"…without ever being able to make it produce anything."*
- after: *"…without ever being able to make it produce anything, **like a switch wired to nothing**."*
- why here: the sentence describes repeated fruitless action and had no picture in it.

**8.2 — the bay, Aglaope's boot**
- before: *"Aglaope had her boots off, working at a seam in one of them with a thumbnail."*
- after: *"…with a thumbnail, **like picking at a splinter**."*
- why here: flattest physical detail in an otherwise well-textured paragraph.

**8.3 — the plateau**
- before: *"…on a plateau the color of wet ash, four buildings and a mast, with the wind coming across it…"*
- after: *"…four buildings and a mast **set down on it like kit off the back of a truck**, with the wind coming across it…"*
- why here: the station is a provisional thing on a bare plateau and "four buildings and
  a mast" was doing none of that work. Soldier's eye, which is whose eye it is.

**8.4 — Goliath at the fuel shed**
- before: *"…running a glove along the seam where the panel met the pad."*
- after: *"…where the panel met the pad **like somebody looking for a draft**."*
- why here: twenty-two minutes of nothing has to be made worth watching, and the
  comparison makes the craft legible without narrating it.

**8.5 — Merrick stands up**
- before: *"…put the meter down on the bench, wiped both hands on his thighs."*
- after: *"…put the meter down on the bench, wiped both **palms** on his thighs **like a man about to shake hands**."*
- why here: first sight of Merrick, and the courtesy is the character. `hands` → `palms`
  is the one word of original prose I changed, to stop my own addition repeating it.

**8.6 — the plant house**
- before: *"The plant house was warm, smelled of hot dust off the heaters, faintly of coffee."*
- after: *"…faintly of coffee, **like a shed with a kettle in it**."*
- why here: the room is where a man has been living inside his job. The smells listed it;
  nothing placed it.

**8.7 — the search for the book ends**
- before: *"…there was no book — Merrick sat down on the crate with his hands hanging."*
- after: *"…with his hands hanging, **like a man at the end of a shift**."*
- why here: the assessment scene's last image. He has just failed to produce the one
  object that proves he is not losing his grip, and he sits down like a man who has
  finished work. Earns its place; nothing is unpacked.

**8.8 — Aglaope in the kitchen**
- before: *"Aglaope had been sitting with her hands round a cup she had not drunk from."*
- after: *"…she had not drunk from, **holding it like a hot water bottle**."*
- why here: the untouched cup is the detail; what she was doing with it was not.

**8.9 — the medical crew on the ramp**
- before: *"…who put a hand under his elbow, did not grip…"*
- after: *"…who put a hand under his elbow **like people steadying a ladder**, did not grip…"*
- why here: support without a hold, which is exactly what the sentence was already
  reaching for with "did not grip" and not quite getting.

**8.10 — the corridor, before Paladin**
- before: *"…the brown fan across the plate dried down to a rim at the edges."*
- after: *"…dried down to a rim at the edges, **like the mark in a bath**."*
- why here: the spill from the day before, dried. It marks elapsed time and it is Vexx
  looking at a floor rather than at the man on the step.

---

## 3. Considered and rejected

| Place | Why not |
|---|---|
| **Ch.8 L144** *"It was the stop of a man who has walked into a doorframe in his own house."* | Already the best comparison in the chapter, in the author's `of a man who` form. Touching it would have been vandalism, and it ruled out every door/house image elsewhere in the scene. |
| **Ch.8, Merrick's introduction** *"a big man gone slightly loose at the edges"* | Tried six versions (kit bag, coat off a hanger, caretaker, machine installed, furniture). Every one was either clever or carried an explanatory tail. The catalogue that follows — *Shaved. Hair cut inside the fortnight. Boots done.* — is doing the work. Left plain. |
| **Ch.8 L116, the Kettle noise** | Echo names the ridge for a noise the reader never hears. A comparison would have spoiled his joke. |
| **Ch.8, the notebook (Aglaope's delivery)** | *"the corners gone furred"* already sees it. A comparison there over-signals an object the chapter deliberately hands over without comment. |
| **Ch.8, the thermos "wide brown fan"** | The image exists. Added one to its dried remains in the corridor instead (8.10). |
| **Ch.8, the commander's unfastened jacket** | The `meant … meant … meant` sentence is anaphoric and already 40+ words. Every candidate cluttered it. |
| **Ch.7, the trestle's burn in the laminate** | Would have bought a real margin on the gate (see §1). Rejected because the brief specified roughly one for Ch.7 and the chapter's register is log lines and white space. Noted as the obvious place to go if Ch.7 ever needs a second. |
| **Ch.6, Corwin's body / the clippers / the soft clothes** | *"the eyes had come forward, out of wherever they had been sitting in the jungle"* is already the reach. Adding would have been gilding. |
| **Ch.6, the saplings on the drive** | Every version (splinted arm, broken finger, something taught to stand) came out thematic — the tied-up sapling at a rehabilitation hospital is too neat. Left as stakes and ties. |
| **Ch.6 L112** *"He might have been reading out a manifest."* | Comparison already, marker or not. Left. |
| Ch.6 flat closers, Ch.7's *"The left one was not flat."*, Ch.8's *"It was a two-man rotation with three men in it."* / *"Nobody fired. Nobody was hurt."* / the failed-stack sentence / the Merrick self-echoes | Working beats. Not decorated. |

---

## 4. Honest read — which of these feel added rather than found

Three. Ranked by how uneasy I am.

**6.4, *"like a man checking a table for dust"* (Corwin and the casing) — most uneasy.**
This is the chapter's emotional centre and the brief warned about exactly this spot. The
gesture genuinely was vague and the comparison genuinely is bare, but it introduces a
*reason* for a movement the author had left unmotivated, and unmotivated is arguably the
point — a man's hands doing something while he talks about an empty box. If one of these
sixteen should come out, it is this one. Ch.6 would fall to 8 markers / 4363 words =
1.8/1k and re-fail, so removing it means finding a replacement elsewhere in Ch.6, not
just deleting.

**8.8, *"holding it like a hot water bottle"* (Aglaope's cup).**
Domestic and unsentimental, which is right, but it is the only addition in the pass that
is about warmth rather than about a physical fact, and Aglaope is already the cast's warm
one. It risks reading as the narration liking her. Defensible, not certain.

**8.1, *"like a switch wired to nothing"* (the flag summary).**
The most *writerly* of the sixteen. It is concrete and Vexx-appropriate and it stops
dead, but the sentence it attaches to was already complete, and I chose it partly because
Ch.8 needed ten and the chapter's dry opening had room. That is a quota reason, and I am
naming it as one.

**The thirteen others I stand behind** as found rather than added — each replaced a place
where the prose had reached for a physical description and settled for a flat one, and
each would survive a reader asking "why is that there."

**Form check on all sixteen:** none is followed by a clause that unpacks it. Every one
ends at a noun phrase and the sentence stops or moves on. Concrete and physical in every
case; drawn from soldiering (kit off a truck, a splinter, a draft, a shift) and ordinary
domestic life (a table, a key, a door spring, a stair tread, knuckles on a pruned tree, a
kettle in a shed, a hot water bottle, a ladder, a bath). No psychology is explained by any
of them.

**Density sanity check:** three `like a man` constructions would have been a new tic, so
two were recast (8.4 to `somebody`, and 8.5 kept). Two cup-images in Ch.8 were avoided by
moving 8.10 from a cup to a bath. `like a hand …` was avoided in Ch.6 because L90 already
has *"like a hand going out after a dropped cup."*
