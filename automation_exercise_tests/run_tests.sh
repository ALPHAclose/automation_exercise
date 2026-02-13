#!/bin/bash

# Run Tests Script

echo "======================================"
echo "Running Automated Tests"
echo "======================================"
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment activated"
    echo ""
fi

# Clean previous results
echo "Cleaning previous test results..."
rm -rf reports/allure-results/*
echo "✅ Previous results cleaned"
echo ""

# Run tests
echo "Running tests..."
pytest -v --tb=short

TEST_EXIT_CODE=$?

echo ""
echo "======================================"

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed. Exit code: $TEST_EXIT_CODE"
fi

echo "======================================"
echo ""

# Ask user if they want to generate report
read -p "Generate Allure report? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Generating Allure report..."
    allure serve reports/allure-results
fi

exit $TEST_EXIT_CODE