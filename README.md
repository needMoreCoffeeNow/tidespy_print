# tidespy-print
Prints a month of NOAA Hi/Lo tide predictions for a selected NOAA tide station. Upon first print, the yearly data for the station ID will be downloaded and stored (along with the within ranges from config.ini) as a json text file is the directory specified in config.ini. Subsequent runs read the saved json file. The data from NOAA is enhanced with the day abbreviation for the date, better key:value entries, and flags indicating whether the tide prediction is a yearly or monthly hi/lo tide or within a min/max range for the month. The values controling monthly hi/low range checks are in the config.ini file. A list of station IDs can be setup in the config file. If more than one station ID is present the user is prompted to select one ID.

A sample print is below. This sample includes the initial NOAA data load for the year. For each line of a month's detail the following highlights may apply. The tide is:
     1) Current date (******)
     2) Sunday (<<<)
     3) Within the month's range of min/max values: (-min) (max)
     4) One of the month's or year's min/max values

Requires: Python3 & requests module.

***Sample Output***

MINMAX loading
STATIONS loading
PATHS loading

---Select desired station---
1: Port Townsend (9444900)
2: Admiralty Head (9447905)
3: NAS Whidbey (9447973)
4: Bellingham (9449211)
select station (1-4, return=exit): 1
enter YYYYMM, return=current year-month: 201901
---
data file not found: /Users/steve/Documents/tides_json_data/9444900_2019_data.json
exit program (y=exit, ret=load data file): 
---load data start---
20190101 status: 200
20190201 status: 200
20190301 status: 200
20190401 status: 200
20190501 status: 200
20190601 status: 200
20190701 status: 200
20190801 status: 200
20190901 status: 200
20191001 status: 200
20191101 status: 200
20191201 status: 200
load complete
---

---------- Port Townsend (9444900) NOAA Tide Predictions  ----------

Yearly max & min tides:

-3.124 = min tide (feet) 2019-07-04 11:45 (Wed)
9.751 = max tide (feet) 2019-01-23 06:47 (Wed)

--------------------------------------------------

2019-01 Monthly High & Low tides

min range: -2.8 to -2.6
max range: 9.6 to 9.8

Tue: 2019-01-01 02:09 (H) =  6.688  
Tue: 2019-01-01 05:42 (L) =  5.420  
Tue: 2019-01-01 12:04 (H) =  9.047  
Tue: 2019-01-01 19:20 (L) =  0.112  
---
Wed: 2019-01-02 03:15 (H) =  7.678  
Wed: 2019-01-02 06:52 (L) =  6.291  
Wed: 2019-01-02 12:38 (H) =  8.834  
Wed: 2019-01-02 19:55 (L) = -0.526  
---
Thu: 2019-01-03 04:06 (H) =  8.473  
Thu: 2019-01-03 07:58 (L) =  6.829  
Thu: 2019-01-03 13:12 (H) =  8.619  
Thu: 2019-01-03 20:28 (L) = -0.940  
---
Fri: 2019-01-04 04:50 (H) =  9.005  
Fri: 2019-01-04 08:57 (L) =  7.093  
Fri: 2019-01-04 13:45 (H) =  8.408  
Fri: 2019-01-04 21:02 (L) = -1.162  
---
Sat: 2019-01-05 05:29 (H) =  9.291  
Sat: 2019-01-05 09:48 (L) =  7.156  
Sat: 2019-01-05 14:20 (H) =  8.200  
Sat: 2019-01-05 21:35 (L) = -1.225  
---
Sun: 2019-01-06 06:04 (H) =  9.385  <<<
Sun: 2019-01-06 10:34 (L) =  7.078  <<<
Sun: 2019-01-06 14:58 (H) =  7.977  <<<
Sun: 2019-01-06 22:10 (L) = -1.148  <<<
---
Mon: 2019-01-07 06:36 (H) =  9.360  
Mon: 2019-01-07 11:18 (L) =  6.894  
Mon: 2019-01-07 15:37 (H) =  7.714  
Mon: 2019-01-07 22:47 (L) = -0.937  
---
Tue: 2019-01-08 07:05 (H) =  9.282  ****** 
Tue: 2019-01-08 12:04 (L) =  6.623  ******
Tue: 2019-01-08 16:20 (H) =  7.385  ******
Tue: 2019-01-08 23:24 (L) = -0.582  ******
---
Wed: 2019-01-09 07:32 (H) =  9.194  
Wed: 2019-01-09 12:53 (L) =  6.263  
Wed: 2019-01-09 17:07 (H) =  6.975  
---
Thu: 2019-01-10 00:01 (L) = -0.064  
Thu: 2019-01-10 07:59 (H) =  9.117  
Thu: 2019-01-10 13:47 (L) =  5.795  
Thu: 2019-01-10 17:58 (H) =  6.487  
---
Fri: 2019-01-11 00:39 (L) =  0.632  
Fri: 2019-01-11 08:26 (H) =  9.047  
Fri: 2019-01-11 14:41 (L) =  5.199  
Fri: 2019-01-11 18:58 (H) =  5.957  
---
Sat: 2019-01-12 01:17 (L) =  1.508  
Sat: 2019-01-12 08:54 (H) =  8.971  
Sat: 2019-01-12 15:33 (L) =  4.461  
Sat: 2019-01-12 20:08 (H) =  5.469  
---
Sun: 2019-01-13 01:56 (L) =  2.539  <<<
Sun: 2019-01-13 09:24 (H) =  8.885  <<<
Sun: 2019-01-13 16:20 (L) =  3.587  <<<
Sun: 2019-01-13 21:36 (H) =  5.178  <<<
---
Mon: 2019-01-14 02:40 (L) =  3.673  
Mon: 2019-01-14 09:55 (H) =  8.800  
Mon: 2019-01-14 17:02 (L) =  2.591  
Mon: 2019-01-14 23:43 (H) =  5.356  
---
Tue: 2019-01-15 03:35 (L) =  4.820  
Tue: 2019-01-15 10:26 (H) =  8.742  
Tue: 2019-01-15 17:42 (L) =  1.505  
---
Wed: 2019-01-16 02:00 (H) =  6.220  
Wed: 2019-01-16 04:45 (L) =  5.842  
Wed: 2019-01-16 11:00 (H) =  8.735  
Wed: 2019-01-16 18:23 (L) =  0.381  
---
Thu: 2019-01-17 03:00 (H) =  7.220  
Thu: 2019-01-17 05:58 (L) =  6.599  
Thu: 2019-01-17 11:37 (H) =  8.791  
Thu: 2019-01-17 19:06 (L) = -0.704  
---
Fri: 2019-01-18 03:43 (H) =  8.090  
Fri: 2019-01-18 07:04 (L) =  7.045  
Fri: 2019-01-18 12:19 (H) =  8.891  
Fri: 2019-01-18 19:49 (L) = -1.658  
---
Sat: 2019-01-19 04:20 (H) =  8.768  
Sat: 2019-01-19 08:03 (L) =  7.204  
Sat: 2019-01-19 13:07 (H) =  8.991  
Sat: 2019-01-19 20:34 (L) = -2.381  
---
Sun: 2019-01-20 04:57 (H) =  9.243  <<<
Sun: 2019-01-20 08:56 (L) =  7.117  <<<
Sun: 2019-01-20 14:00 (H) =  9.028  <<<
Sun: 2019-01-20 21:19 (L) = -2.785 (-min) <<<
---
Mon: 2019-01-21 05:33 (H) =  9.539  
Mon: 2019-01-21 09:49 (L) =  6.817  
Mon: 2019-01-21 14:57 (H) =  8.930  
Mon: 2019-01-21 22:06 (L) = -2.803 (-min for month) 
---
Tue: 2019-01-22 06:10 (H) =  9.694 (max) 
Tue: 2019-01-22 10:42 (L) =  6.336  
Tue: 2019-01-22 15:56 (H) =  8.641  
Tue: 2019-01-22 22:52 (L) = -2.403  
---
Wed: 2019-01-23 06:47 (H) =  9.751 (max for year) 
Wed: 2019-01-23 11:39 (L) =  5.699  
Wed: 2019-01-23 16:58 (H) =  8.140  
Wed: 2019-01-23 23:39 (L) = -1.593  
---
Thu: 2019-01-24 07:24 (H) =  9.740 (max) 
Thu: 2019-01-24 12:41 (L) =  4.930  
Thu: 2019-01-24 18:04 (H) =  7.464  
---
Fri: 2019-01-25 00:26 (L) = -0.423  
Fri: 2019-01-25 08:01 (H) =  9.671 (max) 
Fri: 2019-01-25 13:46 (L) =  4.058  
Fri: 2019-01-25 19:16 (H) =  6.715  
---
Sat: 2019-01-26 01:14 (L) =  1.013  
Sat: 2019-01-26 08:37 (H) =  9.542  
Sat: 2019-01-26 14:54 (L) =  3.129  
Sat: 2019-01-26 20:41 (H) =  6.073  
---
Sun: 2019-01-27 02:04 (L) =  2.581  <<<
Sun: 2019-01-27 09:14 (H) =  9.344  <<<
Sun: 2019-01-27 16:01 (L) =  2.211  <<<
Sun: 2019-01-27 22:35 (H) =  5.851  <<<
---
Mon: 2019-01-28 03:00 (L) =  4.124  
Mon: 2019-01-28 09:51 (H) =  9.083  
Mon: 2019-01-28 17:03 (L) =  1.378  
---
Tue: 2019-01-29 00:45 (H) =  6.400  
Tue: 2019-01-29 04:09 (L) =  5.460  
Tue: 2019-01-29 10:30 (H) =  8.778  
Tue: 2019-01-29 17:58 (L) =  0.694  
---
Wed: 2019-01-30 02:10 (H) =  7.331  
Wed: 2019-01-30 05:32 (L) =  6.407  
Wed: 2019-01-30 11:12 (H) =  8.467  
Wed: 2019-01-30 18:47 (L) =  0.184  
---
Thu: 2019-01-31 03:08 (H) =  8.152  
Thu: 2019-01-31 07:01 (L) =  6.880  
Thu: 2019-01-31 11:56 (H) =  8.193  
Thu: 2019-01-31 19:29 (L) = -0.161  

--------------------------------------------------
