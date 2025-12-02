scenario_name = "Metra Electric - Main Line Through Running, local (160km/h)"

# This scenario sets the max speed to 160kph and uses mile markers in km. The start is set to McCormick Place.


# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 100mph/160kph speed limit

route = [
                                # McCormick Place/23rd Street stop
    (0.0, 1.5, 160, True),
                                # 31st Street stop
    (1.5, 3.3, 160 True),
                                # 39th Street-Oakland stop
    (3.3, 5.2, 160, True),
                                # 47th Street stop
    (5.2, 6.1, 160, True),
                                # 51-53rd Street-Hyde Park stop
    (6.1, 7.1, 160, True),
                                # 55-56-57th Street stop
    (7.1, 8.7, 160, True),                            
                                # 59-60th St-U Chicago top
    (8.7, 9.5, 160, True),
                                # 63rd Street stop
    (9.5, 11.7, 160, True),
                                # 75th-Grand Crossing stop
    (11.7, 12.8, 160, True),
                                # 79th-Chatham stop
    (12.8, 13.3, 160, True),
                                # 83rd-Avalon Park stop
    (13.3, 14.1, 160, True),
                                # 87th-Woodruff stop
    (14.1, 14.9, 160, True),
                                # 91st-Chesterfield stop
    (14.9, 16.2, 160, True),
                                # 95th-Chicago State University stop
    (16.2, 17.8, 160, True),
                                # 103rd Street stop
    (17.8, 18.4, 160, True),
                                # 107th Street stop
    (18.4, 19.2, 160, True),
                                # 111th-Pullman stop
    (19.2, 20.0, 160, True),
                                # 115th-Kensington PARK stop
    (20.0, 24.8, 160, True),
                                # Riverdale stop 
    (24.9, 26.5, 160, True),
                                # Ivanhoe stop 
    (26.5, 27.4, 160, True),
                                # 147th Street stop 
    (27.4, 29.0, 160, True),
                                # Harvey stop 
    (29.0, 32.7, 160, True),
                                # Hazel Crest stop 
    (32.7, 33.7, 160, True),
                                # Calumet stop 
    (33.7, 34.9, 160, True),
                                # Homewood stop 
]

stops = {
0.00: 'McCormick Place/23rd Street',
1.5: '31st Street',
3.3: '39th Street-Oakland',
5.2: '47th Street',
6.1: '51-53rd Street-Hyde Park',
7.1: '55-56-57th Street',
8.7: '59-60th St-U Chicago'
9.5: '63rd Street',
11.7: '75th-Grand Crossing',
12.8: '79th-Chatham',
13.3: '83rd-Avalon Park',
14.1: '87th-Woodruff',
14.9: '91st-Chesterfield',
16.2: '95th-Chicago State University',
17.8: '103rd Street',
18.4: '107th Street',
19.2: '111th-Pullman',
20.0: '115th-Kensington',
24.8: 'Riverdale',
26.5: 'Ivanhoe',
27.4: '147th Street',
29.0: 'Harvey',
32.7: 'Hazel Crest',
33.7: 'Calumet',
34.9: 'Homewood',
}

dwell_time = 30 # seconds
