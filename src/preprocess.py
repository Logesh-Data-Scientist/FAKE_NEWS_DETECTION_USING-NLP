import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    """Clean text by removing special characters and converting to lowercase."""
    # Remove special characters and digits, keep only alphabets and spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', str(text))
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_text(text):
    """Complete preprocessing pipeline for text.
    
    Steps:
    1. Clean text (remove special chars, lowercase)
    2. Tokenize into words
    3. Remove stopwords
    4. Apply stemming
    
    Args:
        text (str): Raw text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Step 1: Clean text
    text = clean_text(text)
    
    # Step 2: Tokenize
    words = word_tokenize(text)
    
    # Step 3: Remove stopwords
    words = [w for w in words if w not in stop_words and len(w) > 1]
    
    # Step 4: Apply stemming
    words = [stemmer.stem(w) for w in words]
    
    return " ".join(words)