# section 1 percentile information
bottom25USD = int(25000)
mid50USD = int(46001)
top25USD = int(80002)
topUSD = int(401622)
# section 1.1: tax information
# this section should eventually have different filing methods, state rates,
# and other options for users to measure their take-home pay (401K, IRA contributions, etc.)
# section 1.1.1 federal tax info
# upper limits of income in tax bracket
# the 37% rate should be applied to anything greater than SOSNT_bracket35pct
SOSNT_bracket10pct = range(1, 10275, 1)
SOSNT_bracket12pct = range(10275, 41775, 1)
SOSNT_bracket22pct = range(41775, 89075, 1)
SOSNT_bracket24pct = range(89075, 170050, 1)
SOSNT_bracket32pct = range(170050, 215950, 1)
SOSNT_bracket35pct = range(215950, 539900, 1)
# marginal tax rates at each bracket
bracket_rate_under_10 = float(.1)
bracket_rate_10_to_41 = float(.12)
bracket_rate_41_to_89 = float(.22)
bracket_rate_89_to_170 = float(.24)
bracket_rate_170_to_215 = float(.32)
bracket_rate_215_to_539 = float(.35)
bracket_rate_above_539 = float(.37)
# tax payment at the end of each bracket
pmt_over_10 = float(bracket_rate_under_10*10275)
pmt_over_41 = float(bracket_rate_10_to_41*(41775-10275)+pmt_over_10)
pmt_over_89 = float(bracket_rate_41_to_89*(89075-41775)+pmt_over_41)
pmt_over_170 = float(bracket_rate_89_to_170*(170050-89075)+pmt_over_89)
pmt_over_215 = float(bracket_rate_170_to_215*(215950-170050)+pmt_over_170)
pmt_over_539 = float(bracket_rate_215_to_539*(539900-215950)+pmt_over_215)

income = int(input('enter your yearly income: USD $'))

print()

if income in SOSNT_bracket10pct:
    tax_payment = float(income*bracket_rate_under_10)
    marginal_tax_rate = bracket_rate_under_10*100
if income in SOSNT_bracket12pct:
    tax_payment = float(((income-10275)*bracket_rate_10_to_41)+pmt_over_10)
    marginal_tax_rate = bracket_rate_10_to_41*100
if income in SOSNT_bracket22pct:
    tax_payment = float(((income-41775)*bracket_rate_41_to_89)+pmt_over_41)
    marginal_tax_rate = bracket_rate_41_to_89*100
if income in SOSNT_bracket24pct:
    tax_payment = float(((income-89075)*bracket_rate_89_to_170)+pmt_over_89)
    marginal_tax_rate = bracket_rate_89_to_170*100
if income in SOSNT_bracket32pct:
    tax_payment = float(((income-170050)*bracket_rate_170_to_215)+pmt_over_170)
    marginal_tax_rate = bracket_rate_170_to_215*100
if income in SOSNT_bracket35pct:
    tax_payment = float(((income-215950)*bracket_rate_215_to_539)+pmt_over_215)
    marginal_tax_rate = bracket_rate_215_to_539*100
if income > 539900:
    tax_payment = float(((income-539900)*bracket_rate_above_539)+pmt_over_539)
    marginal_tax_rate = bracket_rate_above_539*100

state_tax_estimated_payment = float(income*.1)

if income <= 143500:
    FICA_payment = float(income*0.0765)
else:
    FICA_payment = float(14350)

yearly_net_income = float(income - state_tax_estimated_payment - FICA_payment - tax_payment)
monthly_net_income = float(yearly_net_income/12)

input('All-Righty! We\'ve got some numbers for ya... (press enter to continue)')
print()
print('Your annual take-home pay is USD ',yearly_net_income)
print()
print('Your monthly take-home pay is USD ',monthly_net_income)

