#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pretty prints monthly tide data from NOAA download."""

__license__ = "MIT"


import requests
import datetime
import json
import os
from configparser import ConfigParser


def load_config_file(f_path, CONFIG_FILE):
    """ Converts a ConfigParser file into three specific dicts.

    The sections of the config file must be as follows:
    MINMAX format: str: float.
    STATIONS format: int: str.
    PATHS format: str: str.

    Args:
        f_path (str): path to the config file.
        CONFIG_FILE (str): name of the config file.

    Returns:
        3 dicts if successful: minmax, stations, & paths.
        3 None if unsuccessful.
    """
    f_path = '{0}/{1}'.format(f_path, CONFIG_FILE)
    config = ConfigParser(allow_no_value=True, empty_lines_in_values=False)
    with open(f_path) as file:
        config.read_file(file)
    try:
        # print stmts here help identify invalid sections
        print('MINMAX loading')
        minmax = {item[0]:float(item[1]) for item in config.items('MINMAX')}
        print('STATIONS loading')
        stations = {int(item[0]):item[1] for item in config.items('STATIONS')}
        print('PATHS loading')
        paths = {item[0]:item[1] for item in config.items('PATHS')}
    except:
        print('Error in config.ini')
        return None, None, None
    if not os.path.isdir(paths['json_data_dir']):
        print('directory missing: {0}'.format(paths['json_data_dir']))
        return None, None, None
    return minmax, stations, paths


def get_print_day_tic(date_in):
    """ Returns six *s if date == now() month & day else returns ''.

    Args:
        date_in (str or int): a date using YYYYMMDD format.

    Returns
        ****** as string if current date match.
        '' if current date is not matched.
    """
    now_mn = int(datetime.datetime.now().strftime('%m'))
    now_dy = int(datetime.datetime.now().strftime('%d'))
    try:
        in_mn = int(str(date_in)[4:6])
        in_dy = int(str(date_in)[6:])
    except:
        return ''
    if in_mn != now_mn: return ''
    if in_dy != now_dy: return ''
    return ('*' * 6)

def print_tides_month_minmax_ranges(data, month, minmax):
    """ Prints the monthly min/max tide ranges using the tides dict.

    Args:
        data (specific dict format): tides prediction data from NOAA.
        month (int): month number.
        minmax (specific dict format): dict with min/max range limits.
    """
    # get rounded monthly min/max value
    tmin, tmax = find_yearly_or_monthly_minmax(data, month)
    tmin, tmax = round(tmin, 1), round(tmax, 1)
    # calculate min/max limits using within values
    limit_min = round(tmin + minmax['min_within'], 1)
    limit_max = round(tmax - minmax['max_within'], 1)
    # pretty print min/max ranges
    print('min range: {0} to {1}'.format(tmin, limit_min))
    print('max range: {0} to {1}\n'.format(limit_max, tmax))


def print_tides_month_detail(data, month):
    """ Prints one line from the tides data dict for each tide in a month.

    Line highlights are: !0 yearly min/max, 2) Monthly min/max,
    3) Sundays, and 4) Current date.

    Args:
        data (specific dict format): tides prediction data from NOAA.
        month (int): month number.
    """
    last = ''
    for key, item in sorted(data.items()):
        if int(item['date'][5:7]) != month: continue
        day_tic = get_print_day_tic(item['date'].replace('-', ''))
        day_tic += '' if item['abbrev'] != 'Sun' else ('<' * 3)
        if last != item['date'] and len(last) > 0: print('---')
        last = item['date']
        mm_tic = False
        # fixed order for steps used to set mm_tic is important
        # yearly min/max is first
        if item['max_yr']: mm_tic = '(max for year)'
        if item['min_yr']: mm_tic = '(-min for year)'
        # monthly highest/lowest is second
        if not mm_tic and item['max_mn']: mm_tic = '(max for month)'
        if not mm_tic and item['min_mn']: mm_tic = '(-min for month)'
        # min/max within limits is last
        if not mm_tic and item['max_limit']: mm_tic = '(max)'
        if not mm_tic and item['min_limit']: mm_tic = '(-min)'
        mm_tic = '' if not mm_tic else mm_tic
        # tic allows for number alignment given "-" used for low tides
        tic = '' if item['tide'] < 0 else ' '
        print('{0}: {1} {2} ({3}) = {4}{5:0.3f} {6} {7}'.format(
            item['abbrev'],
            item['date'],
            item['time'],
            item['type'],
            tic,
            item['tide'],
            mm_tic,
            day_tic))


def get_print_yyyy_mn():
    """ Prompts for a YYYYMM date or a return for current YYYYMM.

    Returns:
        yyyy, mm input value as ints.
        None, None if input is invalid.
    """
    selected = input('enter YYYYMM, return=current year-month: ')
    if len(selected) == 0:
        yyyy = int(datetime.datetime.now().strftime('%Y'))
        mn = int(datetime.datetime.now().strftime('%m'))
    else:
        try:
            yyyy = int(selected[0:4])
            mn = int(selected[4:])
        except:
            print('invalid input')
            return None, None
    if mn < 1 or mn > 12:
        print('invalid input')
        return None, None
    return yyyy, mn


def get_start_end_dates(yyyy, month):
    """Converts yyyy & month to start & end date YYYYMMDD strings.

    The gap for the end date is fixed at 30 days which is the max
    data request allowed by NOAA (just covers a 31 day month).

    Args:
        yyyyy (int or str): year value.
        month (int or str): month value.

    Returns:
        start, end dates as YYYYMMDD strings.
    """
    selected = '{0}{1:02d}01'.format(yyyy, month)
    s = datetime.datetime.strptime(selected, '%Y%m%d')
    delta = datetime.timedelta(days=30)
    e = s + delta
    start = '{0}{1}{2}'.format(s.strftime('%Y'),
                               s.strftime('%m'), 
                               s.strftime('%d'))
    end =   '{0}{1}{2}'.format(e.strftime('%Y'), 
                               e.strftime('%m'), 
                               e.strftime('%d'))
    return start, end


def get_noaa_url(start, end, station):
    """ Formats url with params for tides request from NOAA.

    Args:
        start (int or str): YYYYMMDD start date.
        end (int or str): YYYYMMDD end date (max 30 days from start).
        station (int or str): NOAA station ID.

    Returns:
        URL for NOAA tides call as string.
    """
    base_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?'
    parameters = [
        'station={0}'.format(station),
        'begin_date={0}'.format(start),
        'end_date={0}'.format(end),
        'product=predictions',
        'application=NOS.COOPS.TAC.WL',
        'time_zone=lst_ldt',
        'datum=MLLW',
        'units=english',
        'interval=hilo',
        'format=json'
    ]
    return '{0}{1}'.format(base_url, '&'.join(parameters))


def print_tides_yearly_min_max(data):
    """ Finds & prints the yearly min/max tides from a specific dict.

    Args:
        data: tides prediction data from NOAA (specific dict format).
    """
    amax = ''
    amin = ''
    for key, value in data.items():
        if value['max_yr']:
            tmax = value['tide']
            dmax = key
            amax = value['abbrev']
        if value['min_yr']:
            tmin = value['tide']
            dmin = key
            amin = value['abbrev']
    print('Yearly max & min tides:\n')
    print('{0:0.3f} = min tide (feet) {1} ({2})'.format(tmin, dmin, amax))
    print('{0:0.3f} = max tide (feet) {1} ({2})'.format(tmax, dmax, amax))


def load_noaa_data_to_json(yyyy, f_path, station, minmax):
    """ Create new tides dict, and json.dump the tides & minmax dicts.

    The tides data dict and the minmax within limits dict are combined
    into a single dict which is then json.dump()'ed as a text file. 

    Args:
        yyyyy (int or str): year value.
        f_path (str): path to the config file.
        station (int or str): NOAA station ID.
        minmax (specific dict format): dict with min/max range limits.

    Returns:
        data as tides data dict.
        None if response to exit NOAA load is yes.
    """
    print('---\ndata file not found: {0}'.format(f_path))
    if input('exit program (y=exit, ret=load data file): ').lower() == 'y':
        return None
    data = load_yyyy_tides_data_file(yyyy, station, minmax)
    if data:
        json_data = {'minmax': minmax, 'data':data}
        with open(f_path, 'w') as outfile:
            json.dump(json_data, outfile)
    print('load complete\n---')
    return data


def load_yyyy_tides_data_file(yyyy, station, minmax):
    """ Processes 12 months of url calls to NOAA for tide predictions.

    Both processes the url request/response, and calls two functions
    to update the flags in the tides data dict to identify hi/lo
    yearly and monthly tide. (those within the minmax ranges).

    Args:
        yyyyy (int or str): year value.
        station (int or str): NOAA station ID
        minmax (specific dict format): dict with min/max range limits.

    Returns:
        data as tides data dict.
        None if there is an error calling the NOAA url.
    """
    print('---load data start---')
    data = {}
    for mn in range(1, 13):
        start, end = get_start_end_dates(yyyy, mn)
        url = get_noaa_url(start, end, station)
        tides_request = requests.get(url)
        if tides_request.status_code != 200:
            print('---error for url: status code={0}\n{1}'.format(
                tides_request.status_code, url))
            return None
        print('{0} status: {1}'.format(start, tides_request.status_code))
        if tides_request.text.find('"error"') > -1:
            # json error text from url call is readable w/o formatting
            print(tides_request.text)
            return None
        data.update(convert_tides_data_to_dict(tides_request.json(), yyyy))
    data = set_yearly_min_max_tides(data)
    data = find_monthly_min_max_tides(data, minmax)
    return data


def convert_tides_data_to_dict(json_in, yyyy):
    """ Converts the NOAA json url response to an enhanced data dict.

    The data dict adds to the NOAA data: day abbrev, flags for monthly
    and yearly minimum & maximum tides. It also uses the keys 'tide' &
    'type' to replace NOAA's 'v' & 't' keys. The NOAA 'date time' key
    is used for the dict key, and broken into 'date' and 'time' values.

    Args:
        json_in (str): json text response from NOAA ties prediction.
        yyyyy (int or str): year value in.
        minmax (specific dict format): dict with min/max range limits.

    Returns:
        data as tides data dict.
    """
    data = {}
    tides_list = []
    for item in json_in['predictions']:
        t_yymm = item['t'].split(' ')[0]
        if int(yyyy) != int(t_yymm[0:4]): continue
        t_time = item['t'].split(' ')[1]
        d_t = datetime.datetime.strptime(item['t'], '%Y-%m-%d %H:%M')
        tides_list.append({
            'date' : t_yymm,
            'time' : t_time,
            'tide' : float(item['v']),
            'type' : item['type'],
            'abbrev' : d_t.strftime('%a'),
            'max_mn' : False,
            'min_mn' : False,
            'max_yr' : False,
            'min_yr' : False,
            'min_limit' : False,
            'max_limit' : False
        })
    for tide in tides_list:
        key = '{0} {1}'.format(tide['date'], tide['time'])
        data[key] = tide
    return data

def find_yearly_or_monthly_minmax(data, month):
    """ Find yearly or monthly Hi/Lo tides in a tides data dict.

    Args:
        data (specific dict format): tides prediction data from NOAA.
        month (bool): True for monthly min/max otherwise False;

    Returns:
        min, max values as ints.
    """
    tmin, tmax = 0.0, 0.0
    for key, item in sorted(data.items()):
        # skip items not in month if month is an integer (1-12)
        if month and month != int(item['date'][5:7]): continue
        tide = item['tide']
        if tide < tmin: tmin, dmin = tide, key
        if tide > tmax: tmax, dmax = tide, key
    return tmin, tmax


def set_yearly_min_max_tides(data):
    """ Sets the specific tides data dict yearly min/max flag.

    Each tide prediction item in the data dict will be checked,
    and the appropriate min/max flags set to True if tide is the
    yearly Hi/Lo value.  

    Args:
        data (specific dict format): tides prediction data from NOAA.

    Returns:
        updated tides data as a dict.
    """
    tmin, tmax = find_yearly_or_monthly_minmax(data, False)
    dmax, dmin = '', ''
    for value in data.values():
        if value['tide'] >= tmax: value['max_yr'] = True
        if value['tide'] <= tmin: value['min_yr'] = True
    return data


def find_monthly_min_max_tides(data, minmax):
    """ Sets the specific tides data dict monthly min/max flag.

    Each tide prediction item in the data dict will be checked,
    and the appropriate min/max flags set to True if tide is the
    within the minmax limit of the monthly Hi/Lo minmax. One item
    has a flag set for having the month's highest/lowest tide.

    Args:
        data (specific dict format): tides prediction data from NOAA.
        minmax (specific dict format): dict with min/max range limits.

    Returns:
        updated tides data as a dict.
        None if minmax within limits entries have an error.
    """
    try:
        min_within = minmax['min_within']
        max_within = minmax['max_within']
    except:
        print('max_within and/or min_within are invalid')
        return None
    for month in range(1, 13):
        # tmax & tmins are used as 4 digit values
        tmin, tmax = find_yearly_or_monthly_minmax(data, month)
        # min/max_limit are tenths used for within limit checks
        min_limit = round(tmin, 1) + min_within
        max_limit = round(tmax, 1) - max_within
        # set appropriate flags for each tide prediction in data
        for value in data.values():
            # skip any data items not in month
            if month != int(value['date'][5:7]): continue
            # set within limit flags
            tide = round(value['tide'], 1) # within limit is tenths
            if tide <= min_limit: value['min_limit'] = True
            if tide >= max_limit: value['max_limit'] = True
            # month single min/max values
            tide = value['tide'] # uses a four decimal value
            if tide <= tmin: value['min_mn'] = True
            if tide >= tmax: value['max_mn'] = True
    return data


def read_yyyy_tides_data(yyyy, station, f_path):
    """ Loads specific tides data & minmax dicts from a json file.

    Args:
        yyyy (int or str): year value as four digits.
        station (int or str): NOAA station ID.
        f_path (str): path to the config file.

    Returns:
        json_data (str from file), f_path (str with file name)
        None, f_path if file is not found.
        None, None if a catastrophic read file error.
    """
    f_path = '{0}/{1}_{2}_data.json'.format(f_path, station, yyyy)
    json_data = None
    try:
        with open(f_path, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        return None, f_path # json_data is None == file not found
    except:
        print('catastrophic error reading: {0}'.format(f_path))
        return None, None # None in f_path position == catastrophy
    return json_data, f_path


def get_tide_station(stations):
    """ Prompts user to select a NOAA station from a list.

    Displays a list of NOAA tide station ID & descritions, and prompts 
    user to select one unless only on station is present. Returns the 
    selected (or sole) station ID and station description, or None if
    user declines to enter any value from a multi-station list.

    Args:
        stations (specific dict): ID key (int) : desc value (str).

    Returns:
        None, None if users enters '' at prompt (exit signal).
        stationID (int), station description (str).
    """
    station_list = sorted(stations.items())
    if len(station_list) == 1:
        return station_list[0][0], station_list[0][1]
    print('\n---Select desired station---')
    # print an enumerated list of station ID: descriptions
    for i, v in enumerate(station_list):
        print('{0}: {1} ({2})'.format(i+1, v[1], v[0]))
    found = False
    indices = len(station_list)
    while not found: # interate until a valid entry is submitted
        index = input('select station (1-{0}, return=exit): '.format(indices))
        if len(index) == 0: return None, None # exit when input empty
        try:
            index = int(index)
        except:
            print('invalid entry')
            continue
        if index < 0 or index > indices:
            print('invalid entry')
            continue
        # return station ID, station description for valid input
        return station_list[index-1][0], station_list[index-1][1]


def main():
    # Sole config file loaded from the module's directory
    CONFIG_FILE = 'config.ini'
    f_path = os.path.dirname(os.path.realpath(__file__))
    minmax, stations, paths = load_config_file(f_path, CONFIG_FILE)
    if not minmax: return
    # update f_path to user data directory from config.ini
    f_path = paths['json_data_dir']
    station, station_desc = get_tide_station(stations)
    if not station: return
    yyyy, mn = get_print_yyyy_mn()
    if not yyyy: return
    # read the json data file & append file name to f_path
    json_data, f_path = read_yyyy_tides_data(yyyy, station, f_path)
    if not f_path: return # catastrophic error in config.ini
    if json_data:
        # update minmax to values used to create the data dict
        data, minmax = json_data['data'], json_data['minmax']
    else:
        data = load_noaa_data_to_json(yyyy, f_path, station, minmax)
    if not data: return
    # pretty print starts here
    header = 'NOAA Tide Predictions'
    print('\n{0} {1} ({2}) {3}  {4}\n'.format('-'*10, 
                                              station_desc, 
                                              station,
                                              header,
                                              '-'*10))
    # yearly hi/lo
    print_tides_yearly_min_max(data)
    print('\n{0}\n'.format('-'*50))
    # month header + detail starts here
    print('{0}-{1:02d} Monthly High & Low tides\n'.format(yyyy, mn))
    print_tides_month_minmax_ranges(data, mn, minmax)
    print_tides_month_detail(data, mn)
    print('\n{0}\n'.format('-'*50))

if __name__ == '__main__':
    main()
