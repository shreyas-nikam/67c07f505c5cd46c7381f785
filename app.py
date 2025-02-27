import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(page_title="QuCreate Streamlit Lab - Portfolio Stress Tester", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab - Portfolio Stress Tester")
st.divider()

# Introduction and Explanation
st.write("""
    ## Portfolio Stress Tester

    This application allows you to simulate the impact of various stress scenarios on a hypothetical investment portfolio. 
    Stress testing is a critical risk management tool, especially for understanding potential extreme losses beyond typical risk measures like Value at Risk (VaR). 
    This tool is designed to be interactive and educational, helping you visualize how different market conditions can affect your portfolio.

    **Key Features:**
    - **Portfolio Input:** Define your portfolio by specifying assets and their weights.
    - **Scenario Definition:** Choose from predefined stress scenarios or customize your own.
    - **Real-time Simulation:** See immediate changes in your portfolio's performance as you adjust scenario parameters.
    - **Interactive Visualizations:** Explore dynamic charts that illustrate portfolio value changes under stress.

    **Learn More:** Stress testing is essential because it helps in:
    - Identifying vulnerabilities in your portfolio that might not be apparent under normal market conditions.
    - Understanding potential losses in extreme but plausible scenarios.
    - Making informed decisions about risk management and portfolio adjustments.

    Let's get started by defining your portfolio and exploring different stress scenarios in the sidebar!
""")

st.divider()

# Sidebar for Portfolio Input and Scenario Definition
with st.sidebar:
    st.header("Portfolio Configuration")
    st.write("Enter your portfolio assets and their weights. Weights should sum to 1.")

    asset_names = []
    asset_weights = []
    num_assets = st.number_input("Number of Assets in Portfolio", min_value=1, value=3, step=1)

    for i in range(num_assets):
        col1, col2 = st.columns(2)
        with col1:
            asset_name = st.text_input(f"Asset {i+1} Name", value=f"Asset {chr(65+i)}")
            asset_names.append(asset_name)
        with col2:
            weight = st.number_input(f"Weight for Asset {i+1}", min_value=0.0, max_value=1.0, value=1.0/num_assets, step=0.05, format="%.2f")
            asset_weights.append(weight)

    # Normalize weights if they don't sum to 1
    total_weight = sum(asset_weights)
    if total_weight != 1.0:
        normalized_weights = [w / total_weight for w in asset_weights]
        st.warning(f"Weights were normalized to sum to 1. Original total weight: {total_weight:.2f}")
        asset_weights = normalized_weights

    portfolio_df = pd.DataFrame({'Asset': asset_names, 'Weight': asset_weights})
    st.write("Current Portfolio:")
    st.dataframe(portfolio_df, hide_index=True)

    st.divider()
    st.header("Stress Scenario Definition")
    scenario_type = st.selectbox("Choose Stress Scenario",
                                 ["Market Crash", "Interest Rate Hike", "Sector Downturn", "Custom Scenario"])

    scenario_params = {}
    if scenario_type == "Market Crash":
        scenario_params['market_drop'] = st.slider("Market Drop Percentage", min_value=5, max_value=50, value=20, step=5, format="%d%%") / 100.0
        st.write(f"Simulating a {scenario_params['market_drop']*100:.0f}% drop across all assets.")
    elif scenario_type == "Interest Rate Hike":
        scenario_params['rate_hike_impact'] = st.slider("Impact on Rate-Sensitive Assets", min_value=-30, max_value=10, value=-15, step=5, format="%d%%") / 100.0
        st.write(f"Rate-sensitive assets are expected to decrease by {scenario_params['rate_hike_impact']*100:.0f}%.")
    elif scenario_type == "Sector Downturn":
        sector_asset_index = st.selectbox("Select Sector Asset", options=asset_names, index=0)
        scenario_params['sector_asset'] = sector_asset_index
        scenario_params['sector_drop'] = st.slider(f"Sector Downturn Impact on {sector_asset_index}", min_value=10, max_value=70, value=40, step=5, format="%d%%") / 100.0
        st.write(f"Simulating a {scenario_params['sector_drop']*100:.0f}% drop in {sector_asset_index}.")
    elif scenario_type == "Custom Scenario":
        custom_asset_impacts = {}
        st.write("Define custom percentage impact for each asset:")
        for i, asset in enumerate(asset_names):
            impact = st.slider(f"Impact on {asset}", min_value=-50, max_value=50, value=0, step=5, format="%d%%", key=f"custom_impact_{i}") / 100.0
            custom_asset_impacts[asset] = impact
        scenario_params['custom_impacts'] = custom_asset_impacts
        st.write("Custom scenario impacts are set for each asset.")


# Main Page - Scenario Simulation and Visualizations
st.header("Portfolio Stress Test Results")

# Simulation Logic
initial_portfolio_value = 10000  # Initial portfolio value for simulation
num_periods = 20
periods = range(1, num_periods + 1)
portfolio_values = [initial_portfolio_value]

asset_initial_values = {name: initial_portfolio_value * weight for name, weight in zip(asset_names, asset_weights)}

asset_value_data = {name: [asset_initial_values[name]] for name in asset_names}


for period in periods[1:]:
    current_portfolio_value = portfolio_values[-1]
    period_asset_values = {}
    for asset_name in asset_names:
        asset_value = asset_value_data[asset_name][-1]
        asset_return = 0 # Base case - no change

        if scenario_type == "Market Crash":
            asset_return = -scenario_params['market_drop']
        elif scenario_type == "Interest Rate Hike":
            if "Asset B" in asset_name: # Example rate-sensitive asset
                asset_return = scenario_params['rate_hike_impact']
        elif scenario_type == "Sector Downturn":
            if asset_name == scenario_params['sector_asset']:
                asset_return = -scenario_params['sector_drop']
        elif scenario_type == "Custom Scenario":
            asset_return = scenario_params['custom_impacts'].get(asset_name, 0) # Get custom impact, default 0


        new_asset_value = asset_value * (1 + asset_return)
        asset_value_data[asset_name].append(new_asset_value)
        period_asset_values[asset_name] = new_asset_value


    current_portfolio_value = sum(period_asset_values.values())
    portfolio_values.append(current_portfolio_value)


# --- Visualizations ---

# Portfolio Value Line Chart
st.subheader("Portfolio Value Over Time Under Stress")
st.write("This chart shows how your portfolio value changes over time under the selected stress scenario.")

chart_data = pd.DataFrame({'Period': periods, 'Portfolio Value': portfolio_values})
line_chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Period:O', title='Period'),
    y=alt.Y('Portfolio Value:Q', title='Portfolio Value'),
    tooltip=['Period', 'Portfolio Value']
).properties(
    title=f'Portfolio Performance - {scenario_type} Scenario'
)
st.altair_chart(line_chart, use_container_width=True)
st.write("The line chart visually represents the trajectory of your portfolio's value under the simulated stress. Observe the potential drawdown and recovery (if any) over the periods.")


# Asset Value Breakdown Bar Chart (Last Period)
st.subheader("Asset Value Breakdown - End of Simulation")
st.write("This bar chart displays the final values of each asset in your portfolio after the stress scenario.")

final_asset_values_df = pd.DataFrame({
    'Asset': asset_names,
    'Final Value': [asset_value_data[name][-1] for name in asset_names]
})

bar_chart = alt.Chart(final_asset_values_df).mark_bar().encode(
    x=alt.X('Asset:N', title='Asset'),
    y=alt.Y('Final Value:Q', title='Final Value'),
    tooltip=['Asset', 'Final Value']
).properties(
    title='Final Asset Values after Stress Test'
)
st.altair_chart(bar_chart, use_container_width=True)
st.write("This bar chart provides a snapshot of how each asset contributed to the final portfolio value after the stress event. It helps identify which assets are most affected by the scenario.")


# Key Metrics Display
st.subheader("Key Stress Test Metrics")
initial_value = portfolio_values[0]
final_value = portfolio_values[-1]
portfolio_drop = ((final_value - initial_value) / initial_value) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Initial Portfolio Value", f"${initial_value:,.2f}")
col2.metric("Final Portfolio Value", f"${final_value:,.2f}")
col3.metric("Portfolio Drop", f"{portfolio_drop:.2f}%")
st.write("These metrics summarize the overall impact of the stress scenario on your portfolio, showing the initial and final values and the percentage drop in value.")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
