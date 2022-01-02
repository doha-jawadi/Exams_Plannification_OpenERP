from openerp.osv import osv,fields
import openerp
class exam_annee(osv.osv):
    _name='exam.annee'
    _columns={
		'name': fields.char('Annee Universitaire'),
			 }
exam_annee()