import sys

def evaluate_submission(notebook_path, student_name):
    print(f"Evaluating {notebook_path} submitted by {student_name}")
    # You can run custom logic here (e.g., grading the notebook)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evaluate.py <notebook_path> <student_name>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    student_name = sys.argv[2]

    evaluate_submission(notebook_path, student_name)
