import requests


class RAGModel:
    def __init__(self):
        self.documents = []

    def add_document(self, content):
        self.documents.append(content)

    def get_answer(self, question):
        # Simulate retrieval with a simple keyword match or use an actual retriever
        relevant_docs = [doc for doc in self.documents if question in doc]

        # Gemini LLM API call
        response = self.call_gemini_llm(question, relevant_docs)
        return

    def call_gemini_llm(self, question, relevant_docs):
            # Replace 'YOUR_GEMINI_API_KEY' with your actual API key for Gemini
        headers = {
                'Authorization': 'Bearer VARIABLE_from_ENV',
                'Content-Type': 'application/json',
            }

        prompt = f"{question}\n\n" + "\n".join(relevant_docs)
        data = {
            'model': 'gemini',  # Assuming Gemini LLM requires a model specifier
            'prompt': prompt,
            'max_tokens': 100,
        }

        response = requests.post('https://api.gemini.com/v1/engines/completions', headers=headers, json=data)
        result = response.json()

        # Extracting the text from the response
        return result['choices'][0]['text']