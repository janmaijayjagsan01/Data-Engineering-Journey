import pandas  as pd

df = pd.read_csv("weather_data.csv")  #read_csv()  → df mein load kiya

print("===RAW DATA===")   #print(df)  → poora data dekha
print(df)

print("\n===SHAPE (rows,columns)===")     #shape  → size check kiya
print(df.shape)

print("\n===DATA TYPES===")   #dtypes →  har column ka data type check kiya
print(df.dtypes)

print("\n===COLUMN NAMES===")     #columns → headings dekhe
print(df.columns.tolist())

print("\n===BASIC DTATS ===")
print(df.describe())                    #describe() → numbers ka analysis kiya


# ===== 1. FILTER =====
print("\n=== HOT CITIES ONLY ===")
hot = df[df['status'] == 'Hot']          #df[df['status'] == 'Hot'] = sirf wahi rows jahan status Hot hai    #soch Excel ka filter button — same kaam Python mein!
print(hot[['city', 'temp_celsius']])


# ===== 2. SORT =====
print("\n=== HOTTEST CITY PEHLE ===")
sorted_df = df.sort_values('temp_celsius', ascending=False)        #sort_values('temp_celsius', ascending=False) = temperature ke hisaab se upar se neeche sort karo  ascending=False = sabse bada pehle, ascending=True = sabse chhota pehle
print(sorted_df[['city', 'temp_celsius']])


# ===== 3. GROUPBY =====
print("\n=== AVG TEMP BY STATUS ===")
print(df.groupby('status')['temp_celsius'].mean())
print(df.groupby('status')['city'].count())

#FILTER   → konsi rows chahiye?     df[df['col'] == 'value']
#SORT     → kis order mein?         df.sort_values('col')
#GROUPBY  → group karke kya?        df.groupby('col').mean()
#SAVE     → kahan save karo?        df.to_csv('file.csv')



## to save the result in csv file

# sorted data save karo
sorted_df.to_csv('sorted_weather_data.csv', index=False)
print("sorted_cities.csv ")
# hot ciies save karo
hot.to_csv('hot_cities.csv', index=False)
print("hot_cities.csv ")


#group results save karo
groupby_df = df.groupby('status')['temp_celsius'].mean().reset_index()  #reset_index() → groupby ke baad index reset kar diya
groupby_df.columns = ['status', 'avg_temp']
groupby_df.to_csv("avg_temp_by_status.csv", index=False)
print("avg_temp_by_status.csv ban gayi!")


print("\n CSV file done!")