import pandas as pd
df1 = pd.read_csv('application_manifest.csv')
App_name = df1.loc[:,'AppShortName'].values[0]
schema = df1.loc[:,'Schema'].values[0]
df = pd.read_csv('CHR12345.csv')
print(df)
df.loc[:,'AppShortName'] = df.loc[:,'AppShortName'].fillna(App_name)
df.loc[:,'Schema'] = df.loc[:,'Schema'].fillna(schema)
print(df)
s_df = df.loc[df['Type'] == 'SQLSCRIPT']
j_df = df.loc[df['Type'] == 'JAVA']
u_df = df.loc[df['Type'] == 'UNIXSCRIPT']
s_df = s_df.sort_values(by=['Sequence'], ascending=True )
j_df = j_df.sort_values(by=['Sequence'], ascending=True )
u_df = u_df.sort_values(by=['Sequence'], ascending=True )
print(s_df)
print(j_df)
print(u_df)
s_df.to_csv('sqllist.csv', index=False)
j_df.to_csv('javalist.csv', index=False)
u_df.to_csv('unixlist.csv', index=False)

df = pd.concat(
    map(pd.read_csv, ['sqllist.csv','javalist.csv','unixlist.csv']),ignore_index=True
)
print (df)
df = df.sort_values(by=['Sequence'], ascending=True )
print (df)
df.to_csv('sourcevalidation.csv',index=False)




