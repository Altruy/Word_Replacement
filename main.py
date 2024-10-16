'''
Author: Turyal Neeshat
Contact: tneeshat@outlook.com
'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
import time
import threading

# Define the model class
class LLMWordReplacer:
    def __init__(self, model='gemma2:2b'):
        # Initialize the model for the Ollama client
        self.model = model
        a = time.time()
        print('Pulling model', self.model)
        # Pull the gemma2:2b model to ensure it is available
        ollama.pull(self.model)
        # Instructions are initialized as a class attribute
        self.instructions = (
            "You are a language model tasked with replacing a specific word in a sentence with a new phrase (maximum 5 words) while maintaining the original context."
        )
        print('Model ready in', time.time() - a)

    def get_word_replacement(self, word_to_replace, context):
        # Create the prompt using the provided word and context
        prompt = f"""
        {self.instructions}

        Word to replace: "{word_to_replace}"
        Context: "{context}"

        Provide only the replacement for the word and not the whole sentence:
        """
        
        # Generate a response from the model
        response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
        # Return the replacement phrase
        return response['message']['content']

# Initialize FastAPI app and the Llama3WordReplacer object
#model = 'llama3'
model = 'gemma2:2b'
app = FastAPI()
replacer = LLMWordReplacer(model = model)

# Define input model for API request
class WordReplacementRequest(BaseModel):
    word_to_replace: str
    context: str

# API endpoint for checking server status
@app.get("/")
def root():
    return {"status": "Server is running!"}

# API endpoint for word replacement
@app.post("/replace_word")
def replace_word(request: WordReplacementRequest):
    try:
        a = time.time()
        replacement = replacer.get_word_replacement(request.word_to_replace, request.context)
        b = str(time.time() - a)[:7]
        print('Inference in', b)
        return {"replacement": replacement,"time":b}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Function to keep the model active
def keep_model_active():
    while True:
        try:
            # Call the model with dummy data to keep it active
            a = time.time()
            replacer.get_word_replacement("attackers", "We are living in the era of cyber warfare where attackers are everywhere.")
            b = str(time.time() - a)[:7]
            print("Model kept active",b)
        except Exception as e:
            print("Error keeping model active:", str(e))
        time.sleep(60)  # Sleep for 1 minutes

# Start the thread to keep the model active
threading.Thread(target=keep_model_active, daemon=True).start()

# Run the FastAPI app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
