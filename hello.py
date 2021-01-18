import pandas as pd
from stemgraphic import stem_graphic

filename = "Data/StemAndLeaf1.txt"

df = open(filename, "r")

stem_graphic(df['40'], scale=5);