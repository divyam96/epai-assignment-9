# EPAi4.0 Assignment 9 
### Submitted by Divyam Malay Shah
### E-mail id: divyam096@gmail.com


# Sequence Types – 1

In Python, a sequence can be defined as a container that can essentially preserve the order of a collection of homogeneous or heterogeneous items which are iterable and indexable. Sequences can be further classified as mutable – where the items can be modified – and non-mutable – where the items cannot be modified. Examples of immutable sequences include tuple, strings etc., whereas examples of mutable sequences include list, dictionaries etc.

The present assignment is about accepting such arguments as number of vertices and the length of the circumradius of a polygon, and then making a module that will include the formula for calculating such measures as ¬¬

## Description of classes implemented in the current code

### Polygon

The class 'Polygon' accepts the number of vertices (greater than or equal to 3) and the circumradius of a polygon as input arguments. The various functions within the class calculate the measures of interior angle, edge length, apothem, area and perimeter for the polygon, till two places after decimal. 

Brief descriptions of the functions defined within the Polygon class are as follows:

#### `__init__()`

The initializer function defines that the class accepts two parameters - the number of vertices  of the polygon whose properties have to be calculated, and the circumradius of the same. Circumradius is expressed as the radius of an imaginary circle that can be inscribed around the polygon.

##### Usage:
Polygon(numberofvertices, circumradius)

#### `__repr__()`

The dunder method of representation function describes the messages that are displayed when the class Polygon is called without an argument.

##### Usage:
Polygon() (this invokes the __repr__ function)

#### `__eq__()`

The dunder method of equality has been defined to compare and return with an affirmative when the dimensions - number of vertices and circumradii - of two input polygons are equal.

##### Usage:
polygon1 == polygon2

where,  polygon1 = Polygon(numberofvertices1, circumradius1),
	 polygon2 = Polygon(numberofvertices2, circumradius2)

#### `__gt__()`

The dunder method of greater than has been defined to compare and return with an affirmative when the number of vertices of one input polygon is greater than the other.

##### Usage:
polygon1 > polygon2

where,  polygon1 = Polygon(numberofvertices1, circumradius1),
	 polygon2 = Polygon(numberofvertices2, circumradius2)
   

### PolygonSequence

This class creates a sequence of polygons with varying number of vertices and the same circumradius. The least possible number of vertices that a polygon can possess is three. The index of the sequence corresponds to the number of vertices in the polygon (which means that index values under 3 are not accepted). The circumradius is assumed to be the same for all the polygons. Brief descriptions of the functions defined within the Polygon class are as follows:


#### `__init__()`
The class is initialized in a way that it can accept the arguments of maximum vertices and circumradius.

##### Usage:
PolygonSequence(maxvertices, circumradius)

#### `__len__()`

The dunder method of length returns the number of polygons that are present within the sequence.

##### Usage:
len(PolygonSequence(maxvertices, circumradius))

#### `__getitem__()`

The dunder method of getitem returns the item in the sequence as per the index or the slice.

##### Usage:
custompolygon[3]

or

custompolygon[5:9:1]

where custompolygon = PolygonSequence (maxvertices, circumradius)


#### `__repr__()`

The dunder method of representation returns the polygon with the maximum number  of vertices and the common circumradius.

##### Usage:
PolygonSequence()

#### `maximum_efficient_polygon()`

A polygon that has the highest area to perimeter ratio is denoted as the maximum efficiency polygon. This function finds the polygon which has the maximum efficiency among all the others within the sequence.

##### Usage:

PolygonSequence(maxvertices, circumradius). maximum_efficient_polygon()

