# Moderated Chatroom

We check if incomming messages contain offensive language using the https://huggingface.co/cardiffnlp/twitter-roberta-base-offensive.

### Downloading and exporting model to onnx

```
optimum-cli export onnx --model cardiffnlp/twitter-roberta-base-offensive  --task sequence-classification onnx_model
```
