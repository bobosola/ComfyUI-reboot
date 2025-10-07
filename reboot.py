import time
import threading
import requests

class ComfyAnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

class RebootComfyUINode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                "server_url": ("STRING",{"default": "http://127.0.0.1:8188"}),
                "wait_seconds": ("INT", {"default": 5}),
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ()
    CATEGORY = "utils"
    FUNCTION = "reboot_comfyui"

    # Added to server URL to make the full path to the API reboot call
    API_REBOOT_PATH = "/api/manager/reboot"

    def reboot_comfyui(self, any: ComfyAnyType, wait_seconds: int, server_url: str):
        # Remove a user-inserted trailing slash in the server url
        reboot_url = f"{server_url.rstrip('/')}{self.API_REBOOT_PATH}"
        # Run the reboot in a separate thread to allow the workflow to complete
        threading.Thread(target = self.delay_then_reboot, args = (wait_seconds, reboot_url,)).start()
        # Must return a tuple, so the trailing comma is required
        return (0, )

    def delay_then_reboot(self, wait_seconds: int, reboot_url: str):
        for i in range(wait_seconds):
            print(f"Rebooting ComfyUI in {wait_seconds - i} seconds...")
            time.sleep(1)
        print("Rebooting ComfyUI now")
        _ = requests.get(reboot_url)

NODE_CLASS_MAPPINGS = {
    "reboot": RebootComfyUINode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "reboot": "Reboot ComfyUI",
}
