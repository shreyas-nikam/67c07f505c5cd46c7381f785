```
# Project Title: QuLab - Portfolio Stress Tester

## Description

QuLab - Portfolio Stress Tester is a Streamlit application designed to simulate the impact of various stress scenarios on investment portfolios. This interactive tool is intended for educational purposes, allowing users to understand and visualize how different market conditions can affect their portfolio's value. By defining a portfolio and selecting from predefined or custom stress scenarios, users can observe real-time simulations and dynamic visualizations of portfolio performance under duress.

**Key Features:**

*   **Portfolio Input:** Users can easily define their portfolio by specifying asset names and their corresponding weights.
*   **Scenario Definition:** Choose from a selection of predefined stress scenarios such as "Market Crash," "Interest Rate Hike," "Sector Downturn," or create a "Custom Scenario" to tailor the stress test.
*   **Real-time Simulation:** The application instantly updates visualizations and metrics as scenario parameters are adjusted, providing immediate feedback on the portfolio's response to stress.
*   **Interactive Visualizations:** Dynamic charts are generated to illustrate portfolio value changes over time and asset value breakdowns at the end of the simulation, enhancing understanding of the stress test results.
*   **Key Metrics:** Displays crucial metrics like initial and final portfolio values, and the percentage drop experienced under the stress scenario.

This tool is valuable for:

*   Identifying potential vulnerabilities in a portfolio that may not be apparent under normal market conditions.
*   Understanding the magnitude of potential losses in extreme but plausible scenarios.
*   Supporting informed decision-making in risk management and portfolio adjustments.

## Installation

To run the QuLab - Portfolio Stress Tester, you need to have Python installed on your system along with pip, the Python package installer.  It is recommended to use Python 3.8 or higher.

**1. Install Python:**

If you don't have Python installed, download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

**2. Install Streamlit and other required libraries:**

Open your terminal or command prompt and install the necessary Python libraries using pip:

```bash
pip install streamlit pandas numpy matplotlib altair
```

This command will install:

*   **streamlit:** The framework for building and sharing data applications.
*   **pandas:** For data manipulation and analysis.
*   **numpy:** For numerical computations.
*   **matplotlib:** For creating static, interactive, and animated visualizations in Python (although altair is primarily used in this app, matplotlib might be a dependency).
*   **altair:** For declarative statistical visualization library for Python.

**3. Save the application code:**

Save the provided Python code as a `.py` file, for example, `portfolio_stress_tester.py`. Ensure this file is in your desired project directory.

## Usage

**1. Run the Streamlit application:**

Navigate to the directory where you saved the `portfolio_stress_tester.py` file in your terminal or command prompt.  Run the application using the following command:

```bash
streamlit run portfolio_stress_tester.py
```

Streamlit will launch the application in your default web browser.

**2. Interact with the application:**

Once the application is running in your browser, you can interact with it through the sidebar and the main panel:

**Sidebar - Portfolio Configuration:**

*   **Number of Assets in Portfolio:**  Use the number input to specify how many assets are in your portfolio.
*   **Asset Name and Weight:** For each asset, enter its name and weight. Weights should be decimal values between 0 and 1, and ideally, the sum of all weights should be 1.  If the weights do not sum to 1, the application will normalize them and display a warning.
*   **Current Portfolio:** A table displays your configured portfolio with asset names and weights.

**Sidebar - Stress Scenario Definition:**

*   **Choose Stress Scenario:** Select a predefined scenario from the dropdown menu:
    *   **Market Crash:** Simulate a percentage drop across all assets. Adjust the "Market Drop Percentage" slider.
    *   **Interest Rate Hike:** Simulate the impact of an interest rate hike on rate-sensitive assets (in this example, "Asset B" is considered rate-sensitive). Adjust the "Impact on Rate-Sensitive Assets" slider.
    *   **Sector Downturn:** Simulate a downturn in a specific sector. Select an asset from the "Select Sector Asset" dropdown and adjust the "Sector Downturn Impact" slider.
    *   **Custom Scenario:** Define a custom percentage impact for each asset individually using sliders.

**Main Panel - Portfolio Stress Test Results:**

*   **Portfolio Stress Test Results:** The main panel displays the results of the stress test based on your configurations.
*   **Portfolio Value Over Time Under Stress:** A line chart visualizes how your portfolio value changes over 20 periods under the selected stress scenario.
*   **Asset Value Breakdown - End of Simulation:** A bar chart shows the final values of each asset after the simulation, illustrating their contribution to the portfolio's final value.
*   **Key Stress Test Metrics:** Displays the "Initial Portfolio Value," "Final Portfolio Value," and "Portfolio Drop" as key metrics summarizing the stress test outcome.

Explore different portfolio configurations and stress scenarios in the sidebar to observe their impact on the portfolio visualizations and metrics in real-time.

## Credits

This application is developed by **QuantUniversity** as part of the QuCreate Streamlit Lab initiative for educational purposes.

For more information about QuantUniversity and our educational resources, please visit: [https://www.quantuniversity.com](https://www.quantuniversity.com)

## License

© 2025 QuantUniversity. All Rights Reserved.

This demonstration is solely for educational use and illustration. For full legal documentation, please visit the provided link within the application (if available) or contact QuantUniversity directly. Reproduction of this demonstration requires prior written consent from QuantUniversity.
```