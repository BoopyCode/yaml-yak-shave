#!/usr/bin/env python3
"""
YAML Yak Shaver - Because shaving yaks is easier than debugging YAML.
"""

import sys
import yaml
from pathlib import Path

# Because YAML is basically "Whitespace: The Programming Language"
def shave_the_yak(file_path):
    """
    Attempts to parse YAML. If it fails, tries to find where the yak got stuck.
    Returns: (is_valid, error_line, error_message)
    """
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True, None, "Yak is smooth! No YAML errors found."
    except yaml.YAMLError as e:
        # YAML errors are like snowflakes - each one uniquely frustrating
        error_msg = str(e)
        
        # Try to extract line number from the error message
        error_line = None
        if "line" in error_msg.lower():
            # This regex finds line numbers in most YAML error messages
            import re
            match = re.search(r'line (\d+)', error_msg)
            if match:
                error_line = int(match.group(1))
        
        return False, error_line, error_msg

def main():
    """Main function - because every yak needs a shepherd."""
    if len(sys.argv) != 2:
        print("Usage: python yaml_yak_shaver.py <yaml_file>")
        print("Example: python yaml_yak_shaver.py deployment.yaml")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found. Did the yak run away?")
        sys.exit(1)
    
    is_valid, error_line, error_msg = shave_the_yak(file_path)
    
    if is_valid:
        print("✅", error_msg)
    else:
        print("❌ YAML Yak Attack!")
        print(f"   Error: {error_msg}")
        if error_line:
            print(f"   Suspect line: {error_line}")
            
            # Show the problematic line if we can
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    if error_line <= len(lines):
                        print(f"   Line content: {lines[error_line-1].rstrip()}")
            except:
                pass  # Sometimes you just can't help a stubborn yak
        
        sys.exit(1)

if __name__ == "__main__":
    # PyYAML is the only dependency because reinventing YAML parsing is a different yak
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML not found. Install with: pip install pyyaml")
        print("Or let the yak stay hairy - your choice.")
        sys.exit(1)
    
    main()