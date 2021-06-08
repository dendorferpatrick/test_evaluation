import pandas as pd
def evaluation():
    df = pd.read_csv("upload/data/upload.csv")
    df.to_csv("upload/output/results.csv")
    return 0

    