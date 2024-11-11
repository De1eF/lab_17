import pandas

series = pandas.read_json("task2/data.json", typ='series', orient='records')

def recursiveAverage(a):  
    if len(a) == 1:  
        return a[0]  
    else:  
        n = len(a)
        return (a[0] + (n - 1) * recursiveAverage(a[1:])) / n    

avrg = recursiveAverage(list(series[:len(series)]))

for k in series.keys():
    series[k] = series[k] - avrg

print(series)
