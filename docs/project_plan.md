Addison - pc
Will - greeks 
Adam - 
Dylan - 
Jason - data loading

- Assign roles

Checklist:

 Function black_scholes_price() created

 Tested with sample inputs

 Docstring explaining parameters and formula

 Notebook (bs_pricing_examples.ipynb) showing example output

Fetch test data using yfinance or similar API.

Retrieve stock price, expiry dates, strike prices, and risk-free rate proxy.

Save sample dataset in /data/ folder.

Return clean pandas.DataFrame.

Implement analytic formulas for Delta, Gamma, Vega, Theta, Rho.

Each function accepts the same inputs as Black-Scholes.

Validate using known formulas and sample results.

 greeks.py created

 Delta, Gamma, Vega, Theta, Rho implemented

 Tested with sample inputs

 Notebook visualization for Greek sensitivities

Create notebooks/option_visualizations.ipynb.
Generate graphs showing:
Price vs Volatility
Price vs Strike
Price vs Time to Expiration
Greeks curves

Add markdown cells interpreting the plots.
Notebook added

 Uses outputs from Black-Scholes + Greeks

 At least 3 clean visualizations with explanations


Expand README to include:

Project motivation and background

Overview of Black-Scholes theory (with equations)

Setup instructions (pip install -r requirements.txt)

Contribution guide (branch naming, PR process)

Add a new file docs/black_scholes_theory.md summarizing the model derivation.


 README updated

 Model theory document created

 Contribution guide section added

 Formatting and math notation clear


7. Assignee: Addison (Coordinator)

Description:

Combine all modules to test full pipeline:

Load stock data

Compute option prices

Print results or simple plots

Ensure all imports and dependencies work together.

Checklist:

 main.py connects data + model

 Output verified

 No import errors or path issues

 Team review completed