
  exit_on_error=false
  exit_on_end=true
  verbosity=2

model = '${model.get('name')}'
new_model_force(model, '')


<%include file="basic_modpar.mako" />


m.airgap          =     2*ag/3
m.nodedist        =     ${model.stator.get('nodedist',1)}


