import subprocess
import task_1

def test_exponentiation_result():
    # Import variables from the task script
    a = task_1.a
    b = task_1.b
    result = task_1.result

    # Check the result
    expected_result = a ** b

    assert result == expected_result, f"Expected result to be {expected_result} but got {result}"

def test_printed_output():

    # Import variables from the task script
    a = task_1.a
    b = task_1.b
    result = task_1.result
  
    # Run the task script
    result = subprocess.run(['python', 'task_1.py'], capture_output=True, text=True)
    
    # Check the printed output
    expected_output = f"Result: {expected_result}"  # Adjust based on example values in the task script
    assert result.stdout == expected_output, f"Expected '{expected_output}' but got '{result.stdout}'"

if __name__ == "__main__":
    test_exponentiation_result()
    test_printed_output()
