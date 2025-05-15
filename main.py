import streamlit as st
from chain import Chain
from portfolio import Portfolio
from proposal_memory import ProposalMemory

def create_streamlit_app(chain, portfolio):
    st.set_page_config(layout="wide", page_title="Proposal Generator with RAG")
    st.title("Upwork Proposal Generator with Portfolio & Past Proposals")

    title_input = st.text_input("Enter Job Title:")
    description_input = st.text_area("Enter Job Description:")
    submit_button = st.button("Generate Proposal")

    if submit_button and title_input.strip() and description_input.strip():
        portfolio_urls = portfolio.query_links(f"{title_input} {description_input}")
        proposal = chain.write_proposal(title_input, description_input, portfolio_urls)
        st.markdown("### AI-Generated Proposal")
        st.code(proposal, language="markdown")

if __name__ == "__main__":
    memory = ProposalMemory("history.csv")
    chain = Chain(memory=memory)
    portfolio = Portfolio(file_path="sample.csv")
    create_streamlit_app(chain, portfolio)
