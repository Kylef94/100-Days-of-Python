import pandas

# data = pandas.read_csv('weather_data.csv')
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# #
# # print(data['temp'].mean())
# #
# # max_val = data['temp'].max()
# # print(max_val)
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_list = data['Primary Fur Color']
counts = squirrel_list.value_counts()
counts = counts.to_list()

counts_dict = {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': counts}
counts_df = pandas.DataFrame.from_dict(data=counts_dict)
counts_df.to_csv('Color Counts')

