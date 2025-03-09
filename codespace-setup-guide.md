# GitHub Codespace Setup for PydanticAI

This guide walks through setting up a GitHub Codespace for working with PydanticAI and Pydantic 2.x.

## 1. Create a New Codespace

1. Navigate to your repository on GitHub
2. Click the "Code" button
3. Select the "Codespaces" tab
4. Click "Create codespace on main"

## 2. Environment Setup

Once your Codespace is running, execute these commands in the terminal:

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install pydantic pydanticai fastapi uvicorn

# Create requirements.txt
cat > requirements.txt << EOF
pydantic>=2.0.0
pydanticai
fastapi
uvicorn
EOF
```

## 3. Project Structure

Set up a basic project structure:

```bash
# Create project directories and initialization files
mkdir -p src/models src/agents tests
touch src/__init__.py src/models/__init__.py src/agents/__init__.py

# Create .gitignore
cat > .gitignore << EOF
# Virtual Environment
.venv/
venv/
ENV/

# Python cache files
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Distribution / packaging
dist/
build/
*.egg-info/

# Local development settings
.env
.env.local

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Testing
.coverage
htmlcov/
.pytest_cache/
EOF
```

## 4. Sample Code

Create a basic example to test your setup:

```bash
# Create a simple example file
cat > src/example.py << EOF
from pydantic import BaseModel, Field
from typing import List, Optional

# Define a Pydantic model
class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    email: str
    tags: List[str] = []
    bio: Optional[str] = None

# Test the model
if __name__ == "__main__":
    # Create a user with valid data
    try:
        user = User(id=1, name="John Doe", email="john@example.com")
        print(f"Valid user created: {user.model_dump_json()}")
    except Exception as e:
        print(f"Error creating user: {e}")

    # Try with invalid data
    try:
        invalid_user = User(id=0, name="J", email="not-an-email")
        print(f"This should not print: {invalid_user}")
    except Exception as e:
        print(f"Expected validation error: {e}")
EOF
```

## 5. Run Your Example

Test that everything is working:

```bash
# Run the example
python src/example.py
```

## 6. Next Steps

- Create more complex Pydantic models
- Experiment with PydanticAI agents
- Integrate with FastAPI for a complete application
- Add proper tests in the tests directory

## 7. Codespace Features to Leverage

- Use the built-in VS Code extensions for Python development
- Set up debugging configurations for your applications
- Use the terminal for running scripts and commands
- Take advantage of GitHub Codespaces' port forwarding for web applications

This setup provides a clean, isolated environment for experimenting with PydanticAI while following Python best practices.