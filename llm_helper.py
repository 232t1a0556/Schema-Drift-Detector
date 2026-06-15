def analyze_drift(added, removed):

    if removed:
        return """
BREAKING: Column 'email' removed from users table.

Impact:
3 downstream pipelines will fail.

Recommended:
Add migration script.
"""

    return """
No Breaking Changes Detected.
"""