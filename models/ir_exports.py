# Copyright 2025 Pragmatic Ingeniería
# Based on work by Ivan Yelizariev, Rafis Bikbov
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class IrExports(models.Model):
    _inherit = "ir.exports"

    api_access_read_one_ids = fields.One2many(
        "api.access",
        "read_one_id", 
        string="API Access Read One"
    )
    api_access_read_many_ids = fields.One2many(
        "api.access",
        "read_many_id",
        string="API Access Read Many"
    )
