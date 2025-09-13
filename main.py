from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_ollama import ChatOllama
import os

load_dotenv()  # Load environment variables from .env file

def main():
    print("Hello from langchain-course!")
    information = """ Bhimrao Ramji Ambedkar (Bhīmrāo Rāmjī Āmbēḍkar; 14 April 1891 – 6 December 1956) was an Indian jurist, economist, social reformer and political leader who chaired the committee that drafted the Constitution of India based on the debates of the Constituent Assembly of India and the first draft of Sir Benegal Narsing Rau.[1][2][3][4][5] Ambedkar served as Law and Justice minister in the first cabinet of Jawaharlal Nehru. He later renounced Hinduism, converted to Buddhism and inspired the Dalit Buddhist movement.[6]

After graduating from Elphinstone College, University of Bombay, Ambedkar studied economics at Columbia University and the London School of Economics, receiving doctorates in 1927 and 1923, respectively, and was among a handful of Indian students to have done so at either institution in the 1920s.[7] He also trained in the law at Gray's Inn, London. In his early career, he was an economist, professor, and lawyer. His later life was marked by his political activities; he became involved in campaigning and negotiations for partition, publishing journals, advocating political rights and social freedom for Dalits, and contributing to the establishment of the state of India. In 1956, he converted to Buddhism, initiating mass conversions of Dalits
     """
    summary_template = """ Give the information {information} about a person, I want to create:
    1. A short summary
    2. Two intersting facts about the person
    3. The person's contribution to society
    """

    prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    #llm = ChatOllama(model="llama2", base_url="http://192.168.1.6:11434", temperature=0)

    chain =  prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":  
    main()
