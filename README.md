# tidespy-print
Prints a month of NOAA Hi/Lo tide predictions for a selected NOAA tide station. Upon first print, the yearly data for the station ID will be downloaded and stored (along with the within ranges from config.ini) as a json text file is the directory specified in config.ini. Subsequent runs read the saved json file. The data from NOAA is enhanced with the day abbreviation for the date, better key:value entries, and flags indicating whether the tide prediction is a yearly or monthly hi/lo tide or within a min/max range for the month. The values controling monthly hi/low range checks are in the config.ini file. A list of station IDs can be setup in the config file. If more than one station ID is present the user is prompted to select one ID.

A sample print is below. This sample includes the initial NOAA data load for the year. For each line of a month's detail the following highlights may apply. The tide is:
     1) Current date (******)
     2) Sunday (<<<)
     3) Within the month's range of min/max values: (-min) (max)
     4) One of the month's or year's min/max values

Requires: Python3 & requests module.
<br>
<br>
***Sample Output***
<br>
<br>
MINMAX loading<br>
STATIONS loading<br>
PATHS loading<br>
<br>
\---Select desired station---<br>
1: Port Townsend (9444900)<br>
2: Admiralty Head (9447905)<br>
3: NAS Whidbey (9447973)<br>
4: Bellingham (9449211)<br>
select station (1-4, return=exit): 1<br>
enter YYYYMM, return=current year-month: 201901<br>
\---<br>
data file not found: /Users/steve/Documents/tides_json_data/9444900_2019_data.json<br>
exit program (y=exit, ret=load data file): <br>
\---load data start---<br>
20190101 status: 200<br>
20190201 status: 200<br>
20190301 status: 200<br>
20190401 status: 200<br>
20190501 status: 200<br>
20190601 status: 200<br>
20190701 status: 200<br>
20190801 status: 200<br>
20190901 status: 200<br>
20191001 status: 200<br>
20191101 status: 200<br>
20191201 status: 200<br>
load complete<br>
\---<br>
<br>
\---------- Port Townsend (9444900) NOAA Tide Predictions  ----------<br>
<br>
Yearly max & min tides:<br>
<br>
\-3.124 = min tide (feet) 2019-07-04 11:45 (Wed)<br>
9.751 = max tide (feet) 2019-01-23 06:47 (Wed)<br>
<br>
\--------------------------------------------------<br>
<br>
2019-01 Monthly High & Low tides<br>
<br>
min range: -2.8 to -2.6<br>
max range: 9.6 to 9.8<br>
<br>
Tue: 2019-01-01 02:09 (H) =  6.688  <br>
Tue: 2019-01-01 05:42 (L) =  5.420  <br>
Tue: 2019-01-01 12:04 (H) =  9.047  <br>
Tue: 2019-01-01 19:20 (L) =  0.112  <br>
\---<br>
Wed: 2019-01-02 03:15 (H) =  7.678  <br>
Wed: 2019-01-02 06:52 (L) =  6.291  <br>
Wed: 2019-01-02 12:38 (H) =  8.834  <br>
Wed: 2019-01-02 19:55 (L) = -0.526  <br>
\---<br>
Thu: 2019-01-03 04:06 (H) =  8.473  <br>
Thu: 2019-01-03 07:58 (L) =  6.829  <br>
Thu: 2019-01-03 13:12 (H) =  8.619  <br>
Thu: 2019-01-03 20:28 (L) = -0.940  <br>
\---<br>
Fri: 2019-01-04 04:50 (H) =  9.005  <br>
Fri: 2019-01-04 08:57 (L) =  7.093  <br>
Fri: 2019-01-04 13:45 (H) =  8.408  <br>
Fri: 2019-01-04 21:02 (L) = -1.162  <br>
\---<br>
Sat: 2019-01-05 05:29 (H) =  9.291  <br>
Sat: 2019-01-05 09:48 (L) =  7.156  <br>
Sat: 2019-01-05 14:20 (H) =  8.200  <br>
Sat: 2019-01-05 21:35 (L) = -1.225  <br>
\---<br>
Sun: 2019-01-06 06:04 (H) =  9.385  <<<<br>
Sun: 2019-01-06 10:34 (L) =  7.078  <<<<br>
Sun: 2019-01-06 14:58 (H) =  7.977  <<<<br>
Sun: 2019-01-06 22:10 (L) = -1.148  <<<<br>
\---<br>
Mon: 2019-01-07 06:36 (H) =  9.360  <br>
Mon: 2019-01-07 11:18 (L) =  6.894  <br>
Mon: 2019-01-07 15:37 (H) =  7.714  <br>
Mon: 2019-01-07 22:47 (L) = -0.937  <br>
\---<br>
Tue: 2019-01-08 07:05 (H) =  9.282  ****** <br>
Tue: 2019-01-08 12:04 (L) =  6.623  ******<br>
Tue: 2019-01-08 16:20 (H) =  7.385  ******<br>
Tue: 2019-01-08 23:24 (L) = -0.582  ******<br>
\---<br>
Wed: 2019-01-09 07:32 (H) =  9.194  <br>
Wed: 2019-01-09 12:53 (L) =  6.263  <br>
Wed: 2019-01-09 17:07 (H) =  6.975  <br>
\---<br>
Thu: 2019-01-10 00:01 (L) = -0.064  <br>
Thu: 2019-01-10 07:59 (H) =  9.117  <br>
Thu: 2019-01-10 13:47 (L) =  5.795  <br>
Thu: 2019-01-10 17:58 (H) =  6.487  <br>
\---<br>
Fri: 2019-01-11 00:39 (L) =  0.632  <br>
Fri: 2019-01-11 08:26 (H) =  9.047  <br>
Fri: 2019-01-11 14:41 (L) =  5.199  <br>
Fri: 2019-01-11 18:58 (H) =  5.957  <br>
\---<br>
Sat: 2019-01-12 01:17 (L) =  1.508  <br>
Sat: 2019-01-12 08:54 (H) =  8.971  <br>
Sat: 2019-01-12 15:33 (L) =  4.461  <br>
Sat: 2019-01-12 20:08 (H) =  5.469  <br>
\---<br>
Sun: 2019-01-13 01:56 (L) =  2.539  <<<<br>
Sun: 2019-01-13 09:24 (H) =  8.885  <<<<br>
Sun: 2019-01-13 16:20 (L) =  3.587  <<<<br>
Sun: 2019-01-13 21:36 (H) =  5.178  <<<<br>
\---<br>
Mon: 2019-01-14 02:40 (L) =  3.673  <br>
Mon: 2019-01-14 09:55 (H) =  8.800  <br>
Mon: 2019-01-14 17:02 (L) =  2.591  <br>
Mon: 2019-01-14 23:43 (H) =  5.356  <br>
\---<br>
Tue: 2019-01-15 03:35 (L) =  4.820  <br>
Tue: 2019-01-15 10:26 (H) =  8.742  <br>
Tue: 2019-01-15 17:42 (L) =  1.505  <br>
\---<br>
Wed: 2019-01-16 02:00 (H) =  6.220  <br>
Wed: 2019-01-16 04:45 (L) =  5.842  <br>
Wed: 2019-01-16 11:00 (H) =  8.735  <br>
Wed: 2019-01-16 18:23 (L) =  0.381  <br>
\---<br>
Thu: 2019-01-17 03:00 (H) =  7.220  <br>
Thu: 2019-01-17 05:58 (L) =  6.599  <br>
Thu: 2019-01-17 11:37 (H) =  8.791  <br>
Thu: 2019-01-17 19:06 (L) = -0.704  <br>
\---<br>
Fri: 2019-01-18 03:43 (H) =  8.090  <br>
Fri: 2019-01-18 07:04 (L) =  7.045  <br>
Fri: 2019-01-18 12:19 (H) =  8.891  <br>
Fri: 2019-01-18 19:49 (L) = -1.658  <br>
\---<br>
Sat: 2019-01-19 04:20 (H) =  8.768  <br>
Sat: 2019-01-19 08:03 (L) =  7.204  <br>
Sat: 2019-01-19 13:07 (H) =  8.991  <br>
Sat: 2019-01-19 20:34 (L) = -2.381  <br>
\---<br>
Sun: 2019-01-20 04:57 (H) =  9.243  <<<<br>
Sun: 2019-01-20 08:56 (L) =  7.117  <<<<br>
Sun: 2019-01-20 14:00 (H) =  9.028  <<<<br>
Sun: 2019-01-20 21:19 (L) = -2.785 (-min) <<<<br>
\---<br>
Mon: 2019-01-21 05:33 (H) =  9.539  <br>
Mon: 2019-01-21 09:49 (L) =  6.817  <br>
Mon: 2019-01-21 14:57 (H) =  8.930  <br>
Mon: 2019-01-21 22:06 (L) = -2.803 (-min for month) <br>
\---<br>
Tue: 2019-01-22 06:10 (H) =  9.694 (max) <br>
Tue: 2019-01-22 10:42 (L) =  6.336  <br>
Tue: 2019-01-22 15:56 (H) =  8.641  <br>
Tue: 2019-01-22 22:52 (L) = -2.403  <br>
\---<br>
Wed: 2019-01-23 06:47 (H) =  9.751 (max for year) <br>
Wed: 2019-01-23 11:39 (L) =  5.699  <br>
Wed: 2019-01-23 16:58 (H) =  8.140  <br>
Wed: 2019-01-23 23:39 (L) = -1.593  <br>
\---<br>
Thu: 2019-01-24 07:24 (H) =  9.740 (max) <br>
Thu: 2019-01-24 12:41 (L) =  4.930  <br>
Thu: 2019-01-24 18:04 (H) =  7.464  <br>
\---<br>
Fri: 2019-01-25 00:26 (L) = -0.423  <br>
Fri: 2019-01-25 08:01 (H) =  9.671 (max) <br>
Fri: 2019-01-25 13:46 (L) =  4.058  <br>
Fri: 2019-01-25 19:16 (H) =  6.715  <br>
\---<br>
Sat: 2019-01-26 01:14 (L) =  1.013  <br>
Sat: 2019-01-26 08:37 (H) =  9.542  <br>
Sat: 2019-01-26 14:54 (L) =  3.129  <br>
Sat: 2019-01-26 20:41 (H) =  6.073  <br>
\---<br>
Sun: 2019-01-27 02:04 (L) =  2.581  <<<<br>
Sun: 2019-01-27 09:14 (H) =  9.344  <<<<br>
Sun: 2019-01-27 16:01 (L) =  2.211  <<<<br>
Sun: 2019-01-27 22:35 (H) =  5.851  <<<<br>
\---<br>
Mon: 2019-01-28 03:00 (L) =  4.124  <br>
Mon: 2019-01-28 09:51 (H) =  9.083  <br>
Mon: 2019-01-28 17:03 (L) =  1.378  <br>
\---<br>
Tue: 2019-01-29 00:45 (H) =  6.400  <br>
Tue: 2019-01-29 04:09 (L) =  5.460  <br>
Tue: 2019-01-29 10:30 (H) =  8.778  <br>
Tue: 2019-01-29 17:58 (L) =  0.694  <br>
\---<br>
Wed: 2019-01-30 02:10 (H) =  7.331  <br>
Wed: 2019-01-30 05:32 (L) =  6.407  <br>
Wed: 2019-01-30 11:12 (H) =  8.467  <br>
Wed: 2019-01-30 18:47 (L) =  0.184  <br>
\---<br>
Thu: 2019-01-31 03:08 (H) =  8.152  <br>
Thu: 2019-01-31 07:01 (L) =  6.880  <br>
Thu: 2019-01-31 11:56 (H) =  8.193  <br>
Thu: 2019-01-31 19:29 (L) = -0.161  <br>
<br>
\--------------------------------------------------<br>
