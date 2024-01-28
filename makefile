BUILD_DIR	:= ./build
TEST_DIR	:= ./tests
TARGET		:= ./src/plox.py
SRC_DIR		:= ./src

# Remove all build outputs
clean:
	@ rm -rf $(BUILD_DIR)

# Run tests
test:
	@ echo -n "\033[35m [mypy]: " && mypy $(SRC_DIR)/*.py
	@ echo ""
	@ echo "\033[35m [plox]: \033[0m"
	@ for f in $(TEST_DIR)/* ; do \
		$(TARGET) $$f ; \
	done
