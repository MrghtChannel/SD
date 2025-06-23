from pypresence import Presence
import time
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="🎉 Congratulations, you've been Rickrolled!",
    details="Rick Astley — Never Gonna Give You Up",
    large_image="rickroll",
    large_text="You know the rules... and so do I!",
)

print("You have been Rickrolled on Discord! Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print("Rickroll disabled.")
