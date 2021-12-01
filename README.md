create env 

```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```

created a req file

install the req
```bash
pip install -r requirements.txt
```
download the data from:  https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

- Develop README.md

- Develop template.py script

- move (manually) dataset into data_given folder

```bash
git init
```
```bash
dvc init 
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```

oneliner updates  for README.md

```bash
git add . && git commit -m "update Readme.md"
```

Open your GITHUB account

Create a new repo named "simple-dvc-demo4"

click on "create repository"

```bash
git remote add origin https://github.com/olufemiolajide/simple-dvc-demo4.git
git branch -M main
git push origin main
```

- Develop params.yaml file

```bash
git add . && git commit -m "params added"
git push origin main
```

# Develop get_data.py

- Install some dependencies

```bash
pip install pandas
pip install PyYAML
```

# Test get_data.py

```bash
python src\get_data.py
git add . && git commit -m "add get_data.py"
git push origin main
```

# Develop load_data.py

```bash
python src\get_data.py
git add . && git commit -m "add get_data.py"
git push origin main
```

# Develop params.yaml
```bash
dvc repro

git add . && git commit -m "add params.yaml"
git push origin main
```

# Add train_and_evalaute.py 

# Add Report Folders - params.json and scores.json - if you havent added them before

```bash
dvc repro

dvc params diff

dvc metrics show

dvc metrics diff

git add . && git commit -m "tracker added"
git push origin main
```

# complete tox.ini

tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r 
```
pytest command
```bash
pytest -v
```
# Develop setup.py file
setup commands -
```bash
pip install -e . 

pip freeze  #to see what packages are installed in th elibrary
```


build your own package commands- 
```bash
python setup.py sdist bdist_wheel
```
# you can delete the dist folder created because it is not required

```bash
tox
```

# Push to repo
git add . && git commit -m "pytest and setup done"
git push origin main
