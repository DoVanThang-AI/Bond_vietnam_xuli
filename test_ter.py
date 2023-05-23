import random
def calculate_inflation(initial_sum, initial_year, final_year, inflation_data):
    years = range(initial_year, final_year + 1)
    adjusted_values = [initial_sum]

    for year in years[1:]:
        inflation_rate = inflation_data.get(year, 0)
        adjusted_value = adjusted_values[-1] * (1 + inflation_rate)
        adjusted_values.append(adjusted_value)

    return adjusted_values
def generate_random_list(start, end, length):
    random_list = [random.uniform(start, end) for _ in range(length)]
    return random_list
start = 0.02
end = 0.04
length = 21

random_values = generate_random_list(start, end, length)
inflation_data = {
    2000: 0.03,
    2001: 0.02,
    2002: 0.035,
    2003:random_values[0],
    2004:random_values[1],
    2005:random_values[2],
    2006:random_values[3],
    2007:random_values[4],
    2008:random_values[5],
    2009:random_values[6],
    2010:random_values[7],
    2011:random_values[8],
    2012:random_values[9],
    2013:random_values[10],
    2014:random_values[11],
    2015:random_values[12],
    2016:random_values[13],
    2017:random_values[14],
    2018:random_values[15],
    2019:random_values[16],
    2020:random_values[17],
    2021:random_values[18],
    2022:random_values[19],
    2023:random_values[20],



    # Add more years and corresponding inflation rates here
}

initial_sum = 1000
initial_year = 2010
final_year = 2022

adjusted_values = calculate_inflation(initial_sum, initial_year, final_year, inflation_data)

print(adjusted_values)

