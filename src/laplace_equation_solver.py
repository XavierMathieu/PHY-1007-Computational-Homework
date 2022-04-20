import numpy as np

from src.fields import ScalarField


class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 1000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def solve(self, constant_voltage: ScalarField) -> ScalarField:
        """
        Solve the Laplace equation to compute the potential field given a constant voltage field.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the wires' voltage at a given point (x, y)
            in space.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e in
            the wires and in the empty space between the wires, while the field V always gives V(x, y) = 0 if (x, y)
            is not a point belonging to an electric wire.
        """

        (x,y) = constant_voltage.shape
        Fils = constant_voltage != 0
        voltage_iter = np.zeros((x+2,y+2))

        voltage_iter[1:-1, 1:-1] = constant_voltage

        i=True
        Voltage = voltage_iter[1:-1, 1:-1]

        for i in range(self.nb_iterations):
            voltage_iter[1:-1, 1:-1] = (voltage_iter[1:-1, 2:]+voltage_iter[1:-1, :-2]+voltage_iter[2:, 1:-1]+voltage_iter[:-2, 1:-1])/4
            voltage_iter[1:-1, 1:-1][Fils==True] = 0
            voltage_iter[1:-1, 1:-1] = voltage_iter[1:-1, 1:-1] + constant_voltage
            

        return ScalarField(voltage_iter[1:-1, 1:-1])
