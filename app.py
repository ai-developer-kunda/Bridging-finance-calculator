import streamlit as st

st.title('Bridging Finance Calculator')

calculation_type = st.radio("Calculation Type", ['Net Loan Amount', 'Gross LTV'])

total_security_value = st.number_input("Total Security Value (£):", min_value=0.0, format='%f')
interest_rate_option = st.selectbox("Interest Rate", ['LendInvest', 'Custom'])
if interest_rate_option == 'LendInvest':
    interest_rate = 0.89
else:
    interest_rate = 1.00 

def calculate_fees(loan_amount):
    arrangement_fee_percentage = 2.0  
    arrangement_fee = loan_amount * (arrangement_fee_percentage / 100)

    title_insurance_fee = 201.60
    general_insurance_fee = 150.00
    fund_transfer_fee = 25.00
    legal_fees = 750.00
    valuation_fees = 380.00

    return arrangement_fee, title_insurance_fee, general_insurance_fee, fund_transfer_fee, legal_fees, valuation_fees

def calculate_interest(loan_amount, rate, period):
    return loan_amount * (rate / 100) * period

def calculate_gross_loan(net_loan, total_interest, fees):
    return net_loan + total_interest + sum(fees)

if calculation_type == 'Net Loan Amount':
    net_loan_amount = st.number_input("Net Loan Amount (£):", min_value=0.0, format='%f')
    retained_interest_period = st.number_input("Retained Interest Period (months):", min_value=0, step=1)

    if st.button('Calculate Net Loan Amount'):
        fees = calculate_fees(net_loan_amount)
        total_interest = calculate_interest(net_loan_amount, interest_rate, retained_interest_period)
        gross_loan = calculate_gross_loan(net_loan_amount, total_interest, fees)

        st.write(f"Gross Loan: £{gross_loan}")
        st.write(f"Gross LTV: {(gross_loan / total_security_value) * 100}%")
        st.write(f"Total Interest: £{total_interest}")
        st.write("Fees:")
        st.write(f"  Arrangement Fee: £{fees[0]}")
        st.write(f"  Title Insurance Fee: £{fees[1]}")
        st.write(f"  General Insurance Fee: £{fees[2]}")
        st.write(f"  Fund Transfer Fee: £{fees[3]}")
        st.write(f"  Legal Fees: £{fees[4]}")
        st.write(f"  Valuation Fees: £{fees[5]}")

elif calculation_type == 'Gross LTV':
    gross_ltv = st.number_input("Gross LTV (%):", min_value=0.0, format='%f')
    retained_interest_period = st.number_input("Retained Interest Period (months):", min_value=0, step=1)
    net_loan_amount = (gross_ltv / 100) * total_security_value

    if st.button('Calculate Gross LTV'):
        fees = calculate_fees(net_loan_amount)
        total_interest = calculate_interest(net_loan_amount, interest_rate, retained_interest_period)
        gross_loan = calculate_gross_loan(net_loan_amount, total_interest, fees)

        st.write(f"Gross Loan: £{gross_loan}")
        st.write(f"Gross LTV: {gross_ltv}%")
        st.write(f"Total Interest: £{total_interest}")
        st.write("Fees:")
        st.write(f"  Arrangement Fee: £{fees[0]}")
        st.write(f"  Title Insurance Fee: £{fees[1]}")
        st.write(f"  General Insurance Fee: £{fees[2]}")
        st.write(f"  Fund Transfer Fee: £{fees[3]}")
        st.write(f"  Legal Fees: £{fees[4]}")
        st.write(f"  Valuation Fees: £{fees[5]}")