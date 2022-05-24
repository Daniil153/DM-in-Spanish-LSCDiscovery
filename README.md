in process...

# Lexical Semantic Change Detection (LSCD) for the Spanish language by the DeepMistake team.
Lexical semantic change detection

This repository contains code to reproduce the best results from the paper:

Daniil Homskiy, Nikolay Arefyev. DeepMistake at LSCDiscovery: Can a Multilingual Word-in-Context Model Replace Human Annotators? 2022.

DeepMistake was 2nd best system in the [Lexical Semantic Change Discovery Shared Task](https://codalab.lisn.upsaclay.fr/competitions/2243#participate).

# Citation
If you use any part of the system, please, cite our paper above.

# Reproduction of the best results

## Installation
Clone repositories:
```shell script
git clone https://github.com/Daniil153/DeepMistake
cd DeepMistake
git clone https://github.com/ameta13/mcl-wic
git clone https://github.com/Garrafao/WUGs
```
Install requirements 
```shell script
pip install -r mcl-wic/requirements.txt
pip install -r WUGs/requirements.txt
 ```
## The solution for the LSCDiscovery Task.
Download data from the command line:
```shell script
bash download_files.sh
```
Download models: 
```shell script
bash download_models.sh WIC+RSS+DWUG+XLWSD WIC_DWUG+XLWSD WIC_RSS
```
To reproduce the best result in evaluation for the 1st phase (graded subtask) you need use:
```shell script
bash eval_WIC_RSS_model_subtask1.sh APD
```
To reproduce the best result in post evaluation for the 1st phase (graded subtask) you need use:
```shell script
bash eval_WIC+RSS+DWUG+XLWSD_model_subtask2.sh APD
```
To reproduce second the best result in post evaluation for the 1st phase (graded subtask) you need use:
```shell script
bash eval_WIC_DWUG+XLWSD_model_subtask2.sh APD
```

To reproduce the best result in post evaluation for the 2nd phase (binary subtask) you need use:
```shell script
bash eval_WIC_DWUG+XLWSD_model_subtask2.sh APD
```

To evaluate the model with Corellation clustering you need use:
```shell script
bash eval_WIC_DWUG+XLWSD_model_subtask2.sh CC
```

## Train models
Also you can train the best three models with 
```shell script
train_WIC+RSS+DWUG+XLWSD_model.sh
train_WIC_DWUG+XLWSD_model.sh
train_WIC_RSS_model.sh
```
