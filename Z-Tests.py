import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import random
import csv

df=pd.read_csv("medium_data.csv")
data=df["id"].tolist()
population_mean=statistics.mean(data)
print("THE POPULATION MEAN IS:- {}".format(population_mean))
fig=ff.create_distplot([data],["id"],show_hist=False)
fig.show()

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for  i in range(0,100):
        set_of_means=random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

first_std_deviation_start, first_std_deviation_end=mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end=mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

fig=ff.create_distplot([mean_list],["id"],show_hist=False)
fig.add_trace(go.scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STD1S"))
fig.add_trace(go.scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STD1E"))
fig.add_trace(go.scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STD2S"))
fig.add_trace(go.scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STD2E"))
fig.add_trace(go.scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="STD3S"))
fig.add_trace(go.scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STD3E"))
fig.show()