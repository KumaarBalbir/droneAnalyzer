from typing import Optional
import numpy as np
from PIL import Image

class CaptioningModel:
    def __init__(self):
        self.using_blip = False
        print("Operating in basic description mode")

    def generate_caption(self, image: Optional[np.ndarray] = None, objects: list = None) -> str:
        """Generate a caption for an image or list of detected objects"""
        try:
            # Fallback to object-based description
            if objects and len(objects) > 0:
                # Group objects by type
                object_groups = {}
                for obj in objects:
                    key = f"{obj['color']} {obj['type']}"
                    if key not in object_groups:
                        object_groups[key] = 0
                    object_groups[key] += 1

                # Create descriptive sentence
                descriptions = []
                for obj, count in object_groups.items():
                    desc = f"{count} {obj}"
                    if count > 1 and not obj.endswith('s'):
                        desc += "s"
                    descriptions.append(desc)

                scene_desc = ", ".join(descriptions[:-1])
                if len(descriptions) > 1:
                    scene_desc += f" and {descriptions[-1]}"
                elif descriptions:
                    scene_desc = descriptions[0]

                return f"Scene contains {scene_desc}"
            return "No objects detected in the scene"
        except Exception as e:
            print(f"Error generating caption: {e}")
            return "Unable to generate caption"