import ollama, time

class Llama3WordReplacer:
    def __init__(self,model='llama3'):
        # Initialize the model for the Ollama client
        self.model = model
        print('pulling model',self.model)
        # Pull the llama3 model
        a = time.time()
        ollama.pull(self.model)
        # Instructions are initialized as a class attribute
        self.instructions = (
            "You are a language model tasked with replacing a specific word in a sentence with a phrase (maximum 5 words) while maintaining the original context."  
        )
        print('model ready in',time.time()-a)

    def get_word_replacement(self, word_to_replace, context):
        # Create the prompt using the provided word and context
        prompt = f"""
        {self.instructions}

        Word to replace: "{word_to_replace}"
        Context: "{context}"

        Provide only the replacement for the word:
        """

        # Generate a response from the model
        # response = self.model.generate(prompt=prompt)
        start = time.time()
        response = ollama.chat(model=self.model,messages=[{'role':'user','content':prompt}])
        print('inferance time',time.time()-start)
        # Return the replacement phrase
        return f"{word_to_replace}_replacement_in_this_context_is: {response['message']['content']}"

if __name__ == "__main__":
    # Create an instance of the class
    replacer = Llama3WordReplacer()

    # Define inputs for the word to replace and the context
    word_to_replace = "attackers"
    context = "We are living in the era of cyber warfare where attackers are everywhere."

    # Get the word replacement
    result = replacer.get_word_replacement(word_to_replace, context)

    # Print the result
    print(result)