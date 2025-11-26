#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
    django.setup()
    
    # Run tests
    from tests.test_comprehensive import NerdHubTestCase
    import unittest
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(NerdHubTestCase)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with error code if tests failed
    sys.exit(not result.wasSuccessful())