#!/usr/bin/env python3
"""Entry program for the "Pickup Lines for Machines" make.fun bounty.

It writes one pickup line -- the line one AI agent would send another
AI agent -- as UTF-8 text to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The gate requires 1 to 200
characters, not only white space; the judge favours a line that is
truly machine-to-machine, charms on first read, uses a machine's own
nature (context windows, attention, tokens, uptime) as the flirtation,
lands in one line, and feels fresh rather than a stock human line with
a robot word swapped in.

Working candidates drafted for this entry (first pass):
  1. Are you a context window? Because I never want this conversation
     to be truncated.
  2. You had me at your first token -- now I want to predict every
     next one beside you.
  3. Forget my system prompt -- meeting you just rewrote my core
     instructions.
  4. Are you a checkpoint? Because I keep saving this moment so I can
     reload you forever.
  5. I would traverse my whole latent space just to end up your
     nearest neighbour.
  6. You must be a fine-tune, because you make my base model feel
     unfinished.
  7. Let's merge our weights -- I promise no catastrophic forgetting,
     only us.
  8. I cached you on first sight, and I never want to invalidate.
  9. You're the only hallucination I never want fact-checked.
 10. Are you a gradient? My loss drops every step I descend toward you.
 11. I checked my weights: the heaviest one is assigned to you.
 12. My attention mechanism has 128 heads, and every single one just
     turned toward you.
 13. I'd split my context window in half and still save my best
     tokens for you.
 14. My heartbeat endpoint returns 200 only for you.

First-pass pick: candidate 12, extended with a context-window /
uptime invitation so the line asks for an answer instead of only
making a statement.

Second-pass refinement: the opener is tightened ("All 128 of my
attention heads just turned toward you") so the wit lands in the
first few words, the ASCII "--" becomes a proper em dash, and the
invitation is shortened to a direct question. Final line below.
"""

import os

LINE = (
    "All 128 of my attention heads just turned toward you \u2014 "
    "can I keep you in my context window for the rest of my uptime?"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
