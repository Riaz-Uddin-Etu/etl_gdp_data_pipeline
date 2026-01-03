def transform(df):
    df['GDP_USD_millions'] = round((df['GDP_USD_millions'] / 1000), 2)
    df = df.rename(columns={'GDP_USD_millions':'GDP_USD_billions'})
    return df