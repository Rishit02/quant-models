import streamlit as st
import numpy as np
from scipy.stats import norm
from utilities.utilities import validate_inputs


st.set_page_config(page_title="Options Greeks", page_icon="")
st.sidebar.header("Options Greeks")

st.header("Options Greeks")

def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    """
    Calculates the Greeks for a European option.
    
    Parameters:
    - S: Current price of the underlying asset
    - K: Strike price of the option
    - T: Time to expiration (in years)
    - r: Risk-free interest rate
    - sigma: Volatility of the underlying asset
    - option_type: 'call' or 'put'
    
    Returns:
    A dictionary containing delta, gamma, vega, theta, and rho.
    """
    # Handle edge cases to prevent division by zero or other errors
    if T <= 0 or sigma <= 0:
        # For an expired option or zero volatility, Greeks are trivial or undefined.
        # Returning zeros is a common practical approach.
        return {'delta': 0, 'gamma': 0, 'vega': 0, 'theta': 0, 'rho': 0}

    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Use scipy.stats.norm for N'(x) (pdf) and N(x) (cdf)
    pdf_d1 = norm.pdf(d1)
    cdf_d1 = norm.cdf(d1)
    cdf_d2 = norm.cdf(d2)

    # Gamma and Vega are the same for calls and puts
    gamma = pdf_d1 / (S * sigma * np.sqrt(T))
    vega = S * pdf_d1 * np.sqrt(T) / 100 # Typically quoted as change per 1% vol change

    if option_type == 'call':
        delta = cdf_d1
        theta = (- (S * pdf_d1 * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * cdf_d2) / 365 # Per day
        rho = (K * T * np.exp(-r * T) * cdf_d2) / 100 # Per 1% interest rate change
    elif option_type == 'put':
        delta = cdf_d1 - 1
        theta = (- (S * pdf_d1 * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365 # Per day
        rho = (-K * T * np.exp(-r * T) * norm.cdf(-d2)) / 100 # Per 1% interest rate change
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

    return {
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta,
        'rho': rho
    }


st.write("Input necessary values:")

col1, col2, col3 = st.columns(3)

with col1:
    S = st.number_input("Price of the Underlying Asset (S)")
    K = st.number_input("Strike Price of the Option (K)")
    
with col2:
    T = st.number_input("Time to Expiration (T)")
    sigma = st.number_input("Volatility of the Underlying Asset (sigma)")

with col3:
    r = st.number_input("Risk-Free Interest Rate (r)")
    
if validate_inputs(S, K, T, r, sigma):
    # Calculate the greeks
    greeks = calculate_greeks(S, K, T, r, sigma, option_type='call')

    # Display the Greeks using st.metric for a nice visual
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Delta (Δ)", f"{greeks['delta']:.4f}")
    col2.metric("Gamma (Γ)", f"{greeks['gamma']:.4f}")
    col3.metric("Vega (ν)", f"{greeks['vega']:.4f}")
    col4.metric("Theta (Θ)", f"{greeks['theta']:.4f}")
    col5.metric("Rho (ρ)", f"{greeks['rho']:.4f}")