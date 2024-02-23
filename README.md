# Moderated Chatroom

We check if incomming messages contain offensive language using the https://huggingface.co/cardiffnlp/twitter-roberta-base-offensive.
The channel works as a simple chatroom, only when offensive language has been detected does the channel repond with a message.

The basic functionality of the messaeg board remains the same, inferece.py was added to check all posted messages and dtect whether it is offensive. If this is the case a message is posted through channel.py.

### Downloading and exporting model to onnx

```
optimum-cli export onnx --model cardiffnlp/twitter-roberta-base-offensive  --task sequence-classification onnx_model
```
