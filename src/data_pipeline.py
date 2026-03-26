import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))
from preprocess import preprocess_text

def load_data():
    base_dir = Path(__file__).parent.parent
    fake = pd.read_csv(base_dir / "data" / "Fake.csv")
    real = pd.read_csv(base_dir / "data" / "True.csv")

    fake['label'] = 0
    real['label'] = 1

    df = pd.concat([fake, real])
    df = df.sample(frac=1).reset_index(drop=True)

    return df

def process_data(df):
    df['text'] = df['text'].apply(preprocess_text)
    return df