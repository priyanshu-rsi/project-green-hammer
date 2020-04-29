import os
print("Current Working Directory " , os.getcwd())
euid = os.geteuid() 
if euid != 0:
  raise EnvironmentError("Please run the application as a root/administrator")
  exit()

from app.home import Landing

from app.preview import preview 




# Create Landing instance
landing = Landing.Home()

# PreviewScreen = preview.Preview()
# PreviewScreen.UI()


# ffmpeg test
