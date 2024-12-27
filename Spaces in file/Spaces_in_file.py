def count_spaces_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            space_count = content.count(' ')
        with open(output_file, 'w') as file:
            file.write(f"Number of spaces: {space_count}\n")
        print(f"Result saved in {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the input file name: ").strip()
    output_file = input("Enter the output file name: ").strip()
    count_spaces_in_file(input_file, output_file)
