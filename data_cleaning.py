import pandas as pd
df= pd.read_csv(r"C:\Users\sarvesh\Downloads\netflix_titles.csv")
print(df.head())
print(df.isnull().sum())
print(df.info())
print(df.describe())
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['duration'] = df['duration'].fillna('0 min')

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

text_columns = ['type', 'title', 'director', 'cast', 'country', 'rating', 'duration', 'listed_in', 'description']
for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')


df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

df['type'] = df['type'].astype('category')
df['rating'] = df['rating'].astype('category')
print(df.head())

print(df.dtypes)
df.to_csv('clean_data.csv', index=False)


