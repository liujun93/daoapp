import pandas as pd

zhongyao = pd.read_csv('csv/中药.csv', dtype=str).fillna('', inplace=False)
yijing = pd.read_csv('csv/易经.csv', dtype=str).fillna('', inplace=False)

data = {
    "理中丸": "人参、干姜、甘草（炙）、白术各三两（9g）"
}


