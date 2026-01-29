scenario_name = "Tunnel to Kankakee"

# This scenario calculates travel time to Kankakee and uses mile markers in km. The start is set to Union.

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 100mph/160kph speed limit

route = [
                                # Union stop
    (0.0, 5.4, 160, False),
                                # Groveland Curve
    (5.4, 10.6, 250, False),                            
                                # South Chicago Curve
    (10.6, 88.7, 320, True),
                                # Kankakee stop
]

stops = {
0.0: 'Union',
88.7: 'Kankakee'
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration