import os
import pandas as pd
import json
import numpy as np
import random

def find_index(r, df):
    context = r['context']
    temp = df[df.sentence1 == context]
    if len(temp) == 0:
        temp = df[df.sentence2 == context]
        start = temp.iloc[0].start2
        end = temp.iloc[0].end2
    else:
        start = temp.iloc[0].start1
        end = temp.iloc[0].end1
    return f"{start}:{end}"


def create_data(path_to_pairs, path_to_pairs_preds, full_path='WUGs/test_uug/data'):
    path = path_to_pairs
    path2 = path_to_pairs_preds
    all_df = pd.DataFrame()
    for w in sorted(os.listdir(path)):
        if not w.endswith('.data'):
            continue
        word = w[:-5]
        f = open(f"{path}/{w}")
        data = json.load(f)
        df = pd.DataFrame(data)
        f.close()
        
        f2 = open(f"{path2}/test.{word}")
        
        bin_pred = json.load(f2)
        bin_df_gold = pd.DataFrame(bin_pred)
        merged_df = df.merge(bin_df_gold, how='inner', on='id')
    
        
        
        merged_df['word'] = [word] * len(merged_df)
        all_df = pd.concat([all_df, merged_df], ignore_index=True)
        
        merged_df['score'] = merged_df['tag'].apply(lambda r: 2 if r == 'T' else 1)
        
        os.makedirs(f"{full_path}/{word}", exist_ok=True)
        earl = merged_df[merged_df.grp == 'EARLIER']
        #comp = merged_df[merged_df.grp == 'COMPARE']
        late = merged_df[merged_df.grp == 'LATER']
        old_sents = list(set(list(earl.sentence1)).union(set(list(earl.sentence2))))
        new_sents = list(set(list(late.sentence1)).union(set(list(late.sentence2))))
        
        uses = pd.DataFrame()
        uses['context'] = old_sents + new_sents
        uses['lemma'] = [word] * len(uses)
        uses['pos'] = ['NOUN'] * len(uses)
        uses['grouping'] = ['old_corpus'] * len(old_sents) + ['new_corpus'] * len(new_sents)
        uses['date'] = ['old'] * len(old_sents) + ['new'] * len(new_sents)
        uses['identifier'] = [f"{word}.{grp}.{i}" for i, grp in enumerate(uses.grouping)]
        uses['description'] = [''] * len(uses)
        uses['indexes_target_token'] = uses.apply(lambda r: find_index(r, merged_df), axis=1)
        
        uses.to_csv(f"{full_path}/{word}/uses.csv", sep='\t')
        
        uses['identifier1'] = uses['identifier']
        uses['sentence1'] = uses['context']
        merged_df1 = merged_df.merge(uses, how="inner", on='sentence1')
        uses = uses.drop(columns=['identifier1', 'sentence1'])
        uses['identifier2'] = uses['identifier']
        uses['sentence2'] = uses['context']
        merged_df2 = merged_df1.merge(uses, how="inner", on='sentence2')
        merged_df2 = merged_df2[['id', 'start1', 'end1', 'start2', 'end2', 'sentence1', 'sentence2', 'grp', 'identifier1', 'identifier2', 'score']]
        
        judgments = pd.DataFrame()
        judgments = merged_df2[['identifier1', 'identifier2', 'score']]
        judgments = judgments.rename(columns={'score': 'judgment'})
        judgments['annotator'] = ['DeepMistake'] * len(judgments)
        judgments['comment'] = [''] * len(judgments)
        judgments['lemma'] = [word] * len(judgments)
        
        judgments.to_csv(f"{full_path}/{word}/judgments.csv", sep='\t')

if __name__ == '__main__':
    fire.Fire(create_data)
