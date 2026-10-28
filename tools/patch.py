import sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
R = [
    # one-liners and cards
    ('| Best-serviced Macedon Ranges town (Shops 7) but modern estates (Nature 7); rail access unclear. |',
     '| Macedon Ranges town with modern estates (Shops 7, Nature 7); rail access unclear. |'),
    ('the lowest Indian-community score of the east, no train', 'a low Indian-community score (2), no train'),
    ('hills plus a real Indian community and strong services, but 74 minutes from family',
     'hills, an India-born share of 2.4% and strong services, but 74 minutes from family'),
    # disagreements
    ('Items 1 to 6 can move a ranking or a hard filter; the rest are smaller.',
     'Items 1 to 6 can move a ranking or a hard filter; 7 to 10 are 27 Oct issues now resolved in the workbook; 11 to 18 are smaller.'),
    ('Kept workbook figure; about +0.09 score if swapped. Replace with a sale median.',
     'Kept workbook figure (score effect not re-run on the workbook weights). Replace with a sale median.'),
    ('Kept 33, flagged "?". About −0.17 score at 50 min. Re-time the true ED route.',
     'Kept 33, flagged "?" (score effect not re-run). Re-time the true ED route.'),
    ('Marked "!". Moves the five tested suburbs 0 to 6 places; top 10 unchanged. Add a "major ED" column.',
     'Marked "!". Rosebud (11th), Rye (13th) and Dromana (14th) rank just below the top 10 on these nearest-ED times; the effect of major-ED times has not been re-run. Add a "major ED" column.'),
    ('**15 of 51** meet 25 and 20:', '**15 of 51** meet 25 and 20 (leave-now basis):'),
    ('Option A has 5 suburbs inside them.',
     'Of the anchors, Frankston (25) and Seaford (24) are inside them; Mordialloc (28) is not. Comparators are on the 10:00 weekday basis and are not compared.'),
    ('| 7 | **Mum\'s 3 Essentials vs the cap of 2** | Cap is 2 per person (Settings) | Raw responses: Mum rated Nature, Near family and Indian community all "D". Dad and Y have two each (Nature, Near family) | Weights are computed as submitted. Round 2 enforces the cap; see scenarios below. |',
     '| 7 | **Essentials cap of 2** | Cap is 2 per person (Settings) | Round 2 ratings in the workbook: Mum has two Essentials (Hospital, Shops and doctor), Dad one (Nature), Y two (Nature, Beach) | Resolved: all within the cap. The 27 Oct issue (Mum with three) is superseded. |'),
    ('| 8 | **Nature cut to 9% though all three rated it Essential** | Final Nature 9.0, Near GW 23.4 | The shift (7.2 points) was typed from earlier weights and the workbook says to recompute it after Round 2. The survey blueprint\'s own rule (loser weight minus winner weight plus 2 points, halved), applied to today\'s survey weights, moves only about 1.0 point (Q10 vote was 2 to 1 for Near family) | Shown as the "rule" column: Nature 15.2, Near GW 17.2, and Belgrave and Eltham return to the top 10. Decision for the family. |',
     '| 8 | **Nature weight after the trade-offs** | Survey Nature 18.5%; final 14.4% after Q11 (Beach over Nature, 2–1) moved 4.1 points to Beach | The 27 Oct issue (Nature cut to 9% by a typed shift) is superseded: the workbook now applies the blueprint rule live | No change. Nature is the second-largest weight; Beach is the largest. |'),
    ('| 9 | **Raw trade-off cells** | Q10 to Q12 cells hold criterion names | Q11 is recorded as "Village character", which matches neither option (flat suburb with beach, or hills with beach an hour away); Q13 is blank | Treat the Q10 to Q12 data as placeholders. Round 2 re-asks Q13 only. |',
     '| 9 | **Trade-off votes** | Q10 to Q13 recorded with each person\'s vote, all 2–1: Nature over Near family, Beach over Nature, Village over Shops, Nature over Indian community | The 27 Oct issue (placeholder cells, Q13 blank) is superseded | No change. |'),
    ('| 10 | **Saved file holds formulas without stored results** | Weights are formulas | Reading cached values gives blanks for CleanedAnswers, PriorityWeights and the final weights | I used the recalculated weights in the context note. Open and recalculate in Excel before relying on any total. |',
     '| 10 | **Formulas need recalculation** | Weights, the formula scores (M, O, T) and the weighted score are formulas; the judgement scores are entered values | A file saved without recalculation can show blank cached values. This report read a recalculated copy of commit 7de29d5 | Open and recalculate in Excel before relying on any total. |'),
    ('| 17 | **Drive-time basis** | Google Maps "leave now", midday, 27 Oct (26 Oct for earlier rows) |',
     '| 17 | **Drive-time basis** | Leave now, 26 Oct (Active Shortlist ranked); Leave now, 27 Oct (Watchlist, Open-mind viewing, Frankston South); 10:00 weekday, 28 Oct (comparators, workbook J/K) |'),
    ('Gisborne timed from the post office | Re-run the shortlist at peak and weekend times. |',
     'Gisborne timed from the post office | Labelled per row in this report. Re-run the anchors at 10:00 on a weekday so they compare like for like with the comparators. |'),
    # unverified
    ('Endeavour Spices and Shri Sanatan Dharam still need verification). For the 51 scored suburbs',
     'Endeavour Spices and Shri Sanatan Dharam\'s opening hours: NEEDS VERIFICATION). For the 51 ranked suburbs'),
    ('Named grocers: **not found** for any suburb.', 'Named grocers: **not found** for any of the 51 ranked suburbs.'),
    ('| Midday "leave now" only for the 51; the comparators are checked at 08:00 and 10:00 weekday, so the two sets differ in basis | Re-time the 12 on a weekday 8am, Saturday 10am and Sunday 5pm, to Glen Waverley and to the ED. |',
     '| Ranked suburbs: Leave now, 26 Oct or Leave now, 27 Oct. Comparators: 10:00 weekday, 28 Oct (workbook J/K). The bases differ | Re-time the three anchors at Wed 10:00, to Glen Waverley and to the ED, so the options compare like for like. |'),
    ('| 38 of 51 prices are AVMs |', '| 38 of 51 ranked prices are AVMs, including Seaford and Mordialloc |'),
    ('Each family member scores the 12 after viewing.', 'Each family member scores the option suburbs after viewing.'),
    # inspection
    ('| Altona, Newport, West Footscray, Chelsea |', '| Altona, Newport, West Footscray, Chelsea, Mordialloc, Seaford |'),
    ('| ED route and a test run | Peninsula and Macedon distances | Dromana, Rye, Woodend, Kyneton |',
     '| ED route and a test run | Peninsula and Macedon distances | Dromana, Rye, Woodend, Kyneton |\n| Walk or drive to the grocer, temple and church | Tests whether the community side feels close in practice | Springvale, Clayton South, Keysborough, Endeavour Hills, Wheelers Hill |'),
]
for a, b in R:
    assert t.count(a) == 1, a[:80]
    t = t.replace(a, b)
open(p, 'w', encoding='utf-8').write(t)
print('patched', len(R))
