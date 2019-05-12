import pygal


def stats():
    with open("info.txt", encoding="utf-8") as f:
        data = f.readlines()
        names = data[0].split(", ")
        values = data[1].split(", ")
    # print(data)
    print(names)
    print(values)
    line_chart = pygal.Bar(show_legend=False)
    line_chart.title = 'Deputies'
    for i in data:
        print(i)
        try:
            line_chart.add(i.split(", ")[0], float(i.split(", ")[1]))
        except:
            pass

    return line_chart


if __name__ == "__main__":
    stats()
