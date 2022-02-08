# how many grey, cinnamon, and black

# build new dataframe - create csv
import pandas

# data = pandas.read_csv("squirrel_count.csv")
#
# # fur color - count
#
# squirrels = data.value_counts("Primary Fur Color")
#
# squirrels.to_csv("squirrels.csv")

data = pandas.read_csv("squirrel_count.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels.csv")

