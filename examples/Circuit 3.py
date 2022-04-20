import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(141, 141))

    wires = [
        Wire(start=(19, 44), stop=(19, 95), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(19, 95), stop=(110, 95), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(110, 95), stop=(120, 95), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(120, 95), stop=(120, 44), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(120, 44), stop=(110, 44), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(110, 44), stop=(19, 44), current=Current(x=-1, y=0), voltage=4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()