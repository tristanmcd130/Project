import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

distances = pd.read_pickle("distances.pkl")
distances.replace(0, float("nan"), inplace=True)
order = [
	"en", "sv", "da", "de", "nl", # Germanic
	"ro", "fr", "it", "es", "pt", # Romance
    "lv", "lt", # Baltic
    "pl", "sk", "cs", "sl", "bg", # Slavic
]
distances = distances.loc[:, order].reindex(order)
sns.heatmap(distances)
plt.title("Average Angular Distance between Sentence Embeddings")
plt.show()