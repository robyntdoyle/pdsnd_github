import time
import datetime
import calendar
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
    while True:
        print('Which city would you like data from: chicago, new york city or washington?')
        city = input()
        city = city.lower()
        if city not in ['chicago', 'new york city', 'washington']:
             print('That is not a valid entry.')
        else:
            print('You entered the city: {}.'.format(city.title()))    
            break
     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('Which month would you like data for?')
        month = input()
        month = month.lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('That is not a valid entry.')
        else:
            print('You entered the month: {}.'.format(month.title()))
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Which day would you like data for?')
        day = input()
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print('You entered the day: {}.'.format(day.title()))
            break
        else:
            print('That is not a valid entry.')   
            
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    
    most_frequent_month = df['month'].mode()[0]
  
    print('Most common month (january, february, march, april, may, june):', most_frequent_month)
 
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    
    common_day = df['day'].mode()[0]
  
    print('Most common day (monday, tuesday, wednesday, thursday, friday, saturday, sunday):', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
  
    print('Most common hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    
    print('The most commonly used start station is: ',  common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    
    print('The most commonly used end station is: ',  common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    
    print('The count of user types is:\n', counts_user_types)

    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    
    print('The count of gender is: \n', counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    print('Earliest birth is: \n', earliest_birth)
    
    most_recent_birth = df['Birth Year'].max()
    print('Most recent birth is:\n', most_recent_birth)
    
    most_common_birth = df['Birth Year'].mode()[0]
    print('Most common birth year is:\n', most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    