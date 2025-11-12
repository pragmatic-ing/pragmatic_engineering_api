# Copyright 2025 Pragmatic Ingeniería
# License OPL-1 (Odoo Proprietary License v1.0).


def post_load():
    """Make import in post_load to avoid applying monkey patches when this
    module is not installed."""
    from . import models
    from . import controllers
