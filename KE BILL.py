def variable_charges (monthly_units):
    if monthly_units > 1 and monthly_units < 1:
        v_charges = monthly_units * 9.43
    if monthly_units > 101 and monthly_units < 200:
        v_charges = monthly_units * 17.9566
    if monthly_units > 201 and monthly_units < 300:
        v_charges = monthly_units * 18.84
    if monthly_units > 301 and monthly_units < 400:
        v_charges = monthly_units * 19.76
    return int(v_charges)

def uniform_adj (June_uni_units):
    result = June_uni_units * 0.5715
    return int(result)

def fuel_adj_a(May):
    m = May * 6.8858
    return int(m)

def fuel_adj_b(Jun):
    j = Jun * 3.0114
    return int(j)
    

def ke_charges (c1, c2, c3, c4):
    result = c1 + c2 + c3 + c4
    return result

def duty (ke_charges):
    result = ke_charges * 0.015
    return int(result)

def sales_tax (ke_charges, duty):
    result = (ke_charges + duty) * 0.17
    return int(result)

def govt_charges (a, b):
    result = a + b
    return int(result)
def total_dues (a, b):
    result = a + b
    return int(result)

Aug_user_input = int(input ("enter Units of Aug: "))
Jun_user_input = int(input ("enter Units of Jun: "))
Jun_uni_user_input = int(input ("enter Units of Jun Uni: "))
May_user_input = int(input ("enter Units of May: "))


def main_calc(Aug, June, Jun_uni, May):
    display_a = variable_charges(Aug)
    print ("\nvariable Charges is: ", display_a)
    
    display_b = uniform_adj(Jun_uni_user_input)
    print ("\nuniform Adjustment is: ", display_b)
    
    display_c = fuel_adj_a(May_user_input)
    print ("\nFuel Adj of May-22 is : ", display_c)
    
    display_d = fuel_adj_b(Jun_user_input)
    print ("\nFuel Adj of June-22 is : ", display_d)
    
    display_e = ke_charges(display_a, display_b, display_c, display_d)
    print ("\nTotal KE charges are: ", display_e)
    
    display_f = duty(display_e)
    print ("\nElectricity duty: ", display_f)
    
    display_g = sales_tax(display_e, display_f)
    print ("\nSales tax: ", display_g)

    display_h = govt_charges(display_f, display_g)
    print ("\nTotal Government charges are: ", display_h)
    
    display_e = total_dues(display_e, display_h)
    print ("\nYour Electricity charges for the period: ", display_e)

main_calc(Aug_user_input, Jun_user_input, Jun_uni_user_input, May_user_input)


# In[ ]:
