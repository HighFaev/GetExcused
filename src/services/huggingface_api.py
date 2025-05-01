from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import random
import time
import os

load_dotenv(dotenv_path='secret_keys.env')

api_key = os.getenv('HUGGINGFACE_API_KEY')
nounsList = open('data/nouns.txt', "r").readlines()
verbsList = open('data/verbs.txt', "r").readlines()

def generate_excuse():
    random.seed(time.time())

    noun = nounsList[random.randint(0, 99)]
    verb = verbsList[random.randint(0, 99)]

    client = InferenceClient(
        provider="novita",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"Generate SHORT(MAXIMUM 10 WORDS), FUNNY excuse. Try to change somehow this words: {noun}, {verb} - to create excuse. GIVE ME ONLY PLAIN TEXT OF THE JOKE. EXAMPLES OF GOOD OUTPUT: 'My toilet just decided to run away from home.', 'My chair just up and decided to sing karaoke tonight.', 'My cat just ran away to become a professional snail trainer.', 'My time machine just broke down in ancient Egypt.'"
            }
        ],
        seed=int(random.random() * 100),
        max_tokens=512,
    )


    return completion.choices[0].message.content
