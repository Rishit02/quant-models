# Options Greeks and Black-Scholes Model Calculator

This interactive Streamlit web app allows users to input parameters related to European options and calculate the option Greeks (Delta, Gamma, Vega, Theta, Rho) as well as the Black-Scholes call price. It also includes a visualization tool for parameter sensitivity analysis to better understand option price behavior.

## Features

- Calculate **Greeks** for European call or put options based on the Black-Scholes model
- Compute the **Black-Scholes theoretical call price** for given input parameters
- Visualize how option price changes when varying a single parameter (Underlying price, Strike price, or Volatility)
- Input validation to ensure numerical correctness
- Clear display of results using Streamlit's UI components

## Technologies Used

- Python
- Streamlit for web UI and interactivity
- NumPy and SciPy for numerical computations
- Matplotlib for plotting sensitivity graphs

## How to Use

1. **Option Greeks Calculation**

   - Enter values for:
     - Current price of the underlying asset (S)
     - Strike price (K)
     - Time to expiration in years (T)
     - Risk-free interest rate (r)
     - Volatility (sigma)
   - Select option type (`call` or `put`)
   - The app instantly displays the Greeks: Delta, Gamma, Vega, Theta, and Rho

2. **Black-Scholes Price Calculation**

   - Input parameters:
     - Stock price (S)
     - Strike price (K)
     - Volatility (sigma)
     - Time to expiration (T)
     - Risk-free interest rate (r)
   - The app calculates and displays the Black-Scholes theoretical call price

3. **Parameter Sensitivity Analysis**
   - Select which parameter to vary (S, K, or sigma)
   - Input range start, end, and step values
   - The app plots how the call price changes with that parameter, helping visualize risk sensitivities

## Installation and Running

Using a virtual environment is recommended

```bash
git clone <repo-url>
cd <repo-directory>
pip install -r requirements.txt
streamlit run app.py
```

Or use the deployed app on the link [here](https://rishit02-quant-models-welcome-n5s179.streamlit.app/~/+/)

## Additional Notes

- The calculation assumes European options with standard Black-Scholes assumptions (no dividends, constant volatility, frictionless markets).
- Greeks are calculated per day for Theta and per 1% change for Vega and Rho, following common market conventions.
- Input validation prevents errors from invalid or edge-case inputs such as zero time to expiration or zero volatility.
