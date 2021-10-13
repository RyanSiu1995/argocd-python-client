.PHONY: generate
generate:
	@openapi-generator generate -i swagger.json -g python \
		--git-host github.com --git-repo-id argocd-python-client \
		--git-user-id RyanSiu1995 -o ./ \
		--additional-properties packageVersion=1.0.2 \
		--package-name argocd_python_client

.PHONY: test
test:
	@tox

.PHONY: clean
clean:
	@rm -rf ./dist || true
	@rm -rf ./build || true
	@rm -rf ./argocd_python_client.egg-info || true

.PHONY: build
build: clean
	python setup.py bdist_wheel

.PHONY: push
push: build
	twine upload ./dist/*
