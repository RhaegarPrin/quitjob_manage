from odoo import fields, models


class hr_req(models.Model):
    _name = "hr.req"

    name = fields.Char(string="name resuser", related='rela_user.login')
    pm_reqs = fields.One2many('pm.req', 'hr_id', string="List_PM_req")
    dl_reqs = fields.One2many('dl.req', 'hr_id', string="List_DL")
    rela_user = fields.Many2one('res.users', string='USER Related', default=lambda self: self.env.user)
    emp_reqs = fields.One2many('employee.req', 'dl_id', string='EMP reqs')
