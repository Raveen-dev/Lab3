import employee_info  # Imports your employee script

def test_get_employees_by_age_range():
    # Employees strictly between 25 and 35 are John (30) and Mike (32)
    result = employee_info.get_employees_by_age_range(25, 35)
    
    # Check that it found exactly 2 employees
    assert len(result) == 2
    # Check that John is one of them
    assert result[0]["name"] == "John"
    assert result[1]["name"] == "Mike"

def test_calculate_average_salary():
    # Total salaries: 50k + 60k + 56k + 70k + 65k + 60k = 361000
    # Average: 361000 / 6 = 60166.67
    expected_average = 361000 / 6
    actual_average = employee_info.calculate_average_salary()
    
    # Standard Python assert to check if they match
    assert actual_average == expected_average

def test_get_employees_by_dept():
    # Test filtering for the 'Marketing' department (Jane and Mary)
    result = employee_info.get_employees_by_dept("Marketing")
    
    assert len(result) == 2
    assert result[0]["name"] == "Jane"
    assert result[1]["name"] == "Mary"