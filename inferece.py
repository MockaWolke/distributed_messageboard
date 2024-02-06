from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import optimum
from optimum.pipelines import pipeline
from loguru import logger
import time

# load model from hub and convert
model = ORTModelForSequenceClassification.from_pretrained("onnx_model")
tokenizer = AutoTokenizer.from_pretrained("onnx_model")
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = "@user" if t.startswith("@") and len(t) > 1 else t
        t = "http" if t.startswith("http") else t
        new_text.append(t)
    return " ".join(new_text)


def is_offensive(text: str) -> bool:

    text = preprocess(text)

    logger.debug(f"Classifying: {text}")

    start = time.time()
    result = pipe(text)[0]

    logger.debug(
        f'Prediction {result["label"]}, Score {result["score"]}, Took {time.time()-start :.4f}s'
    )

    return result["label"] == "offensive"
