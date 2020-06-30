# Tensorflow-serving
Tensorflow Serving with Docker / Docker Compose

# Command 

```bash
# Step 1
docker-compose build

# Step 2 
docker-compose up
```

# Request

- **Input**: base64 image
- HTTP request: `host:8501/v1/models/tlai-serving:predict`
- gRPC request: see [utils.py](utils.py) for more information about how to make gRPC request with protobuf pre-build
