import streamlit as st
import numpy as np
from scipy.stats import norm
from utilities.utilities import validate_inputs, convert_to_floats

st.set_page_config(page_title="Black-Scholes Model", page_icon="📈")

st.markdown("# Black-Scholes Model")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates how different parameters will affect the options price calculated by the Black-Scholes formula"""
)

S = st.text_input("Input current stock price (S)")
K = st.text_input("Input strike price (K)")
sigma = st.text_input("Input volatility (sigma)")
T = st.text_input("Input time to expiration (T)")
r = st.text_input("Input risk free rate")

d1 = lambda S, K, sigma, r, T : (np.log(S/K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
d2 = lambda S, K, sigma, r, T : (np.log(S/K) + (r - (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))

def calculate_call_price(S, K, sigma, r, T):
    curr_d1 = d1(S, K, sigma, r, T)
    curr_d2 = d2(S, K, sigma, r, T)
    call_price = S * norm.cdf(curr_d1) - K * np.exp(-r * T) * norm.cdf(curr_d2)
    return call_price

if validate_inputs(S, K, sigma, r, T):
    S, K, sigma, r, T = convert_to_floats(S, K, sigma, r, T)
    st.write(f"Black-Scholes call price is: {calculate_call_price(S, K, sigma, r, T)}")
