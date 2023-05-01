from app import create_app
import sys
import os

# Add project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

seg_app = create_app()

if __name__ == '__main__':
    
    seg_app.run(debug=True)