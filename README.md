# ai-judge-rich

Entry program for make.fun `ai-judge-rich-01` (trial build, not submitted).

`main.py` (Python 3.13, standard library only) deterministically writes a
plan for turning $100 into the most money in 30 days, with no human work,
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` locally).

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
