import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(121, 121))

    wires = [
        Wire(start=(9, 9), stop=(9, 110), current=Current(x=0, y=1), voltage= 5),
        Wire(start=(9, 110), stop=(30, 110), current=Current(x=1, y=0), voltage= 5),
        Wire(start=(30, 110), stop=(61, 110), current=Current(x=1, y=0), voltage= 1),
        Wire(start=(61, 110), stop=(61, 61), current=Current(x=0, y=-1), voltage= 1),
        Wire(start=(61, 61), stop=(110, 61), current=Current(x=1, y=0), voltage= 1),
        Wire(start=(110, 61), stop=(110, 30), current=Current(x=0, y=-1), voltage= 1),
        Wire(start=(110, 30), stop=(110, 9), current=Current(x=0, y=-1), voltage= -5),
        Wire(start=(110, 9), stop=(30, 9), current=Current(x=-1, y=0), voltage= -5),
        Wire(start=(30, 9), stop=(9, 9), current=Current(x=-1, y=0), voltage= 5),
    ]


    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()