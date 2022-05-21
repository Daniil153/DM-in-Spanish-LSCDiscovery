#!/bin/bash
cd mcl-wic
ckpt=../WIC+RSS+DWUG+XLWSD/pytorch_model.bin
ckpt_path=$(dirname $ckpt)
part=../pairs_sub2
python -u run_model.py --max_seq_len=500 --do_eval --ckpt_path $ckpt_path --eval_input_dir $part/ \
  --eval_output_dir $ckpt_path/scores/$part/ --output_dir $ckpt_path
cd ..
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. APD method is used"
    python src/agg_scores_sub2_apd.py WIC+RSS+DWUG+XLWSD/pairs_sub2 pairs_sub2
    exit 0
fi
for arg in "$@"
do
  if [ "$arg" == APD ]; then
    python src/agg_scores_sub2_apd.py WIC+RSS+DWUG+XLWSD/pairs_sub2 pairs_sub2
  fi
  if [ "$arg" == CC ]; then
    python src/agg_scores_sub2_cc.py WIC+RSS+DWUG+XLWSD/pairs_sub2 pairs_sub2
  fi
done
