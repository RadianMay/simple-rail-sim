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
    (4.3, 11.4, 160, True),
                                # 55-56-57th Street stop
    (11.4, 13.8, 160, True),                            
                                # 63rd Street stop
    (13.8, 20.5, 160, True),
                                # 95th-Chicago State University stop
    (20.5, 24.3, 160, True),
                                # 115th-Kensington stop
    (24.3, 33.3, 160, True),
                                # Harvey stop 
    (33.3, 39.2, 160, True),
                                # Homewood stop 
    (39.0, 41.7, 160, True),
                                # Floorsmoor stop 
    (41.7, 44.2, 160, True),
                                # Olympia fields stop 
    (44.2, 46.0, 160, True),
                                # 211st Street stop 
    (46.0, 48.3, 160, True),
                                # Richton Park stop 
    (48.3, 51.5, 160, True),
                                # University Park stop
    (51.5, 56.3, 160, True),
                                # Monee stop 
    (56.3, 66.7, 160, True),
                                # Peotone stop 
    (66.7, 76.5, 160, True),
                                # Manteno stop 
    (76.5, 88.8, 160, True),
                                # Bradley stop 
    (88.8, 91.4, 160, True),
                                # Kankakee stop 
]

stops = {
0.0: 'Union',
1.9: 'Roosevelt',
4.3: 'McCormick Place/23rd Street',
11.4: '55-56-57th Street',
13.8: '63rd Street',
20.5: '95th-Chicago State University',
24.3: '115th-Kensington',
33.3: 'Harvey',
39.2: 'Homewood',
41.7: 'Floorsmoor',
44.2: 'Olympia Fields',
46.0: '211st Street',
48.3: 'Richton Park',
51.5: 'University Park',
56.3: 'Monee',
66.7: 'Peotone',
76.5: 'Manteno',
88.8: 'Bradley',
91.4: 'Kankakee'
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration