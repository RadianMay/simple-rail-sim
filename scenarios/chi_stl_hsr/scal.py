scenario_name = "St Charles Air Line to South Kankakee"

# This scenario calculates travel time to Kankakee and uses mile markers in km. The start is set to Union.

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 100mph/160kph speed limit

route = [
                                # Union stop
    (0.0, 1.6, 80, False),
                                # SCAL Bridge Curve
    (1.6, 2.6, 60, False),
                                # McCormick Place
    (2.6, 5.4, 160, False),
                                # Groveland Curve
    (5.4, 5.8, 160, False),                            
                                # 55-56-57th Street Curve
    (5.8, 11.2, 250, False),
                                # 55-56-57th Street
    (11.2, 89.3, 320, True),
                                # Kankakee stop
]

stops = {
0.0: 'Union',
89.3: 'Kankakee'
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration