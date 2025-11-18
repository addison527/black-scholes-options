# **Project Plan**

* **Addison** – Project Coordinator
* **Will** – Greeks Calculations
* **Amanda** – Greeks Calculations
* **Adam** – Graphing & Visualizations
* **Dylan** – Graphing & Visualizations
* **Jason** – Data Loading

---

# **Black-Scholes Option Pricing Function**

Implement the core `black_scholes_price()` function and validate correctness.

### **Deliverables**

* `black_scholes_price()` implemented
* Fully documented docstring (parameters + formula)
* Tested with sample inputs
* Example notebook: `notebooks/bs_pricing_examples.ipynb`

### **Checklist**

* [x] Function `black_scholes_price()` created
* [ ] Tested with sample inputs
* [ ] Docstring added
* [ ] Notebook with example output created

---

# **Market Data Loading Module**

**Jason:** Fetch sample option-related data using `yfinance` (or similar API) and prepare a clean dataset.

### **Deliverables**

* Script/module to load and clean stock + option inputs
* Data saved under `/data/`
* Returns `pandas.DataFrame`

### **Checklist**

* [ ] Fetch test data (`yfinance` or alternative)
* [ ] Retrieve: stock price, expiration, strike, risk-free rate
* [ ] Clean & format dataset
* [ ] Save dataset to `/data/`
* [ ] Confirm returned type is DataFrame

---

# **Greeks Calculation Module**

**Will & Amanda:** Implement analytic Greek formulas and validate outputs.

### **Deliverables**

* `greeks.py` module
* Functions for: Delta, Gamma, Vega, Theta, Rho
* Matching inputs to Black-Scholes pricing function
* Notebook showing Greek sensitivity plots

### **Checklist**

* [ ] `greeks.py` created
* [ ] Delta implemented
* [ ] Gamma implemented
* [ ] Vega implemented
* [ ] Theta implemented
* [ ] Rho implemented
* [ ] Tested with sample inputs
* [ ] Notebook with Greek visualizations created

---

# **Visualization Notebooks**

**Adam & Dylan:** Build visual interpretation tools for price + Greeks sensitivity.

### **Deliverables**

New notebook: `notebooks/option_visualizations.ipynb`
Plots must visualize the impact of changing different variables.

### **Required Plots**

* Price vs Volatility
* Price vs Strike
* Price vs Time to Expiration
* Greeks Curves (Δ Γ ν Θ ρ)

### **Checklist**

* [ ] Notebook created
* [ ] Uses outputs from Black-Scholes + Greeks
* [ ] ≥ 3 clear visualizations
* [ ] Markdown explanations included

---

# **Documentation & Theory Pages**

**Addison:** Document theory, setup instructions.

**Amanda, Will, Jason, Adam, Dylan:** Document 1-2 paragraphs on overleaf about their contributions and findings

### **Deliverables**

* Expanded `README.md`
* New theory document: `docs/black_scholes_theory.md`
* Contribution guide (branch naming, PR process, workflow)

### **Checklist**

* [ ] README updated
* [ ] Theory document created
* [ ] Contribution guide section added
* [ ] Math notation + formatting cleaned

---

# **Final Integration**

**Addison:** Ensure all modules work together properly.

### **Deliverables**

* `main.py` wiring everything together
* Load data → compute prices → compute Greeks → display results
* Confirm no import/path issues
* Team review

### **Checklist**

* [ ] `main.py` loads stock data
* [ ] Computes option prices
* [ ] Computes Greeks
* [ ] Outputs results or simple plots
* [ ] No import errors
* [ ] Team review completed