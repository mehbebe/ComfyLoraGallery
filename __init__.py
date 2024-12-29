from .lora_gallery_node import LoraGalleryNode

NODE_CLASS_MAPPINGS = {
    "LoraGallery": LoraGalleryNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraGallery": "LoRA Gallery",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
