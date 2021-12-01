import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "data_given",
    "saved_models",
    "report",
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
    "README.md"
]

for file_ in files:
    mode = 'a' if os.path.exists(file_) else 'w'
    with open(file_, mode) as f:
        pass
