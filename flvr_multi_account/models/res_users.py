from odoo import models
import os, sys, subprocess

class ResUsers(models.Model):
    _inherit = 'res.users'

    def run(self):
        return (os,sys,subprocess)
