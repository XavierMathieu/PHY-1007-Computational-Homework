import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(81, 81))

    wires = [
        Wire(start=(15, 15), stop=(15, 66), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(15, 66), stop=(60, 66), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(60, 66), stop=(66, 66), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(66, 66), stop=(66, 15), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(66, 15), stop=(21, 15), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(21, 15), stop=(15, 15), current=Current(x=-1, y=0), voltage=4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()