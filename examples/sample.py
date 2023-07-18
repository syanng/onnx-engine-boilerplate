import os
import json
import argparse
from onnxengine import ONNXEngine


def parse_args():
    parser = argparse.ArgumentParser(description='Parse response from Textract.')
    parser.add_argument('--model', '-m', required=True, help='model file path')
    parser.add_argument('--image', '-i', required=True ,type=str, help='image file path')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    model = ONNXEngine(model_path=args.model)
    document = model.run(args.image)

    print("Document:")
    print(document.export_json())


if __name__ == '__main__':
    main()