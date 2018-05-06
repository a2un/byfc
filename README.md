# Build Your First Chatbot (byfc)
This is a demo chatbot written in Python using Rasa NLU

1. Ensure you have virtualenv installed

```
 pip install virtualenv
```
 
2. Clone this project from http://bit.ly/DBSPythonMeetup and cd to byfc-master
 ```
 cd byfc-master
 ```
 
3. Create and start a virtual environment 
 ```
 virtualenv venv3 -p python3
 source venv3/bin/activate
 ```

4. Install the required Python packages
 ```
 pip install -r requirements.txt
 ```

Skip to step 7 if you just want to host/start the model

5. Get the data total_word_feature_extractor.dat fle from [Google Drive](https://drive.google.com/open?id=1eCKtB9haQBIRTr1oAFwbN1VzmCIH6PRd)
or from [Github](https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2)

6. Place the .dat file from the zip in AI-Engine/data

7. To train model:
```
python -m rasa_nlu.train -c AI-engine/config_mitie.json
```

8. Deploy flask application
```
python app_engine/deploy.py
```

9. Host/start model
 ```
python -m rasa_nlu.server -c AI-engine/config_mitie.json
```
