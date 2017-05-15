



# =====================================================================
# =====================================================================
# Inputs

# Define price variables
price_booklet = 0.05 # USD per item
price_sticker = 0.15 # USD per item, derived from email titled "LES Article"
                    # which stated "[I] filled in the cost of the stickers
                    # for a 50K run (~$8K)", 8000 / 50000. = ~.15
price_labor = 15 # USD per hour
price_incentive = 10 # USD per survey

# Define survey variables
R_RATE = 0.03 # survey response rate
NB_TEST = 90000
NB_CNTRL = 90000
NB_TOTAL  = NB_TEST + NB_CNTRL

print("\n### Vegan Outreach Budget Summary for LES")
print("   with partners Animal Charity Evaluations,")
print("   The Humane League, and 80K Hours.")

# Keep track of the total donatations of each partner org
vo_total = 0
thl_total = 0
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

print("\nLABOR")
print("   With a Booklet Per Day (BPD) average of {0}".format(BPD_large))
print("   for large schools and {0} for small schools,".format(BPD_small))
print("   a total of {0} schools will need to be visited".format(num_schools))
print("   to hand out the full {0} study complement of books.".format(NB_TOTAL))
print("   ... Vegan Outreach Labor Donation: ${0}".format( BPD_small_ratio * labor_total ))
print("   ... The Humane League Labor Donation: ${0}".format( BPD_large_ratio * labor_total))

vo_total += BPD_small_ratio * labor_total
thl_total += BPD_large_ratio * labor_total

# =====================================================================
# =====================================================================
# Booklet donations (VO, ACE, CTRL)

test_cost = NB_TEST * price_booklet
cntrl_cost = NB_CNTRL * price_booklet
sticker_cost = NB_TOTAL * price_sticker

print("\nBOOKLETS AND STICKERS")
print("   A total of {0} booklets are being handed".format(NB_TOTAL))
print("   out ({0} test, {1} control). Stickers".format(NB_TEST,NB_CNTRL))
print("   advertising the survey are attached.")
print("   ... Vegan Outreach provides test booklets: ${0}".format(test_cost))
print("   ... 80K Hours provides control booklets: ${0}".format(cntrl_cost))
print("   ... ACE Provides stickers: ${0}".format(sticker_cost))

vo_total += test_cost
cntrl_total += cntrl_cost
ace_total += sticker_cost

# =====================================================================
# =====================================================================
# Incentive donations (ACE)

incentive_cost = NB_TOTAL * R_RATE * price_incentive

print("\nSURVEY INCENTIVES")
print("   A ${0} incentive is offered for students".format(price_incentive))
print("   recieving a booklet to take the survey.")
print("   An estimated {0} of 1000 students will respond ({1} response rate)".format(R_RATE * 1000, R_RATE))
print("   ... ACE provides incentives: {0}".format(incentive_cost))

ace_total += incentive_cost


# =====================================================================
# =====================================================================
# Summaries

print("\n### STUDY SUMMARY")
print("   ... distribute {0} booklets ({1} test, {2} control)".format(NB_TOTAL, NB_TEST, NB_CNTRL))
print("   ... visit {0} schools".format(num_schools))
print("   ... offer a ${0} incentive for a {1} survey response rate".format(price_incentive, R_RATE))

print("\n### COST SHARING SUMMARY")
print("   ...Vegan Outreach: ${0}".format(vo_total))
print("   ...Humane League: ${0}".format(thl_total))
print("   ...80K Hours: ${0}".format(cntrl_total))
print("   ...ACE: ${0} <-- ACE Grant Request".format(ace_total))
