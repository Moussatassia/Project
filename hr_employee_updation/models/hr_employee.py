# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Jesni Banu (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
from datetime import datetime, timedelta
from odoo import models, fields, _

GENDER_SELECTION = [('male', 'Male'),
                    ('female', 'Femele'),
                    ('other', 'Autres')]


class HrEmployeeContractName(models.Model):
    """This class is to add emergency contact table"""

    _name = 'hr.emergency.contact'
    _description = 'Contact d\'urgence RH'

    number = fields.Char(string='Numero', help='Numero de contract')
    relation = fields.Char(string='Contact', help='Relation avec l\'employé')
    employee_obj = fields.Many2one('hr.employee', invisible=1)


class HrEmployeeFamilyInfo(models.Model):
    """Table for keep employee family information"""

    _name = 'hr.employee.family'
    _description = 'Famille d\'employés RH'


    employee_id = fields.Many2one('hr.employee', string="Employé", help='Sélectionnez l\'employé correspondant',
                                  invisible=1)

    member_name = fields.Char(string='Nom')
    relation = fields.Selection([('father', 'Pere'),
                                 ('mother', 'Mere'),
                                 ('daughter', 'Fille'),
                                 ('son', 'Fils'),
                                 ('wife', 'Epouse')], string='Relation', help='Relation avec l\'employé')
    member_contact = fields.Char(string=' No Contact')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def mail_reminder(self):
        """Sending expiry date notification for ID and Passport"""

        now = datetime.now() + timedelta(days=1)
        date_now = now.date()
        match = self.search([])
        for i in match:
            if i.id_expiry_date:
                exp_date = fields.Date.from_string(i.id_expiry_date) - timedelta(days=14)
                if date_now >= exp_date:
                    mail_content = "  Hello  " + i.name + ",<br>Your ID " + i.identification_id + "va expirer le " + \
                                   str(i.id_expiry_date) + ". Veuillez le renouveler avant la date d'expiration"
                    main_content = {
                        'subject': _('ID-%s Expired On %s') % (i.identification_id, i.id_expiry_date),
                        'author_id': self.env.user.partner_id.id,
                        'body_html': mail_content,
                        'email_to': i.work_email,
                    }
                    self.env['mail.mail'].sudo().create(main_content).send()
        match1 = self.search([])
        for i in match1:
            if i.passport_expiry_date:
                exp_date1 = fields.Date.from_string(i.passport_expiry_date) - timedelta(days=180)
                if date_now >= exp_date1:
                    mail_content = "  Hello  " + i.name + ",<br>Ton passeport " + i.passport_id + "va expirer le " + \
                                   str(i.passport_expiry_date) + ".Veuillez le renouveler avant la date d'expiration"
                    main_content = {
                        'subject': _('Passport-%s Expired On %s') % (i.passport_id, i.passport_expiry_date),
                        'author_id': self.env.user.partner_id.id,
                        'body_html': mail_content,
                        'email_to': i.work_email,
                    }
                    self.env['mail.mail'].sudo().create(main_content).send()
    personal_mobile = fields.Char(string='Mobile', related='address_home_id.mobile', store=True)
    joining_date = fields.Date(string='Date d\'inscription')
    id_expiry_date = fields.Date(string='Date d\'expiration', help='Date d\'expiration de l\'identification ID')
    passport_expiry_date = fields.Date(string='Date d\'expiration', help='Date d\'expiration du passeport ID')
    id_attachment_id = fields.Many2many('ir.attachment', 'id_attachment_rel', 'id_ref', 'attach_ref',
                                        string="Attachment", help='Vous pouvez joindre la copie de votre identifiant')
    passport_attachment_id = fields.Many2many('ir.attachment', 'passport_attachment_rel', 'passport_ref', 'attach_ref1',
                                              string="Attachement",
                                              help='Vous pouvez joindre la copie du passeport')
    fam_ids = fields.One2many('hr.employee.family', 'employee_id', string='Famille', help='Information Famille ')
    emergency_contacts = fields.One2many('hr.emergency.contact', 'employee_obj', string='Contact Urgence ')



