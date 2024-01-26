BUILD_DIR	:= build
TEST_DIR	:= ./tests
TARGET		:= ./plox.py

# Remove all build outputs
clean:
	@ rm -rf $(BUILD_DIR)

# Run tests
test:
	@ echo -n "\033[35m [mypy]: " && mypy
	@ echo ""
	@ echo "\033[35m [plox]: \033[0m"
	@ for f in $(TEST_DIR)/* ; do \
		$(TARGET) $$f ; \
	done
