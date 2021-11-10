import subprocess

# Install dependency
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "progressist>=0.1.0"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "tqdm>=4.61.1"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "joblib>=1.0.1"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "fastwer>=0.1.3"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "numpy>=1.19.5"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "pandas>=1.2.5"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "torch>=1.9.0"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "pytorch-lightning>=1.4.0"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "nltk>=3.6.2"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "scikit-learn>=0.24.2"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "scipy>=1.7.0"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "librosa>=0.8.1"])
subprocess.run(["pip", "install", "-U", "--upgrade-strategy=only-if-needed", "pythainlp>=2.3.1"])

subprocess.run(["pip", "install", "--editable", "./NLP_Datasets"])
subprocess.run(["pip", "install", "--editable", "./NLP_Losses"])
subprocess.run(["pip", "install", "--editable", "./NLP_Metrics"])
subprocess.run(["pip", "install", "--editable", "./NLP_Models"])
subprocess.run(["pip", "install", "--editable", "./NLP_ModelTrainers"])
subprocess.run(["pip", "install", "--editable", "./NLP_Preprocessors"])