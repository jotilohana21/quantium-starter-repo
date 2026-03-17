from app import app
import pytest

# Simple test to check if the app starts without errors
def test_header_text(dash_duo):
    # Yeh line app ko start karti hai
    dash_duo.start_server(app)
    
    # Yeh check karta hai ke header sahi hai ya nahi
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualiser", timeout=4)

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    # Check if the graph is present
    assert dash_duo.find_element("#sales-line-chart")

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    # Check if the radio buttons are present
    assert dash_duo.find_element("#region-filter")