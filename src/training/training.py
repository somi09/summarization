import pickle
import os

from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
class Training:
    def __init__(self):
        self.model_name = "google/pegasus-xsum" 
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_pegasus = PegasusForConditionalGeneration.from_pretrained(self.model_name).to(device)
        
    def copy_model(self):
        pickle.dump(self.model_name,open("text_model.pkl","wb"))
        pickle.dump(self.model_name,open("text_tokenizer.pkl",'wb'))
        
        
training = Training()
training.copy_model()

