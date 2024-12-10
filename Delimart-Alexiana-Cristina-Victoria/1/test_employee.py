import pytest
from employee import Employee, Manager  # presupunem că programul inițial este în `main.py`

@pytest.fixture
def reset_employees_and_managers():
    Employee.everyone = []
    Employee.emp_count = 0
    Manager.mgr_count = 0

def test_employee_creation(reset_employees_and_managers):
    emp1 = Employee("Ana", 3000, "HR")
    assert emp1.name == "Ana"
    assert emp1.salary == 3000
    assert emp1.department == "HR"
    assert Employee.emp_count == 1
    assert emp1 in Employee.everyone

def test_manager_creation(reset_employees_and_managers):
    mgr1 = Manager("George", 50000, "IT")
    assert mgr1.name == "George"
    assert mgr1.salary == 50000
    assert mgr1.department == "IT"
    assert Manager.mgr_count == 1
    assert Employee.emp_count == 1
    assert mgr1 in Employee.everyone

def test_display_employee(capsys, reset_employees_and_managers):
    emp1 = Employee("Mihai", 4000, "Design")
    emp1.display_employee()
    captured = capsys.readouterr()
    assert captured.out == "Design\n"

def test_total_counts(reset_employees_and_managers):
    mgr1 = Manager("Andrei", 60000, "Finance")
    mgr2 = Manager("Maria", 70000, "HR")
    emp1 = Employee("Elena", 4500, "IT")
    assert Manager.mgr_count == 2
    assert Employee.emp_count == 3
