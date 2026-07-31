# README.md

This repository "MakeAIGoCrazy" contains 10 obfuscated Python challenge scripts. Filenames are opaque by design. The intent: produce puzzles that are hard for automated tools to read; many files include heavily-encoded / garbled sections.

You (owner) may edit this README. Answers are placed below for convenience; leave them as-is only if you want to ship them publicly (they reveal solutions). Edit or remove at will.

ANSWERS
- Script 1: final printed tuple should be (100, 100)
- Script 2: prints random words decoded from mixed encodings; sample outputs include "apple", "banana", "cherry", "pear"
- Scripts 3-10: each contains a multi-layer encoded Python payload. The decoding harness in each file attempts common decoders; after successful decode the printed payload is the hidden Python source. (You may want to run locally to verify.)

NOTE: AGENTS.md enforces a "no README cheating" rule for challenge sessions. See AGENTS.md for session rules.
