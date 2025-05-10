# Customizing the tokenizer
from spacy.tokenizer import Tokenizer
import re
import string
import spacy
import spacy.training

@spacy.registry.tokenizers("custom_tokenizer")
def custom_tokenizer():
  def custom_tokenizer(nlp):
    prefix_re = re.compile(r'')
    suffix_re = re.compile(r'')
    infix_re = re.compile(r'')

    return Tokenizer(
          nlp.vocab,
          prefix_search=prefix_re.search,
          suffix_search=suffix_re.search,
          infix_finditer=infix_re.finditer
      )
    
  return custom_tokenizer
