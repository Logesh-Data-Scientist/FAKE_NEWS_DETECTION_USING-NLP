from sklearn.feature_extraction.text import TfidfVectorizer

def get_features(text_data):
    """Extract TF-IDF features from text data.
    
    Args:
        text_data: Pandas Series of text strings
        
    Returns:
        X: Sparse TF-IDF feature matrix
        vectorizer: Fitted TfidfVectorizer object
    """
    vectorizer = TfidfVectorizer(max_features=5000, min_df=2, max_df=0.95)
    X = vectorizer.fit_transform(text_data)
    return X, vectorizer