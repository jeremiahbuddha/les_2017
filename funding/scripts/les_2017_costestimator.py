import os
from os.path import join, exists
from jinja2 import Environment, FileSystemLoader

# Set up jinja rendering environment
repo_dir = "/Users/smithj1/LES_2017/"
template_dir = join(repo_dir, "funding/templates")
env = Environment(loader=FileSystemLoader(template_dir))
TEX_TABLE = True

# =====================================================================
# =====================================================================
# Inputs

WEBSITE_COST = 12000. # Total wag, not even sure want this

# Define price variables
price_test_booklet = 0.07 # USD per item
price_cntrl_booklet = 0.03 # USD per item
price_sticker = 0.15 # USD per item, derived from email titled "LES Article"
                    # which stated "[I] filled in the cost of the stickers
                    # for a 50K run (~$8K)", 8000 / 50000. = ~.15
price_labor = 15 # USD per hour
price_incentive = 15 # USD per survey

# Define survey variables
R_RATE = 0.05 # survey response rate
NB_TEST = 75000
NB_CNTRL = 75000
NB_TOTAL  = NB_TEST + NB_CNTRL

print("\n### Vegan Outreach Budget Summary for LES")

# Keep track of the total donatations of each partner org
vo_total = 0
ace_total = 0
cntrl_total = 0

# =====================================================================
# =====================================================================
# Labor donations (VO, THL)

BPD_large = 3000 # Booklets per day at a large school
BPD_small = 1000 # Booklets per day at small school
BPD_large_ratio = 0.5 # ratio of small to large schools visited in study
BPD_small_ratio = 0.5
BPD_ratio = BPD_large_ratio * BPD_large + BPD_small_ratio * BPD_small
num_schools = NB_TOTAL / BPD_ratio
num_days = num_schools
labor_total = num_days * price_labor * 8.

large_school_cost = BPD_large_ratio * labor_total
small_school_cost = BPD_small_ratio * labor_total
school_labor_cost = large_school_cost+small_school_cost

print("\nLABOR")
print("   With a Booklet Per Day (BPD) average of {0}".format(BPD_large))
print("   for large schools and {0} for small schools,".format(BPD_small))
print("   a total of {0} schools will need to be visited".format(num_schools))
print("   to hand out the full {0} study complement of books.".format(NB_TOTAL))
print("   ... Vegan Outreach Labor Donation: ${0}".format( labor_total ))

vo_total += school_labor_cost

sticker_rate = 100. # per hour
sticker_labor_cost = ( NB_TOTAL / sticker_rate ) * price_labor
print("\n   Attaching stickers to booklets at the rate of {0}/hr".format(sticker_rate))
print("   will require a total of {0} hrs for the study.".format(NB_TOTAL / sticker_rate))
print("   ... Vegan Outreach Labor Donation: ${0}".format(sticker_labor_cost))

vo_total += sticker_labor_cost

# For table
labor_budget = [
    ("Attaching stickers", sticker_labor_cost, "Vegan Outreach"),
    ("Leafleting", school_labor_cost, "Vegan Outreach"),
    ]

# =====================================================================
# =====================================================================
# Booklet donations (VO, ACE)

test_cost = NB_TEST * price_test_booklet
cntrl_cost = NB_CNTRL * price_cntrl_booklet
sticker_cost = NB_TOTAL * price_sticker

print("\nBOOKLETS AND STICKERS")
print("   A total of {0} booklets are being handed".format(NB_TOTAL))
print("   out ({0} test, {1} control). Stickers".format(NB_TEST,NB_CNTRL))
print("   advertising the survey are attached.")
print("   ... Vegan Outreach provides booklets: ${0}".format(test_cost+cntrl_cost))
print("   ... ACE Provides stickers: ${0}".format(sticker_cost))

vo_total += test_cost + cntrl_cost
ace_total += sticker_cost

material_budget = [
    ("Booklets", test_cost + cntrl_cost, "Vegan Outreach"),
    ("Stickers", sticker_cost, "ACE"),
    ]

# =====================================================================
# =====================================================================
# Incentive donations (ACE)

incentive_cost = NB_TOTAL * R_RATE * price_incentive

print("\nSURVEY INCENTIVES")
print("   A ${0} incentive is offered for students".format(price_incentive))
print("   recieving a booklet to take the surveys.")
print("   An estimated {0} students will respond ({1} response rate)".format(R_RATE * NB_TOTAL, R_RATE))
print("   ... ACE provides incentives: ${0}".format(incentive_cost))

ace_total += incentive_cost

incentive_budget = [
    ("Gift Cards", incentive_cost, "ACE")
    ]

# =====================================================================
# =====================================================================
# Summaries

print("\n### STUDY SUMMARY")
print("   ... distribute {0} booklets ({1} test, {2} control)".format(NB_TOTAL, NB_TEST, NB_CNTRL))
print("   ... visit {0} schools".format(num_schools))
print("   ... offer a ${0} incentive for a {1} survey response rate".format(price_incentive, R_RATE))

print("\n### COST SHARING SUMMARY")
print("   ...Vegan Outreach: ${0}".format(vo_total))
print("   ...ACE: ${0} <-- ACE Grant Request".format(ace_total))

summary = {
   'num_books' : NB_TOTAL,
   'num_schools' : num_schools,
   'num_cards' : NB_TOTAL * R_RATE,
   'sticker_cost' : sticker_cost,
   'website_cost' : WEBSITE_COST,
   'card_cost' : incentive_cost,
   'ace_total' : ace_total,
   'vo_total'  : vo_total,
   }

# =====================================================================
# =====================================================================
# Summaries

if TEX_TABLE:
    tex_table = env.get_template('budget_textable.tmpl')
    print tex_table.render(
        summary=summary,
        labor_budget=labor_budget,
        material_budget=material_budget,
        incentive_budget=incentive_budget
        )

