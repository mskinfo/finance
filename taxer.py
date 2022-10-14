bottom25USD = int(25000)
mid50USD = int(46001)
top25USD = int(80002)
topUSD = int(401622)
SOSNT_bracket10pct = float(9950)
SOSNT_bracket12pct = float(40525)
SOSNT_bracket22pct = float(86375)
SOSNT_bracket24pct = float(164925)
SOSNT_bracket32pct = float(209425)
SOSNT_bracket35pct = float(314150)
SOSNT_bracket37pct = float(314151)


def tax_income_salary(income):
    if income - SOSNT_bracket37pct <= 0:
        if income - SOSNT_bracket35pct <= 0:
            if income - SOSNT_bracket32pct <= 0:
                if income - SOSNT_bracket24pct <= 0:
                    if income - SOSNT_bracket22pct <= 0:
                        if income - SOSNT_bracket12pct <= 0:
                            if income - SOSNT_bracket10pct <= 0:
                                return income * (1 - .10)
                        else:
                            return (income - SOSNT_bracket12pct) * (1 - .12) \
                                   + income * (1 - .10)
                    else:
                        return (income - SOSNT_bracket22pct) * (1 - .22) + (income - SOSNT_bracket12pct) * (1 - .12) \
                               + income * (1 - .10)
                else:
                    return (income - SOSNT_bracket24pct) * (1 - .24) \
                           + (income - SOSNT_bracket22pct) * (1 - .22) + (income - SOSNT_bracket12pct) * (1 - .12) \
                           + income * (1 - .10)
            else:
                return (income - SOSNT_bracket32pct) * (1 - .32) + (income - SOSNT_bracket24pct) * (1 - .24) \
                       + (income - SOSNT_bracket22pct) * (1 - .22) + (income - SOSNT_bracket12pct) * (1 - .12) + \
                       income * (1 - .10)
        else:
            return (income - SOSNT_bracket35pct) * (1 - .35) + (income - SOSNT_bracket32pct) * (1 - .32) + \
                   (income - SOSNT_bracket24pct) * (1 - .24) + (income - SOSNT_bracket22pct) * (1 - .22) + \
                   (income - SOSNT_bracket12pct) * (1 - .12) + income * (1 - .10)
    else:
        return (income - SOSNT_bracket37pct) * (1 - .37) + (income - SOSNT_bracket35pct) * (1 - .35) \
               + (income - SOSNT_bracket32pct) * (1 - .32) + (income - SOSNT_bracket24pct) * (1 - .24) \
               + (income - SOSNT_bracket22pct) * (1 - .22) + (income - SOSNT_bracket12pct) * (1 - .12) \
               + income * (1 - .10)


print('let\'s start with your income before taxes...')
income_type = input("are you paid by the hour or on a salary? ")
if income_type.lower() not in ('by the hour', 'hourly', 'hour', 'per hour', 'h',
                               'on a salary', 'salary', 'salaried', 'salary', 's'):
    print(" if you're paid hourly enter 'by the hour', 'hourly', 'hour', 'per hour', or 'h'. \n "
          "if you are a salaried worker, enter 'on a salary', 'salary', 'salaried', 'salary', or 's' ")
else:
    # salaried user inputs
    if income_type in ('on a salary', 'salary', 'salaried', 'salary', 's'):
        paycheck_times = float(input("how many times per year do you receive your paycheck? "))
        while paycheck_times is None:
            try:
                paycheck_times = float(input("how many times per year do you receive your paycheck? "))
            except ValueError:
                print("'{}' is not an acceptable value.  Try entering a number or an integer, "
                      "like 50.5 or 42.".format(paycheck_times))
        discrete_income_amount = float(input("how large is your paycheck each time your are paid? "))
        while discrete_income_amount is None:
            try:
                discrete_income_amount = float(input("how large is your paycheck each time your are paid? "))
            except ValueError:
                print("'{}' is not an acceptable value.  Try entering a number or"
                      " an integer, like 2000 or 25993.32.".format(discrete_income_amount))
        pretaxincomesalaried_user = discrete_income_amount * paycheck_times
        print()
        print("Your gross annual income: ", pretaxincomesalaried_user)
        if pretaxincomesalaried_user <= bottom25USD:
            print("Your gross annual income is less than that of the top 75% of Americans.")
        else:
            if pretaxincomesalaried_user <= mid50USD:
                print("Your gross annual income is less than that of the top 50% of Americans.")
            else:
                if pretaxincomesalaried_user <= top25USD:
                    print("Your gross annual income is more than that of the bottom 50% of Americans.")
                else:
                    if pretaxincomesalaried_user <= topUSD:
                        print("Your gross annual income is more than that of the top 75% of Americans.")
                    else:
                        if pretaxincomesalaried_user > topUSD:
                            print("Your gross annual income is more than that of the top 99% of Americans.")

        salaried_user_income_taxed = tax_income_salary(pretaxincomesalaried_user)
        tax_payment_salaried_user = -1 * (pretaxincomesalaried_user - salaried_user_income_taxed)
        average_tax_salaried_user = (tax_payment_salaried_user / salaried_user_income_taxed) * 100

        print("your income after taxes is", salaried_user_income_taxed)
        print("your average tax rate is", average_tax_salaried_user, "percent")
        print("uncle sam takes", tax_payment_salaried_user, "out of your gross annual income.")
    # wagie inputs
    if income_type in ('by the hour', 'hourly', 'hour', 'per hour', 'h'):
        wage = float(input("what is your hourly wage? "))
        while wage is None:
            try:
                wage = float(input("how large is your paycheck each time your are paid? "))
            except ValueError:
                print("'{}' is not an acceptable value.  Try entering a number or"
                      " an integer, like 7.25 or 69.".format(wage))
        hours_worked = float(input("how many hours do you work per week? "))
        while hours_worked is None:
            try:
                hours_worked = float(input("how many hours do you work per week? "))
            except ValueError:
                print("'{}' is not an acceptable value.  Try entering a number or"
                      " an integer, like 42.069 or 69".format(hours_worked))
        weeks_worked = float(input("how many weeks do you work per year? "))
        while weeks_worked is None:
            try:
                weeks_worked = float(input("how many weeks do you work per year? "))
            except ValueError:
                print("'{}' is not an acceptable value.  Try entering a number or"
                      " an integer, like 40.5 or 52.".format(weeks_worked))
        pretaxincomewagie = weeks_worked * hours_worked * wage
        print()
        print("Your gross annual income: ", pretaxincomewagie)
        if pretaxincomewagie <= bottom25USD:
            print("Your gross annual income is less than that of the top 75% of Americans.")
        else:
            if pretaxincomewagie <= mid50USD:
                print("Your gross annual income is less than that of the top 50% of Americans.")
            else:
                if pretaxincomewagie <= top25USD:
                    print("Your gross annual income is more than that of the bottom 50% of Americans.")
                else:
                    if pretaxincomewagie <= topUSD:
                        print("Your gross annual income is more than that of the top 75% of Americans.")
                    else:
                        if pretaxincomewagie > topUSD:
                            print("Your gross annual income is more than that of the top 99% of Americans.")

        wagie_income_taxed = tax_income_salary(pretaxincomewagie)
        tax_payment_wagie = (pretaxincomewagie - wagie_income_taxed)
        average_tax_wagie = (tax_payment_wagie / pretaxincomewagie) * 100

        print("your income after taxes is", wagie_income_taxed)
        print("your average tax rate is", average_tax_wagie, "percent")
        print("uncle sam takes", tax_payment_wagie, "out of your gross annual income.")
