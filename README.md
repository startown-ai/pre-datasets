# pre-datasets

![License](https://img.shields.io/github/license/startown-ai/pre-datasets?style=flat-square)

From original data to ready-to-use datasets on [Hugging Face](https://huggingface.co/startown). Each folder downloads one dataset from its source, prepares it, and publishes it.

## Datasets

| Dataset                                                                         | Source                                                                           | Hugging Face                                                                                                               |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Wisconsin Diagnostic Breast Cancer (WDBC)](wisconsin-diagnostic-breast-cancer) | [UCI](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) | [startown/wisconsin-diagnostic-breast-cancer](https://huggingface.co/datasets/startown/wisconsin-diagnostic-breast-cancer) |

## Usage

Open the repository in its dev container, built on [`startown/workspace-py`](https://github.com/startown-ai/workspace-py), and run a dataset's script:

```bash
uv run wisconsin-diagnostic-breast-cancer/prepare.py
```

It writes the splits to the dataset's `data/` folder. To publish them, log in with a Hugging Face token that can write to the `startown` organization, and add `--push`:

```bash
uv run wisconsin-diagnostic-breast-cancer/prepare.py --push
```

## License

This repository is licensed under the [Apache License 2.0](LICENSE). Each dataset keeps the license of its source, given in its README.
