import json
import math

def dev(list, avg):
    temp = 0
    for i in list:
        dev = i - avg
        temp = temp + dev * dev
        if len(list) > 1:
            temp = float(temp) / (len(list) - 1)
    return temp


# Funzione per l'output dei dati su file
def output_file(dictionary, file_name):
    json_file = json.dumps(dictionary)
    with open(file_name, "w") as outfile:
        outfile.write(json_file)


# Calcolo dei valori giornalieri
def data_daily(data):
    days = []
    for key, value in data.items():
        if key == "daily":
            for i in range(0, len(value)):
                temp_list = [value[i]["temp"]["morn"], value[i]["temp"]["day"], value[i]["temp"]["eve"],
                             value[i]["temp"]["night"]]

                sum = temp_list[0] + temp_list[1] + temp_list[2] + temp_list[3]
                avg = sum / 4

                temp = dev(temp_list, avg)

                # Se il meteo premette pioggia verrà inserita la voce "rain", altrimenti no
                if "rain" in value[i]:
                    day = {
                        "type": "daily",
                        "stats": {
                            "min": round(value[i]["temp"]["min"], 1),
                            "max": round(value[i]["temp"]["max"], 1),
                            "avg": round(avg, 1),
                            "dev": round(math.sqrt(temp), 1),
                            "humidity": value[i]["humidity"],
                            "rain": value[i]["rain"]
                        }
                    }
                else:
                    day = {
                        "type": "daily",
                        "stats": {
                            "min": round(value[i]["temp"]["min"], 1),
                            "max": round(value[i]["temp"]["max"], 1),
                            "avg": round(avg, 1),
                            "dev": round(math.sqrt(temp), 1),
                            "humidity": value[i]["humidity"],
                        }
                    }
                days.append(day)
    return days


# Calcolo dei valori di ogni ora
def data_hourly(data):
    for key, value in data.items():
        if key == "hourly":
            temp_list = []
            sum_temp = 0
            sum_humidity = 0
            sum_rain = 0
            j = 0
            for i in range(0, len(value)):
                if i == 0:
                    min = value[i]["temp"]
                    max = value[i]["temp"]
                else:
                    if min > value[i]["temp"]:
                        min = value[i]["temp"]
                    if max < value[i]["temp"]:
                        max = value[i]["temp"]

                sum_temp = sum_temp + value[i]["temp"]
                sum_humidity = sum_humidity + value[i]["humidity"]
                if "rain" in value[i]:
                    sum_rain = sum_rain + value[i]["rain"]["1h"]
                    j += 1

                temp_list.append(value[i]["temp"])

            avg = sum_temp / len(value)
            temp = dev(temp_list, avg)

            # Se il meteo premette pioggia verrà inserita la voce "rain", altrimenti no
            if "rain" in value[i]:
                day = [{
                    "type": "hourly",
                    "stats": {
                        "min": round(min, 1),
                        "max": round(max, 1),
                        "avg": round(avg, 1),
                        "dev": round(math.sqrt(temp), 1),
                        "humidity": round(sum_humidity / len(value), 1),
                        "rain": round(sum_rain / j, 1)
                    }
                }]
            else:
                day = [{
                    "type": "hourly",
                    "stats": {
                        "min": round(min, 1),
                        "max": round(max, 1),
                        "avg": round(avg, 1),
                        "dev": round(math.sqrt(temp), 1),
                        "humidity": round(sum_humidity / len(value), 1),
                    }
                }]
    return day