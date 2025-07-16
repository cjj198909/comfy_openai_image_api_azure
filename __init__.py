"""Top-level package for openai_image_api."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

REQUIRED_PACKAGES = {
    "openai": ">=1.76.2",   
}

__author__ = """Xin"""
__email__ = "unicough.github@gmail.com"
__version__ = "0.0.4"

# Lazy import to avoid torch dependency during testing
def get_node_mappings():
    """Get node mappings with lazy import."""
    from .src.openai_image_api.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    return NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# For ComfyUI compatibility
try:
    from .src.openai_image_api.nodes import NODE_CLASS_MAPPINGS
    from .src.openai_image_api.nodes import NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    # During testing or when torch is not available
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

WEB_DIRECTORY = "./web"
