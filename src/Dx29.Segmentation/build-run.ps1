docker build -t dx29-segmentation:latest .

# /bin/bash
docker run -it --entrypoint '/bin/bash' dx29-segmentation:latest

# Run
docker run --rm -p 8080:8080 dx29-segmentation:latest
docker run --rm -p 8080:8080 -it -m 0.5g --cpus 0.5 dx29-segmentation:latest
