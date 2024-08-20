import cfile
import os
import subprocess

# Step 1: Generate the C code using cfile
C = cfile.CFactory()
code = C.sequence()
code.append(C.blank())
code.append(C.sysinclude("stdio.h"))
code.append(C.blank())
char_ptr_type = C.type("char", pointer=True)
code.append(C.declaration(C.function("main", "int",
                                     params=[C.variable("argc", "int"),
                                             C.variable("argv", char_ptr_type, pointer=True)
                                             ])))
main_body = C.block()
main_body.append(C.statement(C.func_call("printf", C.str_literal(r"Hello World\n"))))
main_body.append(C.statement(C.func_return(0)))
code.append(main_body)

# Step 2: Write the C code to a file in the generated directory
generated_dir = "generated"
os.makedirs(generated_dir, exist_ok=True)
file_path = os.path.join(generated_dir, "test.c")

with open(file_path, "w") as f:
    writer = cfile.Writer(cfile.StyleOptions())
    f.write(writer.write_str(code))

print(f"C code written to {file_path}")

# Step 3: Compile the generated C code using gcc to check for syntax errors
gcc_path = "gcc"  # Change this to your actual gcc path
executable_path = os.path.join(generated_dir, "test")
compile_command = [gcc_path, "-o", executable_path, file_path]

try:
    result = subprocess.run(compile_command, capture_output=True, text=True, check=True)
    print("Compilation successful, no syntax errors.")
except subprocess.CalledProcessError as e:
    print("Compilation failed with the following errors:")
    print("stdout:", e.stdout)
    print("stderr:", e.stderr)
    exit(1)  # Exit if compilation fails

# Step 4: Run the compiled executable if compilation is successful
try:
    run_command = [executable_path]
    run_result = subprocess.run(run_command, capture_output=True, text=True)
    print("Execution Output:")
    print(run_result.stdout)
    if run_result.returncode != 0:
        print("Execution failed with errors:")
        print(run_result.stderr)
except Exception as e:
    print(f"Failed to run the executable: {e}")
