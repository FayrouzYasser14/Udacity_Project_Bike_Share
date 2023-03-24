import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
months = ['january','february','march','april','may','june','july','august',
         'september','october','november', 'december','all']
days= ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city you would like to have data about? : ").lower()
        if city not in CITY_DATA:
            city = input("Please choose from chicago, new york city"
                       " , washington (write the full name)").lower()
        if city in CITY_DATA:
            print(city)
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month you would like to have data about?"
                      " or type 'all' if no specific month : ").lower()
        if month not in months:
            month = input("Please choose the correct month (write the full name)").lower()
        if month in months:
            print(month)
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day you would like to have data about?"
                    "or type 'all' if no specific day : ").lower()
        if day not in days:
            day = input("Please choose the correct day (write the full name)").lower()
        if day in days:
            print(day)
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #convert startdate (String) column  to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract month and day to new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    #print(df.columns)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()
    print('Most Popular month:', popular_month)
    # display the most common day of week
    popular_day = df['day'].mode()
    print('Most Popular day:', popular_day)
    # display the most common start hour
    popular_hour = df['Start Time'].mode()
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('common start station:', common_start_station)
    common_end_station = df['End Station'].mode()
    print('common end station:', common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('total trip duration:', total_trip_duration)
    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('mean trip duration:', mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_userType = df['User Type'].value_counts()
    print('counts of user type:', count_userType)

    # Display counts of gender
    if CITY_DATA == 'washington':
        print('No gender data for this city')

    else:
        count_gender = df['Gender'].value_counts()
        print('counts of gender:', count_gender)


    # Display earliest, most recent, and most common year of birth
    mean_birth_year = df['Birth Year'].mode()
    most_recent_birthYear = df['Birth Year'].max()
    earliest_birthYear = df['Birth Year'].min()

    print('mean birth year:', mean_birth_year)
    print('most recent birth year:', most_recent_birthYear)
    print('earliest birth year:', earliest_birthYear)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df.head())

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        while True:
            view_data = input('Would you like to view 5 rows of data? (yes or No)')
            print(df.iloc[i: i + 5])
            if view_data != 'yes':
               break
            i += 5



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

# used sources: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# used sources: https://careerkarma.com/blog/python-syntaxerror-return-outside-function/
# used sources: https://github.com/ozlerhakan/bikeshare/blob/master/bikeshare.py
# used sources: problems from course website
