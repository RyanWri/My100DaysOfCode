import pandas as pd

def main():
    df = pd.read_csv("My100DaysOfCode/Day25/weather_data.csv")
    temprature = df["temp"]
    print(temprature)


if __name__ == "__main__":
    main()