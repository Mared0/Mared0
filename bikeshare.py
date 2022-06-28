import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    City_Name =['chicago' ,'new york city' ,'washington']
    Months = ['january', 'february', 'march', 'april', 'may', 'june']
    Days=['all', 'saturday' , 'sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    city = input('Please enter the desired city name [ Chicago, New York City, Washington ]').lower()
    while city not in City_Name :
        city = input('Please enter the desired city name [ Chicago, New York City, Washington ]').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the desired month [January, February, March, April, May, June ]').lower()
    while month not in Months:
        month = input('Please enter the desired month [January, February, March, April, May, June ]').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the desired day [All, Saturday , Monday, Tuesday, Wednesday, Thursday, Friday ]').lower()
    while day not in Days :
        day = input('Please enter the desired day [All, Saturday , Monday, Tuesday, Wednesday, Thursday, Friday ]').lower()

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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common travelling month is :',df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('The most common travelling day is :',df['week day'].mode()[0])


    # TO DO: display the most common start hour
    print('The most common travelling hour is :',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    "Displays statistics on the most popular stations and trip."

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commomly start station is :-',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commomly end station is :-',df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('The most commomly combination of start station and end station is :-',(df['Start Station']+' '+df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    'Displays statistics on the total and average trip duration.'

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(' The total traveling time = ',df['Trip Duration'].sum() , ' Seconds')

    # TO DO: display mean travel time
    print(' The Average traveling time = ',df['Trip Duration'].mean() , ' Seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    'Displays statistics on bikeshare users.'

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if city != 'washington':
    # TO DO: Display counts of user types
        print(' The Summary of users type is :-')
        print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
        print(' The Summary of users gender is :-')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print(' The earliest year of birth is ',df['Birth Year'].min())
        print(' The most recent year of birth is ',df['Birth Year'].max())
        print(' The most common year of birth is ',df['Birth Year'].mode()[0])
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return 

def view_data(df):
    print('Do you want to view 5 row of individual trip dat ? press yes or no \n')
    answer = input('please enter yes to view 5 row if individual trip or no\n').lower()
    start_loc = 0
    while str(answer) == 'yes' :
            print(df.iloc[start_loc:(start_loc + 5)])
            start_loc += 5
            answer = input("Do you want another 5 rows of individual trip data ? press yes or no \n").lower()
    
    print('-'*40)                       
    return answer

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
