#!/bin/bash

# Setup Script for Automation Exercise Testing Framework

echo "======================================"
echo "Setting up Automation Testing Framework"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

echo "✅ Python is installed"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

if [ $? -eq 0 ]; then
    echo "✅ Virtual environment created"
else
    echo "❌ Failed to create virtual environment"
    exit 1
fi

echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Install Playwright browsers
echo "Installing Playwright browsers..."
playwright install chromium

if [ $? -eq 0 ]; then
    echo "✅ Playwright browsers installed"
else
    echo "❌ Failed to install Playwright browsers"
    exit 1
fi

echo ""

# Create reports directory
echo "Creating reports directory..."
mkdir -p reports/allure-results
mkdir -p reports/videos

echo "✅ Reports directory created"
echo ""

echo "======================================"
echo "Setup completed successfully! 🎉"
echo "======================================"
echo ""
echo "To run tests:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run tests: pytest"
echo "  3. Generate report: allure serve reports/allure-results"
echo ""
echo "For more information, see README.md"