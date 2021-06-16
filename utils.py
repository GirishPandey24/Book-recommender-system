def recommender(df,genre):
    '''
    recommend top rated book from same genre
    '''
    top= df[df['genre']==genre].sort_values(by='rating',ascending=False)
    if top.shape[0] > 1:
        return dict(top.iloc[0])
    else:
        return dict(df.sort_values(by='rating',ascending=False).iloc[:10].sample(1).squeeze())
