import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "data_given",
    "tests",
    "saved_models",
    "report",
    os.path.join("prediction_service","model"),
    os.path.join("webapp","static", "css"),
    os.path.join("webapp","static", "sctipt"),
    os.path.join("webapp","templates"),
    os.path.join(".github","workflows"),
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
    os.path.join("src", "get_data.py"),
    os.path.join("src", "load_data.py"),
    os.path.join("src", "split_data.py"),
    os.path.join("src", "train_and_evaluate.py"),
    os.path.join("report", "params.json"),
    os.path.join("report", "scores.json"),
    os.path.join("tests", "conftest.py"),
    os.path.join("tests", "test_config.py"),
    os.path.join("tests", "__init__.py"),
    os.path.join("prediction_service", "__init__.py"),
    os.path.join("prediction_service", "prediction.py"),
    os.path.join("prediction_service", "schema_in.json"),
    os.path.join("webapp","static", "css", "main.css"),
    os.path.join("webapp","static", "sctipt", "index.js"),
    os.path.join("webapp","templates", "index.html"),
    os.path.join("webapp","templates", "404.html"),
    os.path.join("webapp","templates", "base.html"),
    os.path.join(".github","workflows", "ci-cd.yaml"),
    "tox.ini",
    "setup.py",
    "app.py",
    "README.md"
]

for file_ in files:
    mode = 'a' if os.path.exists(file_) else 'w'
    with open(file_, mode) as f:
        pass
