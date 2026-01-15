# Boston_House_Price_Prediction

## Softwares and Tools requirements

1. [GithubAccount](https://github.com)
2. [GitCLI](https://git-scm.com/install/)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [HeroKu](https://www.heroku.com/)  -- Cloud platform we used to deploy the application

#### Create a New Environment 

```
python --version  
Python 3.14.0    
do in cmd  
conda create -p venv python==3.14 -y  
conda activate venv/  
or  
python -m venv .venv  
.venv\Scripts\activate  
```

#### Installing requirements  
```  
pip install -r requirements.txt
```

- `python app.py`   run command in cmd

Use this `http://127.0.0.1:5000/predict_api` link to post data

`{"data":  {"CRIM": 0.1, "ZN": 12.5, "INDUS": 7.0, "CHAS": 0, "NOX": 0.4, "RM": 6.2, "AGE": 45.0, "DIS": 4.5, "RAD": 1, "TAX": 250.0, "PTRATIO": 16.0, "B": 390.0, "LSTAT": 5.0}
}`