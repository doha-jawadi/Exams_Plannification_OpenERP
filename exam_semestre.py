from openerp.osv import osv,fields
import openerp
class exam_semestre(osv.osv):
    _name='exam.semestre'
    _columns={
		'name': fields.char('Semestre'),
			 }
exam_semestre()