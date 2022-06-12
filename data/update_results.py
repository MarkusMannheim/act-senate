import pandas as pd

votes = pd.read_csv(
    "https://tallyroom.aec.gov.au/Downloads/SenateInformalByStateDownload-27966.txt",
    sep="\t",
    header=1,
    usecols=[0, 2, 4]
)
votes_formal = votes.at[6, "FormalVotes"]
votes_total = votes.at[6, "TotalVotes"]
votes_counted = votes_total / 314329

results = pd.read_csv(
    "https://tallyroom.aec.gov.au/Downloads/SenateFirstPrefsByStateByGroupByVoteTypeDownload-27966.txt",
    sep="\t",
    header=0
)
update = results.columns[0][
    results.columns[0].index("Generated:") + 10 :
    results.columns[0].index("Generated:") + 29
]

results = pd.read_csv(
    "https://tallyroom.aec.gov.au/Downloads/SenateFirstPrefsByStateByGroupByVoteTypeDownload-27966.txt",
    sep="\t",
    header=1,
    usecols=[0, 1, 2, 14]
)
results = results[results["StateAb"] == "ACT"].loc[:, "GroupAb":]
results.loc[len(results)] = ["notes", update, votes_counted]
results.to_csv("./latest_results.csv", index=False)
