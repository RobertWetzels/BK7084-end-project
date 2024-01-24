from random import randint
import numpy as np
from city import BuildingType


class Optimizer:
    def __init__(self, city):
        """An optimizer that iteratively optimizes a given city grid."""
        self._city = city

    def step(self, treshhold=20, print_info=True):
        """Performs a single optimization step.
        Args:
            print_info (bool):
                Whether to print information about the optimization step.
        """
        # makes a list of all the plot types
        type = []
        for i in range (self._city._plots_per_col):
            for w in range (self._city._plots_per_row):
                type.append(self._city.get_building_type(i, w))     # returns type as 2 letter value, e.q. HS or SK
                # num = i*self._city._plots_per_row+w
                # print('type {num}:', type[i*self._city._plots_per_row+w])

        # calculate avg sunlight score
        avg_sun_score = np.mean(self._city.compute_sunlight_scores())
        print('avg_sun_score: ', avg_sun_score)

        # determine score per plot
        plot_score = np.zeros(len(type))

        # substracting avg sunlight to scores
        plot_score += (11-avg_sun_score)/10*20

        # determining the score of every plot in the city, direct neighbours
        for i in range(len(type)):
            if type[i] is BuildingType.HOUSE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    # check but exclude check_plot when on the other side of the city
                    # first condition checks if check_plot lies within range of the type list
                    # second condition checks if check_plot is a direct neighbour of plot i 
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 15
                        elif type[check_plot] is BuildingType.OFFICE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 15
            elif type[i] is BuildingType.OFFICE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.HOUSE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 10
            elif type[i] is BuildingType.SKYSCRAPER or type[i] is BuildingType.HIGHRISE or type[i] is BuildingType.EMPTY:
                plot_score[i] = 0
            elif type[i] is BuildingType.PARK:
                plot_score[i] = 2 * plot_score[i]
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 20
                        elif type[check_plot] is BuildingType.HOUSE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.OFFICE:
                            plot_score[i] += 10
            # print('type ', i, ':', type[i], ', score: ', plot_score[i]
    
        initial_scores = plot_score
        # print("Initial scores: ", initial_scores)
        print("Initial scores sum: ", sum(initial_scores))
        # print("Initial city layout: ")
        # self._city.print_plots()

        # switch all with score < treshold with empty plots or scores similar to (type empty)
        for i in range(len(plot_score)):
            if plot_score[i] < treshhold and plot_score[i] != 0:
                plot1 = i
                w = 1
                while w < len(plot_score):
                    plot2 = (i+w)%(self._city.plots_per_col*self._city.plots_per_row)
                    if type[plot2] == BuildingType.EMPTY or (plot_score[plot2] != 0 and plot_score[plot2] < plot_score[plot1]):
                        break
                    w +=1
                
                # switch plots 1 and 2
                row1, col1 = plot1 // self._city.plots_per_row, plot1 % self._city.plots_per_row
                row2, col2 = plot2 // self._city.plots_per_row, plot2 % self._city.plots_per_row
                self._city.swap_buildings(row1, col1, row2, col2)
                type[plot2] = type[plot1]
                type[plot1] = BuildingType.EMPTY
                plot_score[plot2] = 0       # this plot shouldn't be optimized anymore before new score is determined

        # calculate avg sunlight score
        avg_sun_score = np.mean(self._city.compute_sunlight_scores())
        print('new_avg_sun_score: ', avg_sun_score)
        
        # determine score per plot
        plot_score = np.zeros(len(type))

        # substracting avg sunlight to scores
        plot_score += (11-avg_sun_score)/10*20

        # determining the new score of every plot in the city, just like before
        for i in range(len(type)):
            if type[i] is BuildingType.HOUSE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    # check but exclude check_plot when on the other side of the city
                    # first condition checks if check_plot lies within range of the type list
                    # second condition checks if check_plot is a direct neighbour of plot i 
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 15
                        elif type[check_plot] is BuildingType.OFFICE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 15
            elif type[i] is BuildingType.OFFICE:
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.PARK:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.HOUSE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 10
            elif type[i] is BuildingType.SKYSCRAPER or type[i] is BuildingType.HIGHRISE or type[i] is BuildingType.EMPTY:
                plot_score[i] = 0
            elif type[i] is BuildingType.PARK:
                plot_score[i] = 2 * plot_score[i]
                for w in range(9):
                    check_plot = (i-1) + self._city._plots_per_row * (w // 3 - 1) + w % 3
                    if 0 <= check_plot < self._city._plots_per_row * self._city._plots_per_col and np.abs((i%self._city._plots_per_row)-(check_plot%self._city._plots_per_row)) <= 1:
                        if type[check_plot] is BuildingType.SKYSCRAPER or type[check_plot] is BuildingType.HIGHRISE:
                            plot_score[i] -= 20
                        elif type[check_plot] is BuildingType.HOUSE:
                            plot_score[i] += 10
                        elif type[check_plot] is BuildingType.OFFICE:
                            plot_score[i] += 10
            # print('type ', i, ':', type[i], ', score: ', plot_score[i])
                
        new_scores = plot_score
        if print_info:
            # print("New scores: ", new_scores)
            print("New scores sum: ", sum(new_scores))
            # print("New city layout: ")
            # self._city.print_plots()
            self._city.get_buliding_numbers()
        return sum(new_scores)

    def optimize(self, n_steps=1000):
        """
        Runs the optimizer for a fixed number of steps.
        Args:
            n_steps (int):
                The number of optimization steps.
        """
        print("Optimizing...")

        # define some values
        best_score = float('-inf')
        no_improvement_count = 0
        improvement_treshold = 10
        minimum_score_of_plot = 35
        patience = 10

        for i in range(n_steps):
            print(f"Step: {i}", end="\r")
            score = self.step(minimum_score_of_plot)
            # TODO: Add a stopping criterion here.
            if best_score < -100000:
                first_score = score
            if score > best_score + improvement_treshold:
                best_score = score
                no_improvement_count = 0
            else:
                no_improvement_count += 1
            if no_improvement_count >=patience:
                print(f"\nStopping optimization. No improvement for the last {patience} steps.")
                break
            
            print('count: ', no_improvement_count)

        print(f"\nDone! \nFinal score: {score} \nScore before optimizing: {first_score}")