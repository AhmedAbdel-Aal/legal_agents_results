import streamlit as st
import json
import os

def load_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        else:
            return file.read()

def main():
    st.title("Legal AI Agent Viewer")
    
    agents_dir = 'agents'
    
    # Get list of agents
    agents = [d for d in os.listdir(agents_dir) if os.path.isdir(os.path.join(agents_dir, d))]
    
    # Select an agent
    selected_agent = st.sidebar.selectbox("Choose an Agent", agents)
    
    # Get cases for the selected agent
    cases_dir = os.path.join(agents_dir, selected_agent, 'cases')
    summaries = os.path.join(agents_dir, selected_agent, 'summaries')
    outputs_dir = os.path.join(agents_dir, selected_agent, 'outputs')
    cases = [f for f in os.listdir(cases_dir) if f.endswith('.json')]
    
    # Select a case
    selected_case = st.sidebar.selectbox("Choose a Case", cases)
    selected_case_summary = selected_case.replace('.json', '_summary.json')
    selected_case_output = selected_case.replace('.json', '_output.json')
    
    # View case or output
    view_option = st.sidebar.radio("View", ["Case", "Summary", "Output"])
    
    if view_option == "Case":
        case_path = os.path.join(cases_dir, selected_case)
        case_content = load_file(case_path)
        st.subheader("Case Content")
        st.json(case_content)

    if view_option == "Summary":
        case_path = os.path.join(summaries, selected_case_summary)
        case_content = load_file(case_path)
        only_summary_dict = {}
        only_summary_dict['summarized_case'] = case_content['summarized_case']
        st.subheader("Case Summary")
        st.json(only_summary_dict)
        
    elif view_option == "Output":
        case_path = os.path.join(outputs_dir, selected_case_output)
        case_content = load_file(case_path)
        st.subheader("Case Predicted Importance")
        st.json(case_content)

if __name__ == '__main__':
    main()