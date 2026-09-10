import json
import sys
from config import REPORTS_DIR

MIN_ACCURACY = 0.90

with open(REPORTS_DIR/"metrics.json") as f:
    metrics = json.load(f)

accuracy = metrics["accuracy"]
print(f"Model accuracy: {accuracy:.4f}")
print(f"Required accuracy: {MIN_ACCURACY:.4f}")

if accuracy < MIN_ACCURACY:
    print("FAILED: Model performance below threshold")
    sys.exit(1)

print("PASSED: Model performance acceptable")