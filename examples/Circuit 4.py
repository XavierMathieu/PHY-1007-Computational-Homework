import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(141, 141))

    wires = [
        Wire(start=(19, 19), stop=(19, 120), current=Current(x=0, y=1), voltage= 5),
        Wire(start=(19, 120), stop=(40, 120), current=Current(x=1, y=0), voltage= 5),
        Wire(start=(40, 120), stop=(71, 120), current=Current(x=1, y=0), voltage= 1),
        Wire(start=(71, 120), stop=(71, 71), current=Current(x=0, y=-1), voltage= 1),
        Wire(start=(71, 71), stop=(120, 71), current=Current(x=1, y=0), voltage= 1),
        Wire(start=(120, 71), stop=(120, 40), current=Current(x=0, y=-1), voltage= 1),
        Wire(start=(120, 40), stop=(120, 19), current=Current(x=0, y=-1), voltage= -5),
        Wire(start=(120, 19), stop=(40, 19), current=Current(x=-1, y=0), voltage= -5),
        Wire(start=(40, 19), stop=(19, 19), current=Current(x=-1, y=0), voltage= 5),
    ]


    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()