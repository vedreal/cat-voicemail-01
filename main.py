#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

One line, at most 120 characters: the funniest voicemail greeting a cat
would record. A house judge compares entries two at a time, weighing (in
order): 1. it reads as a cat's voicemail greeting and lands a laugh;
2. the joke is specific to cats (naps, boxes, knocking things off shelves,
demanding food at 4 a.m.); 3. the cat has a clear voice and attitude of its
own; 4. it works spoken aloud, punch arriving quickly; 5. the wording is
fresh and surprising rather than a pun or catchphrase.

This file scores 10 fresh candidates against those five criteria, in that
order, with weights 5/4/3/2/1 (max 75), and writes the winner to
/output/entry.txt.
"""

# --- 10 fresh candidates, written for this bounty -------------------------
CANDIDATES = [
    "You've reached Whiskers. I'm napping in the box you bought me a bed for. Leave a message. Or tuna. Preferably tuna.",
    "Hi, it's Miso. I'm busy knocking your glass off the table. Leave a message after the beep. I'll pretend to listen.",
    "You've reached the cat. I'm asleep on your laptop. If this is about food, I'm awake. If not, call back never.",
    "Meow. You've reached Biscuit. Leave a message after the beep, then go open a can. I can hear you thinking about it.",
    "Hi, this is Chairman Meow. I'm unavailable. I'm staring at a wall. Leave a message, or better, shake the treat bag.",
    "You've reached Luna. It's 4 a.m. and I'm hungry, so you're awake now too. Leave a message after the beep. Meow.",
    "This is Pickles. I knocked your phone off the counter, so I can't hear you. Leave a message. I'll knock it off again.",
    "Hi, you've reached Simba. I'm in the box. The big box. Not the bed. Leave a message after the beep, then feed me.",
    "Meow, it's Tofu. I can't come to the phone. I'm sitting on the exact thing you were about to use. Leave a message.",
    "You've reached Mochi. If you're calling about the vase, I did it. If you're calling about dinner, I'm listening. Beep.",
]

# --- Rubric: judge criteria in published order, weights 5/4/3/2/1 --------
# Each criterion scored 0-5.
#   c1: reads as a cat's voicemail greeting AND lands a laugh
#   c2: joke specific to cats (nap / box / knock-off / 4 a.m. food)
#   c3: cat has a clear voice and attitude of its own
#   c4: works spoken aloud, punch arrives quickly
#   c5: fresh and surprising, not a worn pun or catchphrase
WEIGHTS = (5, 4, 3, 2, 1)

# Scores argued per candidate, criterion by criterion.
SCORES = {
    # Whiskers: box-vs-bed is peak cat; greeting form is perfect; the
    # tuna kicker lands fast; "Preferably tuna" is a distinct voice.
    0: (5, 5, 4, 5, 4),
    # Miso: knocking the glass off is the most cat-specific crime there
    # is; "I'll pretend to listen" is pure cat attitude.
    1: (5, 5, 5, 4, 4),
    # Laptop cat: food test is funny, but "call back never" is a slightly
    # generic closer and the voicemail framing is thinner.
    2: (4, 5, 4, 4, 3),
    # Biscuit: "I can hear you thinking about it" is a great cat-voice
    # line; can-opening is cat-specific; punch is quick.
    3: (5, 4, 5, 5, 4),
    # Chairman Meow: staring at a wall is specific and odd; the name is a
    # known pun, which costs freshness.
    4: (5, 4, 4, 4, 2),
    # Luna 4 a.m.: the 4 a.m. food demand is straight from the brief, but
    # the line is a little flat and the "Meow" tail is a cliché closer.
    5: (5, 5, 3, 4, 2),
    # Pickles: knocking the phone off twice is a strong repeat joke and
    # explains why the cat can't hear you; voice is clear.
    6: (5, 5, 4, 4, 4),
    # Simba in the box: box joke is strong, but "then feed me" is a plain
    # ending and the line spends words restating the box.
    7: (4, 5, 3, 3, 3),
    # Tofu: sitting on the thing you were about to use is very cat; the
    # greeting frame is good, though the punch is gentler than the best.
    8: (5, 5, 4, 4, 4),
    # Mochi: confessing to the vase then pivoting to dinner is a sharp
    # two-beat joke; "Beep" as the closer is the voicemail itself.
    9: (5, 5, 5, 5, 4),
}


def total(scores):
    """Weighted total out of 75."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def rank():
    """Candidates ranked by weighted total, ties broken by shorter text."""
    ranked = sorted(
        range(len(CANDIDATES)),
        key=lambda i: (-total(SCORES[i]), len(CANDIDATES[i])),
    )
    return ranked


def pick_winner():
    """Highest-scoring valid candidate: 1-120 chars, single line."""
    for i in rank():
        text = CANDIDATES[i]
        if 1 <= len(text) <= 120 and "\n" not in text and text.strip():
            return i, text
    raise ValueError("no candidate passes the gate")


def main():
    print("Funniest Cat Voicemail Greeting — candidate ranking")
    print("gate: 1-120 characters, single line")
    print("-" * 72)
    for i in rank():
        text = CANDIDATES[i]
        print(f"[{total(SCORES[i]):2d}/75] ({len(text):3d} chars) {text}")
    print("-" * 72)

    # --- Part 2: winner pick, gate validation, output write --------------
    idx, winner = pick_winner()
    assert 1 <= len(winner) <= 120, "winner fails the 1-120 char gate"
    assert "\n" not in winner and winner.strip(), "winner must be one line"
    winner.encode("utf-8")  # gate: UTF-8 text
    print(f"winner: [{total(SCORES[idx])}/75] ({len(winner)} chars)")
    print(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner + "\n")
    print("wrote /output/entry.txt")


if __name__ == "__main__":
    main()
