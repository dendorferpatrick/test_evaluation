import pandas as pd
def evaluation(upload_folder ):
    df = pd.read_csv(upload_folder+"/data/upload.csv")
    df.to_csv(upload_folder+"/output/results.csv")
    return 0

    