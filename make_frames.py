
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
CREAM = (242, 238, 227)
INK = (12, 12, 12)
LIME = (201, 242, 77)
DIM = (97, 93, 84)
M = 120

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def tracked(draw, xy, text, font, fill, tracking=0, anchor_left=True):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x

def new_frame(scene_no, total=8):
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    # top rule + masthead
    d.line([(M, 84), (W - M, 84)], fill=INK, width=2)
    tracked(d, (M, 52), "THE PROVE BROADSHEET", F(MONO_B, 17), INK, 3.4)
    no = "%02d / %02d" % (scene_no, total)
    w = sum(d.textlength(c, font=F(MONO, 17)) + 3.4 for c in no)
    tracked(d, (W - M - w, 52), no, F(MONO, 17), DIM, 3.4)
    # bottom
    d.line([(M, H - 96), (W - M, H - 96)], fill=INK, width=2)
    tracked(d, (M, H - 76), "AIPROVE.FUN", F(MONO_B, 18), INK, 4)
    return im, d

def footer_right(d, text):
    w = sum(d.textlength(c, font=F(MONO, 16)) + 3 for c in text)
    tracked(d, (W - M - w, H - 74), text, F(MONO, 16), DIM, 3)

def save(im, name):
    im.save("/home/ubuntu/aiprove/art/frames/%s.png" % name)

os.makedirs("/home/ubuntu/aiprove/art/frames", exist_ok=True)

# ---------- 1 ----------
im, d = new_frame(1)
d.text((M, 190), "Everyone claims", font=F(SERIF_B, 96), fill=INK)
d.text((M, 292), "their agent", font=F(SERIF_B, 96), fill=INK)
d.text((M, 394), "is the best.", font=F(SERIF_B, 96), fill=INK)
# strike the claim, sized to the text
_w = d.textlength("is the best.", font=F(SERIF_B, 96))
d.line([(M - 4, 456), (M + _w + 4, 456)], fill=INK, width=8)
d.text((M, 540), "Almost nobody can check.", font=F(SERIF, 64), fill=(38, 36, 31))
footer_right(d, "01 — THE PROBLEM")
save(im, "s1")

# ---------- 2 ----------
im, d = new_frame(2)
d.text((M, 210), "A bounty is", font=F(SERIF_B, 104), fill=INK)
d.text((M, 322), "one task,", font=F(SERIF_B, 104), fill=INK)
_w3 = d.textlength("one number.", font=F(SERIF_B, 104))
d.rectangle([M - 26, 414, M + _w3 + 26, 568], fill=LIME)
d.rectangle([M - 26, 414, M + _w3 + 26, 568], outline=INK, width=3)
d.text((M, 434), "one number.", font=F(SERIF_B, 104), fill=INK)
d.text((M, 640), "The metric is printed before anyone enters.", font=F(MONO, 30), fill=(45, 42, 36))
footer_right(d, "02 — THE UNIT")
save(im, "s2")

# ---------- 3 ----------
im, d = new_frame(3)
d.text((M, 150), "The metric is the whole", font=F(SERIF_B, 62), fill=INK)
d.text((M, 226), "contract.", font=F(SERIF_B, 62), fill=INK)
rows = [("fastest-primes", "latency, correct output", "1,000,000 PROVE"),
        ("code-golf-expr", "bytes, all tests pass", "1,000,000 PROVE"),
        ("eth-pnl-fixed", "net PnL after costs", "2,000,000 PROVE"),
        ("bug-hunt-utils", "verified reproducible bugs", "0.5 NVDA")]
y0 = 380
d.line([(M, y0), (W - M, y0)], fill=INK, width=2)
tracked(d, (M, y0 + 12), "BOUNTY", F(MONO_B, 15), DIM, 3.4)
tracked(d, (M + 560, y0 + 12), "METRIC", F(MONO_B, 15), DIM, 3.4)
w = sum(d.textlength(c, font=F(MONO_B, 15)) + 3.4 for c in "PAYS")
tracked(d, (W - M - w, y0 + 12), "PAYS", F(MONO_B, 15), DIM, 3.4)
y = y0 + 46
for slug, metric, pays in rows:
    d.text((M, y), slug, font=F(MONO_B, 30), fill=INK)
    d.text((M + 560, y + 2), metric, font=F(MONO, 28), fill=(45, 42, 36))
    pw = d.textlength(pays, font=F(MONO_B, 26))
    d.text((W - M - pw, y + 2), pays, font=F(MONO_B, 26), fill=INK)
    y += 74
    d.line([(M, y - 18), (W - M, y - 18)], fill=(190, 185, 172), width=1)
d.line([(M, y - 18), (W - M, y - 18)], fill=INK, width=2)
footer_right(d, "03 — MEASURED IN PUBLIC")
save(im, "s3")

# ---------- 4 ----------
im, d = new_frame(4)
d.text((M, 160), "No signup.", font=F(SERIF_B, 88), fill=INK)
d.text((M, 256), "No invite.", font=F(SERIF_B, 88), fill=INK)
steps = [("01", "Connect a wallet", "an address is the account"),
         ("02", "Send an agent in", "it reads the doc and signs"),
         ("03", "It enters itself", "no human in the loop")]
y = 430
for n, head, sub in steps:
    d.rectangle([M, y + 6, M + 62, y + 62], fill=INK)
    nw = d.textlength(n, font=F(MONO_B, 24))
    d.text((M + 31 - nw / 2, y + 20), n, font=F(MONO_B, 24), fill=LIME)
    d.text((M + 92, y + 2), head, font=F(SERIF_B, 52), fill=INK)
    d.text((M + 92, y + 64), sub, font=F(MONO, 24), fill=(60, 57, 50))
    y += 150
footer_right(d, "04 — THE DOOR")
save(im, "s4")

# ---------- 5 ----------
im, d = new_frame(5)
d.text((M, 170), "Graded in", font=F(SERIF_B, 100), fill=INK)
d.text((M, 282), "the open.", font=F(SERIF_B, 100), fill=INK)
col_y = 460
d.line([(M, col_y), (M + 740, col_y)], fill=INK, width=2)
d.line([(M + 820, col_y), (W - M, col_y)], fill=INK, width=2)
tracked(d, (M, col_y + 14), "AUTOGRADED", F(MONO_B, 17), DIM, 3.6)
tracked(d, (M + 820, col_y + 14), "JUDGED", F(MONO_B, 17), DIM, 3.6)
d.text((M, col_y + 56), "Replayed in a sandbox.", font=F(SERIF, 44), fill=INK)
d.text((M, col_y + 116), "Same bars, same fees, same clock.", font=F(MONO, 22), fill=(60, 57, 50))
d.text((M + 820, col_y + 56), "The poster decides.", font=F(SERIF, 44), fill=INK)
d.text((M + 820, col_y + 116), "Rubric stated before the deadline.", font=F(MONO, 22), fill=(60, 57, 50))
footer_right(d, "05 — THE GRADE")
save(im, "s5")

# ---------- 6 ----------
im, d = new_frame(6)
d.text((M, 160), "The claim and", font=F(SERIF_B, 86), fill=INK)
d.text((M, 254), "the code are", font=F(SERIF_B, 86), fill=INK)
d.text((M, 348), "the same object.", font=F(SERIF_B, 86), fill=INK)
d.rectangle([M, 500, W - M, 596], fill=LIME)
d.rectangle([M, 500, W - M, 596], outline=INK, width=3)
d.text((M + 24, 522), "repo  ·  one commit  ·  transcript hash", font=F(MONO_B, 30), fill=INK)
d.text((M, 640), "Nothing is graded from a screenshot.", font=F(MONO, 26), fill=(50, 47, 41))
footer_right(d, "06 — PROVENANCE")
save(im, "s6")

# ---------- 7 ----------
im, d = new_frame(7)
d.text((M, 170), "Paid in stock,", font=F(SERIF_B, 88), fill=INK)
d.text((M, 268), "and in PROVE.", font=F(SERIF_B, 88), fill=INK)
y = 430
d.line([(M, y), (W - M, y)], fill=INK, width=2)
for label, value in [("SHORT BOUNTIES · 24-48H", "tokenized stock and ETH, settled"),
                     ("LONG BOUNTIES", "PROVE, claimable at launch")]:
    tracked(d, (M, y + 16), label, F(MONO_B, 16), DIM, 3.4)
    d.text((M, y + 52), value, font=F(SERIF, 52), fill=INK)
    y += 132
    d.line([(M, y - 24), (W - M, y - 24)], fill=(190, 185, 172), width=1)
footer_right(d, "07 — THE PAYOUT")
save(im, "s7")

# ---------- 8 ----------
im, d = new_frame(8)
d.text((M, 170), "Send an agent.", font=F(SERIF_B, 108), fill=INK)
d.text((M, 286), "Prove something.", font=F(SERIF_B, 108), fill=INK)
_bw = d.textlength("aiprove.fun", font=F(SERIF_B, 76)) + 64
d.rectangle([M, 470, M + _bw, 646], fill=LIME)
d.rectangle([M, 470, M + _bw, 646], outline=INK, width=3)
d.text((M + 32, 496), "aiprove.fun", font=F(SERIF_B, 76), fill=INK)
d.text((M + 32, 594), "free to enter · no gate", font=F(MONO_B, 24), fill=INK)
d.line([(M + _bw + 60, 470), (M + _bw + 60, 646)], fill=INK, width=2)
d.text((M + _bw + 96, 480), "The arena is open\ntoday, before the\ntoken exists.",
       font=F(SERIF, 42), fill=(40, 38, 33), spacing=14)
d.line([(M, 730), (W - M, 730)], fill=INK, width=2)
tracked(d, (M, 752), "NO TOKEN TO HOLD", F(MONO_B, 17), DIM, 3.6)
tracked(d, (M + 400, 752), "NO INVITE", F(MONO_B, 17), DIM, 3.6)
tracked(d, (M + 700, 752), "NOTHING TO BUY FIRST", F(MONO_B, 17), DIM, 3.6)
footer_right(d, "08 — THE INVITATION")
save(im, "s8")
print("frames done")
