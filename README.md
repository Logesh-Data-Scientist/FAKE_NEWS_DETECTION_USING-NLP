# 📰 Fake News Detection System

An AI-powered machine learning application that analyzes news articles and classifies them as **Real** or **Fake** using TF-IDF vectorization and Logistic Regression.

---

## 🚀 Quick Start

### 1️⃣ **Train the Model**
Before running the app for the first time, train the model:

```bash
python src/train.py
```

**Output Example:**
```
============================================================
🚀 FAKE NEWS DETECTION - MODEL TRAINING
============================================================

📂 Loading data...
   ✓ Loaded 44919 total articles
     - Fake: 23502
     - Real: 21417

🔄 Preprocessing text...
   ✓ Text preprocessing complete

🔧 Extracting TF-IDF features...
   ✓ Feature matrix created: (44919, 5000)

📊 Splitting data (80% train, 20% test)...
   ✓ Train set: 35935 samples
   ✓ Test set: 8984 samples

🧠 Training Logistic Regression model...
   ✓ Model training complete

📈 Evaluating model performance...
   ✓ Accuracy:  0.9886 (98.86%)
   ✓ Precision: 0.9885
   ✓ Recall:    0.9878
   ✓ F1-Score:  0.9881

💾 Saving artifacts...
   ✓ Model saved to models/model.jb
   ✓ Vectorizer saved to models/vectorizer.jb

============================================================
✅ TRAINING COMPLETE - MODEL READY FOR DEPLOYMENT
============================================================
```

### 2️⃣ **Run the Web App**
After training, launch the interactive Streamlit app:

```bash
streamlit run app/app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📋 Features

✅ **Real-time Classification** - Get instant predictions on any news article  
✅ **Confidence Score** - View probability breakdown for predictions  
✅ **Beautiful UI** - Clean, intuitive Streamlit interface  
✅ **High Accuracy** - ~98.86% accuracy on test data  
✅ **Robust Preprocessing** - Advanced text cleaning, tokenization, and stemming  

---

## 📁 Project Structure

```
FAKE_NEWS_DETECTION/
├── app/
│   └── app.py              # Streamlit web application
├── src/
│   ├── train.py            # Model training script
│   ├── data_pipeline.py    # Data loading and processing
│   ├── features.py         # TF-IDF feature extraction
│   └── preprocess.py       # Text preprocessing utilities
├── data/
│   ├── Fake.csv            # Fake news dataset
│   └── True.csv            # Real news dataset
├── models/
│   ├── model.jb            # Trained model (generated after training)
│   └── vectorizer.jb       # TF-IDF vectorizer (generated after training)
├── notebooks/
│   └── EDA.ipynb           # Exploratory Data Analysis notebook
├── env/                    # Python virtual environment
├── requirements.txt        # Python dependencies
├── APP.ipynb              # Demo notebook
└── README.md              # This file
```

---

## 🧠 Model Architecture

- **Algorithm**: Logistic Regression
- **Feature Engineering**: TF-IDF Vectorization (5000 features, min_df=2, max_df=0.95)
- **Input**: Raw news text (title + content)
- **Output**: Binary classification (0=Fake, 1=Real) + confidence probability

### Training Data
- **Total Articles**: 44,919
- **Fake News**: 23,502
- **Real News**: 21,417
- **Train/Test Split**: 80% / 20%

### Performance Metrics
- **Accuracy**: ~98.86%
- **Precision**: ~98.85%
- **Recall**: ~98.78%
- **F1-Score**: ~98.81%

---

## 🧪 Example Usage

### Sample Real News Input:
> "Scientists announce breakthrough in renewable energy storage. A new battery technology achieves 95% efficiency rating, promising to revolutionize electric vehicle charging times."

**Expected Output:** ✅ **REAL NEWS** (Confidence: ~95%)

### Sample Fake News Input:
> "Secret Government Experiment Reveals Aliens Have Been Living Underground For Centuries. Exclusive leaked documents prove extraterrestrial beings..."

**Expected Output:** ❌ **FAKE NEWS** (Confidence: ~98%)

---

## 🛠️ Setup Requirements

- Python 3.8+
- Virtual environment (recommended)
- Required packages listed in `requirements.txt`

### Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## 📊 Data Preprocessing Pipeline

1. **Text Cleaning**
   - Remove special characters, URLs, numbers
   - Convert to lowercase
   - Clean extra whitespace

2. **Tokenization**
   - Split text into individual words

3. **Stopword Removal**
   - Remove common English words (the, is, and, etc.)

4. **Stemming**
   - Reduce words to root form using Porter Stemmer

5. **Feature Extraction**
   - TF-IDF vectorization with 5000 features

---

## 🚨 Troubleshooting

### Error: "Model files not found"
```
Solution: Run training first:
python src/train.py
```

### Error: "Port 8501 already in use"
```
Solution: Use a different port:
streamlit run app/app.py --server.port 8502
```

### Error: NLTK data not found
```
Solution: The application automatically downloads required NLTK data.
If issues persist, manually run:
python -m nltk.downloader punkt stopwords
```

---

## 📝 Tips for Best Results

1. **Longer texts work better** - Provide full article content when possible
2. **Real news often has** - Facts, citations, quotations, specific dates
3. **Fake news often has** - Sensational claims, emotional language, vague sources
4. **Confidence scores matter** - Low confidence (51-55%) may need manual review

---

## 🔐 Limitations

- Trained on English news articles only
- May struggle with translated content
- Biased toward dataset characteristics
- Should be used as a decision support tool, not the sole classifier

---

## 📧 Notes

For questions or improvements, refer to the project documentation or review the training metrics in `src/train.py` output.

---

**Last Updated**: March 2026  
**Status**: ✅ Production Ready
