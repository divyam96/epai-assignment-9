import pytest
import polygon
import inspect
import re


def test_function_name_had_cap_letter():
    """PEP8 gudelines state that function names cannnot have capital letters in them. This test checks if there are any \
    capital lettes within function names and throws error if there are."""

    functions = inspect.getmembers(polygon.polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


################################ Validation for Objective 1: Creating a polygon.Polygon class,  polygon_class ######################################

def test_polygon_class_number_of_vertices():
    """Test to ensure that the input argument for the number of vertices is an interger."""

    with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
        polygon.Polygon("hello", 5)


def test_polygon_class_positive_value_for_vertices():
    """Test to ensure that the input argument for the number of vertices is a positive value."""

    with pytest.raises(ValueError, match=r".*The number of vertices should be a positive value*"):
        polygon.Polygon(-3, 5)


def test_polygon_class_greater_than_or_equal_to_three_vertices():
    """Test to ensure that the value of the input argument for the number of vertices is equal to greater than 3."""

    with pytest.raises(ValueError, match=r".*The number of vertices should be greater than or equal to three*"):
        polygon.Polygon(1, 5)


def test_polygon_class_circumradius_int_or_float():
    """Test to ensure that the value of the input argument for the circumradius is either of an int or a float type."""

    with pytest.raises(TypeError, match=r".*The value of circumradius should be an int or a float*"):
        polygon.Polygon(4, "circumradius")


def test_polygon_class_value_of_properties_are_positive():
    """Test to ensure that the calculated values of the interior angle, edge length, apothem, area and perimeter are positive."""

    p = polygon.Polygon(4, 5)
    assert (p.interiorangle > 0), "The value of the interior angle should be a positive value"
    assert (p.edgelength > 0), "The value of the edge length should be a positive value"
    assert (p.apothem > 0), "The value of the apothem should be a positive value"
    assert (p.area > 0), "The value of the area should be a positive value"
    assert (p.perimeter > 0), "The value of the perimeter should be a positive value"


def test_polygon_class_output_check():
    """Test to ensure that the defined representation class returns the appropriate results"""

    p = polygon.Polygon(4, 5)
    assert (bool(p) == True), "The class is not giving appropriate output"

def test_polygon_class_repr_check():
    """Test to ensure that the proper description of the class is being output by \
    the representation class."""

    check_list = ["interior angle", "edge length", "apothem", "area", "perimeter"]
    reprcomplete = True
    p = polygon.Polygon(4, 5)
    reprout = p.__repr__()
    for c in check_list:
        if c not in reprout:
            reprcomplete = False
    assert reprcomplete == True, "The representation function has not been implemented"


def test_polygon_class_equality_check():
    """Test to ensure that the values of the number of vertices and circumradiuses are being compared with accuracy."""

    p1 = polygon.Polygon(4, 5)
    p2 = polygon.Polygon(4, 5)
    assert (p1 == p2),"The comparison of number of vertices and circumradius is not accurate"


def test_polygon_class_greater_than_check():
    """Test to ensure that the algorithm is correctly distinguishing between two polygons whose vertices are not the same, \
    specifically when one is greater than the other."""
    p1 = polygon.Polygon(5, 5)
    p2 = polygon.Polygon(4, 5)
    assert (p1 > p2),"The comparison of number of vertices is not accurate"




################################ Validation for Objective 2: Creating a Custom Polygon Sequence ######################


def test_polygon_sequence_class_repr_check():
    """Test to ensure that the proper description of the class is being output by \
    the representation class."""

    check_list = ["PolygonSequence", "class",  "polygons", "vertices", "circumradius"]
    reprcomplete = True
    ps = polygon.PolygonSequence(10, 5)
    reprout = ps.__repr__()
    for c in check_list:
        if c not in reprout:
            print(c)
            reprcomplete = False
    assert reprcomplete == True, "The representation function has not been implemented"


def test_polygon_sequence_length_check():
    """Test to check the length of the polygon sequence
    """
    ps = polygon.PolygonSequence(10, 5)
    assert len(ps) == 10, "Length function not implemnted correctly"


def test_polygon_sequence_index_access():
    """Test to check if indexing works on our PolygonSequence class
    """
    ps = polygon.PolygonSequence(10, 5)
    p1 = ps[3]
    p2 = ps[5]
    assert isinstance(p1, polygon.Polygon), "Indexing does not seem to work on PolygonSequence"
    assert isinstance(p2, polygon.Polygon), "Indexing does not seem to work on PolygonSequence"


def test_polygon_sequence_maximum_efficient_polygon():
    """Test to check the maximum_efficient_polygon function
    """
    ps = polygon.PolygonSequence(10, 5)
    assert round(ps.maximum_efficient_polygon(), 2) == 2.35, "Something is wrong in finding maximum efficient polygon"
