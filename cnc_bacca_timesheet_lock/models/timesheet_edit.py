from odoo import fields, models, api


class Timesheet_project(models.Model):
    _inherit = 'project.task'

    compute_field = fields.Boolean(string="check field", default=False, compute="_compute_is_project_admin")

    def _compute_is_project_admin(self):
        if self.project_id.user_id.id == self.env.user.id:
            self.compute_field = True

        else:

            self.compute_field = False


class Timesheet_project(models.Model):
    _inherit = 'account.analytic.line'

    compute_field = fields.Boolean(string="check field", default=False, compute="_compute_is_project_admin")

    def _compute_is_project_admin(self):
        if self.user_has_groups('hr_timesheet.group_timesheet_manager'):
            self.is_admin = True
        else:

            self.is_admin = False
