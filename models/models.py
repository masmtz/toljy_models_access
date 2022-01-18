# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class toljy_models_access(models.Model):
#     _name = 'toljy_models_access.toljy_models_access'
#     _description = 'toljy_models_access.toljy_models_access'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
