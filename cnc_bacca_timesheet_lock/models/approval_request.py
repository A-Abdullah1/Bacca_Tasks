from odoo import models, fields, api, _


class ApprovalForTask(models.Model):
    _name = 'project.approvalrequest'
    _description = "Approval Request"
    project_id = fields.Many2one('project.project', string="Project", required=True)
    task_id = fields.Many2one('project.task', string="Task", required=True)

    employee_id = fields.Many2one('hr.employee', string="Employee",
                                  required=True)

    comment = fields.Text(string="Comment", required=True)

    needed_hours = fields.Float(string="New Allocated Hours")
    spent_hours = fields.Float(string="Spent Hours")
    requested_hours = fields.Float(string="Requested Hours")
    approval_status = fields.Selection(
        [('pending', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        string="Task Status",
        default='pending'
    )

    def action_extend_request_approved(self):
        self.task_id.new_allocated_time = self.needed_hours
        self.task_id.planned_hours = self.needed_hours + self.task_id.planned_hours
        self.approval_status = 'approved'

    def action_extend_request_rejected(self):
        self.approval_status = 'rejected'
