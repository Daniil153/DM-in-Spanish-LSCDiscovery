#!/bin/bash
cd mcl-wic
ckpt=../WIC+RSS+DWUG+XLWSD/pytorch_model.bin
ckpt_path=$(dirname $ckpt)
part=../pairs_sub2
python -u run_model.py --max_seq_len=500 --do_eval --ckpt_path $ckpt_path --eval_input_dir $part/ \
  --eval_output_dir $ckpt_path/scores/$part/ --output_dir $ckpt_path
