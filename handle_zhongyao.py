from os import sep
import pandas as pd
import re
from glob import glob
from tqdm import tqdm

# df = pd.DataFrame(columns=['品类', '类型', '名称', '性味', '神农本草经文', '其他'])
# for path in glob(f'中药/神农本草经/*.txt'):
#     print(path)
#     pinglei, leixing = re.findall(r'中药/神农本草经/(.+?)\.txt', path)[0].split('-')
#     with open(path) as f:
#         data = f.read()

#     data = re.sub(r'\n（.+?）\n', '\n', data)
#     sentences = re.split(r"(\n.+?\n味)", data)
#     # sentences.append("")
#     sentences = sentences[0:1] + ["".join(i) for i in zip(sentences[1::2], sentences[2::2])]
#     for text in sentences:
#         # print(text)
#         name, att, _, content, other = text.strip().split('\n', maxsplit=4)
#         other = '\n'.join([other] + re.findall(r'（.+?）', content) + re.findall(r'（.+?）', att))
#         content = re.sub(r'（.+?）', '', content)
#         att = re.sub(r'（.+?）', '', att)
#         df.loc[df.shape[0]] = [pinglei, leixing, name, att, content, other]
#         # print(text, '\n-------')
# df.to_csv(f'中药/神农本草经/内容.csv', header=1, index=0)

df = pd.read_csv(f'中药/神农本草经/内容.csv')
df2 = pd.read_csv('中药/中药功效与主治.csv', sep='\t')

rdf = pd.DataFrame(columns=['品类', '类型', '名称', '性味', '神农本草经文', '功效与主治'])
rdf = rdf.append(df.loc[:, ['品类', '类型', '名称', '性味', '神农本草经文']])

for leixing, name, content in tqdm(zip(df2['类型'], df2['名称'], df2['功效与主治'])):
    ids = df[df['名称']==name].index.values.tolist()
    if not ids:
        rdf.loc[rdf.shape[0], ['类型', '名称', '功效与主治']] = [leixing, name, content]
    else:
        origin_leixing = rdf.loc[ids[0], '类型']
        rdf.loc[ids[0], ['类型', '功效与主治']] = [f'{origin_leixing}/{leixing}', content]

rdf.to_csv(f'csv/中药.csv', header=1, index=0)