# audiocraft_plus as an extension and installable package

## Installation

```bash
# As a package / legacy branch
pip install git+https://github.com/rsxdalv/extension_audiocraft_plus@legacy#egg=extension_audiocraft_plus
# or as an extension of tts-generation-webui on the 'main' branch
pip install git+https://github.com/rsxdalv/extension_audiocraft_plus@main#egg=extension_audiocraft_plus
```

## Usage

```python
from extension_audiocraft_plus.main import ui_full, ui_full_inner

launch_kwargs = {
    "server_name": "0.0.0.0",
    "server_port": 7861,
    "inbrowser": True,
    "share": False,
}
ui_full(launch_kwargs)

# OR as a part of a bigger UI

import gradio as gr
with gr.Blocks() as demo:
    ui_full_inner()
    demo.queue().launch()
```

## This project allows audiocraft_plus to be developed independently of audiocraft itself, focusing on the UI. Additionally, the installation is no longer handled by this repository.

## Original repository:
https://github.com/GrandaddyShmax/audiocraft_plus

## This repository functions as an extension to tts-generation-webui on the 'main' branch. The 'legacy' branch is the installable package.
