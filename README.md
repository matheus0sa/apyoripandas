# Apyori for Pandas

This package is designed to simplify the integration of the Apyori library with Pandas.

## Example Usage:

```python

from apyoripandas.apriori import Apriori
import pandas as pd

# Example Test
df_test = pd.read_csv('test.csv')

rules = Apriori(df_test, min_support=0.1, min_confidence=0.9, min_length=18)

```

In this example, the `rules` variable contains a Pandas DataFrame.