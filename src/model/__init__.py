import pickle
import os

model = pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'text_model.pkl'),'rb'))
tokenizer = pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'text_tokenizer.pkl'),'rb'))