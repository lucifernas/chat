import openai
import os

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

n=True
while n==True:
	prompt=input("\n> ")
	if prompt=="no":
		break;
	else:
		completion = openai.Completion.create(
    		engine=model_engine,
    		prompt=prompt,
    		max_tokens=1024,
   			n=1,
    		stop=None,
    		temperature=0.5,
		)

		response = completion.choices[0].text
		print(response)