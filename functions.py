import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats


# budget0, genres1, homepage2, id3, keywords, original_language, original_title, overview, popularity 8 ,
# production_companies, production_countries, release_date 11, revenue 12 , runtime13, spoken_lang, status,
# tagline, title, vote_average 18, vote_count


def get_data():
    with open('Q:\\OneDrive\\Projects\\Prob.Theory\\Lab.3\\tmdb.csv', encoding="utf_8_sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = {"budget": list(), "popularity": list(), "release": list(), "revenue": list(), "runtime": list(),
                "vote_average": list(), "vote_count": list(), "id": list()}

        for row in csv_reader:
            if int(row[0]) <= 1000000 or row[13] == "" or float(row[8]) > 200 or float(row[12]) < 100000:
                continue
            data["budget"].append(float(row[0]))
            data["popularity"].append(float(row[8]))
            data["id"].append(float(row[3]))
            data["release"].append(row[11])
            data["runtime"].append(float(row[13]))
            data["revenue"].append(float(row[12]))
            data["vote_average"].append(float(row[18]))
            data["vote_count"].append(float(row[-1]))
    print(np.min(data['popularity']))
    print(np.max(data['popularity']))
    print(np.min(data['revenue']))
    print(np.max(data['revenue']))
    print(np.min(data['revenue']))
    print(np.max(data['revenue']))
    return data


def get_koefs(data, par1, par2):
    temp_mean_x = np.mean(data[par1])
    temp_mean_y = np.mean(data[par2])

    temp_mult = 0
    temp_der_x = 0
    temp_der_y = 0

    for i in range(len(data[par1])):
        temp_mult += (data[par1][i] - temp_mean_x) * (data[par2][i] - temp_mean_y)
        temp_der_x += (data[par1][i] - temp_mean_x) ** 2
        temp_der_y += (data[par2][i] - temp_mean_y) ** 2
    temp_der_x *= temp_der_y
    temp_der_x = np.sqrt(temp_der_x)
    res = temp_mult / temp_der_x

    print("Корреляция " + str(par1) + "/" + str(par2) + "=" + str(res))
    print("Проверим гипотезу о наличии линейной коллеряционной связи")
    print(
        "Нулевая гипотеза: Rген = 0 и наша гипотеза Rген != 0, где Rген - коэффициент корреляции в генеральной совокупности")
    print("t наблюдаемое = r*sqrt(n-2)/sqrt(1-r^2)")
    print("t наблюдаемое = " + str(res * np.sqrt(len(data[par1]) - 2) / np.sqrt(1 - res ** 2)))
    print("t критическое = 1.96, с " + str(len(data[par1]) - 2) + " степенями свободы")
    if (res * np.sqrt(len(data[par1]) - 2) / np.sqrt(1 - res ** 2)) >= 1.96:
        print(
            "Так как t наблюдаемое больше t критического, можно сделать вывод что линейный коэффициент корреляции"
            " значим и есть существование взаимосвязи между двумя выборками")
    else:
        print(
            "Так как t наблюдаемое меньше t критического, можно сделать вывод что линейный коэффициент корреляции"
            " не значим и взаимосвязи между двумя факторами нету")
    print()
    print_plot(data, par1, par2)


def regression_analize(data, param1, param2):
    x = data[param1]
    y = data[param2]

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(param1 + "/" + param2)
    print("Уравнение вида Y = а * Х + b")
    print("Уравнение вида Y = " + str(round(slope, 3)) + " * X + " + str(round(intercept, 3)))
    print("Коэффициент наклона прямой (a) = " + str(slope))
    print("Свободный член (b) = " + str(intercept))
    print("Коэффициент корелляция = " + str(r_value))
    print("Коэффициент детерминации = " + str(r_value ** 2))
    print("Остатки = " + str(std_err))
    print()
    sb.regplot(x, y, scatter_kws={'s': 2})
    plt.show()


def print_plot(data, param1, param2):
    temp_data1 = data[param1].copy()
    temp_data2 = data[param2].copy()

    temp_data1 = np.array(temp_data1).astype(np.float)
    temp_data2 = np.array(data[param2]).astype(np.float)
    plt.xlim(np.min(temp_data1), np.max(temp_data1))
    plt.ylim(np.min(temp_data2), np.max(temp_data2))
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.scatter(temp_data1, temp_data2, s=1)
    plt.show()
