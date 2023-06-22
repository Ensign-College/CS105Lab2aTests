import os
from subprocess import run, Popen, PIPE


def remove_main(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file: {e.filename} - {e.strerror}")


def compile_and_run_java(java_file):
    # Compile the Java file
    run(['javac', java_file])

    # Get the class name by removing the file extension
    class_name = java_file.rsplit('.', 1)[0]

    # Run the Java program and pass input
    process = Popen(
        ['java', class_name], 
        stdin=PIPE, 
        stdout=PIPE, 
        stderr=PIPE, 
        text=True)
    inputs = "John Doe\nIce Cream\nBlue\nNew York\nDog\nButterflies\nElder Holland"


    try:
        stdout, stderr = process.communicate(inputs)
        stderr = stderr.strip() if stderr is not None else ""
        
    except Exception as e:
        print("Exception:", str(e))
        stdout = ""
        stderr = ""


    # # Print the output and error messages

    expected_output = """Please enter your name:
Hello John Doe!
What is your favorite dessert? 
I hope you like coding Java as much as you like to eat Ice Cream.
What is your favorite color? 
So, you like the color Blue. My favorite color is 0000ff.
Where were you born?
I was born in Silicon Valley. If I had been born in New York, perhaps we would have been friends.
What is your favorite kind of pet? 
I'm sure a Dog is safer than my pet. I have a pet mouse.... but it always BYTES! HaHaHa!
What is your favorite insect? 
Wow! You like Butterflies!?! I like spiders. They make great WEB sites but sometimes they BUG me!
Who was your favorite speaker at the last General Conference? 
I agree. Elder Holland was great! I'm just glad they didn't make Java against the Word of Wisdom!!!
"""
    
    stdout_lines = stdout.splitlines()
    expected_output_lines = expected_output.splitlines()


    if(stdout_lines == expected_output_lines):
        print("Well done!")
        remove_main("Main.class")
    else:
        print("Work again")
        remove_main("Main.class")


    if stderr:
        print("Error:")
        print(stderr)
        remove_main("Main.class")

# Specify the path to your Java file
java_file_path = "Main.java"


# Call the function to compile and run the Java file
compile_and_run_java(java_file_path)

