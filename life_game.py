import json
import os
import time


class Life:
    def __init__(self, filename, visibility):
        with open(filename, 'r') as fh:
            parameters: dict = json.loads(fh.read())

        self._visibility: bool = visibility
        self._live_cell: str = parameters['live_cell']
        self._lifeless_cell: str = parameters['lifeless_cell']
        self._generations_quantity: int = parameters['generations_quantity']
        self._length: int = parameters['field_length']
        self._width: int = parameters['field_width']
        self._the_beginnings_of_life: list = parameters['first_generation']
        self._generation: list = self._get_first_generation()

    def _get_empty_field(self) -> list:
        empty_field = [
            [
                self._lifeless_cell for column in range(self._length)
            ] for line in range(self._width)
        ]

        return empty_field

    def _get_first_generation(self) -> list:
        first_generation: list = self._get_empty_field()

        for line_index, line_value in enumerate(self._the_beginnings_of_life):

            for column_index, column_value in enumerate(line_value):

                if column_value == self._live_cell:
                    first_generation[line_index][column_index]: str = column_value

        return first_generation

    def _save_life_result(self) -> None:
        record = ''
        for line in self._generation:
            record += f"{''.join(line)}\n"

        with open(f'life_result timestamp_{int(time.time())}.txt', 'w') as fh:
            fh.write(record)

    def _get_next_generation(self) -> None:
        next_generation: list = self._get_empty_field()
        neighbors = [-1, 0, 1]

        for line_index, line_value in enumerate(self._generation):

            for column_index, column_value in enumerate(line_value):
                neighbors_counter = 0

                for offset_line_index in neighbors:
                    for offset_column_index in neighbors:
                        # central cell
                        if offset_column_index == offset_line_index == 0:
                            continue

                        neighbor_line_index = 0 if (
                            line_index + offset_line_index == self._width
                        ) else line_index + offset_line_index

                        neighbor_column_index = 0 if (
                            column_index + offset_column_index == self._length
                        ) else column_index + offset_column_index

                        neighbors_counter += 1 if (
                            self._generation[neighbor_line_index][neighbor_column_index] == self._live_cell
                        ) else 0

                if column_value == self._live_cell:
                    # Checking living conditions
                    if neighbors_counter > 3 or neighbors_counter < 2:
                        next_generation[line_index][column_index] = self._lifeless_cell

                    else:
                        next_generation[line_index][column_index] = self._live_cell

                else:
                    # Checking the conditions of the origin of life.
                    if neighbors_counter == 3:
                        next_generation[line_index][column_index] = self._live_cell

        self._generation = next_generation

    def _draw_a_glider(self) -> None:
        for line in self._generation:
            for symbol in line:

                if symbol == self._live_cell:
                    print(self._live_cell, end='')

                else:
                    print(' ', end='')
            print(end='\n')

        tmp = os.system('cls') if os.name == 'nt' else os.system('clear')

    def _end_game(self) -> bool:
        result = False

        for line in self._generation:
            if self._live_cell in line:
                break
        else:
            result = True

        return result

    def life_itself(self) -> None:
        for generation in range(self._generations_quantity):

            try:
                if self._visibility:
                    self._draw_a_glider()
                    time.sleep(0.6)

                self._get_next_generation()

                if self._end_game():
                    break

            except KeyboardInterrupt:
                break

        self._save_life_result()


def main() -> None:
    filename = 'parameters.json'

    visibility = False
    if input('Do you want to see it?\n"y" - yes, another - no ').lower() == 'y':
        visibility = True

    life = Life(filename, visibility)
    life.life_itself()

    print('Done.')


if __name__ == '__main__':
    main()
