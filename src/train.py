from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from data_pipeline import load_data, process_data
from features import get_features


def train_model():
    print("\n" + "="*60)
    print("🚀 FAKE NEWS DETECTION - MODEL TRAINING")
    print("="*60)
    
    try:
        print("\n📂 Loading data...")
        df = load_data()
        print(f"   ✓ Loaded {len(df)} total articles")
        print(f"     - Fake: {(df['label']==0).sum()}")
        print(f"     - Real: {(df['label']==1).sum()}")
        
        print("\n🔄 Preprocessing text...")
        df = process_data(df)
        print("   ✓ Text preprocessing complete")
        
        print("\n🔨 Extracting TF-IDF features...")
        X, vectorizer = get_features(df['text'])
        y = df['label']
        print(f"   ✓ Feature matrix created: {X.shape}")
        
        print("\n📊 Splitting data (80% train, 20% test)...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"   ✓ Train set: {X_train.shape[0]} samples")
        print(f"   ✓ Test set: {X_test.shape[0]} samples")
        
        print("\n🤖 Training Logistic Regression model...")
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train, y_train)
        print("   ✓ Model training complete")
        
        print("\n📈 Evaluating model performance...")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        print(f"   ✓ Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"   ✓ Precision: {precision:.4f}")
        print(f"   ✓ Recall:    {recall:.4f}")
        print(f"   ✓ F1-Score:  {f1:.4f}")
        
        # Create models directory if needed
        models_dir = Path(__file__).parent.parent / "models"
        models_dir.mkdir(exist_ok=True)
        
        print("\n💾 Saving artifacts...")
        model_path = models_dir / "model.jb"
        vectorizer_path = models_dir / "vectorizer.jb"
        
        joblib.dump(model, model_path)
        joblib.dump(vectorizer, vectorizer_path)
        
        print(f"   ✓ Model saved to {model_path}")
        print(f"   ✓ Vectorizer saved to {vectorizer_path}")
        
        print("\n" + "="*60)
        print("✅ TRAINING COMPLETE - MODEL READY FOR DEPLOYMENT")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    train_model()