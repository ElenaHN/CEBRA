# CEBRA 
CEBRA: CasE-Based Reasoning Application.

## Installation
Assuming you have a [Python3](https://www.python.org/) distribution with [pip](https://pip.pypa.io/en/stable/installing/), you only need to install the pycbr package:
```
pip3 install pycbr
```

To launch the application, clone the repository or download the files and run:
```
python3 cebra.py
```

A production deployment can be set using gunicorn:
```
pip install gunicorn
gunicorn --workers 1 --bind 0.0.0.0:5000 --timeout 600 cebra:app
```
