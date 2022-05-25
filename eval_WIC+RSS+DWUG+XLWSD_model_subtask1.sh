#!/bin/bash
cd mcl-wic
ckpt=../WIC+RSS+DWUG+XLWSD/pytorch_model.bin
ckpt_path=$(dirname $ckpt)
part=../pairs_sub1
python -u run_model.py --max_seq_len=500 --do_eval --ckpt_path $ckpt_path --eval_input_dir $part/ \
  --eval_output_dir $ckpt_path/scores/$part/ --output_dir $ckpt_path
cd ..
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. APD method is used"
    python src/agg_scores_sub1_apd.py WIC+RSS+DWUG+XLWSD/pairs_sub1 pairs_sub1
    exit 0
fi
method=$1
pairs=$2 
if [ $method == APD ]; then
  python src/agg_scores_sub1_apd.py WIC+RSS+DWUG+XLWSD/${pairs} $pairs
fi
if [ $method == CC ]; then
  python src/agg_scores_sub1_cc.py WIC+RSS+DWUG+XLWSD/${pairs} $pairs
fi
