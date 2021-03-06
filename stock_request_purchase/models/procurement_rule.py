# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _prepare_purchase_order_line(self, product_id, product_qty,
                                     product_uom, values, po, supplier):
        vals = super(ProcurementRule, self)._prepare_purchase_order_line(
            product_id, product_qty, product_uom, values, po, supplier)
        if 'stock_request_id' in values:
            vals['stock_request_ids'] = [(4, values['stock_request_id'])]
        return vals

    def _prepare_purchase_order_line_update(self, line,
                                            procurement_uom_po_qty,
                                            price_unit, values):
        vals = super(ProcurementRule,
                     self)._prepare_purchase_order_line_update(
            line, procurement_uom_po_qty, price_unit, values
        )
        if 'stock_request_id' in values:
            vals['stock_request_ids'] = [(4, values['stock_request_id'])]
        return vals
