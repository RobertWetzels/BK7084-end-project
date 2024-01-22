from random import randint
import numpy as np
from city import BuildingType


class Optimizer:
    def __init__(self, city):
        """An optimizer that iteratively optimizes a given city grid."""
        self._city = city

    def step(self, print_info=True):
        """Performs a single optimization step.
        Args:
            print_info (bool):
                Whether to print information about the optimization step.
        """
        #######
        # calculate avg sunlight score
        avg_sun_score = np.mean(self._city.compute_sunlight_scores())
        print('avg_sun_score: ', avg_sun_score)

        # makes a list of all the plot types
        type = []
        for i in range (self._city._plots_per_col):
            for w in range (self._city._plots_per_row):
                type.append(self._city.get_building_type(w, i))     # returns type as 2 letter value, e.q. HS or SK
                # print('type ', i*self._city._plots_per_row+w, ':', type[i*self._city._plots_per_row+w])

        # determine score per plot
        plot_score = np.zeros(len(type))

        # substracting avg sunlight to scores
        plot_score += (11-avg_sun_score)/11*20

        for i in range(len(type)):
            if type[i] is BuildingType.HOUSE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 15
                        elif type[check_plot] is BuildingType.OFFICE:
                            plot_score[i] += 5
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 10
            elif type[i] is BuildingType.OFFICE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 15
                        elif type[check_plot] is BuildingType.HOUSE:
                            plot_score[i] += 5
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 10
            elif type[i] is BuildingType.SKYSCRAPER or type[i] is BuildingType.HIGHRISE or type[i] is BuildingType.EMPTY:
                plot_score[i] = 0
            elif type[i] is BuildingType.PARK:
                plot_score[i] = 2 * plot_score[i]

            print(f"Plot {i}: {plot_score[i]}")
        
        # for i in range(len(type)):
        #     if plot_score[i] < 5 and plot_score[i] != 0:                   
                    

        #######
        # buildingtype = []
        # for row in range(self._city._plots_per_col):
        #     for col in range(self._city._plots_per_row):
        #         buildingtype.append(self._city.get_building_type(col, row))   # gives 'HS' for exmple
        
        # score = np.zeros(len(buildingtype))
        # for row in range(self._city._plots_per_col):
        #     for col in range(self._city._plots_per_row):
        #         current_plot = row*self._city._plots_per_row + col
        #         print("\n\n\n\nType:")
        #         print(type(buildingtype[current_plot]))
        #         print(buildingtype[current_plot])
        #         print(BuildingType.HOUSE is buildingtype[current_plot])
        #         if buildingtype[current_plot] is BuildingType.HOUSE: 
        #             print("Hoi")
        #             score[current_plot] += 10
        #         print(buildingtype[current_plot], score[current_plot])


        # TODO: Implement your optimization algorithm here.
        # #  Hint: You can use the following code to swap two buildings:
        # row1, col1 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        # row2, col2 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        # self._city.swap_buildings(row1, col1, row2, col2)
        #  Hint: You can use the function `compute_sunlight_scores` of the City class
        #  to compute the sunlight scores
        new_scores = self._city.compute_sunlight_scores()
        if print_info:
            print("New scores: ", new_scores)
            print("New scores sum: ", sum(new_scores))
            print("New city layout: ")
            self._city.print_plots()
        return sum(new_scores)

    def optimize(self, n_steps=100, print_info=False):
        """
        Runs the optimizer for a fixed number of steps.
        Args:
            n_steps (int):
                The number of optimization steps.
            print_info (bool):
                Whether to print information about the optimization step.
        """
        # TODO: Change this method to add a stopping criterion, e.g. stop when
        #  the score does not improve anymore.
        self._city.reset_grid()
        print("Initial scores: ", self._city.compute_sunlight_scores())
        print("Initial scores sum: ", sum(self._city.compute_sunlight_scores()))
        print("Initial city layout: ")
        self._city.print_plots()
        print("Optimizing...")
        for i in range(n_steps):
            print(f"Step: {i}", end="\r")
            score = self.step(print_info)
            # TODO: Add a stopping criterion here.
        print(f"\nDone! Final score: {score}")