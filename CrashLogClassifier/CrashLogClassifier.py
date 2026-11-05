import os

# IMPORTANT: Ensure this path points exactly to where you saved your Unreal log file.
# Keep the 'r' at the start of the quotes!
log_file_path = r"C:\Users\yeyian\Desktop\QATestProject.log" 

print(f"Scanning file: {log_file_path}\n")

# Keywords Unreal uses when things go wrong
crash_keywords = ["Fatal error", "Access violation", "Assertion failed", "Exception"]

try:
    # Open the file and read it line by line
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        
    crash_detected = False
    
    # Loop through every line in the log
    for line_number, line in enumerate(lines, 1):
        # Check if any of our keywords are in this line
        for keyword in crash_keywords:
            if keyword.lower() in line.lower():
                print(f"🚨 CRASH DETECTED on line {line_number}:")
                print(f"   {line.strip()}")
                crash_detected = True
                break # Move to the next line once we find a match
                
    # If we checked the whole file and found nothing
    if not crash_detected:
        print("✅ No fatal errors found in the log.")

except FileNotFoundError:
    print(f"❌ Error: Could not find the file at {log_file_path}. Check the path!")
