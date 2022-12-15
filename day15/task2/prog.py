import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Point,PointType, Grid,Offset



lines = get_lines_from_file(day_number=15)



SENSORS:dict[str,Point] = {}
BEACONS:dict[str,Point] = {}
GRID: Grid = Grid()
for line in lines:
    line = strip_line(line)
    inputs = line.split(' ')
    sensor_x = int(inputs[2].split('=')[1].split(',')[0])
    sensor_y = int(inputs[3].split('=')[1].split(':')[0])
    beacon_x = int(inputs[8].split('=')[1].split(',')[0])
    beacon_y = int(inputs[9].split('=')[1])
    sensor = Point(sensor_x,sensor_y,PointType.SENSOR)
    beacon = Point(beacon_x,beacon_y,PointType.BEACON)
    sensor.set_beacon(beacon)
    GRID.check_min_max(sensor)
    GRID.check_min_max(beacon)
    SENSORS.update({sensor.get_dict_key():sensor})
    if beacon.get_dict_key() not in BEACONS:
        BEACONS.update({beacon.get_dict_key():beacon})


def in_grid(x:int,y:int,max_num:int):
    return x >= 0 and x <=max_num and y>=0 and y<=max_num

RIGHT_DOWN=Offset(1,1)
LEFT_DOWN=Offset(-1,1)
RIGHT_UP=Offset(1,-1)
LEFT_UP= Offset(-1,-1)
TRACKING_ORDER=[RIGHT_DOWN,LEFT_DOWN,LEFT_DOWN,RIGHT_UP]

def solve(max_num):

    num_checks = 0
    num_points = 0


    for key,sensor in SENSORS.items():
        tracking_index = 0
        offset = TRACKING_ORDER[tracking_index]
        # print (sensor)
        y = sensor.y - (sensor.distance_to_beacon+1) # Just outside range
        x = sensor.x 
        p = Point(x,y,PointType.NOT_COVERED)    
        # print (f"{p.x},{p.y}, {tracking_index}")
        while tracking_index < len(TRACKING_ORDER):
            num_points +=1
            inside = False
            if in_grid(p.x,p.y,max_num) and p.get_dict_key() not in SENSORS and p.get_dict_key() not in BEACONS:
                for key2,test_sensor in SENSORS.items():
                    if key2 == key: # Do not want to test against same SENSOR
                        # print (key,key2,"Same Sensor")
                        continue
                    # print (f"test_sensor {test_sensor}, {test_sensor.get_distance_to(p)}")
                    num_checks += 1
                    if test_sensor.is_closer_or_equal_to_beacon(p): # Covered by sensor
                        # print (f"inside sensor: {key2}: distance to sensor:{test_sensor.get_distance_to(p)}: distance to beacon:{test_sensor.distance_to_beacon}" )
                        inside = True
                        break
                if not inside:
                    print (num_points,num_checks)
                    return p
            # else:
                # print (f"IN_GRID: {in_grid(x,y,max_num)}")
                # print (f"SENSORS: {p.get_dict_key() not in SENSORS}")
                # print (f"BEACONS: {p.get_dict_key() not in BEACONS}")
            new_p: Point = Point(p.x+offset.x,p.y+offset.y,PointType.NOT_COVERED)
            if sensor.distance_to_beacon+1 < sensor.get_distance_to(new_p):
                tracking_index+=1
                if tracking_index== len(TRACKING_ORDER):
                    break
                offset = TRACKING_ORDER[tracking_index]
                p = Point(p.x+offset.x,p.y+offset.y,PointType.NOT_COVERED)
            else:
                p = new_p
            # print (f"{p.x},{p.y}, {tracking_index}")
         



p = solve(4000000)
print (p)
print (4000000*p.x + p.y)

print (num_points,num_checks)


# COVERED:dict[str:Point] = {}
# for key,sensor in SENSORS.items():
#     print (sensor)
#     # Does the sensor distance reach row test-y
#     radial_distance = sensor.distance_to_beacon - abs(sensor.y - test_y)
#     print (f"amount of cross over of row:{test_y} -> radial_distance {radial_distance}")
#     if radial_distance >0 : # we are closer
#         r = range(sensor.x - radial_distance,sensor.x + radial_distance+1)
#         for test_x in r:
#             p = Point(test_x,test_y,PointType.COVERED)
#             point_key = p.get_dict_key()
#             if point_key not in SENSORS and point_key not in BEACONS and point_key not in COVERED:
#                 COVERED.update({point_key:p})
#     else:
#         print ("DOES NOT REACH")
    

# print (len(COVERED))
# GRID.calculate_dimensions()
# GRID.build_grid()
# for key,sensor in SENSORS.items():
#     GRID.add_point(sensor)
# for key,beacon in BEACONS.items():
#     GRID.add_point(beacon)
# # sensor = SENSORS["8_7"]
# for key,sensor in SENSORS.items():
#     top_left_x = sensor.x - sensor.distance_to_beacon
#     top_left_y = sensor.y - sensor.distance_to_beacon
#     test_y = top_left_y
#     while test_y <=sensor.y + sensor.distance_to_beacon:
#         test_x = top_left_x
#         while test_x <= sensor.x + sensor.distance_to_beacon:
#             test_p = Point(test_x,test_y,PointType.NOT_COVERED)
#             if Grid.point_on_grid(test_p): 
#                 if Grid.point_is_not_covered(test_p):
#                     if sensor.is_closer_or_equal_to_beacon(test_p):
#                         test_p.set_covered()
#                     GRID.add_point(test_p)
#             test_x += 1
#         test_y += 1
    
# GRID.print_grid()

