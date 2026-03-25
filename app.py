# To install Streamlit, run in your shell:
# pip install streamlit

import streamlit as st

st.title("Loan Amortization AI Agent")

def monthly_payment(principal, monthly_rate, months):
    if months == 0:
        return 0.0
    if monthly_rate > 0:
        return principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return principal / months

def amortization_schedule(principal, monthly_rate, months, payment):
    schedule = []
    balance = principal
    for m in range(1, months + 1):
        interest = round(balance * monthly_rate, 10)
        principal_paid = payment - interest
        if principal_paid > balance:
            principal_paid = balance
            payment = interest + principal_paid
        balance = round(balance - principal_paid, 10)
        if balance < 1e-8:
            balance = 0.0
        schedule.append({
            "Month": m,
            "Payment": payment,
            "Principal": principal_paid,
            "Interest": interest,
            "Balance": balance,
        })
        if balance <= 0:
            break
    return schedule

P = st.number_input("Loan Amount ($)", min_value=0.0, value=10000.0, step=100.0)
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1)
years = st.number_input("Loan Term (years)", min_value=1, value=5, step=1)

r = (annual_rate / 100) / 12
n = int(years * 12)

if st.button("Calculate"):
    if P <= 0 or n <= 0:
        st.error("Please enter a positive loan amount and term.")
    else:
        M = monthly_payment(P, r, n)
        total_payment = M * n
        total_interest = total_payment - P

        st.metric("Monthly Payment", f"${M:,.2f}")
        st.metric("Total Payment", f"${total_payment:,.2f}")
        st.metric("Total Interest", f"${total_interest:,.2f}")

        st.subheader("Amortization Schedule")
        schedule = amortization_schedule(P, r, n, M)
        st.write("Showing the first 12 rows and last 12 rows:")
        if len(schedule) > 24:
            st.dataframe(schedule[:12])
            st.write("...")
            st.dataframe(schedule[-12:])
        else:
            st.dataframe(schedule)

        st.download_button(
            label="Download Full Schedule as CSV",
            data="Month,Payment,Principal,Interest,Balance\n" + "\n".join(
                f"{row['Month']},{row['Payment']:.2f},{row['Principal']:.2f},{row['Interest']:.2f},{row['Balance']:.2f}" for row in schedule
            ),
            file_name="amortization_schedule.csv",
            mime="text/csv",
        )

st.write("\n")
st.caption("This simple agent calculates monthly payments and amortization schedule from loan params.")