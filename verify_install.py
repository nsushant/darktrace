#!/usr/bin/env python3
"""
Installation verification script for darktrace package.
Run this script to verify that the package is properly installed and configured.
"""

import sys

def test_imports():
    """Test that all key imports work correctly."""
    print("Testing imports...")
    
    try:
        import darktrace
        print("✓ darktrace imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import darktrace: {e}")
        return False
    
    try:
        from darktrace.config import config
        print("✓ darktrace.config imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import darktrace.config: {e}")
        return False
    
    try:
        from darktrace import tagging, edge, analysis
        print("✓ All submodules imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import submodules: {e}")
        return False
    
    return True

def test_config():
    """Test that configuration system works."""
    print("\nTesting configuration system...")
    
    try:
        from darktrace.config import config
        paths = config.get_all_paths()
        print(f"✓ Found {len(paths)} configured paths:")
        for key, path in paths.items():
            print(f"  - {key}: {path}")
        
        # Test config access
        ftag = config.get('tagging', 'ftag')
        print(f"✓ Config value ftag: {ftag}")
        
        return True
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False

def test_package_data():
    """Test that package data (config.json) is accessible."""
    print("\nTesting package data access...")
    
    try:
        from darktrace.config import config
        # This will fail if config.json is not accessible
        test_path = config.get_path('tangos_path')
        print("✓ Package data (config.json) is accessible")
        return True
    except FileNotFoundError as e:
        print(f"✗ Package data not found: {e}")
        print("  This suggests the package was not installed correctly")
        print("  Try: pip install -e .")
        return False
    except Exception as e:
        print(f"✗ Package data test failed: {e}")
        return False

def main():
    """Run all tests and provide summary."""
    print("=== Darktrace Installation Verification ===\n")
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_config),
        ("Package Data Test", test_package_data)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"✗ {test_name} crashed: {e}")
            results.append(False)
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    if all(results):
        print("🎉 ALL TESTS PASSED!")
        print("✓ Darktrace is properly installed and configured")
        print("\nYou can now use the package:")
        print("  import darktrace as dtrace")
        print("  from darktrace.config import config")
        print("\nFor examples, see the examples/ directory")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        failed_tests = sum(1 for r in results if not r)
        print(f"✗ {failed_tests} out of {len(results)} tests failed")
        
        print("\nTroubleshooting:")
        print("1. Make sure you ran: pip install -e .")
        print("2. Check that config/config.json exists")
        print("3. Verify all dependencies are installed")
        return 1

if __name__ == "__main__":
    sys.exit(main())