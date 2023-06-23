import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').count()['age'].sort_values(ascending=False)

    # What is the average age of men?
    average_age_men = round(df['age'][df['sex'] == 'Male'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'][df['education'] == 'Bachelors'].count() / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    # count_higher = df['education'][df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()
    # count_higher_50k = df['education'][(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].count()
    # count_lower = df['education'][~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()
    # count_lower_50k = df['education'][(~df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')].count()
    #
    # # percentage with salary >50K
    # higher_education_rich = round(count_higher_50k / count_higher * 100, 1)
    # lower_education_rich = round(count_lower_50k / count_lower * 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']['salary'].count() / higher_education.shape[0]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']['salary'].count() / lower_education.shape[0]

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    count_min = df['salary'][df['hours-per-week'] == min_work_hours].count()
    count_min_50k = df['salary'][(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].count()
    rich_percentage = count_min_50k / count_min * 100

    # What country has the highest percentage of people that earn >50K?
    num_workers_bycountry = df.groupby('native-country').count()['salary']
    num_workers_bycountry_50k = df[df['salary'] == '>50K'].groupby('native-country').count()['salary']
    df2 = pd.DataFrame({'50k': num_workers_bycountry_50k, 'total': num_workers_bycountry})
    df2['percent'] = df2['50k'] / df2['total']
    result = df2[df2['percent'] == df2['percent'].max()]
    highest_earning_country = result.index[0]
    highest_earning_country_percentage = round(result['percent'][0] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    # num_popular = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')].groupby('occupation').count()['salary'].max()
    # df3 = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')].groupby('occupation').count().loc[:, ['salary']]
    # top_IN_occupation = df3[df3['salary'] == num_popular].index[0]

    s = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')].groupby('occupation').count()['salary']
    top_IN_occupation = s.loc[s == s.max()].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
