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
git clone https://github.com/Garrafao/WUGs #todo: rev
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
bash src/change_WUG.sh
bash eval_WIC_DWUG+XLWSD_model_subtask2.sh CC
```

## Results
Results of the LSCD task are presented in the following table. To reproduce them, follow the instructions above to install the correct dependencies. 


<table>
    <thead>
        <tr>
            <th rowspan=1><b>Model</b></th>
            <th colspan=1><b>RuShiftEval avg</b></th>
            <th colspan=1><b>RuShiftEval1</b></th>
            <th colspan=1><b>RuShiftEval2</b></th>
            <th colspan=1><b>RuShiftEval3</b></th>
            <th colspan=1><b>Script</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>MCL+RSS+DWUG_es<sup>bin2</sup><sub>ALL</sub></td>
            <td>0.795</td>
            <td>0.812</td>
            <td>0.78</td>
            <td>0.795</td>
            <td>eval_best_eval_model.sh</td>
        </tr>
        <tr>
            <td>mean+dist_l1ndotn-hs0 on MCL<sup>nen-acc</sup><sub>CE</sub> &rarr; RSS<sup>dev2-sentSpear</sup><sub>MSE</sub>, Mean (https://zenodo.org/record/4992633/files/mean_dist_l1ndotn_MSE.zip)</td>
            <td>0.833</td>
            <td>0.839</td>
            <td>0.834</td>
            <td>0.826</td>
            <td>eval_2best_post-eval_model.sh</td>
        </tr>
        <tr>
            <td>mean+dist_l1ndotn-hs0 on MCL<sup>nen-acc</sup><sub>CE</sub> &rarr; RSS<sup>dev2-sentSpear</sup><sub>CE</sub>, Mean (https://zenodo.org/record/4992613/files/mean_dist_l1ndotn_CE.zip)</td>
            <td>0.85</td>
            <td>0.863</td>
            <td>0.854</td>
            <td>0.834</td>
            <td>eval_best_post-eval_model.sh</td>
        </tr>
    </tbody>
</table>


## Train models
Also you can train the best three models with 
```shell script
train_WIC+RSS+DWUG+XLWSD_model.sh
train_WIC_DWUG+XLWSD_model.sh
train_WIC_RSS_model.sh
```
