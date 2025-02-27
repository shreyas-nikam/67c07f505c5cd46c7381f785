```
# QuLab - Portfolio Stress Tester

## Description

The **QuLab - Portfolio Stress Tester** is a Streamlit application designed to demonstrate the impact of various stress scenarios on an investment portfolio. This tool is invaluable for risk management education, allowing users to visualize potential portfolio losses under extreme but plausible market conditions.

**Key Features:**

*   **Interactive Portfolio Definition:** Easily input your portfolio by specifying asset names and their respective weights.
*   **Diverse Stress Scenarios:** Choose from predefined scenarios like "Market Crash," "Interest Rate Hike," "Sector Downturn," or create a "Custom Scenario" tailored to your specific needs.
*   **Real-time Simulation:** Observe immediate changes in your portfolio's value as you adjust scenario parameters through interactive sliders and inputs.
*   **Dynamic Visualizations:** Explore interactive charts that clearly illustrate the changes in portfolio value and asset breakdown under stress.
*   **Key Performance Metrics:** Get a quick overview of the stress test results with metrics like initial portfolio value, final portfolio value, and the percentage portfolio drop.

This application serves as an educational tool to understand the importance of stress testing in identifying portfolio vulnerabilities and making informed risk management decisions.

## Installation

To run the Portfolio Stress Tester application, you need to have Python installed on your system. It is recommended to use Python 3.8 or higher. Follow these steps to install and set up the application:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [repository-url] # Replace [repository-url] with the actual repository URL if available.
    cd [repository-directory] # Navigate into the cloned directory.
    ```

2.  **Install Python packages:**
    If you downloaded the Python script directly (without cloning a repository), ensure you have the required Python libraries installed. Use pip to install them by running the following command in your terminal or command prompt:

    ```bash
    pip install streamlit pandas numpy matplotlib altair
    ```
    This command will install Streamlit, pandas for data manipulation, numpy for numerical operations, matplotlib for basic plotting (though not directly used in the final app, it might be a dependency), and altair for interactive charts.

## Usage

1.  **Run the Streamlit application:**
    Navigate to the directory containing the Python script (`portfolio_stress_tester.py` - ensure you save the provided Python code as this file) in your terminal and run the following command:

    ```bash
    streamlit run portfolio_stress_tester.py
    ```

2.  **Access the application in your browser:**
    Streamlit will automatically open the application in your default web browser. If it doesn't, you can manually open your browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3.  **Configure Your Portfolio (Sidebar):**
    *   **Number of Assets:** In the sidebar on the left, use the number input to specify the number of assets in your portfolio.
    *   **Asset Names and Weights:** For each asset, enter a name and its corresponding weight. Ensure that the weights sum up to 1. If the weights do not sum to 1, the application will automatically normalize them and display a warning.
    *   **View Portfolio:** The "Current Portfolio" section will display a table showing your configured assets and their weights.

4.  **Define Stress Scenario (Sidebar):**
    *   **Choose Stress Scenario:** Select a scenario type from the "Choose Stress Scenario" dropdown:
        *   **Market Crash:** Simulate a percentage drop across all assets. Use the slider to adjust the "Market Drop Percentage."
        *   **Interest Rate Hike:** Simulate the impact of an interest rate hike on rate-sensitive assets. The application assumes "Asset B" is rate-sensitive by default. Adjust the "Impact on Rate-Sensitive Assets" slider.
        *   **Sector Downturn:** Simulate a downturn in a specific sector represented by one of your assets. Select the "Sector Asset" from the dropdown and adjust the "Sector Downturn Impact" slider.
        *   **Custom Scenario:** Define a custom percentage impact for each asset individually using sliders provided for each asset.
    *   Read the descriptive text under each scenario type for guidance on the simulation.

5.  **View Stress Test Results (Main Page):**
    *   **Portfolio Value Over Time Under Stress:**  A line chart displays how your portfolio value changes over 20 periods under the selected stress scenario. Observe the potential drawdown and recovery.
    *   **Asset Value Breakdown - End of Simulation:** A bar chart shows the final values of each asset after the stress test, highlighting which assets were most affected.
    *   **Key Stress Test Metrics:**  View the "Initial Portfolio Value," "Final Portfolio Value," and "Portfolio Drop" percentage to quickly understand the overall impact of the stress scenario on your portfolio.

6.  **Experiment and Learn:**
    Adjust portfolio configurations and stress scenario parameters to observe how different factors influence your portfolio's performance under stress. This interactive tool is designed to enhance your understanding of portfolio risk management.

## Credits

This application is developed by **QuantUniversity** as part of the QuCreate Streamlit Lab.

[![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)](https://www.quantuniversity.com)

For more information about QuantUniversity and our educational resources, please visit [www.quantuniversity.com](https://www.quantuniversity.com).

## License

**Copyright © 2025 QuantUniversity. All Rights Reserved.**

This demonstration is provided for educational purposes only. Any reproduction or commercial use of this application without prior written consent from QuantUniversity is prohibited. For full legal documentation and licensing inquiries, please contact QuantUniversity through our website.
```