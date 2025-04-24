import sys
from pathlib import Path

# Set up paths
INDIC_NLP_LIB_HOME = str(Path("indic_nlp_library").absolute())
INDIC_NLP_RESOURCES = str(Path("indic_nlp_resources").absolute())

sys.path.append(INDIC_NLP_LIB_HOME)

# Import tokenizer
from indicnlp.tokenize import indic_tokenize

# Marathi text example
marathi_text = "मी अर्चना देशमुख आहे आणि मी पायथॉन शिकत आहे."

# Correct function for tokenization
tokens = indic_tokenize.trivial_tokenize(marathi_text)

# Print tokens
print(tokens)
