# Build the Project

Goal: establish a production-style ML repository before introducing automation.

Flow:
raw data -> preprocess -> train -> model artifact

Run:
```bash
pip install -r requirements.txt
python src/preprocess.py
python src/train.py
```
# Data Engineering

Industry-style flow:

incoming batch
    -> validate
    -> reject to quarantine OR promote to raw/iris.csv
    -> preprocess
    -> train

The ingestion job is the entry point:

```bash
python src/ingest_batch.py data/incoming/iris_batch_good.csv
```

Bad data:
```bash
python src/ingest_batch.py data/incoming/iris_batch_bad.csv
```
