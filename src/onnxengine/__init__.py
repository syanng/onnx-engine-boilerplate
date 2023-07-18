import onnxruntime
from PIL import Image
from uuid import uuid4
from readyocr.entities import Document, Page


class ONNXEngine():
    
    def __init__(
        self,
        model_path: str
    ):
        self.session = onnxruntime.InferenceSession(model_path)

    def run(self, image_path: str):
        print("Running inference...")

        print("Model metadata:")
        print(self.session.get_modelmeta())
        print("Input metadata:")
        print(self.session.get_inputs()[0])
        print("Output metadata:")
        print(self.session.get_outputs()[0])
        print("Input shape:")
        print(self.session.get_inputs()[0].shape)
        print("Output shape:")
        print(self.session.get_outputs()[0].shape)

        image = Image.open(image_path)

        document = Document(num_pages=1)
        page = Page(
            id=str(uuid4()),
            width=image.width,
            height=image.height,
            page_num=1
        )
        document.pages.append(page)

        return document