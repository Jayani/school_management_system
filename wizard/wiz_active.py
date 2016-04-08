# -*- coding: utf-8 -*-
from openerp import api, fields, models

class wiz_show_active(models.TransientModel):
    _name = 'wiz.show.active'

    @api.multi
    def show_active(self):
        stud_obj = self.env['school.admission']
        for res in self:
            sdata = stud_obj.search([('active', '=', False)])
            print sdata
            for i in sdata:
                i.active = [('active', '=', True)]
