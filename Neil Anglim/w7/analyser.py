import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__))) #insuring that the working directory is the same as the file
#the use of classes in this seems to be overengineering as this is quite simple
class Sentence:
    def __init__(self, text):
         self.text = text
         
    def word_count(self):
        words = self.text.split()
        return len(words)
    
    def char_count(self):
        return len(self.text)
    
    def char_count_no_spaces(self):
        return len(self.text.replace(" ","").replace("\n", ""))
    
    
class Paragraph:
    def __init__(self, text):
        self.text = text

    def sentence_count(self):
        return len(re.split(r'[.!?]', self.text))

class TextFileAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.paragraphs = []
        
    def analyze(self): 
        if not os.path.exists(self.file_path):
            return "File not found."
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        self.paragraphs = [Paragraph(paragraph) for paragraph in re.split(r'\n\n', content)]
    #assigning the different variables names, and using the functions and methods to describe them as desired
        word_count = 0
        char_count = len(content)
        char_count_no_spaces = len(content.replace(" ", "").replace("\n", ""))
        sentence_count = 0
        for paragraph in self.paragraphs:
            sentence_count += paragraph.sentence_count()
            for sentence in re.split(r'[.!?]', paragraph.text):
                word_count += Sentence(sentence).word_count()
        paragraph_count = len(self.paragraphs)
        
    # Calculate averages
        average_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
        average_sentences_per_paragraph = sentence_count / paragraph_count if paragraph_count > 0 else 0
        
        metadata = {
            "File Name": os.path.basename(self.file_path),
            "Word Count": word_count,
            "Character Count": char_count,
            "Character Count (excluding whitespace)": char_count_no_spaces,
            "Sentence Count": sentence_count,
            "Paragraph Count": paragraph_count,
            "Average Words Per Sentence": average_words_per_sentence, 
            "Average Sentences Per Paragraph": average_sentences_per_paragraph}
        return metadata

if __name__ == "__main__":
    file_path = input("Enter the name of the text file: ")
    analyzer = TextFileAnalyzer(file_path)
    result = analyzer.analyze()
    
    if isinstance(result, dict): #to check if it is still a dict object
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)