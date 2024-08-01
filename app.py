import os
import streamlit as st
import json

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading file {file_path}: {e}")
        return None

def main():
    st.title("Legal AI Agent Viewer")
    
    agents_dir = 'agents'
    data_dir = 'data'
    
    # Get list of agents
    agents = [d for d in os.listdir(agents_dir) if os.path.isdir(os.path.join(agents_dir, d))]
    
    # Select an agent
    selected_agent = st.sidebar.selectbox("Choose an Agent", agents)
    
    # Get cases for the selected agent
    cases_dir = os.path.join(data_dir)
    outputs_dir = os.path.join(agents_dir, selected_agent, 'outputs')
    cases = [f for f in os.listdir(cases_dir) if f.endswith('.json')]
    
    # Select a case
    selected_case = st.sidebar.selectbox("Choose a Case", cases)
    selected_case_output = selected_case.replace('.json', '_output.json')
    st.write("Selected case:", selected_case)
    st.write("Selected case output:", selected_case_output)
    
    # View case or output
    view_option = st.sidebar.radio("View", ["Case", "Output"])
    
    if view_option == "Case":
        case_path = os.path.join(cases_dir, selected_case)
        st.write("Case path:", case_path)
        case_content = load_file(case_path)
        if case_content:
            st.subheader("Case Content")
            st.json(case_content)
        else:
            st.error("Failed to load case content")

    elif view_option == "Output":
        case_path = os.path.join(outputs_dir, selected_case_output)
        st.write("Output case path:", case_path)
        case_content = load_file(case_path)
        if case_content:
            st.subheader("Case Predicted Importance")
            st.json(case_content)
        else:
            st.error("Failed to load case output")

if __name__ == "__main__":
    main()
