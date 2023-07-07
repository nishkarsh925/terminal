import pyfiglet
import time
from colorama import Fore, Style

def print_typewriter_colored(text):
    for char in text:
        color = Fore.RED  # Change the color here
        print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.001)  # Adjust the delay as desired

# Example usage
text = "ZEUS..."
ascii_art = pyfiglet.figlet_format(text)
print_typewriter_colored(ascii_art)
import time

def print_with_delay(statement, delay):
    for char in statement:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

delay = 0.01  # Time gap between each character (in seconds)

import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define your prompt
while True:

  
  enter = "Enter anything you want to ask..."
  print_typewriter_colored(enter)
  
  
  i = input()
  prompt = i

  # Generate text using the OpenAI API
  response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=100
   )

  # Get the generated text from the response
  generated_text = response.choices[0].text.strip()

  #  Print the generated text
  print_with_delay(generated_text, delay)
  ask = '''\n\n\n\n\n\n\nPress "q" to quit , "c" to continue'''
  print_with_delay(ask, delay)
    
        
  l = input()
  if l == "q":
    break
  else:
    continue
