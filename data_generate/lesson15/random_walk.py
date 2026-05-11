from random import choice 

class RandomWalk:
    """Клас, що генерує випадкові блукання."""

    def __init__(self, num_points=5000):
        """Ініціалізувати атрибути блукання."""
        self.num_points = num_points

        #Всі блукання починаються з (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Обчислити всі точки блукання."""
        # Продовжувати робити кроки, доки блукання не досягне
        # необхідної довжини
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Відкинути кроки які нікуди не просуваються
            if x_step  == 0 and y_step == 0:
                continue

            # Розрахувати нову позицію
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
                    
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        # Вирішити, в якому напрямку рухатися та як довго 
        step_direction = choice([1, -1])
        step_distance = choice([0, 1, 2, 3, 4])
        step = step_direction * step_distance
        return step