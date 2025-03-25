

from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Displays all registered URLs'

    def handle(self, *args, **kwargs):
        resolver = get_resolver()
        url_patterns = resolver.url_patterns  # Get the URL patterns

        for pattern in url_patterns:
            self.stdout.write(self.get_pattern(pattern))

    def get_pattern(self, pattern, prefix=""):
        """Recursively get all URL patterns"""
        if hasattr(pattern, 'url_patterns'):
            return "\n".join(self.get_pattern(p, prefix + pattern.pattern.regex.pattern) for p in pattern.url_patterns)
        return f"{prefix}{pattern.pattern}"
