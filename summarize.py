from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked to extract specific information from the following text content: {content}. "
    "Please follow these instructions carefully: \n\n"
    "1. Only extract the information that directly matches the provided description: {summary}. "
    "2. Do not include any additional text, comments, or explanations in your response. "
    "3. If no information matches the description, return No matching information found."
    "4. Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.2:1b")

def summarize_with_ollama(dom_chunks,description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"content": chunk, "summary": description}
        )
        print(f"Batch: {i} of {len(dom_chunks)}")
        results.append(response)

    return "\n".join(results)