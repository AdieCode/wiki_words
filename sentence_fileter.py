import re
import time
from tqdm import tqdm
from memory_profiler import profile

def convert_paragraphs_to_sentences(paragraphs):
    sentences = []
    for paragraph in paragraphs:
        # Split the paragraph into sentences using regex pattern
        # The pattern assumes that a sentence ends with a period, exclamation mark, or question mark, followed by a space
        # You may need to modify the pattern based on your specific requirements
        pattern = r"[^\s\w\?!.,:'\"]"

        paragraph_sentences = re.sub(pattern,"", paragraph)
        # Add the sentences to the list
        sentences.extend(paragraph_sentences)
    
    my_string = ''.join(sentences)
    with open("Textfiles/new_info.txt", "w", encoding="utf-8") as file:

        file.write(my_string)

with open("Textfiles/info.txt", "r", encoding="utf-8") as file:
    paragraphs = file.readlines()
    
   
    convert_paragraphs_to_sentences(paragraphs)
