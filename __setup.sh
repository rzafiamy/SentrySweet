#!/bin/bash

# Define project structure
PROJECT_ROOT="."

# Create initial Python files
echo "Creating initial files..."
touch "$PROJECT_ROOT/__init__.py"
touch "$PROJECT_ROOT/config.py"
touch "$PROJECT_ROOT/system_info.py"
touch "$PROJECT_ROOT/manager.py"

# Create README and requirements.txt
echo "Creating README.md and requirements.txt..."
cat << EOF > "$PROJECT_ROOT/README.md"
# SentrySweet

This script generates a report containing information about the system's disks, filesystems, CPU, and RAM.

## Setup

1. Install the required packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Run the script:

\`\`\`bash
python manager.py
\`\`\`

The report will be printed in a tabular format directly to your console.
EOF

cat << EOF > "$PROJECT_ROOT/requirements.txt"
psutil==5.8.0
tabulate==0.8.9
EOF

# Optional: Initialize a Git repository
cd "$PROJECT_ROOT" || exit
git init
git add .
git commit -m "Initial project setup"

echo "Setup complete. Project structure created and initialized with Git."
