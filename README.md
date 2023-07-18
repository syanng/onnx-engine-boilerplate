# ONNX Engine Package

This is a boilerplate for PIP Package Model ONNX. The model will simply load onnx package and return ReadyOCR python object.


## Edit Package

Go to the file ```src/onnxengine/__init__.py``` and edit ```ONNXEngine``` class. Please remember to update ```version``` in ```pyproject.toml``` for each update.

## Install Locally

After git clone, you can access the codebase and simply run the following command line:

```
python -m pip install -e .
```

If you want to add dependancies, go to file ```pyproject.toml``` and edit lines:

```
dependencies = [
    "onnxruntime",
    "readyocr"
]
```

## Basic Usage

After installing, we can use the ONNX engine as following:

```
from onnxengine import ONNXEngine

model = ONNXEngine(model_path="any_model.onnx")
model.run(image_path)
```

Or you can run ```examples/sample.py``` file as following:

```
python sample.py -m `link/to/model.onnx' -i 'link/to/image'
```