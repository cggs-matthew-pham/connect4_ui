import tkinter as tk


class Connect4UI:

    def __init__(self, on_column=None):

        self.on_column = on_column

        self.root = tk.Tk()
        self.root.title("Robot Connect 4")

        self.cells = []

        self.create_buttons()
        self.create_board()

        self.status = tk.Label(
            self.root,
            text="Your turn",
            font=("Arial", 14)
        )

        self.status.pack(pady=(5, 20))


    def create_buttons(self):

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=(20, 5))

        for column in range(7):

            button = tk.Button(
                frame,
                text=str(column + 1),
                width=6,
                command=lambda c=column: self.column_clicked(c)
            )

            button.grid(
                row=0,
                column=column,
                padx=2
            )


    def create_board(self):

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=10)

        for row in range(6):

            row_cells = []

            for column in range(7):

                cell = tk.Label(
                    frame,
                    text="●",
                    width=4,
                    height=2,
                    font=("Arial", 24),
                    fg="light grey"
                )

                cell.grid(
                    row=row,
                    column=column,
                    padx=2,
                    pady=2
                )

                row_cells.append(cell)

            self.cells.append(row_cells)


    def column_clicked(self, column):

        if self.on_column:
            self.on_column(column)


    def update_board(self, board):

        colours = {
            0: "light grey",
            1: "red",
            2: "gold"
        }

        for row in range(6):
            for column in range(7):

                value = board[row][column]

                self.cells[row][column].config(
                    fg=colours[value]
                )


    def set_status(self, message):
        self.status.config(text=message)


    def run(self):
        self.root.mainloop()