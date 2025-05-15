# Upwork Proposal Generator with RAG (HuggingFace Embeddings)

This project builds a Streamlit-based AI Agent that generates Upwork proposals using Retrieval-Augmented Generation (RAG). It smartly selects portfolio items and formats proposals based on past examples, using HuggingFace sentence embeddings.

---

## Features

- 📝 Generates professional Upwork proposals using job title and description.
- 📂 Matches the most relevant portfolio using semantic search.
- 📜 Uses previously written proposals as RAG examples for formatting.
- 🚀 Built with Streamlit, LangChain, HuggingFace embeddings, and Pandas.

---

## Project Structure

Upwork-Proposal-Generator/
│
├── app/
│ ├── main.py # Streamlit app UI
│ ├── proposal_generator.py # Core proposal generation logic
│ └── ...
│
├── data/
│ └── your_portfolio.pdf # Your uploaded portfolio (PDF or TXT)
│
├── vectorstore/ # ChromaDB index files
│
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Create a Virtual Environment (optional but recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

## Install Dependencies

```bash
pip install -r requirements.txt

## Run the App

```bash
streamlit run app.py

## 🧠 How It Works

1. **Input**  
   You provide the **Job Title** and **Job Description** of the freelance job you want to apply for.

2. **Portfolio Matching**  
   The system uses **HuggingFace sentence-transformers embeddings** to convert your job title and description into vector representations.  
   It then compares these vectors against embeddings of your portfolio entries (from `sample.csv`) to find the most relevant portfolio links.

3. **Retrieve Past Proposals**  
   It uses a **Retrieval-Augmented Generation (RAG)** approach by searching a database of your previous proposals (stored in `proposals.json`) to find similar proposals matching the current job context.

4. **Generate Proposal**  
   Using **LangChain** and the matched portfolio URLs plus retrieved past proposals, the system crafts a customized and persuasive proposal message.

5. **Output**  
   The final proposal text is displayed to you, ready to be sent to the client.


## 📸 UI Screenshot

![Proposal Generator UI](./ui_screenshot.png)

---

## 👤 Created By

**Asad Aslam**  
[GitHub](https://github.com/ashadx) | [LinkedIn](https://linkedin.com/in/asadaslam330)  
Email: asadaslam330@gmail.com
