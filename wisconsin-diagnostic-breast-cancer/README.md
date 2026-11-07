---
license: cc-by-4.0
pretty_name: Wisconsin Diagnostic Breast Cancer (WDBC)
size_categories:
  - n<1K
task_categories:
  - tabular-classification
---

# Wisconsin Diagnostic Breast Cancer (WDBC)

This tabular dataset contains 569 breast masses, each sampled by fine-needle aspiration (FNA) and diagnosed as benign or malignant. Each row holds the diagnosis and 30 features of the cell nuclei in a digitized image of the sample.

## Usage

```python
import datasets

dataset = datasets.load_dataset("startown/wisconsin-diagnostic-breast-cancer")
```

## Columns

`diagnosis` is the label: `0` for benign and `1` for malignant, converted from the original `B` and `M`.

The other 30 columns describe the nuclei. On each image, several nuclei are outlined, and 10 features are measured on each one:

| Feature             | Description                                              |
| ------------------- | -------------------------------------------------------- |
| `radius`            | mean distance from the center to points on the perimeter |
| `texture`           | standard deviation of gray-scale values                  |
| `perimeter`         | length of the nuclear contour                            |
| `area`              | number of pixels inside the contour                      |
| `smoothness`        | local variation in radius lengths                        |
| `compactness`       | perimeter² / area − 1                                    |
| `concavity`         | severity of concave portions of the contour              |
| `concave_points`    | number of concave portions of the contour                |
| `symmetry`          | difference in length between opposite radial lines       |
| `fractal_dimension` | "coastline approximation" − 1                            |

Three columns summarize each feature over the nuclei of an image: `<feature>_mean` is the mean, `<feature>_standard_error` the standard error, and `<feature>_worst` the mean of the three largest values. For example, `radius_mean`, `radius_standard_error`, and `radius_worst` summarize the radii of the nuclei in one image. Values have four significant digits, and none are missing.

## Splits

The samples are split 80/20 into training and test sets, stratified by diagnosis with seed 1. The original ID column is dropped.

| Split   | Samples | Benign (`0`) | Malignant (`1`) |
| ------- | ------: | -----------: | --------------: |
| `train` |     455 |          285 |             170 |
| `test`  |     114 |           72 |              42 |

## Source

The data is from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic). To cite it, use:

```bibtex
@misc{breast_cancer_wisconsin_(diagnostic)_17,
  author       = {Wolberg, William and Mangasarian, Olvi and Street, Nick and Street, W.},
  title        = {{Breast Cancer Wisconsin (Diagnostic)}},
  year         = {1993},
  howpublished = {UCI Machine Learning Repository},
  note         = {{DOI}: https://doi.org/10.24432/C5DW2B}
}
```
