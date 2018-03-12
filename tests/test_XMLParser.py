
"""Tests for XMLParser"""

import pytest
import os

from pychemkin.parsers.XMLParser import XMLParser


# ======================= TESTS FOR XML PARSER OBJECT ====================== #

def test_XMLParser_file_not_found():
    """Test when xml file is nonexistent"""
    with pytest.raises(OSError):
        parser = XMLParser("no_such_file")

def test_XMLParser_species():
    """Test when reaction rate coefficient is modified
    Arrhenius but R is changed by user"""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert parser.get_species() == ({'H': None,'O': None, 'OH': None,
                                    'H2': None, 'H2O': None, 'O2': None})
    
def test_XMLParser_type():
    """Test get_rxn_type() for an elementary reaction."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert parser.reaction_list[0].rxn_type == 'Elementary'
    
def test_XMLParser_rate_coeffs_components():
    """Test get_rate_coeffs_components for reaction 1."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert (parser.reaction_list[0].rate_coeffs_components ==
            {'A': 35200000000.0, 'E': 71400.0})
    
def test_XMLParser_is_reversible():
    """Test get_is_reversible for reaction irreversible reaction."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert parser.reaction_list[0].is_reversible == False

def test_XMLParser_rxn_equation():
    """Test get_rxn_equation for reaction 1."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert parser.reaction_list[0].rxn_equation == 'H + O2 =] OH + O'
    
def test_XMLParser_reactant_stoich_coeffs():
    """Test get_reactant_stoich_coeffs for reaction 1."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert (parser.reaction_list[0].reactant_stoich_coeffs ==
            {'H': 1, 'H2': 0, 'H2O': 0, 'O': 0, 'O2': 1, 'OH': 0})

def test_XMLParser_product_stoich_coeffs():
    """Test get_product_stoich_coeffs for reaction 1."""
    xml_filename = "tests/test_xml_files/rxns.xml"
    parser = XMLParser(xml_filename)
    assert (parser.reaction_list[0].product_stoich_coeffs ==
            {'H': 0, 'H2': 0, 'H2O': 0, 'O': 1, 'O2': 0, 'OH': 1})

def test_arr_A():
    """Test when parameter A (for computing
    Arrrhenius reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/A_arr.xml"
        parser = XMLParser(xml_filename)
        
def test_arr_E():
    """Test when parameter E (for computing
    Arrrhenius reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/E_arr.xml"
        parser = XMLParser(xml_filename)

def test_mod_arr_A():
    """Test when parameter A (for computing
    modified Arrrhenius reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/A_mod_arr.xml"
        parser = XMLParser(xml_filename)

def test_mod_arr_b():
    """Test when parameter b (for computing
    modified Arrrhenius reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/b_mod_arr.xml"
        parser = XMLParser(xml_filename)
        
def test_mod_arr_E():
    """Test when parameter E (for computing
    modified Arrrhenius reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/E_mod_arr.xml"
        parser = XMLParser(xml_filename)
        
def test_const_k():
    """Test when k (for computing
    constant reaction rate coeff)
    is missing from xml file"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/k_const.xml"
        parser = XMLParser(xml_filename)

def test_convert_units_when_no_units():
    """Test when set convert_units to True but no units in xml"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/A_arr.xml"
        parser = XMLParser(xml_filename, convert_units=True)

    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/A_mod_arr.xml"
        parser = XMLParser(xml_filename, convert_units=True)

def test_unhandled_k():
    """Test when unhandled k inputed"""
    xml_filename = "tests/test_xml_files/unhandled_k.xml"
    with pytest.raises(NotImplementedError):
        parser = XMLParser(xml_filename)
        test_rxn = parser.reaction_list[0]
        parser.get_rate_coeffs_components(test_rxn)

def test_unhandled_k():
    """Test when b in arrhenius"""
    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/faulty_A_arr.xml"
        parser = XMLParser(xml_filename)

    with pytest.raises(ValueError):
        xml_filename = "tests/test_xml_files/faulty_A_arr.xml"
        parser = XMLParser(xml_filename, convert_units=True)

def test_madeup_units():
    """Test when unhandled units in xml"""
    with pytest.raises(NotImplementedError):
        xml_filename = "tests/test_xml_files/madeup_units_arr.xml"
        parser = XMLParser(xml_filename, convert_units=True)

    with pytest.raises(NotImplementedError):
        xml_filename = "tests/test_xml_files/madeup_units_mod_arr.xml"
        parser = XMLParser(xml_filename, convert_units=True)

