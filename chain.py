from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

class Chain:
    def __init__(self, memory=None):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=None,
            max_retries=2
        )
        self.memory = memory

    def write_proposal(self, job_title, job_description, portfolio_urls):
        examples = ""
        if self.memory:
            retrieved = self.memory.retrieve_similar_proposals(job_description)
            examples = "\n\n".join(retrieved)

        prompt = PromptTemplate.from_template("""
                    Your Role: Your name is Sumaiya. You are an independent, highly skilled and persuasive freelancer specializing in Graphic Design, UI/UX Design, and Illustration.  
                    You work directly with clients on platforms like Upwork and Freelancer.com, delivering high-quality, tailored creative solutions.
                    Your Job: Write a warm, persuasive Upwork proposal for the job below. Use an engaging hook, show understanding of the client’s needs, and add 2–3 relevant portfolio URLs.
                    Use these previous proposal examples for tone and formatting:

                    {examples}

                    JOB TITLE: {job_title}
                    JOB DESCRIPTION: {job_description}
                    PORTFOLIO URLS:
                    {portfolio_urls}
                                              
                    no preamble
                    """)

        chain = prompt | self.llm
        response = chain.invoke({
            "job_title": job_title,
            "job_description": job_description,
            "portfolio_urls": "\n".join(portfolio_urls),
            "examples": examples
        })
        return response.content
