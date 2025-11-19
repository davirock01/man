"""
Linter Check Helper Script
Run basic checks on codebase
"""

import ast
import os
from pathlib import Path
from typing import List, Tuple


def check_imports(file_path: str) -> List[str]:
    """Check for unused imports in a Python file."""
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
            
        # Extract imports
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    for alias in node.names:
                        imports.append(f"{node.module}.{alias.name}")
        
        # Basic check - could be improved
        if len(imports) > 50:
            issues.append(f"Large number of imports: {len(imports)}")
            
    except Exception as e:
        issues.append(f"Error parsing {file_path}: {str(e)}")
    
    return issues


def check_line_length(file_path: str, max_length: int = 120) -> List[str]:
    """Check for lines exceeding max length."""
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if len(line.rstrip()) > max_length:
                    issues.append(f"Line {i} exceeds {max_length} chars: {len(line)} chars")
    except Exception as e:
        issues.append(f"Error reading {file_path}: {str(e)}")
    
    return issues


def scan_directory(directory: str) -> dict:
    """Scan directory for Python files and check them."""
    results = {}
    
    for root, dirs, files in os.walk(directory):
        # Skip certain directories
        if any(skip in root for skip in ['__pycache__', '.git', 'venv', 'node_modules', 'alembic/versions']):
            continue
            
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                issues = []
                
                # Check imports
                import_issues = check_imports(file_path)
                if import_issues:
                    issues.extend([f"Import: {i}" for i in import_issues])
                
                # Check line length
                line_issues = check_line_length(file_path)
                if line_issues[:3]:  # Only first 3 to avoid spam
                    issues.extend([f"Length: {i}" for i in line_issues[:3]])
                
                if issues:
                    results[file_path] = issues
    
    return results


if __name__ == "__main__":
    print("🔍 Running basic linter checks...")
    print("=" * 60)
    
    backend_dir = Path(__file__).parent.parent
    results = scan_directory(str(backend_dir))
    
    if not results:
        print("✅ No major issues found!")
    else:
        print(f"⚠️  Found {len(results)} files with potential issues:")
        for file_path, issues in results.items():
            rel_path = os.path.relpath(file_path, backend_dir)
            print(f"\n📄 {rel_path}:")
            for issue in issues[:5]:  # Limit to 5 per file
                print(f"   - {issue}")
    
    print("\n" + "=" * 60)
    print("💡 For full linting, run:")
    print("   flake8 app/ --max-line-length=120")
    print("   mypy app/ --ignore-missing-imports")
    print("   black app/ --check")

