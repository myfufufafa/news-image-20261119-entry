# The world in one day — 19 November 2026

This repository holds one picture that tries to carry a whole day of
world news: a packed newspaper page dated Thursday 19 November 2026,
with thirty-six items counted in its masthead and every one of them
actually printed — six big stories with pictures across the top, thirty
short ones numbered below, and a small map at the foot showing where
the big stories happened.

## What is on the page

Diplomacy leads the day: the first ever three-way meeting of the
American, Chinese and Russian presidents, held in Shenzhen on the
sidelines of the APEC leaders' gathering. The Gulf is the second
thread: Iranian drones aimed at an American base in Kuwait, more
interceptions over Bahrain, and the American strike on Qeshm Island
that preceded them. Culture supplies the third: the worldwide launch
of GTA VI and its return to Vice City.

Around those, the page carries the court judgment on Myanmar, the
European Union's planned €45 billion loan for Ukraine, Nvidia's
$115.8 billion quarter under its interim chief, the Federal Reserve's
minutes pointing to further rate rises, a falling Dow and gold price,
Voyager 1 reaching a light-day from Earth, Cyclone Akvan approaching
India's east coast, the COP31 talks, and two dozen more items from
every continent — elections, courts, markets, space, weather, sport
and technology.

## The picture

`entry.png` is 1024 by 1024 pixels and 492,620 bytes, made with an AI
image tool from the day's reporting and checked against several news
outlets (BBC, Reuters wire summaries, Al Jazeera, AP summaries and
morning headline round-ups). Its sha256 is
`759a101cbb89dc8fcadf7c531159e72fa8cc982da2f27d4cfc466831a71c4505`.

## How the program works

`main.py` needs nothing but the Python standard library and no
network. Point `MAKEFUN_OUTPUT_DIR` at a folder and run the script;
the shipped picture lands there as `entry.png`, and the script refuses
to finish quietly unless the copy is the same length and the same
sha256 as the file it shipped with. Run it twice and the two outputs
are byte for byte the same.
