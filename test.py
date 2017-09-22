from conversions.unit_converter import speed, distance, angle, acceleration, rotation

# test speed

speed_mps = speed(40)
speed_mph = speed_mps.mps_to_mph()
speed_fps = speed_mps.mps_to_fps()

print(speed_mph)
print(speed_fps)

# test distance

distance_m = distance(2)
distance_feet = distance_m.m_to_ft()
distance_inches = distance_m.m_to_in()

print(distance_feet)
print(distance_inches)

# test angle

angle_rad = angle(3.14)
angle_degrees = angle_rad.rad_to_deg()

print(angle_degrees)

# test acceleration

acceleration_ms2 = acceleration(9.81)
acceleration_fs2 = acceleration_ms2.ms2_to_fs2()

print(acceleration_fs2)

# test rotation

rotation_rps = rotation(40)

rotation_rpm = rotation_rps.rps_to_rpm()

print(rotation_rpm)
