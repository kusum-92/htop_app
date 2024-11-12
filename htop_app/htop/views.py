from django.http import HttpResponse
import os
from datetime import datetime
import subprocess

def htop_view(request):
    name = "KUSUM" 
    username = os.getenv("USERNAME", "default_user") 
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST") 

    
    try:
        top_output = subprocess.check_output("top -bn1 | head -n 10", shell=True, text=True)
    except Exception as e:
        top_output = f"Could not retrieve task list: {str(e)}"

    content = f"""
    <html>
    <head><title>HTOP Endpoint</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time:</strong> {server_time}</p>
        <h2>TOP Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(content)
