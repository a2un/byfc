# byfc
This is a demo chatbot written in Python using Rasa nlu

Clone this project from https://bit.ly/2FDqQHb

Get the data total_word_feature_extractor.dat fle from https://drive.google.com/open?id=1eCKtB9haQBIRTr1oAFwbN1VzmCIH6PRd

to train model
python -m rasa_nlu.train -c AI-engine/config_mitie.json

to host/start model
python -m rasa_nlu.server -c AI-engine/config_mitie.json
