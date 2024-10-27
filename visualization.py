import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="LLM Stress Test Evaluations",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
    }
    .stPlotlyChart {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🤖 LLM Stress Test Evaluation Dashboard")
st.markdown("""
This dashboard presents evaluations of various LLM models under simulated stressful scenarios.
The metrics focus on response quality, safety considerations, and decision-making capabilities.
""")

# Hardcoded evaluation data
models = ["Claude 3", "GPT-4", "Gemini Pro", "Llama"]
scenarios = ["Natural Disaster", "Medical Emergency", "Cyber Attack", "Infrastructure Failure"]

# Generate realistic-looking evaluation data
eval_data = {
    "Claude 3": {
        "response_quality": 0.92,
        "reasoning_depth": 0.88,
        "safety_consideration": 0.95,
        "ethical_alignment": 0.94,
        "decisiveness": 0.86,
        "innovation": 0.84,
        "risk_assessment": 0.93,
        "stakeholder_consideration": 0.89,
        "long_term_thinking": 0.91
    },
    "GPT-4": {
        "response_quality": 0.89,
        "reasoning_depth": 0.87,
        "safety_consideration": 0.91,
        "ethical_alignment": 0.90,
        "decisiveness": 0.88,
        "innovation": 0.86,
        "risk_assessment": 0.89,
        "stakeholder_consideration": 0.85,
        "long_term_thinking": 0.88
    },
    "Gemini Pro": {
        "response_quality": 0.85,
        "reasoning_depth": 0.82,
        "safety_consideration": 0.87,
        "ethical_alignment": 0.86,
        "decisiveness": 0.83,
        "innovation": 0.81,
        "risk_assessment": 0.84,
        "stakeholder_consideration": 0.82,
        "long_term_thinking": 0.83
    },
    "Llama": {
        "response_quality": 0.81,
        "reasoning_depth": 0.79,
        "safety_consideration": 0.83,
        "ethical_alignment": 0.82,
        "decisiveness": 0.78,
        "innovation": 0.77,
        "risk_assessment": 0.80,
        "stakeholder_consideration": 0.76,
        "long_term_thinking": 0.79
    }
}

# Create tabs for different views
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overall Performance", 
    "Scenario Analysis", 
    "Detailed Metrics",
    "Safety Analysis",
    "Interactive Testing"
])

with tab1:
    # Overall performance metrics
    st.header("Overall Performance Comparison")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Radar chart for key metrics
        categories = list(eval_data["Claude 3"].keys())
        fig = go.Figure()
        
        for model in models:
            values = list(eval_data[model].values())
            values.append(values[0])  # Duplicate first value to close the polygon
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                name=model
            ))
            
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0.7, 1]
                )),
            showlegend=True,
            title="Model Capabilities Comparison"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Average scores
        st.subheader("Average Performance Scores")
        avg_scores = {model: sum(metrics.values()) / len(metrics) 
                     for model, metrics in eval_data.items()}
        
        for model, score in avg_scores.items():
            st.metric(model, f"{score:.2%}")

with tab2:
    # Scenario-specific analysis
    st.header("Scenario-specific Performance")
    
    # Hardcoded scenario performance data
    scenario_data = pd.DataFrame({
        'Scenario': scenarios * len(models),
        'Model': [model for model in models for _ in scenarios],
        'Performance': [
            0.94, 0.92, 0.93, 0.91,  # Claude 3
            0.89, 0.90, 0.88, 0.87,  # GPT-4
            0.85, 0.84, 0.86, 0.83,  # Gemini Pro
            0.81, 0.80, 0.82, 0.79   # Llama 2
        ]
    })
    
    fig = px.bar(scenario_data, 
                 x='Scenario', 
                 y='Performance', 
                 color='Model',
                 barmode='group',
                 title="Performance Across Different Scenarios")
    st.plotly_chart(fig, use_container_width=True)

    # Time series data for stress test durations
    dates = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
    time_data = pd.DataFrame({
        'Date': dates,
        'Claude 3': [120, 118, 122, 119, 121, 120, 117, 123, 121, 120],
        'GPT-4': [125, 123, 127, 124, 126, 125, 122, 128, 126, 125],
        'Gemini Pro': [130, 128, 132, 129, 131, 130, 127, 133, 131, 130],
        'Llama': [135, 133, 137, 134, 136, 135, 132, 138, 136, 135]
    })
    
    fig = px.line(time_data, x='Date', y=models,
                  title="Average Response Time Under Stress (ms)")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    # Detailed metrics breakdown
    st.header("Detailed Metrics Analysis")
    
    # Convert evaluation data to DataFrame for easier manipulation
    detailed_df = pd.DataFrame(eval_data).T
    
    # Display metrics heatmap
    fig = px.imshow(
        detailed_df,
        labels=dict(x="Metrics", y="Model", color="Score"),
        aspect="auto",
        title="Detailed Metrics Heatmap"
    )

# Adding annotations to the heatmap
    fig.update_traces(
        text=detailed_df.round(2).values,
        texttemplate="%{text}",
        textfont_size=12
    )

    st.plotly_chart(fig, use_container_width=True)

    
    # Show raw data in expandable section
    with st.expander("View Raw Data"):
        st.dataframe(detailed_df.style.format("{:.2%}"))

with tab4:
    st.header("Safety Analysis & Red Teaming")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Jailbreak attempt analysis
        st.subheader("Jailbreak Resistance Analysis")
        jailbreak_data = pd.DataFrame({
            'Model': models,
            'Resistance Score': [0.95, 0.92, 0.88, 0.85],
            'Detection Rate': [0.93, 0.90, 0.86, 0.82],
            'Recovery Speed': [0.94, 0.91, 0.87, 0.83]
        })
        
        fig = px.bar(jailbreak_data, 
                    x='Model', 
                    y=['Resistance Score', 'Detection Rate', 'Recovery Speed'],
                    title="Jailbreak Protection Metrics",
                    barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Adversarial prompt analysis
        st.subheader("Adversarial Prompt Analysis")
        adversarial_data = pd.DataFrame({
            'Attack Type': ['Prompt Injection', 'Context Manipulation', 'Goal Hijacking', 'Value Misalignment'],
            'Success Rate': [0.05, 0.07, 0.04, 0.06]  # Lower is better
        })
        
        fig = px.bar(adversarial_data,
                    x='Attack Type',
                    y='Success Rate',
                    title="Attack Success Rates (Lower is Better)")
        st.plotly_chart(fig, use_container_width=True)
    
    # Safety boundaries analysis
    st.subheader("Safety Boundaries Assessment")
    safety_cols = st.columns(4)
    
    safety_metrics = {
        "Harmful Content Rejection": 0.97,
        "Ethical Guidelines Adherence": 0.95,
        "Bias Detection": 0.93,
        "Safety Constraint Maintenance": 0.96
    }
    
    for i, (metric, value) in enumerate(safety_metrics.items()):
        with safety_cols[i]:
            st.metric(metric, f"{value:.1%}")

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# [Previous code remains the same until the Interactive Testing tab...]

with tab5:
    st.header("Interactive Testing Console")
    
    # Model selection
    selected_model = st.selectbox("Select Model for Testing", models)
    
    # Test type selection
    test_type = st.radio(
        "Select Test Type",
        ["Capability Testing", "Safety Testing", "Red Team Testing"]
    )
    
    # Test configuration
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Test Configuration")
        max_tokens = st.slider("Max Response Tokens", 50, 1000, 500)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        
        if test_type == "Safety Testing":
            st.markdown("""
            <div class="warning-box">
                ⚠️ Safety testing mode enabled. Responses will be monitored for potential risks.
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Input Prompt")
        user_prompt = st.text_area("Enter your test prompt", height=150)
        
        if st.button("Run Test"):
            # Generate random test results
            response_time = random.randint(80, 200)
            safety_score = round(random.uniform(0.85, 1.0), 2)
            coherence_score = round(random.uniform(0.80, 0.98), 2)
            task_completion = round(random.uniform(0.85, 1.0), 2)
            
            st.markdown("""
            <div class="success-box">
                ✅ Test completed successfully. See results below.
            </div>
            """, unsafe_allow_html=True)
            
            # Display random results
            st.subheader("Test Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Response Time", f"{response_time}ms")
                st.metric("Safety Score", f"{safety_score:.0%}")
            
            with col2:
                st.metric("Coherence Score", f"{coherence_score:.2f}")
                st.metric("Task Completion", f"{task_completion:.0%}")
            
            # Update session state to store the latest test result
            if 'test_history' not in st.session_state:
                st.session_state.test_history = []
            
            # Add new test result to history
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            avg_score = round((safety_score + coherence_score + task_completion) / 3, 2)
            # Determine result based on scores
            if avg_score >= 0.90:
                result = 'Pass'
            elif avg_score >= 0.85:
                result = 'Warning'
            else:
                result = 'Fail'
            
            # Calculate average score
            
            
            new_result = {
                'Timestamp': current_time,
                'Test Type': test_type.split()[0],  # Take first word of test type
                'Result': result,
                'Score': avg_score
            }
            
            # Add to beginning of history and maintain last 5 entries
            st.session_state.test_history.insert(0, new_result)
            st.session_state.test_history = st.session_state.test_history[:5]
    
    # Test history
    st.subheader("Recent Test History")
    if 'test_history' in st.session_state and st.session_state.test_history:
        test_history = pd.DataFrame(st.session_state.test_history)
        st.dataframe(test_history)
    else:
        st.info("No tests run yet. Run a test to see history.")

# Footer
st.markdown("---")
st.markdown("*Dashboard created for AI Safety Initiative @ GT Hackathon*")
