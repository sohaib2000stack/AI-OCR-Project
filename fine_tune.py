from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_dataset

# Load model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load dataset
dataset = load_dataset("text", data_files={"train": "data.txt"})

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    save_total_limit=2,
    num_train_epochs=3,
    logging_dir="./logs",
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

trainer.train()














































# from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer
# from datasets import load_dataset

# # Load tokenizer and model
# model_name = "gpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# # Load and tokenize dataset
# dataset = load_dataset("text", data_files={"train": "dataset/train.txt", "test": "dataset/test.txt"})

# def tokenize_function(examples):
#     return tokenizer(examples["text"], padding="max_length", truncation=True)

# tokenized_datasets = dataset.map(tokenize_function, batched=True)

# # Training arguments
# training_args = TrainingArguments(
#     output_dir="./results",
#     evaluation_strategy="epoch",
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     save_total_limit=2,
#     num_train_epochs=3,
#     logging_dir="./logs",
# )

# # Train model
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenized_datasets["train"],
#     eval_dataset=tokenized_datasets["test"]
# )

# if __name__ == "__main__":
#     trainer.train()
