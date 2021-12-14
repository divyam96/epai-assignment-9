# Objective 1

import math

new_line = "\n"


class Polygon:
    """The class 'Polygon' accepts the number of vertices (greater than or equal to 3) and the circumradius \
    of a polygon as input arguments. The various functions within the class calculate the measures of \
    interior angle, edge length, apothem, area and perimeter for the polygon,to upto two places after decimal."""

    def __init__(self, numberofvertices, circumradius):
        """The initializer function defines that the class accepts two parameters - the number of vertices \
        of the polygon whose properties have to be calculated, and the circumradius of the same. Circumradius \
        is expressed as the radius of an imaginary circle that can be inscribed around the polygon."""

        if (isinstance(numberofvertices, int)) == False:
            raise TypeError("Please enter an integer only")
        if (numberofvertices < 0):
            raise ValueError("The number of vertices should be a positive value")
        if (numberofvertices <= 2):
            raise ValueError("The number of vertices should be greater than or equal to three")
        if ((isinstance(circumradius, int) or isinstance(circumradius, float)) == False):
            raise TypeError("The value of circumradius should be an int or a float")

        self.numberofvertices = numberofvertices
        self.circumradius = circumradius
        self.interiorangle = round((numberofvertices - 2) * (180 / numberofvertices), 2)
        self.edgelength = round(2 * circumradius * math.sin(math.pi / numberofvertices), 2)
        self.apothem = round(circumradius * math.cos(math.pi / numberofvertices), 2)
        self.area = round(((1 / 2) * numberofvertices * self.edgelength * self.apothem), 2)
        self.perimeter = round((numberofvertices * self.edgelength), 2)

    def __repr__(self):
        """The dunder method of representation function describes the messages that are displayed when the class Polygon \
        is called without an argument."""

        return (
            f'For a polygon with the number of vertices {self.numberofvertices} and a circumradius of {self.circumradius}{new_line}, \
        The measure of interior angle is {self.interiorangle}{new_line}. \
        The measure of edge length is {self.edgelength}{new_line}. \
        The measure of apothem is {self.apothem}{new_line}. \
        The measure of area is {self.area}{new_line}. \
        The measure of perimeter is {self.perimeter}{new_line}')

    def __eq__(self, other):
        """The dunder method of equality has been defined to compare and return with an affirmative when the dimensions - \
        number of vertices and circumradius - of two input polygons are equal."""

        if (self.numberofvertices == other.numberofvertices) and (self.circumradius == other.circumradius):
            return True
        else:
            return False

    def __gt__(self, other):
        """The dunder method of greater than has been defined to compare and return with an affirmative when the number of \
        vertices of one input polygon is greater than the other."""

        if self.numberofvertices > other.numberofvertices:
            return True
        else:
            return False


class PolygonSequence:
    """This class creates a sequence of polygons with varying number of vertices and the same circumradius.The least possible \
    number of vertices that a polygon can possess is three. Thus, the indexing of the polygon in the sequence will be initiated \
    in such a way that the 0th element corresponds to 3 and so on. The circumradius is assumed to be the same for all the polygons."""

    def __init__(self, maxvertices, circumradius):
        """The class is initialized in a way that it can accept the arguments of maximum vertices and circumradius."""

        self._maxn = maxvertices
        self._r = circumradius

    def __len__(self):
        """The dunder method of length returns the number of polygons that are present within the sequence"""

        return self._maxn

    def __getitem__(self, s):
        """The dunder method of getitem selects the highest possible index"""

        if isinstance(s, int):
            # single item requested
            if 0 <= s < 3:
                return None
            if s > self._maxn:
                raise IndexError
            if s < 0:
                s = self._maxn + s
            if s < 0 or s > self._maxn - 1:
                raise IndexError
            return Polygon(s, self._r)
        else:
            # slice being requested
            print(f'requesting [{s.start}:{s.stop}:{s.step}]')
            idx = s.indices(self._maxn)
            rng = range(idx[0], idx[1], idx[2])
            return [Polygon(n, self._r) if n>2 else None for n in rng]

    def __repr__(self):
        """The dunder method of representation returns the polygon with the maxium number  of vertices and the common
        circumradius. """

        return (f'This is a PolygonSequence class with polygons upto {self._maxn} vertices and {self._r} circumradius')

    def maximum_efficient_polygon(self):
        """A polygon that has the highest area:perimeter ratio is denoted as the maximum efficiency polygon.\
        This function finds the polygon which has the maximum efficiency among all the others within the sequence."""

        print("Maximum efficient polygon")
        apr_list = []
        for idx in range(3, self._maxn):
            p = Polygon(idx, self._r)
            area_perimeter_ratio = p.area / p.perimeter
            apr_list.append(area_perimeter_ratio)
        return max(apr_list)
