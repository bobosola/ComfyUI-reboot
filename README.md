# ComfyUI-reboot

This is a custom ComfyUI node to reboot (i.e. restart) ComfyUI at the end of a workflow. It does exactly the same thing as either of the following:

* hitting the **Restart** button in the ComfyUI Manager window, or
* right-clicking in an empty area and selecting **Reboot ComfyUI**

### Why reboot?

This node was written to fix issues with some Apple MLX Flux model loaders. These loaders were super-quick compared with regular Flux loaders but failed to free the system memory on completion of the workflow. None of the usual utilities could clear the memory (_Manager -> Unload models_, _Manager -> Free model & node cache_ plus various custom nodes such as _EasyUse -> Clean VRAM_, _Unload Model_, and _Unload All Models_). Nothing worked, the memory was never freed.

So this is a solution of last resort. I use it in workflows when calling ComfyUI from Open WebUI to generate images. The automated ComfyUI reboot at (or near) the end of a workflow allows the system to reclaim the memory without having to manually reboot the ComfyUI server after each image generation.

### Installation
You can either:

* search for **Reboot** in the ComfyUI Custom Nodes Manager and install it from there, or
* manually install it as follows (assumes you have `git` installed):
    * `cd /path/to/ComfyUI`
    * `cd custom_nodes`
    * `git clone https://github.com/bobosola/ComfyUI-reboot.git`
    * Restart ComfyUI

### Usage
You will find **Reboot ComfyUI** in the **utils** folder of the nodes menu. Alternatively, you can double-click in an empty area of the workspace and enter _reboot_ into the node search box.

Place it at end of your workflow attached to the output of any node. If your final node has no output to attach to, then attach it to the node nearest to the end which does have an output connector and adjust the delay parameter accordingly. When you run the workflow ComfyUI will be rebooted after your chosen delay period. Example (near end of workflow):

![How to use the Reboot node](https://raw.githubusercontent.com/bobosola/repo/ComfyUI-reboot/assets/screenshot01.png)

### Parameters
* `url` (_string_) - the server URL in the format `{scheme}://{host}:{port}`. Defaults to the local server as `http://127.0.0.1:8188`.
* `wait_seconds` (_integer_) - the number of seconds to wait until the ComfyUI reboot. Default is 5 seconds. You can change this according to your needs.

### Acknowledgements

This is based on watarika's [ComfyUI-exit](https://github.com/watarika/ComfyUI-exit). I just amended it for my purpose. So many thanks to him.

### Change Log
- v1.0.0 (07-Oct-2025) - 1st release.
