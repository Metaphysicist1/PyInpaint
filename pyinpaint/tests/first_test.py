import pytest
import os
from pyinpaint import Inpaint




def test_inpainter_initialization():
    local_path = os.path.dirname(__file__)
    data_path = os.path.join(local_path, "..", "data")
    image_path = os.path.join(data_path, "barbara.jpg")
    mask_path = os.path.join(data_path, "mask_barbara.png")


    inpainter = Inpaint(image_path, mask_path, ps=7)
    assert inpainter is not None
    assert isinstance(inpainter, Inpaint)


if __name__ == "__main__":
    pytest.main()