# TTSG

<!-- <div align="center">
    <img src="./files/TTSG_framework.png" width="70%" height="auto" />
</div> -->

## Env

Run the following command to create the required conda environment:

```
conda create -n TTSG python=3
conda activate TTSG
conda install pytorch cudatoolkit=11 -c pytorch
```

All dependencies can be installed via:

```
pip install -r requirements.txt
```

## Datasets

### 20News Group

The 20News Group dataset can be accessed from [here](https://huggingface.co/datasets/SetFit/20_newsgroups) and the downloaded file is placed in the `data` directory.

### BBC News

The BBC News dataset can be accessed from [here](https://huggingface.co/datasets/SetFit/bbc-news) and the downloaded file is placed in the `data` directory.


## How to run script

### Summary Generation
```
python BRIO/run_summary.py
```
In this section, we use the [BRIO](https://github.com/yixinL7/BRIO) approach to generate summaries.


### Document Summary Clustering
```
python k-cloest.py
```

### Topic Sentence Generation
```
bash centrum/topic.sh
```
Here, we use [Centrum](https://github.com/ratishsp/centrum) method to generate topic sentences.

## Acknowledgement

We appreciate [BRIO](https://github.com/yixinL7/BRIO), [Centrum](https://github.com/ratishsp/centrum) and many other related works for their open-source contributions.
