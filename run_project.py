import subprocess
import os
import sys
import time

def main():
    python_path = r"C:\Users\Dhruv Oswal\AppData\Local\Programs\Python\Python312\python.exe"
    npm_path = r"C:\Program Files\nodejs\npm.cmd"
    
    frontend_dir = r"d:\Projects\Second_Brain\frontend"
    backend_dir = r"d:\Projects\Second_Brain\backend"
    
    print("Step 1: Installing frontend dependencies (npm install)...")
    try:
        subprocess.run([npm_path, "install"], cwd=frontend_dir, check=True, shell=True)
        print("Frontend dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing frontend dependencies: {e}")
        sys.exit(1)
        
    print("\nStep 2: Starting FastAPI Backend on http://localhost:8000...")
    # Run uvicorn
    backend_process = subprocess.Popen(
        [python_path, "-m", "uvicorn", "app.main:app", "--reload", "--port", "8000"],
        cwd=backend_dir,
        shell=True
    )
    
    print("\nStep 3: Starting Frontend Dev Server on http://localhost:5173...")
    # Run npm run dev
    frontend_process = subprocess.Popen(
        [npm_path, "run", "dev"],
        cwd=frontend_dir,
        shell=True
    )
    
    print("\nBoth servers started successfully!")
    print("- Backend: http://localhost:8000 (docs at /docs)")
    print("- Frontend UI: http://localhost:5173")
    print("\nKeeping scripts active. Press Ctrl+C to terminate.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Servers stopped.")

if __name__ == "__main__":
    main()
