#!/bin/bash
method=$1
pairs=$2
cd mcl-wic
ckpt=../WIC_DWUG+XLWSD/pytorch_model.bin
ckpt_path=$(dirname $ckpt)
part=../${pairs}
python -u run_model.py --max_seq_len=500 --do_eval --ckpt_path $ckpt_path --eval_input_dir $part/ \
  --eval_output_dir $ckpt_path/scores/$part/ --output_dir $ckpt_path
cd ..
if [ $method  == APD ]; then
  python src/agg_scores_sub1_apd.py WIC_DWUG+XLWSD/${pairs} ${pairs}
fi
if [ $method == CC ]; then
  python src/agg_scores_sub1_cc.py WIC_DWUG+XLWSD/${pairs} ${pairs}
fi
