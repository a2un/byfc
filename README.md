# Build Your first Chatbot (byfc)
This is a demo chatbot written in Python using Rasa nlu

Clone this project from http://bit.ly/DBSPythonMeetup

Ensure you have virtualenv installed

```
 pip install virtualenv
```
 
 
 * To create and start a virtual environment 
 ```
 virtualenv venv3 -p python3
 source venv3/bin/activate
 ```
 
Get the data total_word_feature_extractor.dat fle from https://drive.google.com/open?id=1eCKtB9haQBIRTr1oAFwbN1VzmCIH6PRd
or from https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2

 * To train model:
```
python -m rasa_nlu.train -c AI-engine/config_mitie.json
```

 * To host/start model
 ```
python -m rasa_nlu.server -c AI-engine/config_mitie.json
```

