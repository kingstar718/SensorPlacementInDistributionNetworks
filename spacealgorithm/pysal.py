from pointpats import PointPattern
import pointpats
points = [[66.22, 32.54], [22.52, 22.39], [31.01, 81.21],
              [9.47, 31.02], [30.78, 60.10], [75.21, 58.93],
              [79.26,  7.68], [8.23, 39.93], [98.73, 77.17],
              [89.78, 42.53], [65.19, 92.08], [54.46, 8.48]]

pp = PointPattern(points)

print(pp.n)

print(pointpats.mean_center(points))