from ast import arg
import os
from typing import List
import openai
import argparse
import re

MAX_INPUT_LENGTH =12

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"user input : {user_input}")
    if validate_length(user_input):
       genarate_branding_anippet(user_input) 
       genarate_keyword(user_input)

    else:
        raise ValueError("Input lenght to long , Must be under {MAX_INPUT_LENGTH}")


def genarate_keyword(promt:str) ->List[str]:

    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"  
    # openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_promt = f"Genarate Related Branding key words for  {promt}:"
    print(enriched_promt)

    response = openai.Completion.create(model="text-davinci-002", prompt=enriched_promt, temperature=0, max_tokens=32)

    #separate answer
    keywords_text = response["choices"][0]["text"]
    
    #Strip answer
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-",keywords_text)
    keywords_array =[k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k)> 0]

    print(f"Keywords : {keywords_array}")
    return keywords_array


def validate_length(promt: str) -> bool:
    return len(promt)<=12


def genarate_branding_anippet(promt:str) ->str:

    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"  
    # openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_promt = f"generate upbeat branding snippet for {promt}:"
    print(enriched_promt)

    response = openai.Completion.create(model="text-davinci-002", prompt=enriched_promt, temperature=0, max_tokens=32)

    #separate answer
    branding_text = response["choices"][0]["text"]
    
    #Strip answer
    branding_text = branding_text.strip()
    
    #add ... to last line
    last_char = branding_text[-1]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    return branding_text



if __name__ =="__main__":
    main ()