import os
import openai
import tkinter as tk

def Net4moly(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",# ai langauge model hedha a7sn naw3
        prompt = text,#
        temperature = 0.6, #random text akthr wl a9al min 0.6 
        max_tokens = 150 #max words eli besh yar3o 
    )
    return print(response.choices[0].text)
def main():
    
    
    while True:
        print('Net4Moly: ')
        myQn = input()
    
        Net4moly(myQn)
        print('\n')

main()









            

    
