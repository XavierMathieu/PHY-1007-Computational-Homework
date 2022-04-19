import numpy as np
from scipy.constants import mu_0, pi

from src.fields import VectorField


class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def solve(self, electric_current: VectorField) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world.
        """

        Fils_Hor = np.where(electric_current.x != 0)
        #donne deux arrays (x et y) qui sont les coordonnées des fils
        Fils_Vert = np.where(electric_current.y != 0)
        #donne deux arrays (x et y) qui sont les coordonnées des fils

        
        raise NotImplementedError
