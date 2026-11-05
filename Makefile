.PHONY: install check test lint format pipeline export-frontend recon evals

install:
	uv sync --all-extras

test:
	uv run pytest -q

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff check --fix .

check: lint test

pipeline:
	uv run python -m pipeline.run

export-frontend:
	mkdir -p frontend/public/data
	cp data/processed/*.json frontend/public/data/

recon:
	uv run python prep/recon_psi.py
	uv run python prep/recon_ntrs.py

evals:
	uv run python evals/run_evals.py
