import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './chicago.csv',
              'new york city': './new_york_city.csv',
              'washington': './washington.csv' }

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
        try:
            city = pd.read_csv(CITY_DATA[input('Insert, which city you seek? \n cities are: chicago, new york city and washington\n').lower()])
        except KeyError:
            print('Invalid city name, please Enter your city again!!')
            continue
        break
      

    if 'Gender'and 'Birth Year' not in city.columns:
        city['Gender'] = 'NaN'
        city['Birth Year'] = 'NaN'

    while True:
        try:
            months = {'jan': 'january', 'feb': 'february', 'mar': 'march', 'apr': 'april',\
                      'may': 'may','jun': 'june', 'all': 'all'}
            month = (months[input('Insert, Which month you seek? jan, feb, mar ...\n').lower()])
        except KeyError:
            print('Invalid month name, Enter which month again!!')
            continue
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            days = {'sat': 'saturday', 'sun': 'sunday', 'mon': 'monday', 'tue': 'tuesday',\
                      'wed': 'wednesday','thu': 'thursday','fri': 'friday','all': 'all'}
            day = (days[input('Insert, Which day you seek? sat, sun, mon ...\n').lower()])
        except KeyError:
            print('Invalid day name, Enter which day again!!')
            continue
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

    # load data file into a dataframe
    df = city

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august', 'september', 'october', 'novemeber', 'december']
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
    df['End Time']   = pd.to_datetime(df['End Time'])

    # extract hour from the Start Time column to create an hour column

    df['str_date']   = df['Start Time'].dt.date
    df['str_year']   = df['Start Time'].dt.year
    df['str_month']  = df['Start Time'].dt.month_name(locale = 'English')
    df['str_day']    = df['Start Time'].dt.day_name(locale = 'English')
    df['str_hour']   = df['Start Time'].dt.hour
    df['str_minute'] = df['Start Time'].dt.minute
    df['str_second'] = df['Start Time'].dt.second
    df['end_date']   = df['End Time'].dt.date
    df['end_year']   = df['Start Time'].dt.year
    df['end_month']  = df['Start Time'].dt.month_name(locale = 'English')
    df['end_day']    = df['Start Time'].dt.day_name(locale = 'English')
    df['end_hour']   = df['End Time'].dt.hour
    df['end_minute'] = df['End Time'].dt.minute
    df['end_second'] = df['End Time'].dt.second

    most_month            = df['str_month'].mode()[0]
    popular_hour          = df['str_hour'].mode()[0]
    most_common_day       = df['str_day'].mode()[0]

    print('the most common month          : ',most_month)
    print('the most common day of week    : ', most_common_day)
    print('the most common start hour     : ', popular_hour)
    print('-'*41)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*37)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_str_station            = df['Start Station'].mode()[0]
    most_end_station            = df['End Station'].mode()[0]
    

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station is   : ',most_str_station)
    print('Most Commonly Used End Station is     : ', most_end_station)
    print('Most Frequent Start and End station is: {} and {}'.format(most_str_station ,most_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*37)
	
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Total Travel Time is: ', total_travel_time)
    print('Mean Travel Time is : ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*22)
	
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time     = time.time()
    
    total_users    = df['User Type'].count()
    tot_subscriber = df['User Type'].value_counts()['Subscriber']
    tot_customer   = df['User Type'].value_counts()['Customer']
    tot_dependent  = df['User Type'].value_counts()['Dependent']
    
    tot_gender     = df['Gender'].count()
    tot_Male       = df['Gender'].value_counts()['Male']
    tot_Female     = df['Gender'].value_counts()['Female']
    
    birth_yar_cunt = df['Birth Year'].count()
    recent_birth   = df['Birth Year'].min()
    earliest_birth = df['Birth Year'].max()
    most_com_birth = df['Birth Year'].mode()[0]
    
    # TO DO: Display counts of user types
    print('User Categories and numbers are... \n')

    print('total subscribers: ', tot_subscriber)
    print('total Customers  : ', tot_customer)
    print('total Dependent  : ', tot_dependent)
    print('-'*26)
    print('total users are  :  {}'.format(total_users))
    print('-'*26, '\n')
    
    # TO DO: Display counts of gender
    print('User Gender and numbers are...\n')

    print('Total Males   : ', tot_Male)
    print('Total Female  : ', tot_Female)
    print('-'*23)
    print('Total Gender  :  {}'.format(tot_gender))
    print('-'*23, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    print('Birth Years Recent, Earliest and most common...\n')
    
    print('Most Recent Birth Year is: ',recent_birth)
    print('Most Early Birth Year is : ',earliest_birth)
    print('Most Common Birth Year is: ',most_com_birth)    
    print('-'*33)
    print('Available Birth years    :', birth_yar_cunt)
    print('-'*33, '\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*38)


#     tot_dependent  = df['User Type'].value_counts()['Dependent'] it's not there in some monthes.

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head(5))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
		
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()