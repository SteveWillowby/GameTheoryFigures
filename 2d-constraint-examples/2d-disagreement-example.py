import matplotlib.pyplot as plt
import matplotlib.lines as mlines

points_x = [0, 1, 2, 5, 8, 9,10,11,12,13,14,15,16,19,22,23,26,27,28,31,32,36,39,40]
points_y = [9, 7, 6, 5, 4, 2,10,11,14,13,12,23,22,21,20,19,18,17,16,15,29,28,27,24]

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


def newsegment(p1, p2):
    ax = plt.gca()
    l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='gray', linestyle='--', linewidth=1.0)
    ax.add_line(l)
    return l


plt.scatter(points_x, points_y, c='green', #marker='s',
            label='Potential\nOutcomes')
# newline([-0.5,0],[-0.5,1])
newsegment([9.5,-0.5],[9.5,10.5])
newsegment([10.5,9.5],[10.5,11.5])
newsegment([11.5,10.5],[11.5,14.5])
newsegment([14.5,11.5],[14.5,23.5])
newsegment([31.5,14.5],[31.5,30.5])

newsegment([-1.5,9.5],[10.5,9.5])
newsegment([9.5,10.5],[11.5,10.5])
newsegment([10.5,11.5],[14.5,11.5])
newsegment([11.5,14.5],[31.5,14.5])
newsegment([14.5,23.5],[41.5,23.5])
# plt.suptitle('Transitivity of Disagreement Equality')
# plt.title('When Utilities are Unique')
plt.xlabel('Utility of Agent 1')
plt.ylabel('Utility of Agent 2')
plt.legend(loc=2)
plt.show()
