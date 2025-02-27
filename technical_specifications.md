# Technical Specification for Portfolio Stress Tester

## Objective
The primary purpose of the Portfolio Stress Tester application is to provide users with an intuitive and interactive platform to simulate and analyze the impact of various stress scenarios on investment portfolios. This application encapsulates key learnings from risk management, particularly emphasizing stress testing as a critical tool beyond Value at Risk (VaR). It aligns with the recommendations from the Basel Committee on Banking Supervision, focusing on identifying potential future extreme adverse outcomes.

## Features
- **Portfolio Input**:
  - **Asset Entry**: Users can input their portfolio holdings, including asset names and corresponding weights.
  - **Scenario Definition**: Allow users to define stress scenarios such as market crashes, interest rate hikes, and sector-specific downturns via user input fields.
- **Scenario Simulation**:
  - **Return Modeling**: Simulate portfolio returns under specified scenarios to display potential losses.
  - **Real-Time Calculation**: Provide immediate calculations of portfolio performance changes based on user-defined scenarios.
- **Interactive Visualizations**:
  - **Dynamic Charts**: Use line charts, bar graphs, and scatter plots to showcase portfolio value changes under different scenarios.
  - **Annotations & Tooltips**: Enhance visualizations with insights and explanations directly on the charts for better data interpretation.
- **User Guidance**:
  - **Inline Help**: Offer built-in help features and tooltips to guide users through the application, ensuring ease of use.
  - **Parameter Widgets**: Interactive widgets for users to adjust parameters and observe real-time visualization updates.

## User Interface
- **Streamlit Components**:
  - **Sidebar**: Contains input forms for portfolio data and stress scenario settings.
  - **Main Page**: Displays visualizations and calculated results.
- **Interaction Flow**:
  1. Users enter portfolio details in the sidebar.
  2. Define and adjust stress scenario parameters using dropdowns and sliders.
  3. View updated visualizations on the main page, reflecting real-time changes based on inputs.

## Data Management
- **Inputs**:
  - User-defined portfolio data and stress scenarios.
- **Outputs**:
  - Visualizations of portfolio performance under different scenarios.
- **Data Sources**:
  - Synthetic datasets to demonstrate data handling and visualizations.
  - No external API interactions; all data manipulation is performed within the application using uploaded or synthetic data.

## Libraries and Tools
- **Streamlit**: For building the interactive web application interface.
  - Provides an easy-to-use framework for creating interactive applications.
- **Pandas**: For data manipulation and preprocessing.
  - Necessary for handling and organizing input data.
- **NumPy**: Used for numerical computations and portfolio simulation calculations.
- **Matplotlib/Seaborn**: For creating static visualizations.
  - Useful for crafting detailed and customizable plots.
- **Altair**: For dynamic and interactive visualizations.
  - Offers lightweight and interactive charting options suitable for real-time updates.

## Learnings and References

### Related Learnings
- **Risk Management**: The application reflects risk management principles, emphasizing the importance of stress testing in assessing portfolio vulnerability.
- **Financial Theory**: Expands on traditional methods like VaR, highlighting the limitations and the need for stress testing.
- **Data Visualization**: Demonstrates how raw data can be transformed into meaningful insights via interactive visualizations.

### References
- Basel Committee on Banking Supervision publications on stress testing.
- Risk Management textbooks and articles focused on complementing VaR with stress testing.
- Documentation and tutorials from Streamlit, Pandas, NumPy, Matplotlib, Seaborn, and Altair for technical guidance.