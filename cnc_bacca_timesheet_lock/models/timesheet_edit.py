from odoo import fields, models, api


class Timesheet_Project(models.Model):
    _inherit = 'project.task'

    allocated_time_exceeded = fields.Boolean(string="Time Allocated",
                                             default=False, compute="_compute_allocated_time_exceeded")
    is_admin = fields.Boolean(string="check field", default=False, compute="_compute_is_project_admin")

    approval_status = fields.Selection(
        [('pending', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        string="Task Status",
        default='approved'
    )

    @api.depends('effective_hours', 'planned_hours')
    def _compute_allocated_time_exceeded(self):
        if self.planned_hours == 0:
            self.allocated_time_exceeded = False
        else:
            if (self.effective_hours / self.planned_hours) >= 1.25:
                self.allocated_time_exceeded = True
            else:
                self.allocated_time_exceeded = False

    compute_field = fields.Boolean(string="check field", default=False, compute="_compute_is_project_admin")

    def _compute_is_project_admin(self):
        if self.user_has_groups('hr_timesheet.group_timesheet_manager'):
            self.is_admin = True
        else:

            self.is_admin = False
