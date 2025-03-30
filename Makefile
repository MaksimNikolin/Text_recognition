VENV_NAME=myenv
output_files = build dist summarize.egg-info

.DEFAULT_GOAL := run

clean:
	@rm -rf output_files
	@echo "FILES REMOVED."

rebuild: clean
	@echo "REBUILDING THE ENVIRONMENT..."
	@python3 -m venv $(VENV_NAME)
	@. $(VENV_NAME)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "VIRTUAL ENVIRONMENT '$(VENV_NAME)' REBUILT ANT DEPENDENCIES INSTALLED."

run: clean
	@echo "LOADING ENVIRONMENT VARIABLES FROM .env..."
	@bash -c 'source .env && echo "ENVIRONMENT LOADED."'
	@bash -c 'set -a && source .env && set +a'
	@echo ""

	@if [ -z "$$HUGGINGFACE_TOKEN" ]; then \
		echo "Error: HUGGINGFACE_TOKEN is not set."; \
		exit 1; \
	fi

	@echo "LOGGING INTO HuggingFace WITH THE PROVIDED TOKEN..."
	@. $(VENV_NAME)/bin/activate && huggingface-cli login --token $$HUGGINGFACE_TOKEN --add-to-git-credential
	@echo ""
	@echo "RUNNING SUMMARIZER..."
	@python3 app.py
