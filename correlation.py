#making a new df to apply correlation
new_df = new_df.reset_index()
corr_df = pd.DataFrame()
corr_df = new_df[['business_stars','user_stars']]

#correlation-1 
new_df.corr()

#correlation-2
new_df.corr(method='kendall')

#correlation-3
new_df.corr(method='spearman')
