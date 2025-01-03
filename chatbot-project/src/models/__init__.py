from transformers import BartForSequenceClassification, BartTokenizer

model_name = 'facebook/bart-large-mnli'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForSequenceClassification.from_pretrained(model_name)