#!/usr/bin/env python3


import re

class MyString:
    def __init__(self, value=''):
        # Ensure value is a string; otherwise raise an error
        if not isinstance(value, str):
            raise ValueError("value must be a string")
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val    

    def is_sentence(self):
        # Checks if value ends with a period '.'
        return self.value.endswith('.')

    def is_question(self):
        # Checks if value ends with a question mark '?'
        return self.value.endswith('?')

    def is_exclamation(self):
        # Checks if value ends with an exclamation mark '!'
        return self.value.endswith('!')

    def count_sentences(self):
        # Split on punctuation marks that typically end sentences: '.', '!', and '?'
        # Use regex to split on one or more punctuation marks, e.g. "!!" counts as a single split
        # The pattern "[.!?]+" matches one or more of . or ! or ?
        sentences = re.split(r'[.!?]+', self.value)

        # Filter out empty strings after the split
        filtered_sentences = [s for s in sentences if s.strip() != '']

        # The count of filtered sentences
        return len(filtered_sentences)
