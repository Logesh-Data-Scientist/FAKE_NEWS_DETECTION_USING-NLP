# 🎯 HOW TO RUN THE FAKE NEWS DETECTION PROJECT

## 🎬 Start Here

This guide walks you through getting the project up and running in 3 simple steps.

---

## STEP 1: Check Your Environment ✅

Before running anything, make sure you have all dependencies installed.

### Option A: Automatic Check
```bash
python run.py
```
Choose option "1" from the menu to check everything.

### Option B: Manual Install
```bash
pip install -r requirements.txt
```

---

## STEP 2: Train the Model 🧠

The model learns from your data. **Run this once before using the app.**

### Option A: Windows Users (Easiest)
**Double-click:** `train.bat`

The training window will open and show progress. Wait for it to complete (2-5 minutes).

### Option B: Command Line
```bash
cd C:\Users\Hey!\OneDrive\Desktop\FAKE_NEWS_DETECTION
env\Scripts\python.exe src\train.py
```

### Option C: Using Helper Script
```bash
python run.py
```
Choose option "3" from the menu.

### Expected Output:
```
============================================================
🚀 FAKE NEWS DETECTION - MODEL TRAINING
============================================================

📂 Loading data...
   ✓ Loaded 44919 total articles
   
🔄 Preprocessing text...
   ✓ Text preprocessing complete

... (more progress) ...

📈 Evaluating model performance...
   ✓ Accuracy:  0.9886 (98.86%)
   ✓ Precision: 0.9885
   ✓ Recall:    0.9878
   ✓ F1-Score:  0.9881

💾 Saving artifacts...
   ✓ Model saved to models/model.jb
   ✓ Vectorizer saved to models/vectorizer.jb

✅ TRAINING COMPLETE - MODEL READY FOR DEPLOYMENT
============================================================
```

✅ **When you see "TRAINING COMPLETE", you're ready for step 3!**

---

## STEP 3: Launch the App 🚀

Now run the interactive web application.

### Option A: Windows Users (Easiest)
**Double-click:** `launch_app.bat`

A browser window will automatically open. The app runs at `http://localhost:8501`

### Option B: Command Line
```bash
cd C:\Users\Hey!\OneDrive\Desktop\FAKE_NEWS_DETECTION
env\Scripts\streamlit.exe run app/app.py
```

### Option C: Using Helper Script
```bash
python run.py
```
Choose option "4" from the menu.

---

## 🌐 Using the Web App

Once the app is open in your browser, you'll see:

```
┌──────────────────────────────────────────────┐
│ 📰 Fake News Detection System                │
│                                              │
│ This AI-powered tool analyzes news articles  │
│ and classifies them as Real or Fake.         │
│ Enter your news text below to get a          │
│ prediction.                                  │
│                                              │
│ ┌──────────────────────────────────────────┐│
│ │  📝 Enter News Text                       ││
│ │  [Paste or type here...]                  ││
│ │                                            ││
│ │  [.............. 🔍 Analyze ............]││
│ └──────────────────────────────────────────┘│
└──────────────────────────────────────────────┘
```

### How to Use:

1. **Copy news text** from an article
2. **Paste into the text box** (or type)
3. **Click "🔍 Analyze"** button
4. **View results** with confidence score

---

## 📝 Test Examples

### Example 1: Real News ✅

Copy and paste this into the app:

```
Reuters - Scientists at Stanford University announce breakthrough 
in battery technology. The new lithium-ion design achieves 500 charge 
cycles while maintaining 95% capacity. The research team published 
their findings in Nature Energy and is now seeking commercial partners 
for mass production. Funding came from the U.S. Department of Energy.
```

**Expected Result:** ✅ **REAL NEWS** (Confidence: 90%+)

---

### Example 2: Fake News ❌

Copy and paste this into the app:

```
SHOCKING! Secret Government Document Reveals Angels Are Living Among Us!
Thousands of photos LEAKED! Scientists HATE this one trick! The government 
has been HIDING the TRUTH about angels for 50 years! See the unbelievable 
proof here! This will SHOCK you! Don't let them suppress this information!
```

**Expected Result:** ❌ **FAKE NEWS** (Confidence: 95%+)

---

### Example 3: Real News ✅

Copy and paste this into the app:

```
Federal Reserve raises interest rates by 0.5% at today's policy meeting. 
Federal Reserve Chair Janet Yellen cited concerns about inflation and 
unemployment. The decision follows months of economic data analysis. 
Markets responded positively to the announcement with stock indices up 
1.2% by market close. Analysts expect further rate adjustments in coming months.
```

**Expected Result:** ✅ **REAL NEWS** (Confidence: 85%+)

---

## 🛑 Troubleshooting

### Problem: "Model files not found"
**Solution:** Run training first (Step 2)

### Problem: "Port 8501 already in use"
**Solution:** Wait a moment and try again, or use a different port:
```bash
streamlit run app/app.py --server.port 8502
```

### Problem: App won't launch
**Solution:** Make sure you completed Step 2 (training)

### Problem: "NLTK data not found"
**Solution:** This is handled automatically, but if issues persist:
```bash
python -m nltk.downloader punkt stopwords
```

### Problem: Dependencies missing
**Solution:** Install requirements:
```bash
pip install -r requirements.txt
```

---

## 📊 Understanding the Results

### Real News Indicators:
- ✅ Specific dates and locations
- ✅ Named sources and quotations
- ✅ Factual claims with evidence
- ✅ Balanced reporting
- ✅ Professional language

### Fake News Indicators:
- ❌ Sensational headlines
- ❌ Emotional language
- ❌ Vague sources ("Scientists say...")
- ❌ All-caps words for emphasis
- ❌ Unbelievable claims

### Confidence Score:
- **95-100%:** Very confident prediction
- **75-95%:** Confident prediction
- **55-75%:** Somewhat confident (may warrant review)
- **51-55%:** Borderline (manual review recommended)

---

## 🔄 Retraining the Model

If you want to retrain with the same data:

```bash
python src/train.py
```

Or use the helper script:
```bash
python run.py
```
Choose option "3"

---

## ⏰ How Long Does It Take?

| Task | Time |
|------|------|
| Installing dependencies | 2-5 min |
| Training the model | 2-5 min |
| Launching the app | <1 min |
| Making a prediction | <1 sec |

**Total first-time setup:** ~10 minutes

---

## 🎓 How It Works (Quick Version)

1. **Data Loading** - Reads 44,919 news articles (23,502 fake + 21,417 real)
2. **Text Processing** - Cleans text, removes stopwords, stems words
3. **Feature Extraction** - Converts text to 5,000 numerical features using TF-IDF
4. **Model Training** - Trains a Logistic Regression classifier
5. **Model Saving** - Saves model and vectorizer for app use
6. **App Prediction** - When you enter text, app processes it and predicts

**Model Accuracy:** 98.86%

---

## 🔗 Additional Resources

- **Full Documentation:** See `README.md`
- **Quick Reference:** See `QUICK_START.md`
- **All Changes:** See `CHANGES.md`
- **Project Structure:** See project folder

---

## 💡 Tips for Best Results

1. **Use longer texts** - Provide full article content, not just headlines
2. **Copy exact text** - Don't paraphrase or summarize
3. **Include details** - More information helps the model decide
4. **Real news usually has:**
   - Specific names and dates
   - News organization attribution
   - Multiple sources
   - Balanced perspective

5. **Fake news usually has:**
   - Sensational language
   - Vague sources
   - Emotional appeals
   - Lack of verifiable facts

---

## ✅ You're Ready!

That's it! You now have a fully functional Fake News Detection system.

### Quick Summary:
1. ✅ Double-click `train.bat` (first time only)
2. ✅ Double-click `launch_app.bat`
3. ✅ Paste news and click Analyze
4. ✅ See if it's Real or Fake!

---

## 📧 Questions?

Refer to:
- README.md - Detailed information
- QUICK_START.md - Fast reference
- CHANGES.md - What was improved
- This file (HOW_TO_RUN.md) - Step by step guide

---

**Happy Detecting! 🎉**
