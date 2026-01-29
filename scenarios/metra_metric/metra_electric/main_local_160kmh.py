scenario_name = "Metra Electric - Main Line Through Running, local (160km/h)"

# This scenario sets the max speed to 160kph and uses mile markers in km. The start is set to McCormick Place.


# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 100mph/160kph speed limit

route = [
                                # Union stop
    (0.0, 1.9, 80, True),
                                # Roosevelt stop
    (1.9, 4.3, 80, True),
                                # McCormick Place/23rd Street stop
    (4.3, 5.8, 160, True),
                                # 31st Street stop
    (5.8, 7.6, 160, True),
                                # 39th Street-Oakland stop
    (7.6, 9.5, 160, True),
                                # 47th Street stop
    (9.5, 10.4, 160, True),
                                # 51-53rd Street-Hyde Park stop
    (10.4, 11.4, 160, True),
                                # 55-56-57th Street stop
    (11.4, 13.0, 160, True),                            
                                # 59-60th St-U Chicago top
    (13.0, 13.8, 160, True),
                                # 63rd Street stop
    (13.8, 16.0, 160, True),
                                # 75th-Grand Crossing stop
    (16.0, 17.1, 160, True),
                                # 79th-Chatham stop
    (17.1, 17.6, 160, True),
                                # 83rd-Avalon Park stop
    (17.6, 18.4, 160, True),
                                # 87th-Woodruff stop
    (18.4, 19.2, 160, True),
                                # 91st-Chesterfield stop
    (19.2, 20.5, 160, True),
                                # 95th-Chicago State University stop
    (20.5, 22.1, 160, True),
                                # 103rd Street stop
    (22.1, 22.7, 160, True),
                                # 107th Street stop
    (22.7, 23.5, 160, True),
                                # 111th-Pullman stop
    (23.5, 24.3, 160, True),
                                # 115th-Kensington PARK stop
    (24.3, 29.1, 160, True),
                                # Riverdale stop 
    (29.2, 30.8, 160, True),
                                # Ivanhoe stop 
    (30.8, 31.7, 160, True),
                                # 147th Street stop 
    (31.7, 33.3, 160, True),
                                # Harvey stop 
    (33.3, 37.0, 160, True),
                                # Hazel Crest stop 
    (37.0, 38.0, 160, True),
                                # Calumet stop 
    (38.0, 39.2, 160, True),
                                # Homewood stop 
]

stops = {
0.0: 'Union',
1.9: 'Roosevelt',
4.30: 'McCormick Place/23rd Street',
5.8: '31st Street',
7.6: '39th Street-Oakland',
9.5: '47th Street',
10.4: '51-53rd Street-Hyde Park',
11.4: '55-56-57th Street',
13.0: '59-60th St-U Chicago',
13.8: '63rd Street',
16.0: '75th-Grand Crossing',
17.1: '79th-Chatham',
17.6: '83rd-Avalon Park',
18.4: '87th-Woodruff',
19.2: '91st-Chesterfield',
20.5: '95th-Chicago State University',
22.1: '103rd Street',
22.7: '107th Street',
23.5: '111th-Pullman',
24.3: '115th-Kensington',
29.1: 'Riverdale',
30.8: 'Ivanhoe',
31.7: '147th Street',
33.3: 'Harvey',
37.0: 'Hazel Crest',
38.0: 'Calumet',
39.2: 'Homewood',
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration