import sys

from dbconnection.oracle import Connector
from sql.queries_templates import quotes
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

def transform(labels_, groups):
    new_l = []
    for element in labels_:
        if element >= groups:
            new_l.append(-1)
        else:
            new_l.append(element)
    return numpy.array(new_l)

def splitData(data, group_marks, max_groups=None):
    g_marks = numpy.copy(group_marks)
    if len(data) != len(g_marks):
        raise Exception("Data size should bew equal group mark size")

    if max_groups is not None:
        for i in range(0, len(g_marks)):
            if g_marks[i] >= max_groups:
                g_marks[i] = -1

    groups_id = set(g_marks)

    groups = {}
    for group_id in groups_id:
        groups[group_id] = []
        indexes, = numpy.where(g_marks == group_id)
        for index in indexes:
            groups[group_id].append(data[index])
        groups[group_id] = numpy.array(groups[group_id])
    return groups

config = {
    "ip": '10.0.3.199',
    "port": '1521',
    "user": 'FUZZY_SEARCH',
    "password": '123456',
    "tnsname": 'TEST'
}

connector = Connector(config)

sql = quotes["ROUTE_SUM_DAY_OF_YEAR"]["sql_template"].format(route_name='SU1210')
su36_df = connector.executeDataFrame(sql)
su36_df.ON_DAY = pd.to_numeric(su36_df.ON_DAY, errors='coerce')

data = su36_df[["ON_DAY", "SUM_VALUES"]].values

clustering = DBSCAN(eps=15, min_samples=1).fit(data)

groups = splitData(data, clustering.labels_, max_groups = 1)

for group_id in groups:
    x = groups[group_id][:, 0]
    y = groups[group_id][:, 1]
    if group_id == -1:
        plt.scatter(x, y, c='black', label="Anomaly data")
    else:
        plt.scatter(x, y, c='greenyellow', label="Normal data") #numpy.full((1, len(x)), group_id)[0]

plt.title("Route SU1210")
plt.xlabel("Day of the year")
plt.ylabel("Passengers count")
plt.legend()
plt.show()
