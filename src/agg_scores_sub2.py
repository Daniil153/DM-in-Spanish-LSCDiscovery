import pandas as pd
import json
import os
import fire
import numpy as np

def agg_scores(r):
    if len(r) == 2:
        return (float(r[0]) + float(r[1])) / 2
    else:
        return float(r[0])

def create_help_df(path):
    dict_df = dict()
    for i in os.listdir(path):
         f = open(f"{path}/{i}")
         data = json.load(f)
         tmp_df = pd.DataFrame(data)
         word = tmp_df.iloc[0]['id'].split('.')[1]
         dict_df[word] = tmp_df
    return dict_df

def submission_subtask1(path_to_scores, path_to_data):
    path_to_model = '/'.join(path_to_scores.split('/')[:-1])
    df_scores = pd.DataFrame()
    words = []
    scores = []
    help_df = create_help_df(path_to_data)
    for i in os.listdir(path_to_scores):
         if not i.endswith('scores'):
             continue
         f = open(f"{path_to_scores}/{i}")
         data = json.load(f)
         df = pd.DataFrame(data)
         temp_word = df.iloc[0]['id'].split('.')[1]
         
         df = df.merge(help_df, how='inner', on='id')
         df = df[df.grp == 'COMPARE']
         df['agg_score'] = df['score'].apply(lambda r: agg_scores(r))
         scores.append(np.mean(list(df.agg_score)))
         temp_word = df.iloc[0]['id'].split('.')[1]
         words.append(temp_word)
    df_scores['word'] = words
    df_scores['change_graded'] = scores
    df_scores['COMPARE'] = scores
    binary_scores = list(df_scores['change_graded'].apply(lambda r: 1 if r >= 0.5 else 0))
    df_scores['change_binary'] = binary_scores
    df_scores['change_binary_gain'] = binary_scores
    df_scores['change_binary_loss'] = binary_scores
    df_scores.to_csv(f"{path_to_model}/subtask2_submission_apd.tsv", sep='\t')

if __name__ == '__main__':
    fire.Fire(submission_subtask1)
