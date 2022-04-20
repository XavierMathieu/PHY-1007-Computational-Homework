import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(121, 121))

    wires = [
        Wire(start=(9, 34), stop=(9, 85), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(9, 85), stop=(100, 85), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(100, 85), stop=(110, 85), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(110, 85), stop=(110, 34), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(110, 34), stop=(100, 34), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(100, 34), stop=(9, 34), current=Current(x=-1, y=0), voltage=4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()