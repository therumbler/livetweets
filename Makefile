run:
	pipenv run uvicorn \
		--host=0.0.0.0 \
		--log-level debug \
		main:app
