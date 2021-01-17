tests_src = tests
app_src = {{cookiecutter.project_name}}

.PHONY: format
format:
	@poetry run black $(tests_src) $(app_src)
