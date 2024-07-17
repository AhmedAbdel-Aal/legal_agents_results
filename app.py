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
    outputs_dir = os.path.join(agents_dir, selected_agent, 'outputs')
    cases = [f for f in os.listdir(cases_dir) if f.endswith('.json')]

    print(cases_dir)
    print(outputs_dir)
    print(cases)
    
    # Select a case
    selected_case = st.sidebar.selectbox("Choose a Case", cases)
    
    # View case or output
    view_option = st.sidebar.radio("View", ["Case", "Output"])
    
    if view_option == "Case":
        case_path = os.path.join(cases_dir, selected_case)
        case_content = load_file(case_path)
        st.subheader("Case Content")
        st.json(case_content)
        
    elif view_option == "Output":
        output_summary_file_name = selected_case.replace('.json', '_summary.json')
        output_importance_file_name = selected_case.replace('.json', '_output.json')
        output_files = [output_summary_file_name, output_importance_file_name]
        if output_files:
            selected_output = st.sidebar.selectbox("Choose an Output File", output_files)
            output_path = os.path.join(outputs_dir, selected_output)
            output_content = load_file(output_path)
            
            st.subheader("Output Content")
            if selected_output.endswith('.json'):
                st.json(output_content)
            else:
                st.text(output_content)
        else:
            st.warning("No output file found for the selected case.")

if __name__ == '__main__':
    main()