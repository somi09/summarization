from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import pickle

model = BartForConditionalGeneration.from_pretrained(
    'facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained(
    'facebook/bart-large-cnn')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print ("device ",device)
model = model.to(device)


pickle.dump(model,open("model/text_model.pkl","wb"))
pickle.dump(tokenizer,open("model/text_tokenizer.pkl",'wb'))