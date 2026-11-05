import os
import re

log_file_path = r"C:\Users\yeyian\Desktop\QATestProject.log" 

print(f"Scanning file: {log_file_path}\n")

# This is the Regex pattern. It looks for "[File:" and "[Line:" and grabs the text inside.
crash_pattern = re.compile(r"\[File:(.*?)\]\s*\[Line:\s*(\d+)\]")
crash_keywords = ["Fatal error", "Access violation", "Assertion failed", "Exception"]

try:
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        
    crash_detected = False
    
    for line_number, line in enumerate(lines, 1):
        for keyword in crash_keywords:
            if keyword.lower() in line.lower():
                print(f"🚨 CRASH DETECTED on log line {line_number}:")
                
                # Search the line for the File and Line pattern
                match = crash_pattern.search(line)
                if match:
                    file_path = match.group(1)
                    source_line = match.group(2)
                    
                    # Extract just the filename (e.g., UnrealEngine.cpp) from the long path
                    file_name = file_path.split('\\')[-1]
                    
                    print(f"   📍 Location: {file_name} at line {source_line}")
                else:
                    print(f"   {line.strip()}")
                    
                print("-" * 40) 
                crash_detected = True
                break 
                
    if not crash_detected:
        print("✅ No fatal errors found in the log.")

except FileNotFoundError:
    print(f"❌ Error: Could not find the file at {log_file_path}. Check the path!")
