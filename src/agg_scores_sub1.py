import pandas as pd
import json
import os
import fire

def agg_scores(r):
    if len(r) == 2:
        return (float(r[0]) + float(r[1])) / 2
    else:
        return float(r[0])

def submission_subtask1(path_to_scores):
    path_to_model = '/'.join(path_to_scores.split('/')[:-1])
    df_scores = pd.DataFrame()
    words = []
    scores = []
    for i in os.listdir(path_to_scores):
         if not i.endswith('scores'):
             continue
         f = open(f"{path_to_scores}/{i}")
         data = json.load(f)
         df = pd.DataFrame(data)
         df['agg_score'] = df['score'].apply(lambda r: agg_scores(r))
         scores.append(np.mean(list(df.agg_score)))
         temp_word = df.iloc[0]['id'].split('.')[1]
         words.append(temp_word)
    f = open("population_restricted.txt")
    tg_words = f.read().split('\n')[:-1]
    missed_words = list(set(tg_words).intersection(set(words)))
    words.extend(missed_words)
    scores.extend([0.5] * len(missed_words))
    df_scores['word'] = words
    df_scores['change_graded'] = scores
    df_scores['COMPARE'] = scores
    df_scores.to_csv(f"{path_to_model}/subtask1_submission.tsv", sep='\t')

if __name__ == '__main__':
    fire.Fire(submission_subtask1)
