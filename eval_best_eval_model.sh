#!/bin/bash
cd mcl-wic
python run_model.py --do_eval --ckpt_path ../WIC_RSS --eval_input_dir ../pairs_sub1 --eval_output_dir rusemshift_predictions/ --output_dir ../WIC_RSS --loss crossentropy_loss --pool_type mean --symmetric true --train_scd 
cd ..
mkdir -p sampled_data
mkdir -p sampled_data/score
mkdir -p sampled_data/ans
mv first_concat/rusemshift_predictions/*.scores sampled_data/score/
mv first_concat/rusemshift_predictions/* sampled_data/ans/ 
python src/constr.py --type mean --model_name first_concat
python src/mean_method.py --model_name first_concat
python src/statistics_method.py --model_name first_concat
python src/iso_method.py --model_name first_concat
