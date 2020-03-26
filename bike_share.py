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

def data_stats(df):
    data_stats = input('Do you seek some statistics about your city data? Type yes or no... \n')
    if data_stats.lower() == 'yes':
        print('\nCalculating Some Stats about your city:. \n')
        start_time = time.time()
        col_names  = df.columns.values.tolist()
        descriptive_info = df.describe(exclude=[np.number])
        
        print('Columns names are: \n',col_names)
        print('-'*43)
        print('Some descriptive info about your city data: \n', descriptive_info)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*38)
    else:
        print('as you wish!')
        pass

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    time_stats = input('Do you seek some Time Statistics? Type yes or no...\n')
    if time_stats.lower() == 'yes':
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # extract hour from the Start Time column to create an hour column


        most_month          = df.loc[:,'Start Time'].dt.month_name().mode()[0]        
        most_common_day     = df.loc[:,'Start Time'].dt.day_name().mode()[0]

        most_comn_str_hours = pd.to_datetime(df.loc[:,'Start Time']).dt.hour.mode()[0]
        most_comn_end_hours = pd.to_datetime(df.loc[:,'Start Time']).dt.hour.mode()[0]       

        print('The Most Common Month          : ', most_month)
        print('The Most Common Day of Week    : ', most_common_day)
        print('The Most Common Start Hour     : ', most_comn_str_hours)
        print('The Most Common End Hour       : ', most_comn_end_hours)
        print('-'*43)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*37)
    else:
        print('as you wish!')
        pass

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    station_stats = input('Do you seek some station stats? Type yes or no... \n')
    if station_stats.lower() == 'yes':
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()
        most_str_station            = df['Start Station'].mode()[0]
        most_end_station            = df['End Station'].mode()[0]
        comn_str_end_station        = ('Start Station: '+df.loc[:,'Start Station']+ ', End Station: ' +df.loc[:,'End Station']).mode()[0]

        # TO DO: display most commonly used start station
        print('Most Commonly Used Start Station is    : ',most_str_station)
        print('Most Commonly Used End Station is      : ', most_end_station)
        print('Most Combinaton Start & End Station is : ', comn_str_end_station)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*39)
    else:
        print('As you wish!') 
        pass



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    trip_duration_stats = input('Do you seek some trip duration stats? Type yes or no...\n')
    if trip_duration_stats.lower() == 'yes':
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()
        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        min_travel_time  = df['Trip Duration'].min()
        max_travel_time  = df['Trip Duration'].max()
        comm_travel_time = df['Trip Duration'].mode()[0]

        print('Total Travel Time is : {} hour(s)'.format(total_travel_time//60))
        print('Max Travel Time is   : {} hour(s)'.format(max_travel_time//60))
        print('Min Travel Time is   : {} hour(s)'.format(min_travel_time//60))
        print('Common Travel Time is: {} hour(s)'.format(comm_travel_time//60))
        print('Mean Travel Time is  : {} hour(s)'.format(mean_travel_time//60))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*38)
    else:
        print('As you wish!')
        pass
	
def user_stats(df):
    """Displays statistics on bikeshare users."""
    user_stats = input('Do you seek some User Stats? Type yes or no...\n')
    if user_stats.lower() == 'yes':
        print('\nCalculating User Stats...\n')
        start_time      = time.time()

        total_users     = df['User Type'].count()
        tot_user_list   = df['User Type'].value_counts()

        tot_gender      = df['Gender'].count()
        tot_gender_list = df['Gender'].value_counts()

        birth_yar_cunt  = df['Birth Year'].count()
        recent_birth    = df['Birth Year'].min()
        earliest_birth  = df['Birth Year'].max()
        most_com_birth  = df['Birth Year'].mode()[0]

        # TO DO: Display counts of user types
        print('User Categories and numbers are... \n')

        print('User list: \n', tot_user_list)
        print('-'*29)
        #print('total users are  :  {}'.format(total_users))
        #print('-'*26, '\n')

        # TO DO: Display counts of gender
        print('User Gender and numbers are...\n')

        print('Total Gender list   : \n', tot_gender_list)
        print('-'*26)
        #print('Total Gender  :  {}'.format(tot_gender))
        #print('-'*23, '\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Years Recent, Earliest and most common...\n')

        print('Most Recent Birth Year is: ',recent_birth)
        print('Most Early Birth Year is : ',earliest_birth)
        print('Most Common Birth Year is: ',most_com_birth)    
        print('-'*34)
        print('Available rows           : ', birth_yar_cunt)
        print('-'*34, '\n')

        print("\nThis took %s seconds." % (time.time() - start_time))

    else:
        print('As you wish!')
        pass

def display_data(df):
    show_5_row = input('Do you want to see 5 raws of data? Type yes or no...\n')   
    if show_5_row.lower() == 'yes':
        print('\nRetrieving first 5 raws in your city...\n')
        start_time      = time.time()
        
        print(df.head(5))
        show_5_more = input('Do you seek next 5 raws? Type yes or no \n')
        if show_5_more.lower() == 'yes':
            print(df.iloc[5:11])
            show_raw = input('Do you seek raw by raw? type yes or no..\n')
            if show_raw == 'yes':
                for i in range(11, len(df)):
                    print(df.iloc[i])
            else:
                print('As you wish... no raws for you...')            
        else:
            print('don\'t push... no next 5 raws for you.')
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 35,'\n')
    else:
        print('ok no heads for you, it\'s enough.')
        pass

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head())
        

        data_stats(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()