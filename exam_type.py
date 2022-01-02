class exam_type(osv.osv):
    _name='exam.type'
    _columns={
		'name': fields.char('Type de Local', size=64),
        'salle_id': fields.one2many('exam.salle','type_id',string='Salles'),
			 }
exam_type()