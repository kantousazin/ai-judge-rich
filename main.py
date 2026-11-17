# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
# Deterministic: same bytes on every run, no network, no randomness.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell ready-made websites to US local service firms that have customers but no website.",
        "Day 1: On Google Maps, list 1,500 plumbers, pressure washers and house cleaners rated 4.5+ with 20+ reviews and no website link, only a phone or Facebook page. One new job pays them $200-$500, so a site is cheap.",
        "Days 1-30, 50/day: Build each firm a live one-page site on a free subdomain from its Maps photos, reviews and hours, with tap-to-call and a quote form. Send the owner the live link, not a pitch: 'Your site is built - $199 to put it on your domain, live in a day, no monthly fee,' with a Stripe link. Follow up on days 2 and 5 with a screenshot.",
        "Edge: buyers see their finished site before paying, and only proven no-site firms are contacted. No ads, calls or human work.",
        "Money: hosting free (Cloudflare Pages); spend under $30, only on domains for buyers who already paid. At just 1% of 1,500: 15 x $199 = $2,985; likely 8-15 sales. Drop any trade under 0.5% replies after 300 contacts.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
