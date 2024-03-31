from apyori import apriori as ap
import pandas as pd

def Apriori(dataframe, min_support=0.1, min_confidence=0.9, min_lift=1, min_length=18):
    '''
    Apriori function for association rule mining using the Apyori library.

    Parameters:
    -----------
    dataframe : pandas DataFrame
        Input DataFrame containing transaction data.

    min_support : float, optional
        Minimum support threshold for itemsets to be considered frequent. Default is 0.1.

    min_confidence : float, optional
        Minimum confidence threshold for generating association rules. Default is 0.9.

    min_lift : float, optional
        Minimum lift threshold for generating association rules. Default is 1.

    min_length : int, optional
        Minimum length of the itemsets to consider. Default is 18.

    Returns:
    --------
    pandas DataFrame
        DataFrame containing the association rules with columns:
        - items: The combined items of the itemset.
        - items_base: The base items of the association rule.
        - items_add: The added items of the association rule.
        - support: The support value of the itemset.
        - confidence: The confidence value of the association rule.
        - lift: The lift value of the association rule.
    '''
    df = dataframe.copy()
    df = df.astype(str)
    for i in df.columns:
        df[i] = f'{i} = ' + df[i]
    data = df.values
    results = list(ap(data, 
                      min_support=min_support,
                      min_confidence=min_confidence, 
                      min_lift=min_lift, 
                      min_length=min_length))
    
    if not(results): return None
    
    df2 = pd.DataFrame(results)

    df2['items_base'] = df2.ordered_statistics.str[0].str[0]
    df2['items_add'] = df2.ordered_statistics.str[0].str[1]
    df2['confidence'] = df2.ordered_statistics.str[0].str[2]
    df2['lift'] = df2.ordered_statistics.str[0].str[3]

    df2.drop(columns=['ordered_statistics'], inplace=True)

    return df2[['items', 'items_base', 'items_add', 'support', 'confidence', 'lift']]