# working code, second print stament gives only the required answer
# first print statement gives you complete response from chatGPT which includes total number of tokens used
import openai
#from apikey import APIKEY
APIKEY = "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"
openai.api_key = APIKEY

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
             "Write me a python script for hosting machine learning model"}]
)

# Print out the whole output dictionary
print(output)

# Get the output text only
print(output['choices'][0]['message']['content'])