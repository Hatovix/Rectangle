import math

from typing import List, Tuple


class Rectangle:
    """
    A class used to represent a Rectangle, using only five sine qua non parameters.

    Attributes
    ----------
    x_center : float
        center of the rectangle on x axis
    y_center : float
        center of the rectangle on y axis
    radius : float
        distance from the center to any vertex
    alpha_angle : float
        orientation of the first diagonal
    beta_angle : float
        orientation of the second diagonal
    p1 : Tuple[float, float]
        first vertex of the rectangle, on first diagonal
    p2 : Tuple[float, float]
        second vertex of the rectangle, on second diagonal
    p3 : Tuple[float, float]
        third vertex of the rectangle, on first diagonal
    p4 : Tuple[float, float]
        fourth vertex of the rectangle, on second diagonal
    area : float
        area of the rectangle
    """

    def __init__(self, x_center: float, y_center: float, radius: float, alpha_angle: float, beta_angle: float) -> None:
        """
        Parameters
        ----------
        x_center : float
            center of the rectangle on x axis
        y_center : float
            center of the rectangle on y axis
        radius : float
            distance from the center to any vertex
        alpha_angle : float
            orientation of the first diagonal
        beta_angle : float
            orientation of the second diagonal
        """
        self.x_center = x_center
        self.y_center = y_center
        self.radius = abs(radius)
        self.alpha_angle = alpha_angle
        self.beta_angle = beta_angle
        self.p1 = self.vertex_calculation(self.alpha_angle)
        self.p2 = self.vertex_calculation(self.beta_angle)
        self.p3 = self.opposite_vertex(self.p1)
        self.p4 = self.opposite_vertex(self.p2)
        self.area = self.area_calculation()

    def vertex_calculation(self, angle: float) -> Tuple[float, float]:
        """
        Vertex calculation following a given angle orientation from rectangle center.

        Parameters
        ----------
        angle : float
            angle orientation from center to vertex

        Returns
        ----------
        Tuple[float, float]
            the resulting vertex point coordinates (x, y)
        """
        return (self.radius * math.cos(angle) + self.x_center,
                self.radius * math.sin(angle) + self.y_center)

    def opposite_vertex(self, vertex: Tuple[float, float]) -> Tuple[float, float]:
        """
        Opposite vertex calculation (same diagonal) of a given vertex.

        Parameters
        ----------
        vertex : Tuple[float, float]
            the source vertex to consider

        Returns
        ----------
        Tuple[float, float]
            the resulting vertex point coordinates (x, y)
        """
        return (2 * self.x_center - vertex[0],
                2 * self.y_center - vertex[1])

    def distance_calculation(self, point_a: Tuple[float, float], point_b: Tuple[float, float]) -> float:
        """
        Euclidean distance between two given points.

        Parameters
        ----------
        point_a : Tuple[float, float]
            the first point to consider
        point_b : Tuple[float, float]
            the second point to consider

        Returns
        ----------
        float
            the Euclidean distance between the two points
        """
        return math.sqrt(pow(point_a[0] - point_b[0], 2) + pow(point_a[1] - point_b[1], 2))

    def area_calculation(self) -> float:
        """
        Area calculation of the rectangle.

        Returns
        ----------
        float
            the area of the rectangle
        """
        return self.distance_calculation(self.p1, self.p2) * self.distance_calculation(self.p2, self.p3)

    def change_x_center(self, new_x_center: float) -> None:
        """
        Change the center of the rectangle on x axis.

        Parameters
        ----------
        new_x_center : float
            new center of the rectangle on x axis
        """
        delta = new_x_center - self.x_center
        self.x_center = new_x_center
        self.p1 = (self.p1[0] + delta, self.p1[1])
        self.p2 = (self.p2[0] + delta, self.p2[1])
        self.p3 = (self.p3[0] + delta, self.p3[1])
        self.p4 = (self.p4[0] + delta, self.p4[1])

    def change_y_center(self, new_y_center: float) -> None:
        """
        Change the center of the rectangle on y axis.

        Parameters
        ----------
        new_y_center : float
            new center of the rectangle on y axis
        """
        delta = new_y_center - self.y_center
        self.y_center = new_y_center
        self.p1 = (self.p1[0], self.p1[1] + delta)
        self.p2 = (self.p2[0], self.p2[1] + delta)
        self.p3 = (self.p3[0], self.p3[1] + delta)
        self.p4 = self.p4[0], self.p4[1] + delta

    def change_radius(self, new_radius: float) -> None:
        """
        Change the radius of the rectangle.

        Parameters
        ----------
        new_radius : float
            new distance from the center to any vertex
        """
        self.radius = abs(new_radius)
        self.p1 = self.vertex_calculation(self.alpha_angle)
        self.p2 = self.vertex_calculation(self.beta_angle)
        self.p3 = self.opposite_vertex(self.p1)
        self.p4 = self.opposite_vertex(self.p2)
        self.area = self.area_calculation()

    def change_alpha_angle(self, new_alpha_angle: float) -> None:
        """
        Change the alpha_angle of the rectangle.

        Parameters
        ----------
        new_alpha_angle : float
            new orientation of the first diagonal
        """
        self.alpha_angle = new_alpha_angle
        self.p1 = self.vertex_calculation(self.alpha_angle)
        self.p3 = self.opposite_vertex(self.p1)
        self.area = self.area_calculation()

    def change_beta_angle(self, new_beta_angle: float) -> None:
        """
        Change the beta_angle of the rectangle.

        Parameters
        ----------
        new_beta_angle : float
            new orientation of the second diagonal
        """
        self.beta_angle = new_beta_angle
        self.p2 = self.vertex_calculation(self.beta_angle)
        self.p4 = self.opposite_vertex(self.p2)
        self.area = self.area_calculation()

    def get_vertices(self) -> List[Tuple[float, float]]:
        """
        Gets in consecutive order the four vertices of the rectangle.

        Returns
        ----------
        List[Tuple[float, float]]
            list of the four vertices of the rectangle
        """
        return [self.p1, self.p2, self.p3, self.p4]

    def get_center(self) -> Tuple[float, float]:
        """
        Gets the center of the rectangle.

        Returns
        ----------
        Tuple[float, float]
            coordinates of the center (x, y)
        """
        return (self.x_center,
                self.y_center)

    def get_x_center(self) -> float:
        """
        Gets the center of the rectangle on x axis.

        Returns
        ----------
        float
            center of the rectangle on x axis
        """
        return self.x_center

    def get_y_center(self) -> float:
        """
        Gets the center of the rectangle on y axis.

        Returns
        ----------
        float
            center of the rectangle on y axis
        """
        return self.y_center

    def get_radius(self) -> float:
        """
        Gets the radius of the rectangle.

        Returns
        ----------
        float
            distance from the center to any vertex
        """
        return self.radius

    def get_alpha_angle(self) -> float:
        """
        Gets the alpha_angle of the rectangle.

        Returns
        ----------
        float
            orientation of the first diagonal
        """
        return self.alpha_angle

    def get_beta_angle(self) -> float:
        """
        Gets the beta_angle of the rectangle.

        Returns
        ----------
        float
            orientation of the second diagonal
        """
        return self.beta_angle

    def pretty_point(self, name: str, point: Tuple[float, float]) -> str:
        """
        Gets a pretty version of a given point.

        Parameters
        ----------
        name : str
            name of the point
        point : Tuple[float, float]
            coordinates of the point

        Returns
        ----------
        str
            a pretty version of the given point
        """
        return f'{name} ({round(point[0], 3)};{round(point[1], 3)})'
    
    def __eq__(self, other: 'Rectangle') -> bool:
        """
        Rectangle equality comparison.

        Returns
        ----------
        bool
            the equality comparison result
        """
        return self.get_center() == other.get_center() \
               and self.radius == other.get_radius() \
               and (self.alpha_angle == other.get_alpha_angle() and self.beta_angle == other.get_beta_angle()
                    or self.alpha_angle == other.get_beta_angle() and self.beta_angle == other.get_alpha_angle())

    def __str__(self) -> str:
        """
        Gets the readable version of the rectangle.

        Returns
        ----------
        str
            the readable version of the rectangle
        """
        return f'\n'.join([self.pretty_point(f'P{i+1}', point) for i, point in enumerate(self.get_vertices())])

    def __repr__(self) -> str:
        """
        Gets the unambiguous version of the rectangle.

        Returns
        ----------
        str
            the unambiguous version of the rectangle
        """
        return f'Rectangle(' \
               f'x_center={self.x_center}, ' \
               f'y_center={self.y_center}, ' \
               f'radius={self.radius}, ' \
               f'alpha_angle={self.alpha_angle}, ' \
               f'beta_angle={self.beta_angle}' \
               f')\n'
