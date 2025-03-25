import json
from datasets import Dataset

def load_text_data(file_path):
    """Load and prepare text data from a file"""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    dataset = Dataset.from_dict({"text": lines})
    return dataset

if __name__ == "__main__":
    dataset = load_text_data("data.txt")  # Example text file with training data
    print(dataset)
