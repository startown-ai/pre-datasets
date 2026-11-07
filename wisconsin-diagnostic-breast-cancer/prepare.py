"""Prepare the Wisconsin Diagnostic Breast Cancer dataset and push it to Hugging Face."""

import argparse
import pathlib

import datasets
import huggingface_hub
import typeguard

SRC_URL = "https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip"
REPO_ID = "startown/wisconsin-diagnostic-breast-cancer"
SEED = 1

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--push", action="store_true", help=f"push to {REPO_ID}")
args = parser.parse_args()

src_dir = typeguard.check_type(
    value=datasets.DownloadManager().download_and_extract(SRC_URL),
    expected_type=str,
)
features = [
    "radius",
    "texture",
    "perimeter",
    "area",
    "smoothness",
    "compactness",
    "concavity",
    "concave_points",
    "symmetry",
    "fractal_dimension",
]
columns = (
    ["id", "diagnosis"]
    + [f"{feature}_mean" for feature in features]
    + [f"{feature}_standard_error" for feature in features]
    + [f"{feature}_worst" for feature in features]
)

dataset = typeguard.check_type(
    value=(
        datasets.Dataset.from_csv(f"{src_dir}/wdbc.data", header=None, names=columns)
        .remove_columns("id")
        .map(lambda row: {"diagnosis": 0 if row["diagnosis"] == "B" else 1})
        .cast_column("diagnosis", datasets.ClassLabel(names=["benign", "malignant"]))
        .train_test_split(test_size=0.2, seed=SEED, stratify_by_column="diagnosis")
    ),
    expected_type=datasets.DatasetDict,
)
print(dataset)

here = pathlib.Path(__file__).parent
for split, split_dataset in dataset.items():
    split_dataset.to_parquet(here / "data" / f"{split}.parquet")

if args.push:
    dataset.push_to_hub(REPO_ID, commit_message=f"feat: split with seed {SEED}")

    card = typeguard.check_type(
        value=huggingface_hub.DatasetCard.load(REPO_ID, "dataset"),
        expected_type=huggingface_hub.DatasetCard,
    )
    local = typeguard.check_type(
        value=huggingface_hub.DatasetCard.load(here / "README.md"),
        expected_type=huggingface_hub.DatasetCard,
    )
    for key, value in local.data.to_dict().items():
        card.data[key] = value
    card.text = local.text
    card.push_to_hub(
        repo_id=REPO_ID,
        repo_type="dataset",
        commit_message="docs: update dataset card",
    )
