# Customizing the tokenizer
from spacy.tokenizer import Tokenizer
import re
import string
import spacy
import spacy.training

@spacy.registry.tokenizers("custom_tokenizer")
def custom_tokenizer():
  def custom_tokenizer(nlp):
    my_punct = f"[{re.escape(string.punctuation)}]"
    my_punct = my_punct.replace("<", "")
    my_punct = my_punct.replace(">", "")
    html_tag_pattern = re.compile(r'<[^>]+>')

    all_prefixes_re = spacy.util.compile_prefix_regex(tuple(list(nlp.Defaults.prefixes) + [html_tag_pattern.pattern] + [my_punct]))
    infix_re = spacy.util.compile_infix_regex(nlp.Defaults.infixes)
    suffix_re = spacy.util.compile_suffix_regex(tuple(list(nlp.Defaults.suffixes) + [html_tag_pattern.pattern] + [my_punct]))

    return Tokenizer(nlp.vocab,
                      nlp.Defaults.tokenizer_exceptions,
                      prefix_search = all_prefixes_re.search, 
                      infix_finditer = infix_re.finditer,
                      suffix_search = suffix_re.search,
                      token_match=None)
    
  return custom_tokenizer
