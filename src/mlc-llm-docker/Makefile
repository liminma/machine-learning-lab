.PHONY: build

build:
	docker build -t mlcllm-env .

compile-model:
	docker run --rm -it \
		-v ~/github-repositories/generative-ai-lab/notebooks/merged-llama-7b-samsum:/llama-2-7b-chat-samsum \
        -v ~/github-repositories/generative-ai-lab/notebooks/compiled-models:/compiled-models \
		--gpus '"device=0"' \
		mlcllm-env bash

serve-model:
	docker run --rm -it \
        -p 9000:9000 \
		--gpus '"device=0"' \
		-v ~/github-repositories/generative-ai-lab/notebooks/compiled-models/llama-2-7b-chat-samsum-q4f16_1:/dist/llama-2-7b-chat-samsum-q4f16_1 \
		mlcllm-env bash
