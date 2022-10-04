import numpy as np
import matplotlib.pyplot as plt


class preprocessing:
    max_time = 10000
    grid_size = 100

    def __init__(self, time):
        self.time = time
        # initial conditions
        self.alpha = 1.5
        self.del_x = 1
        # boundary conditions
        self.first_wall = 200.0
        self.all_other_walls = 20.0

    def make_arr(self):
        arr = np.zeros((self.time, self.grid_size, self.grid_size))
        arr[:, self.grid_size - 1:, :] = self.first_wall
        arr[:, :, 0] = self.all_other_walls
        arr[:, :, -1] = self.all_other_walls

        return arr


# using finite difference method
class calc:
    def __init__(self, time):
        self.inst = preprocessing(time)
        self.del_t = ((self.inst.del_x) ** 2) / (5 * self.inst.alpha)

    def value_calc(self):
        mat = self.inst.make_arr()
        for i in range(0, self.inst.time - 1):
            for j in range(1, self.inst.grid_size - 1, self.inst.del_x):
                for k in range(1, self.inst.grid_size - 1, self.inst.del_x):
                    mat[i + 1, j, k] = ((self.inst.alpha * self.del_t) / (self.inst.del_x ** 2) )* (
                            mat[i, j + 1, k] + mat[i, j - 1, k] + mat[i, j, k + 1] + mat[i, j, k - 1] - 4 * mat[
                        i, j, k]) + mat[i, j, k]
        return mat
inp = int(input(f"Enter time less than {preprocessing.max_time} and greater than 0:"))
def graph(k,t):
    plt.clf()
    plt.title("Heat Equation graph")
    plt.xlabel("x")
    plt.ylabel("y")
    a=preprocessing(t)
    plt.pcolormesh(obj.value_calc()[k], cmap=plt.cm.jet, vmin=0, vmax=a.first_wall)
    plt.colorbar()
    plt.show()


if inp>0 and inp<preprocessing.max_time:
    obj = calc(inp)
    inp1=int(input("Enter an instance on which you want to view the graph(must be less than the time entered earlier):"))
    if inp1<inp and inp1>0:
        graph(inp1,inp)
    else:
        print("Invalid value for instance")
else:
    print("Invalid value for time")

