import sys

from stats import generate_report

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    generate_report(filepath)


if __name__ == "__main__":
    main()