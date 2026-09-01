import subprocess
import os
import sys

def generate_pdf():
    html_path = os.path.abspath("resume.html")
    pdf_path = os.path.abspath("Sonu_Kumar_Resume.pdf")
    
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    
    browser_bin = None
    for p in edge_paths:
        if os.path.exists(p):
            browser_bin = p
            break
            
    if not browser_bin:
        print("No browser found for PDF printing.")
        return False
        
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-margins",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        file_url
    ]
    
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", res.returncode)
    print("Stdout:", res.stdout)
    print("Stderr:", res.stderr)
    
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print(f"Successfully generated: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        return True
    else:
        print("PDF generation failed.")
        return False

if __name__ == "__main__":
    generate_pdf()
