# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ContractType(models.Model):

    _name = 'hr.contract.type'
    _description = 'Contract Type'
    _order = 'sequence, id'

    name = fields.Char(string='Type de contract', required=True)
    sequence = fields.Integer(help="Donne la séquence lors de l'affichage d'une liste de contrat.", default=10)

class ContractInherit(models.Model):

    _inherit = 'hr.contract'

    type_id = fields.Many2one('hr.contract.type', string="Categorie employé",
                              required=True,
                              default=lambda self: self.env['hr.contract.type'].search([], limit=1))
