import random
from statistics import mean, median, mode, pstdev, pvariance, stdev, variance
from tv_series import TVSeries

the_office = TVSeries("The Office", {
    1 : 6,
    2 : 22,
    3 : 25,
    4 : 19,
    5 : 28,
    6 : 26,
    7 : 26,
    8 : 24,
    9 : 25},
    22,
    2005,
    2012,
    False,
    "Comedy",
    "Netflix")

community = TVSeries("Community", {
    1 : 25,
    2 : 24,
    3 : 22,
    4 : 13,
    5 : 13,
    6 : 13},
    22,
    2009,
    2015,
    False,
    "Comedy",
    "Amazon Prime")

game_of_thrones = TVSeries("Game of Thrones", {
    1 : 10,
    2 : 10,
    3 : 10,
    4 : 10,
    5 : 10,
    6 : 10,
    7 : 7,
    8 : 6},
    50,
    2011,
    2019,
    False,
    "Drama, Adventure",
    "Crave -> HBO")

final_space = TVSeries("Final Space", {
    1 : 10,
    2 : 13},
    22,
    2018,
    2020,
    True,
    "Comedy, Sci-fi",
    "Netflix")

parks_and_rec = TVSeries("Parks and Recreation", {
    1 : 6,
    2 : 24,
    3 : 16,
    4 : 22,
    5 : 22,
    6 : 22,
    7 : 13},
    22,
    2009,
    2015,
    False,
    "Comedy",
    "Prime TV")

silicon_valley = TVSeries("Silicon Valley", {
    1 : 8,
    2 : 10,
    3 : 10,
    4 : 10,
    5 : 8,
    6 : 7},
    22,
    2014,
    2019,
    False,
    "Comedy",
    "Crave -> HBO")

brooklyn_9_9 = TVSeries("Brooklyn Nine-Nine", {
    1 : 22,
    2 : 23,
    3 : 23,
    4 : 22,
    5 : 22,
    6 : 18,
    7 : 13},
    22,
    2013,
    2020,
    True,
    "Comedy",
    "Netflix")

workaholics = TVSeries("Workaholics", {
    1 : 10,
    2 : 10,
    3 : 20,
    4 : 13,
    5 : 13,
    6 : 10,
    7 : 10},
    22,
    2011,
    2017,
    False,
    "Comedy",
    "Crave")
    
trailer_park_boys = TVSeries("Trailer Park Boys", {
    1 : 6,
    2 : 7,
    3 : 8,
    4 : 8,
    5 : 10,
    6 : 6,
    7 : 10,
    8 : 10,
    9 : 10,
    10 : 10,
    11 : 10,
    12 : 10},
    22,
    2001,
    2018,
    False,
    "Comedy",
    "Netflix")
    
arrested_development = TVSeries("Arrested Develpoment", {
    1 : 22,
    2 : 18,
    3 : 13,
    4 : 15,
    5 : 16},
    22,
    2003,
    2019,
    False,
    "Comedy",
    "Netflix")
    
chernobyl = TVSeries("Chernobyl", {
    1 : 5},
    60,
    2019,
    2019,
    False,
    "Drama, Documentary",
    "Crave -> HBO")

breaking_bad = TVSeries("Breaking Bad",{
    1 : 7,
    2 : 13,
    3 : 13,
    4 : 13,
    5 : 16},
    50,
    2008,
    2013,
    False,
    "Drama, Thriller",
    "Netflix")
    
black_mirror = TVSeries("Black Mirror", {
    1 : 3,
    2 : 3,
    3 : 6,
    4 : 6,
    5 : 3},
    60,
    2011,
    2019,
    False,
    "Drama, Sci-fi",
    "Netflix")
    
better_call_saul = TVSeries("Better Call Saul", {
    1 : 10,
    2 : 10,
    3 : 10,
    4 : 10,
    5 : 10},
    50,
    2015,
    2020,
    True,
    "Drama, Law",
    "Netflix")
    
the_it_crowd = TVSeries("The IT Crowd", {
    1 : 6,
    2 : 6,
    3 : 6,
    4 : 7},
    22,
    2006,
    2013,
    False,
    "Comedy, Tech",
    "Netflix")
    
avatar_last_airbender = TVSeries("Avatar, the Last Airbender", {
    1 : 20,
    2 : 20,
    3 : 21},
    22,
    2005,
    2008,
    False,
    "Drama, Adventure",
    "Netflix")
    
peaky_blinders = TVSeries("Peaky Blinders", {
    1 : 6,
    2 : 6,
    3 : 6,
    4 : 6,
    5 : 6},
    50,
    2013,
    2020,
    True,
    "Drama, Period",
    "Netflix")
    
curb_your_enthusiasm = TVSeries("Curb your Enthusiasm", {
    1 : 10,
    2 : 10,
    3 : 10,
    4 : 10,
    5 : 10,
    6 : 10,
    7 : 10,
    8 : 10,
    9 : 10,
    10 : 10},
    30,
    2000,
    2020,
    True,
    "Comedy",
    "Crave -> HBO")
    
letterkenny = TVSeries("Letterkenny", {
    1 : 6,
    2 : 6,
    3 : 6,
    4 : 6,
    5 : 6,
    6 : 6,
    7 : 6,
    8 : 7},
    22,
    2016,
    2020,
    True,
    "Comedy",
    "Crave")
	
prison_break = TVSeries("Prison Break", {
    1 : 22,
	2 : 22,
	3 : 13,
	4 : 24,
	5 : 9},
	42,
	2005,
	2017,
	False,
	"Drama, Thriller",
	"Netflix")
	
scrubs = TVSeries("Scrubs", {
	1 : 24,
	2 : 22,
	3 : 22,
	4 : 25,
	5 : 24,
	6 : 22,
	7 : 11,
	8 : 19,
	9 : 13},
	22,
	2001,
	2010,
	False,
	"Comedy",
	"Prime TV")
	
yugioh = TVSeries("Yu-Gi-Oh!", {
	1 : 49,
	2 : 48,
	3 : 47,
	4 : 40,
	5 : 52},
	22,
	1998,
	2006,
	False,
	"Anime",
	"Prime TV")
	
misfits = TVSeries("Misfits", {
	1 : 6,
	2 : 7,
	3 : 8,
	4 : 8,
	5 : 8},
	44,
	2009,
	2013,
	False,
	"Comedy",
	"Netflix")

series_list = [
    the_office,
    community,
    game_of_thrones,
    final_space,
    parks_and_rec,
    silicon_valley,
    brooklyn_9_9,
    workaholics,
    trailer_park_boys,
    arrested_development,
    chernobyl,
    breaking_bad,
    black_mirror,
    better_call_saul,
    the_it_crowd,
    avatar_last_airbender,
    peaky_blinders,
    curb_your_enthusiasm,
    letterkenny,
	prison_break,
	scrubs,
	yugioh,
	misfits]
   
def longest_series_title(series_list) :
    num = 0
    for series in series_list :
        name = series.name
        if len(name) > num :
            num = len(name)
    return num
    
metric_possibilities = [
    "start year",
    "end year",
    "shortest series run length",
    "longest series run length",
    "least number seasons",
    "most number seasons",
    "least number episodes",
    "most number episodes",
    "shortest time",
    "longest time"
    ]
    
def ask_print_style(series_list) :
    question = "\n\tHow would you like to print the stats?\n"
    for i in range(len(metric_possibilities)) :
        question += str(i + 1) + "\t-\tBy " + metric_possibilities[i] + "\n" 
        
    selection = input(question + "\n")
    metric = None
    if (len(selection) == 0 or len(selection) > 2) :
        print("\nNo sorting performed\n")
        return metric
    try :
        selection = int(selection)
    except :
        print("\nNo sorting performed\n")
        return metric
    
    if selection == 1 :
        print("\nsorting by start year...\n")
        metric = (False, lambda s : s.start_year, metric_possibilities[0])
    elif selection == 2 :
        print("\nsorting by end year...")
        metric = (False, lambda s : s.end_year, metric_possibilities[1])
    elif selection == 3 :
        print("\nsorting by shortest series length...\n")
        metric = (False, lambda s : s.calc_series_run(), metric_possibilities[2])
    elif selection == 4 :
        print("\nsorting by longest series length...\n")
        metric = (True, lambda s : s.calc_series_run(), metric_possibilities[3])
    elif selection == 5 :
        print("\nsorting by least number of seasons...\n")
        metric = (False, lambda s : s.number_seasons(), metric_possibilities[4])
    elif selection == 6 :
        print("\nsorting by most number of seasons...\n")
        metric = (True, lambda s : s.number_seasons(), metric_possibilities[5])
    elif selection == 7 :
        print("\nsorting by least number of episodes...\n")
        metric = (False, lambda s : s.count_episodes(), metric_possibilities[6])
    elif selection == 8 :
        print("\nsorting by most number of episodes...\n")
        metric = (True, lambda s : s.count_episodes(), metric_possibilities[7])
    elif selection == 9 :
        print("\nsorting by shortest time...\n")
        metric = (False, lambda s : s.how_long_is_series()[1], metric_possibilities[8])
    elif selection == 10 :
        print("\nsorting by longest time...\n")
        metric = (True, lambda s : s.how_long_is_series()[1], metric_possibilities[9])
    else :
        print("\nNo sorting performed\n")
    
    return metric
        
def print_time_line_horizontal(series_list, start_year, end_year) :
    metric = ask_print_style(series_list)
    metric_val = ""
    if metric :
        rev_val = metric[0]
        sort_metric = metric[1]
        metric_val = metric[2]
        series_list.sort(reverse=rev_val, key=sort_metric)
        
    longest_title_len = longest_series_title(series_list) + len("\t")
    space_border = "".join(["#" for i in range(longest_title_len)])
    
    year_border = space_border
    year_border += "| " + metric_val + " " if metric else "" 
    year_border += "|" + "|".join([str(i) for i in range(start_year, end_year + 1)]) + "|"
    year_border += " " + metric_val + " |" if metric else "" 
    year_border += space_border
    
    top_border = "".join(["#" for i in range(len(year_border))])
    res = top_border + "\n" + year_border + "\n"
    
    for series in series_list :
        res += "|" + "{0:{1}}".format(series.name, longest_title_len - 1)
        if metric :
            value = sort_metric(series)
            int_val = int(value)
            float_val = float(value)
            # print("value BEFORE: " + str(value) + ", int_val: " + str(int_val) + ", float_val: " + str(float_val))
            if int_val != float_val :
                value = "{0:^{1}f}".format(sort_metric(series), len(metric_val))
            else :
                value = str(value)
            # print("after AFTER: " + str(value))
            # else :
            res += "|{0:^{1}s}".format(value, (len(metric_val) + 2))
        for year in range(start_year, end_year + 1) :
            res += "|"
            if series.start_year <= year and year <= series.end_year :
                res += "".join(["*" for i in range(len(str(year)))])
            else :
                res += "".join([" " for i in range(len(str(year)))])
        if metric :
            value = sort_metric(series)
            int_val = int(value)
            float_val = float(value)
            # print("value BEFORE: " + str(value) + ", int_val: " + str(int_val) + ", float_val: " + str(float_val))
            if int_val != float_val :
                value = "{0:^{1}f}".format(sort_metric(series), len(metric_val))
            else :
                value = str(value)
            # print("after AFTER: " + str(value))
            # else :
            res += "|{0:^{1}s}".format(value, (len(metric_val) + 2))
        res += "|" + "{0:{1}}".format(series.name, longest_title_len - 1) + "|\n"
    res += top_border
    return res
	
def print_series_stats(series_list) :
    metric = ask_print_style(series_list)
    metric_val = ""
    if metric :
        rev_val = metric[0]
        sort_metric = metric[1]
        metric_val = metric[2]
        series_list.sort(reverse=rev_val, key=sort_metric)
        
    longest_title_len = longest_series_title(series_list) + len("\t")
    top_border = "".join(["#" for i in range(longest_title_len + len(metric_val) + 4)])
    space_border = "".join(["#" for i in range(longest_title_len)])
    res = top_border + "\n"
    res += space_border + "| " + metric_val + " |\n"
    
    for series in series_list :
        res += "|" + "{0:{1}}".format(series.name, longest_title_len - 1)
        if metric :
            value = sort_metric(series)
            int_val = int(value)
            float_val = float(value)
            # print("value BEFORE: " + str(value) + ", int_val: " + str(int_val) + ", float_val: " + str(float_val))
            if int_val != float_val :
                value = "{0:^{1}f}".format(sort_metric(series), len(metric_val))
            else :
                value = str(value)
            # print("after AFTER: " + str(value))
            # else :
            res += "|{0:^{1}s}".format(value, (len(metric_val) + 2))
        else :
            res += "|{0:^{1}s}".format("-", (len(metric_val) + 2))
        res += "|\n"
    res += top_border
    if metric :
	# median', 'median_grouped', 'median_high', 'median_low', 'mode', 'numbers', 'pstdev', 'pvariance', 'stdev', 'variance'
      stats_list = [sort_metric(series) for series in series_list]
      res += "\n\nMean:\t\t" + "{0:6.2f}".format(mean(stats_list))
      res += "\nMedian:\t\t" + "{0:6.2f}".format(median(stats_list))
      res += "\nPstdev:\t\t" + "{0:6.2f}".format(pstdev(stats_list))
      res += "\nPvariance:\t" + "{0:6.2f}".format(pvariance(stats_list))
      res += "\nStdev:\t\t" + "{0:6.2f}".format(stdev(stats_list))
      res += "\nVariance:\t" + "{0:6.2f}".format(variance(stats_list))
    return res

if __name__ == "__main__" :
  for series in series_list :
    print(series)
    
  selected_series = random.choice(series_list)
  print("\n\n\tWhat to watch?\n")
  print("Series:\n" + str(selected_series))
  selected_season = random.choice([seasonKey for seasonKey in selected_series.episodes_list.keys()])
  print("\nSeason: " + str(selected_season))
  selected_episode = random.choice([i for i in range(1, selected_series.episodes_list[selected_season] + 1)])
  print("Episode: " + str(selected_episode))
    
    
  for i in range(10) :
    print(print_time_line_horizontal(series_list, 1995, 2021))
    print(print_series_stats(series_list))