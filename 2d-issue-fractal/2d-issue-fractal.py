import matplotlib.pyplot as plt
import matplotlib.lines as mlines

basic_points = [[0, 2], [1, 0], [2, 1]]
points = [[0, 2], [1, 0], [2, 1]]
iterations = 10
for i in range(0, iterations):
    new_points = []
    for point in points:
        for p in range(0, 3):
            new_points.append([point[0] * 3 + basic_points[p][0], point[1] * 3 + basic_points[p][1]])
    points = new_points

points_x = [p[0] for p in points]
points_y = [p[1] for p in points]

plt.scatter(points_x, points_y, c='green', #marker='s',
            label='Potential\nOutcomes')
plt.title('Fractal of Intransitivity')
plt.xlabel('Utility of Agent 1')
plt.ylabel('Utility of Agent 2')
plt.legend(loc=2)
plt.show()
