new_df = new_df.reset_index()

#method1
#making a new df to apply correlation
corr_df = pd.DataFrame()
corr_df = new_df[['business_stars','user_stars']]
np.correlate(corr_df["business_stars"], corr_df["user_stars"])

#method2
#correlation-1 
new_df.corr()

#correlation-2
new_df.corr(method='kendall')

#correlation-3
new_df.corr(method='spearman')
