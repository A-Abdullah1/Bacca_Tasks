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


