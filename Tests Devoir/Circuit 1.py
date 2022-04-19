#import examples.env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(81, 81))

    wires = [
        Wire(start=(14, 14), stop=(14, 55), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(14, 55), stop=(40, 55), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(40, 55), stop=(55, 55), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(55, 55), stop=(55, 14), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(55, 14), stop=(40, 14), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(40, 14), stop=(14, 14), current=Current(x=-1, y=0), voltage=4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()
