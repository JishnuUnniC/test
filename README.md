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
# DVC

Industry-style behavior:

new approved data
    -> promoted to data/raw/iris.csv
    -> DVC detects changed dependency
    -> dvc repro reruns only invalidated stages
    -> preprocessing reruns
    -> training reruns
    -> model is regenerated

Local trigger:
```bash
python src/ingest_batch.py data/incoming/iris_v2.csv
```

CI trigger:
`.github/workflows/data-pipeline.yml` runs the DVC pipeline when data/DVC metadata changes are pushed.