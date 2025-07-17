import streamlit as st
import numpy as np
from scipy.stats import norm
from utilities.utilities import validate_inputs, convert_to_floats
import matplotlib.pyplot as plt

st.set_page_config(page_title="Black-Scholes Model", page_icon="📈")

st.markdown("# Black-Scholes Model")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates how different parameters will affect the
      options price calculated by the Black-Scholes formula"""
)

S = st.number_input("Input current stock price (S)", key="stock_price")
K = st.number_input("Input strike price (K)", key="strike_price")
sigma = st.number_input("Input volatility (sigma)", key="volatility")
T = st.number_input("Input time to expiration (T)", key="time_to_expiration")
r = st.number_input("Input risk free rate", key="risk_free_rate")

d1 = lambda S, K, sigma, r, T : (np.log(S/K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
d2 = lambda S, K, sigma, r, T : (np.log(S/K) + (r - (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))

def calculate_call_price(S, K, sigma, r, T):
    curr_d1 = d1(S, K, sigma, r, T)
    curr_d2 = d2(S, K, sigma, r, T)
    call_price = S * norm.cdf(curr_d1) - K * np.exp(-r * T) * norm.cdf(curr_d2)
    return call_price

if validate_inputs(S, K, sigma, r, T):
    S, K, sigma, r, T = convert_to_floats(S, K, sigma, r, T)
    st.write(f"Black-Scholes call price is: {calculate_call_price(S, K, sigma, r, T):.5f}")


st.divider()

st.subheader("Parameter sensitivity analysis")

parameter = st.selectbox(
    "What parameter would you like to change?",
    ("S", "sigma", "K"),
    index=None,
)

start_range = st.number_input("Start value", key="start_range")
end_range = st.number_input("End value", key="end_range")
parameter_step = st.number_input("Parameter step", key="parameter_step")

option_prices = None
if validate_inputs(K, sigma, T, r, start_range, end_range, parameter_step) and parameter == "S":
    parameter_range = np.arange(start_range, end_range, parameter_step)
    option_prices = [calculate_call_price(S, K, sigma, r, T) for S in parameter_range]

elif validate_inputs(K, sigma, T, r, start_range, end_range, parameter_step) and parameter == "sigma":
    parameter_range = np.arange(start_range, end_range, parameter_step)
    option_prices = [calculate_call_price(S, K, sigma, r, T) for sigma in parameter_range]
    
elif validate_inputs(K, sigma, T, r, start_range, end_range, parameter_step) and parameter == "K":
    parameter_range = np.arange(start_range, end_range, parameter_step)
    option_prices = [calculate_call_price(S, K, sigma, r, T) for K in parameter_range]

if option_prices:
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(parameter_range, option_prices)
    ax.set_xlabel(f"{parameter}")
    ax.set_ylabel("Call Option Price")
    ax.set_title(f"Call Price Sensitivity to {parameter} (Black-Scholes Model)")
    ax.grid(True)

    st.pyplot(fig)
