# make.fun cutest-picture-01 — STATUS

- Bounty: cutest-picture-01 "Make the cutest picture" ($250, 20 places: 1st $50)
- Deadline: 13 Nov 2026 17:00 WIB (2026-11-13T10:00:00Z)
- Entry: "Duckling in a Rain Hat" — baby duckling, yellow rain hat, pink flower
- Program: main.py (Python 3.13 stdlib only) copies assets/entry.jpg to /output/entry.png
- Output: 1024x1024 JPEG, 179,336 bytes (< 1 MiB), deterministic (sha256 a0bca4a2…ddae9, identical across 2 runs)
- Note: PNG at 1024 does NOT fit 1 MiB (1,088,178 bytes optimized), so JPEG is used; brief allows PNG or JPEG and fixes the output path as /output/entry.png, so the gate must sniff content.
- Harness: fresh Gemini CLI session (gemini-3.5-flash-lite; 3.5-flash 503-overloaded 5x, killed, retried on lite)
- Session transcript: ~/.gemini/tmp/makefun-cutest-picture/chats/session-2026-11-12T08-56-355685f1.jsonl — check-session-usage.py PASS (33 msgs, 21 with per-message usage)
- Candidates rejected: kitten (daisy crown + plush fish, very close 2nd), otter, red panda — kept in ~/workspace/makefun-cutest-picture-candidates/
- Status: BUILT + REVIEWED, NOT SUBMITTED — submit needs Hasan's separate 'gas'
