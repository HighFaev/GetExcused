from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import random
import time
import os

#Get key for hugging face api
load_dotenv(dotenv_path='secret_keys.env')
api_key = os.getenv('HUGGINGFACE_API_KEY')

#Load dictionariesof most popular nouns and verbs
nounsList = open('data/nouns.txt', "r").readlines()
verbsList = open('data/verbs.txt', "r").readlines()

#Generate excuse from LLM
def generate_excuse():
    random.seed(time.time())

    #Get random noun and verb from dictionaries
    noun = nounsList[random.randint(0, 99)]
    verb = verbsList[random.randint(0, 99)]

    #Choose client from hugging face to work with
    client = InferenceClient(
        provider="novita",
        api_key=api_key,
    )

    #Make request to LLM
    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"Generate SHORT(MAXIMUM 10 WORDS), FUNNY excuse. Try to change somehow this words: {noun}, {verb} - to create excuse. GIVE ME ONLY PLAIN TEXT OF THE JOKE. EXAMPLES OF GOOD OUTPUT: 'My toilet just decided to run away from home.', 'My chair just up and decided to sing karaoke tonight.', 'My cat just ran away to become a professional snail trainer.', 'My time machine just broke down in ancient Egypt.'"
            }
        ],
        #Set seed to increase randomise
        seed=int(random.random() * 100),
        max_tokens=512,
    )

    #Return generated joke
    return completion.choices[0].message.content
