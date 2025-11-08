upload:
	git add .
	@echo "Enter the commit message: "; \
	read message; \
	git commit -m "$$message"; \
	git push origin main

install:
	pip install -r requirements.txt

run:
	uv run main.py

dev:
	uv run dev

test:
	uv run test