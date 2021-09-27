.PHONY: generate
generate:
	@openapi-generator generate -i swagger.json -g python \
		--git-host github.com --git-repo-id argocd-python-client \
		--git-user-id RyanSiu1995 -o ./ \
		--package-name argocd_python_client
