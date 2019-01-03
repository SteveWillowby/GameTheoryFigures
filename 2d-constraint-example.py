import matplotlib.pyplot as plt
import matplotlib.lines as mlines

points_x = [0, 0, 1, 2, 3, 5, 6, 8, 9, 9, 9,10,10,11,12,13,14,14,15,16,16,19,21,22,23,25,26,27,27,28,28,29,31,32,35,36,38,39,40,40]
points_y = [9,10, 7, 6, 5, 5, 5, 4, 0, 2, 3,11,12,13,16,15,14,15,25,23,25,23,23,22,21,21,20,19,20,18,19,17,17,30,30,30,29,29,26,28]

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax], color='gray', linestyle='--', linewidth=1.0)
    ax.add_line(l)
    return l

plt.scatter(points_x, points_y, c='green', #marker='s',
            label='Potential\nOutcomes')
# newline([-0.5,0],[-0.5,1])
newline([9.5,0],[9.5,1])
newline([10.5,0],[10.5,1])
newline([11.5,0],[11.5,1])
newline([14.5,0],[14.5,1])
newline([31.5,0],[31.5,1])

newline([0,10.5],[1,10.5])
newline([0,12.5],[1,12.5])
newline([0,13.5],[1,13.5])
newline([0,16.5],[1,16.5])
newline([0,25.5],[1,25.5])
plt.title('Transitivity of Indifference Equality')
plt.xlabel('Utility of Agent 1')
plt.ylabel('Utility of Agent 2')
plt.legend(loc=2)
plt.show()
