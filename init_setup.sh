echo [$(date)]:"START"
echo [$(date)]:"Creating conda env with python 3.8"
conda create -p venv python=3.10 -y
echo [$(date)]:"activate env"
source activate ./env
echo [$(date)]:"installing requirements"
pip install -r requirements.txt
echo [$(date)]:"END"