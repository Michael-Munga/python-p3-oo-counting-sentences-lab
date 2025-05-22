#!/usr/bin/env python3
import re 
class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split by any of the sentence-ending punctuation marks
        sentences = re.split(r'[.!?]', self._value)
        # Remove empty strings and strings with just whitespace
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  
print(string.is_exclamation())  
print(string.is_question())     
print(string.is_sentence())     
