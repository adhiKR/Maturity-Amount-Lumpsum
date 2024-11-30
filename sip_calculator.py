import streamlit as st 

def compound_interest(principal, annual_rate, compounding_frequency, years):
    """
    Calculate the maturity amount for compound interest.

    :param principal: The initial investment or principal amount.
    :param annual_rate: The annual interest rate (in percentage).
    :param compounding_frequency: The number of times interest is compounded per year.
    :param years: The investment period in years.
    :return: Maturity amount of the investment.
    """
    # Convert annual rate to a decimal
    rate = annual_rate / 100
    # Calculate the maturity amount
    maturity_amount = principal * ((1 + rate / compounding_frequency) ** (compounding_frequency * years))
    return maturity_amount

# Streamlit app
st.title("Maturity Amount Calculator (Lumpsum)")
st.write("Know how much returns your investments will make for you over a given period of time on a given rate of interest using compounding")

# Input fields for the user
principal = st.number_input("Principal Amount (₹):", min_value=0.0, value=10000.0, step=100.0)
annual_rate = st.number_input("Annual Interest Rate (%):", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
compounding_frequency = st.selectbox("Compounding Frequency:", options=[1, 2, 4, 12], format_func=lambda x: f"{x} times/year")
years = st.slider("Investment Tenure (Years):", min_value=1, max_value=50, value=10)

# Button to calculate compound interest maturity amount
if st.button("Calculate"):
    # Calculate results
    maturity_amount = compound_interest(principal, annual_rate, compounding_frequency, years)
    total_investment = principal
    total_interest = maturity_amount - total_investment

    # Display results
    st.success(f"Maturity Amount: ₹{maturity_amount:,.2f}")
    st.info(f"Total Investment: ₹{total_investment:,.2f}")
    st.success(f"Total Interest Earned: ₹{total_interest:,.2f}")

